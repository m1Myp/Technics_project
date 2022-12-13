import { Component, OnInit } from '@angular/core';
import { Title, Meta } from '@angular/platform-browser';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';


import { TestService } from "../../test.service";
import { Info } from "../../test-contracts";

@Component({
  selector: 'product-page',
  templateUrl: 'product-page.component.html',
  styleUrls: ['product-page.component.css'],
})
export class ProductPage implements OnInit {
  id: number = 0;
  public productData: Info = <Info> {
    product_ID: '',
    product_name: '',
    product_manufacturer: '',
    pictures: [],
    urls: []
  };

  constructor (private route: ActivatedRoute, private testService: TestService) {
    this.route.params.subscribe(data => {
      this.id = data['id'];
    })
  }

  ngOnInit() {
    this.getProduct();
  }

  getProduct() {
    this.testService.getProduct(this.id).subscribe(
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
