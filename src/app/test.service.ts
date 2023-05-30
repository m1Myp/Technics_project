import { Injectable } from '@angular/core';
import { Observable } from "rxjs";
import { HttpClient, HttpHeaders } from "@angular/common/http";

import { InfoArray, UrlArray } from "./test-contracts";
import { Info, PageResponse } from "./test-contracts";
import { NgForm } from '@angular/forms';


@Injectable({
 providedIn: 'root'
})
export class TestService {

 constructor(private http: HttpClient) { }

 getTest(): Observable<InfoArray> {
   return this.http.get('http://127.0.0.1:8000/products/api/v1/test/') as Observable<InfoArray>;
 }

 getProduct(id: number): Observable<Info> {
  return this.http.get('http://127.0.0.1:8000/products/api/v1/product/'+id) as Observable<Info>; 
 }

 getItems(category: string, page: number, sorting: string): Observable<PageResponse> {
  return this.http.get('http://127.0.0.1:8000/products/api/v1/c='+category+'/p='+page+'&sorting='+sorting) as Observable<PageResponse>;
 }

 searchItems(searchString: string, page: number, sorting: string): Observable<PageResponse> {
  return this.http.get('http://127.0.0.1:8000/products/api/v1/q='+searchString+'/p='+page+'&sorting='+sorting) as Observable<PageResponse>;
 }

  async sendBugReport(email: string, message: string) {
    try {
      const response = await fetch('https://formspree.io/f/mjvdazgd', {
        method: 'POST',
        body: JSON.stringify({
          'email': email, 'bug_report_message': message,
        }),
        headers: { 'Content-Type': 'application/json'}
      });

      if (!response.ok) {
        throw new Error('Error: status: ${{response.status}}');
      }
    } catch (error) {
      if (error instanceof Error) {
        console.log('error message: ', error.message);
      } else {
        console.log('unexpected error ', error);
      }
    }
  }

  getMinPrice(urls: UrlArray): number {
    var len = urls.length, min = Infinity;
    while (len--) {
      if (Number(urls[len].cost.product_cost) < min) {
        min = Number(urls[len].cost.product_cost);
      }
    }
    return min;
  }

  getMaxPrice(urls: UrlArray): number {
    var len = urls.length, max = -Infinity;
    while (len--) {
      if (urls[len].cost.product_cost > max) {
        max = urls[len].cost.product_cost;
      }
    }
    return max;
  }
}
