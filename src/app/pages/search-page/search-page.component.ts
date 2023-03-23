import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { TestService } from "../../test.service";
import { Info, InfoArray, Category } from "../../test-contracts";

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

  public category: string = '';
  constructor (private route: ActivatedRoute, private testService: TestService) {
    this.route.params.subscribe(data => {
      this.category = data['category'];
    })
  }

  ngOnInit(): void {
    this.getItems(this.category, 0);
  }

  ////////////////////////////
  public current: number = 1;
  public total: number = 1;
  public itemsToDisplay: InfoArray = []
  public perPage: number = 7;
  getItems(category: string, page: number) {
    this.testService.getItems(category, page).subscribe(
      {
        next: (data) => {
          this.itemsToDisplay = data.products;
          this.total = Math.ceil(data.total_count_products / this.perPage);
          console.log(data);
        },
        error: (error) => {
          console.log(error);
        }
      }
      );
  }

  public onGoTo(page: number): void {
    this.current = page;
    this.getItems(this.category, this.current - 1);
  }
  public onNext(page: number): void {
    this.current = page + 1;
    this.getItems(this.category, this.current - 1);
  }
  public onPrevious(page: number): void {
    this.current = page - 1;
    this.getItems(this.category, this.current - 1);
  }
}

