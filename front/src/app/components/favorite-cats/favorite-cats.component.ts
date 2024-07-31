import { Component, OnInit } from '@angular/core';
import { FavoriteService } from '../../services/favorite.service';
import { Cat } from 'src/app/models/cats.model';
import { IonicModule } from '@ionic/angular';
import { CommonModule } from '@angular/common';
import { CatCardComponent } from '../cat-card/cat-card.component';
import { Toast } from '@capacitor/toast';


@Component({
  selector: 'app-favorite-cats',
  templateUrl: './favorite-cats.component.html',
  styleUrls: ['./favorite-cats.component.scss'],
  imports: [ IonicModule, CommonModule, CatCardComponent ],
  standalone: true
})
export class FavoriteCatsComponent implements OnInit {
  favoriteCats: Cat[] = [];

  constructor(private favoriteService: FavoriteService) {}

  ngOnInit() {
    this.favoriteService.favoriteCatsSubject.subscribe(cats => {
      this.favoriteCats = cats;
      if (cats.length !== 0) {
        Toast.show({
          text: `Cat added to favorites!`,
          duration: 'short'
        });
    }
    });
  }
}
