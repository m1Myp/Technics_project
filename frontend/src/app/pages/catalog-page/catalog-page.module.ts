import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
import { CommonModule } from '@angular/common'
import { ComponentsModule } from '../../components/components.module'
import { CatalogPage } from './catalog-page.component'

import { BrowserModule } from '@angular/platform-browser'
import { HttpClientModule } from "@angular/common/http"

import { AppRoutingModule } from '../../app-routing.module'

import { NgxPaginationModule } from 'ngx-pagination'
import { PaginationModule } from '../../pagination/pagination.module'
import { DropdownListModule } from '../../components/dropdown-list/dropdown-list.module'


@NgModule({
  declarations: [CatalogPage],
  imports: [ 
    BrowserModule, 
    CommonModule,
    AppRoutingModule, 
    ComponentsModule, 
    HttpClientModule, 
    NgxPaginationModule, 
    PaginationModule,
    DropdownListModule,
  ],
  exports: [CatalogPage],
  //bootstrap:[SearchPage],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class CatalogPageModule {}

