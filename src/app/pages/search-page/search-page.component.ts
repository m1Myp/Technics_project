import { Component, OnInit, Input } from '@angular/core';
import { TestService } from "../../test.service";
import {Info, InfoArray} from "../../test-contracts";

@Component({
  selector: 'search-page',
  templateUrl: 'search-page.component.html',
  styleUrls: ['search-page.component.css'],
})
export class SearchPage implements OnInit{
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

  POSTS: any;
  page = 1;
  count = 0;
  tableSize = 7;

  public productData: InfoArray = [];
  public product: Info | null = null;
  public productNumber: number = 0;

  constructor(private testService: TestService) { }

  ngOnInit(): void {
    this.getTest();
  }

  getTest() {
    this.testService.getTest().subscribe(
      {
        next: (data) => {
          this.productData = data;
          console.log(data);
        },
        error: (error) => {
          console.log(error);
        }
      }
      );
  }

  onTableDataChange(event: any) {
    this.page = event;
    this.getTest();
  }
}

