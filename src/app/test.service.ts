import { Injectable } from '@angular/core';
import { Observable } from "rxjs";
import { HttpClient } from "@angular/common/http";

import { InfoArray } from "./test-contracts";
import { Info, PageResponse } from "./test-contracts";


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
}
