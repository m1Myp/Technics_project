import { Injectable } from '@angular/core';
import { Observable } from "rxjs";
import { HttpClient } from "@angular/common/http";

import { ProductArray } from "./products";


@Injectable({
 providedIn: 'root'
})

export class ProductsService {

 constructor(private http: HttpClient) { }

 getProducts(): Observable<ProductArray> {
   return this.http.get('http://127.0.0.1:8000/api/v1/products/') as Observable<ProductArray>;
 }
}
