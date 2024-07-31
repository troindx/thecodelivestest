import { Component, OnInit } from '@angular/core';
import { CatService } from '../services/cat.service';

import { Toast } from '@capacitor/toast';
import { Cat } from '../models/cats.model';
import { CommonModule } from '@angular/common';
import { IonicModule } from '@ionic/angular';
import { CatCardComponent } from '../components/cat-card/cat-card.component';
import { CatformComponent } from '../components/catform/catform.component';
import { FavoriteCatsComponent } from '../components/favorite-cats/favorite-cats.component';
import { FavoriteService } from '../services/favorite.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.page.html',
  styleUrls: ['./home.page.scss'],
  standalone: true,
  providers: [CatService, FavoriteService],
  imports: [CommonModule, IonicModule, CatCardComponent, CatformComponent, FavoriteCatsComponent]
})
export class HomePage implements OnInit {
  cats: Cat[] = [];
  catFormVisible = false;
  expandedCatId?: string;
  selectedCat?: Cat;
  favoriteCats: Cat[] = [];

  constructor(private catService: CatService) {}

  ngOnInit() {
    this.loadCats();
  }

  loadCats() {
    try {
      this.catService.getCats().subscribe(data => {
        this.cats = data;
      });
    } catch (error) {
      Toast.show({
        text: 'Error loading cats',
        duration: 'long'
      });
    }
    
  }

  showCatForm() {
    this.selectedCat = undefined;
    this.catFormVisible = true;
  }

  editCat(cat: Cat) {
    this.selectedCat = cat;
    this.catFormVisible = true;
  }

  catFormClosed() {
    this.catFormVisible = false;
    this.loadCats();
  }

  toggleExpand(cat: Cat) {
    this.expandedCatId = this.expandedCatId === cat.id ? undefined : cat.id;
  }

}
