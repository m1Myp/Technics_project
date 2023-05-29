import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
import { CommonModule } from '@angular/common'
import { DropdownListComponent } from './dropdown-list.component';
import { ComponentsModule } from '../../components/components.module'
import { NgxPaginationModule } from 'ngx-pagination'



@NgModule({
  declarations: [DropdownListComponent],
  exports: [DropdownListComponent],
  imports: [
    CommonModule,
    ComponentsModule,
    NgxPaginationModule, 
],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class DropdownListModule { }