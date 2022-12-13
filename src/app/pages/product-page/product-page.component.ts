import { Component, OnInit } from '@angular/core'
import { Title, Meta } from '@angular/platform-browser'
import { Router, ActivatedRoute, ParamMap } from '@angular/router';

@Component({
  selector: 'product-page',
  templateUrl: 'product-page.component.html',
  styleUrls: ['product-page.component.css'],
})
export class ProductPage implements OnInit {
  raw6aot: string = ''
  id: number | null = null;

  constructor (private route: ActivatedRoute) {
    this.route.params.subscribe(data => {
      console.log(data);
    })
  }

  ngOnInit() {
    this.route.queryParams.subscribe(params => {
      this.id = params['id'];
    });
  }
}
