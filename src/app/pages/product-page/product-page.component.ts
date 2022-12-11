import { Component } from '@angular/core'
import { Title, Meta } from '@angular/platform-browser'

@Component({
  selector: 'product-page',
  templateUrl: 'product-page.component.html',
  styleUrls: ['product-page.component.css'],
})
export class ProductPage {
  raw6aot: string = ' '

  constructor(private title: Title, private meta: Meta) {
    this.title.setTitle('ProductPage - exported project')
    this.meta.addTags([
      {
        property: 'og:title',
        content: 'ProductPage - exported project',
      },
    ])
  }
}
