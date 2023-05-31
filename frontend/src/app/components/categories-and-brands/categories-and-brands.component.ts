import { Component, Input } from '@angular/core'

@Component({
  selector: 'categories-and-brands',
  templateUrl: 'categories-and-brands.component.html',
  styleUrls: ['categories-and-brands.component.css'],
})
export class CategoriesAndBrands {
  @Input()
  rootClassName: string = ''
  @Input()
  button: string = 'бренды'

  constructor() {}
}
