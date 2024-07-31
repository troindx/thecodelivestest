import { animate, state, style, transition, trigger } from '@angular/animations';
import { CommonModule, DatePipe } from '@angular/common';
import { Component, Input, Output, EventEmitter } from '@angular/core';
import { IonicModule } from '@ionic/angular';
import { Cat } from 'src/app/models/cats.model';
import { FavoriteService } from 'src/app/services/favorite.service';

@Component({
  selector: 'app-cat-card',
  templateUrl: './cat-card.component.html',
  styleUrls: ['./cat-card.component.scss'],
  standalone: true,
  providers: [DatePipe],
  imports: [IonicModule, CommonModule],
  animations: [
    trigger('expandCollapse', [
      state('collapsed', style({
        height: '190px',
      })),
      state('expanded', style({
        height: '*'
      })),
      transition('collapsed <=> expanded', [
        animate('300ms ease-in-out')
      ])

    ])
  ]
})
export class CatCardComponent {
  @Input() cat!: Cat;
  @Input() expanded!: boolean;
  @Output() editCat = new EventEmitter<Cat>();
  @Output() expand = new EventEmitter<void>();
  isExpanded = false;

  constructor(private datePipe: DatePipe, private favoriteService: FavoriteService) {}

  onEditCat() {
    this.editCat.emit(this.cat);
  }
  
  toggleExpand() {
    this.isExpanded = !this.isExpanded;
    this.expand.emit();
  }

  isFavorite(): boolean {
    return this.favoriteService.isFavorite(this.cat);
  }

  toggleFavorite() {
    if (this.isFavorite()) {
      this.favoriteService.removeFavoriteCat(this.cat);
    } else {
      this.favoriteService.addFavoriteCat(this.cat);
    }
  }

  getFormattedDate(date: string): string | null {
    return this.datePipe.transform(date, 'yyyy-MM-dd');
  }
}
