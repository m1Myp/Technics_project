import { Component, Input, OnInit } from '@angular/core'
import { Info, UrlArray } from '../../test-contracts'
import { TestService } from '../../test.service'

@Component({
  selector: 'app-optionwindow',
  templateUrl: 'optionwindow.component.html',
  styleUrls: ['optionwindow.component.css'],
})
export class Optionwindow implements OnInit {
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

  urlsToShow!: UrlArray;

  constructor(private testService: TestService) {
  }
  ngOnInit(): void {
    this.urlsToShow = this.element.urls.slice(0,3);
  }

  public getMinPrice(urls: UrlArray): number {
    return this.testService.getMinPrice(urls);
  }

  public getMaxPrice(urls: UrlArray): number {
    return this.testService.getMaxPrice(urls);
  }
}
