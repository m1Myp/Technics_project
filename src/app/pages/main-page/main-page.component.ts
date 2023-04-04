import { Component } from '@angular/core'
import { Title, Meta } from '@angular/platform-browser'
import { ModalService } from '../../_modal/modal.service'

@Component({
  selector: 'main-page',
  templateUrl: 'main-page.component.html',
  styleUrls: ['main-page.component.css'],
})
export class MainPage {
  constructor(private title: Title, private meta: Meta, private modalService: ModalService) {
    this.title.setTitle('technics nearby')
    this.meta.addTags([
      {
        property: 'og:title',
        content: 'technics nearby',
      },
    ])
  }

  openModal(id: string) {
    this.modalService.open(id);
  }
  
  closeModal(id: string) {
    this.modalService.close(id);
  }
}
