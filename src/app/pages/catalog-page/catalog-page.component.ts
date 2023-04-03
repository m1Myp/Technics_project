import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { TestService } from "../../test.service";
import { InfoArray } from "../../test-contracts";

@Component({
  selector: 'catalog-page',
  templateUrl: 'catalog-page.component.html',
  styleUrls: ['catalog-page.component.css'],
})
export class CatalogPage implements OnInit{
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

  public category: string = '';
  constructor (private route: ActivatedRoute, private testService: TestService) {
    this.route.params.subscribe(data => {
      this.category = data['category'];
    })
  }

  ngOnInit(): void {
    this.getItems(this.category, 0, this.sorting);
  }

  public current: number = 1;
  public total: number = 1;
  public itemsToDisplay: InfoArray = []
  public perPage: number = 7;
  public getItems(category: string, page: number, sorting: string) {
    this.testService.getItems(category, page, sorting).subscribe(
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
    this.getItems(this.category, this.current - 1, this.sorting);
  }
  public onNext(page: number): void {
    this.current = page + 1;
    this.getItems(this.category, this.current - 1, this.sorting);
  }
  public onPrevious(page: number): void {
    this.current = page - 1;
    this.getItems(this.category, this.current - 1, this.sorting);
  }

  public doSorting(sorting: string): void {
    this.sorting = sorting;
    this.current = 1;
    this.getItems(this.category, 0, this.sorting);
  }
}

