import { Component, OnInit } from '@angular/core';
import { ProductsService } from "../products.service";
import {Product, ProductArray} from "../products";

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {
  productData: ProductArray = [];

  constructor(private productsService: ProductsService) { }

  ngOnInit(): void {
    this.getProducts();
  }

  getProducts() {
    this.productsService.getProducts().subscribe(
      {
        next: (data) => {
          this.productData = data;
        },
        error: (error) => {
          console.log(error);
        }
      }
      );
  }

}
