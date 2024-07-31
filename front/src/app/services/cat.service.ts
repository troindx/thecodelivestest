import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { Cat } from '../models/cats.model';

@Injectable({
  providedIn: 'root'
})
export class CatService {
  private apiUrl = `${environment.apiUrl}/api/cats`;

  constructor(private http: HttpClient) {}

  getCats(): Observable<Cat[]> {
    return this.http.get<Cat[]>(this.apiUrl);
  }

  getCat(id: string): Observable<Cat> {
    return this.http.get<Cat>(`${this.apiUrl}/${id}`);
  }

  createCat(cat: Cat): Observable<string> {
    return this.http.post<string>(this.apiUrl, cat);
  }

  updateCat(id: string, cat: Cat): Observable<boolean> {
    return this.http.put<boolean>(`${this.apiUrl}/${id}`, cat);
  }

  deleteCat(id: string): Observable<boolean> {
    return this.http.delete<boolean>(`${this.apiUrl}/${id}`);
  }
}
