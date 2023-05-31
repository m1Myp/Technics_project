import { Component, EventEmitter, Output } from '@angular/core';
import { TestService } from '../../test.service';

@Component({
  selector: 'dropdown-list',
  templateUrl: './dropdown-list.component.html',
  styleUrls: ['./dropdown-list.component.css']
})
export class DropdownListComponent {
  @Output() 
  doSorting: EventEmitter<string> = new EventEmitter<string>()

  public sorting: string = "min_price_asc"

  public setSorting(sorting: string): void {
    this.doSorting.emit(sorting);
  }

  constructor() { }
}
