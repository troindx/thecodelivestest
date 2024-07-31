import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { FormArray, FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { Cat, Vaccination } from 'src/app/models/cats.model';
import { CatService } from 'src/app/services/cat.service';
import { Camera, CameraResultType, Photo } from '@capacitor/camera';
import { Toast } from '@capacitor/toast';
import { CommonModule } from '@angular/common';
import { IonicModule } from '@ionic/angular';

@Component({
  selector: 'app-cat-form',
  templateUrl: './catform.component.html',
  styleUrls: ['./catform.component.scss'],
  standalone: true,
  imports: [CommonModule, IonicModule, FormsModule, ReactiveFormsModule]
})
export class CatformComponent implements OnInit {
  catForm: FormGroup;
  image: string ;
  @Input() cat?: Cat;
  @Output() formSubmitted = new EventEmitter<void>();
  @Output() formClose = new EventEmitter<void>();
  
  constructor(private catService:CatService,  private formBuilder: FormBuilder) {
    this.catForm = this.formBuilder.group({
      name: ['', Validators.required],
      age: ['', Validators.required],
      breed: ['', Validators.required],
      vaccinations: this.formBuilder.array([]),
      image: [''],
    });
    this.image = "";

  }

  ngOnInit() {
    if (this.cat) {
      this.catForm.patchValue({
        name: this.cat.name,
        age: this.cat.age,
        breed: this.cat.breed,
        image: this.cat.image,
      });
      this.image = this.cat.image;
      this.cat.vaccinations.forEach(vaccination => {
        this.addVaccination(vaccination);
      });
    }
  }

  get vaccinations() {
    return this.catForm.get('vaccinations') as FormArray;
  }

  addVaccination(vaccination?: Vaccination) {
    this.vaccinations.push(this.formBuilder.group({
      type: [vaccination?.type || '', Validators.required],
      date: [vaccination?.date ? this.formatDate(vaccination.date) : '', Validators.required]
    }));
  }

  formatDate(date: string): string {
    const d = new Date(date);
    return d.toISOString().split('T')[0];
  }

  removeVaccination(index: number) {
    this.vaccinations.removeAt(index);
  }
  
  async submitForm() {
    if (this.catForm.valid) {
      const cat: Cat = this.catForm.value;
      cat.image = this.image;
      try {
        if (this.cat && this.cat.id) {
          this.catService.updateCat(this.cat.id, cat).subscribe(response => {
            console.log('Cat updated successfully', response);
            this.formSubmitted.emit();
            Toast.show({
              text: 'Cat updated successfully',
              duration: 'short'
            });
            this.closeForm();
          });
        } else {
          this.catService.createCat(cat).subscribe(response => {
            console.log('Cat created successfully', response);
            this.formSubmitted.emit();
            this.closeForm();
            Toast.show({
              text: 'Cat created successfully',
              duration: 'short'
            });
          });
        }
      } catch (error) {
        await Toast.show({
          text: 'There is some sort of error with your camera. Can you please fix it? Without it you cannot take beautiful pictures of your cats',
        });
      }
    }
  }

  async takePicture(){
    try {
      const imageData = await Camera.getPhoto({
        quality: 90,
        allowEditing: true,
        resultType: CameraResultType.Base64
      });
      if (imageData.base64String) {
        const catImage = 'data:image/jpeg;base64,' + imageData.base64String;
        this.image = catImage; // Update the image property with the base64 encoded string
        this.catForm.patchValue({ image: catImage }); 
      }

      const catImage = 'data:image/jpeg;base64,' + imageData.base64String;
      this.catForm.patchValue({image: catImage});
    } catch (error) {
      await Toast.show({
        text: 'There is some sort of error with your camera. Can you please fix it? Without it you cannot take beautiful pictures of your cats',
      });
    }
  };

  closeForm() {
    this.formClose.emit();
  }
}
