import { Component } from '@angular/core';
import { Title, Meta } from '@angular/platform-browser'

@Component({
  selector: 'products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css'],
})
export class ProductsComponent {
  constructor(private title: Title, private meta: Meta) {
    this.title.setTitle('technics nearby')
    this.meta.addTags([
      {
        property: 'og:title',
        content: 'technics nearby',
      },
    ])
  }
}
