import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { TestService } from "../../test.service";
import { InfoArray } from "../../test-contracts";
import { ViewportScroller } from "@angular/common"

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

  sorting: string = 'min_price_asc';

  POSTS: any;

  public searchString: string = '';
  constructor (private route: ActivatedRoute, private testService: TestService, private viewport: ViewportScroller) {
    this.route.params.subscribe(data => {
      this.searchString = data['search'];
      this.searchItems(this.searchString, 0, this.sorting);
    })
  }

  ngOnInit(): void {
    this.searchItems(this.searchString, 0, this.sorting);
  }

  public current: number = 1;
  public total: number = 1;
  public itemsToDisplay: InfoArray = []
  public perPage: number = 7;
  public searchItems(searchString: string, page: number, sorting: string) {
    this.testService.searchItems(searchString, page, sorting).subscribe(
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
    this.searchItems(this.searchString, this.current - 1, this.sorting);
    this.viewport.scrollToPosition([0, 0]);
  }
  public onNext(page: number): void {
    this.current = page + 1;
    this.searchItems(this.searchString, this.current - 1, this.sorting);
    this.viewport.scrollToPosition([0, 0]);
  }
  public onPrevious(page: number): void {
    this.current = page - 1;
    this.searchItems(this.searchString, this.current - 1, this.sorting);
    this.viewport.scrollToPosition([0, 0]);
  }

  public doSorting(sorting: string): void {
    this.sorting = sorting;
    this.current = 1;
    this.searchItems(this.searchString, 0, this.sorting);
  }
}

