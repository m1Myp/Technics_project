import { Component } from '@angular/core'
import { Title, Meta } from '@angular/platform-browser'

@Component({
  selector: 'main-page',
  templateUrl: 'main-page.component.html',
  styleUrls: ['main-page.component.css'],
})
export class MainPage {
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
