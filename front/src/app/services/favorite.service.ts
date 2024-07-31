import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Cat } from '../models/cats.model';


@Injectable({
  providedIn: 'root'
})
export class FavoriteService {
  private favoriteCats: Cat[] = [];
  favoriteCatsSubject = new BehaviorSubject<Cat[]>([]);

  constructor() {
    console.log('FavoriteService created');
  }

  getFavoriteCats(): Cat[] {
    return this.favoriteCats;
  }

  addFavoriteCat(cat: Cat): void {
    console.log('Adding favorite cat', cat);
    this.favoriteCats.push(cat);
    this.favoriteCatsSubject.next(this.favoriteCats);
  }

  removeFavoriteCat(cat: Cat): void {
    this.favoriteCats = this.favoriteCats.filter(favCat => favCat.id !== cat.id);
    this.favoriteCatsSubject.next(this.favoriteCats);
  }

  isFavorite(cat: Cat): boolean {
    return this.favoriteCats.some(favCat => favCat.id === cat.id);
  }
}
