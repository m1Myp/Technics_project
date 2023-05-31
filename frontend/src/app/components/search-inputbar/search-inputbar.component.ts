import { Component, Input } from '@angular/core'
import { Location } from '@angular/common';
import { SearchPage } from '../../pages/search-page/search-page.component';
import { Router } from '@angular/router';

@Component({
  selector: 'search-inputbar',
  templateUrl: 'search-inputbar.component.html',
  styleUrls: ['search-inputbar.component.css'],
})
export class SearchInputbar {
  @Input()
  rootClassName: string = ''
  @Input()
  searchValue: string = ''

  static searchString: string;

  constructor(private location: Location, private router : Router) { 
  }

  public doSearch(searchString: string): void {
    SearchInputbar.searchString = searchString;
    this.router.navigateByUrl('/products/search-page/'+searchString, {skipLocationChange: false});
  }

  public onEnter(searchString: string) {
    SearchInputbar.searchString = searchString;
    this.router.navigateByUrl('/products/search-page/'+searchString, {skipLocationChange: false});
  }
}
