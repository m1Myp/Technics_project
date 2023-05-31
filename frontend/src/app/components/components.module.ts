import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
import { RouterModule } from '@angular/router'
import { CommonModule } from '@angular/common'

import { CategoriesAndBrands } from './categories-and-brands/categories-and-brands.component'
import { Optionwindow } from './optionwindow/optionwindow.component'
import { SearchInputbar } from './search-inputbar/search-inputbar.component';
import { BugReportComponent } from './bug-report/bug-report.component'
import { ModalModule } from '../_modal/modal.module'
import { FormsModule }   from '@angular/forms';

@NgModule({
  declarations: [CategoriesAndBrands, Optionwindow, SearchInputbar, BugReportComponent],
  imports: [CommonModule, RouterModule, ModalModule, FormsModule],
  exports: [CategoriesAndBrands, Optionwindow, SearchInputbar, BugReportComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class ComponentsModule {}
