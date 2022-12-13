import { Injectable } from '@angular/core';
import { Observable } from "rxjs";
import { HttpClient, HttpHeaders, HttpParams } from "@angular/common/http";

import { InfoArray } from "./test-contracts";
import { Info } from "./test-contracts";


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
}
