import { Component, Input } from '@angular/core'

@Component({
  selector: 'app-optionwindow',
  templateUrl: 'optionwindow.component.html',
  styleUrls: ['optionwindow.component.css'],
})
export class Optionwindow {
  @Input()
  text: string = 'Text'
  @Input()
  image_alt: string = 'image'
  @Input()
  rootClassName: string = ''
  @Input()
  image_src: string = 'https://play.teleporthq.io/static/svg/default-img.svg'
  @Input()
  text1: string = 'Text'

  constructor() {}
}
