import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FaqService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  queryFaq(question: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/query`, { question });
  }
}
