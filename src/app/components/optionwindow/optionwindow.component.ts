import { Component, Input } from '@angular/core'
import { Info, UrlArray } from '../../test-contracts'

@Component({
  selector: 'app-optionwindow',
  templateUrl: 'optionwindow.component.html',
  styleUrls: ['optionwindow.component.css'],
})
export class Optionwindow {
  @Input()
  text: string = 'Скоро появятся... :)'
  @Input()
  image_alt: string = 'image'
  @Input()
  rootClassName: string = ''
  @Input()
  image_src: string = 'https://play.teleporthq.io/static/svg/default-img.svg'
  @Input()
  text1: string = 'Text'
  @Input()
  element!: Info

  constructor() {}

  public getMinPrice(urls: UrlArray): number {
    var len = urls.length, min = Infinity;
    while (len--) {
      if (Number(urls[len].cost.product_cost) < min) {
        min = Number(urls[len].cost.product_cost);
      }
    }
    return min;
  }

  public getMaxPrice(urls: UrlArray): number {
    var len = urls.length, max = -Infinity;
    while (len--) {
      if (urls[len].cost.product_cost > max) {
        max = urls[len].cost.product_cost;
      }
    }
    return max;
  }
}
