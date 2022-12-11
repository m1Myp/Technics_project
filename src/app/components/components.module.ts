import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
import { RouterModule } from '@angular/router'
import { CommonModule } from '@angular/common'

import { CategoriesAndBrands } from './categories-and-brands/categories-and-brands.component'
import { Optionwindow } from './optionwindow/optionwindow.component'

@NgModule({
  declarations: [CategoriesAndBrands, Optionwindow],
  imports: [CommonModule, RouterModule],
  exports: [CategoriesAndBrands, Optionwindow],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class ComponentsModule {}
