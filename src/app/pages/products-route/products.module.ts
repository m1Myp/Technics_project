import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
import { BrowserModule } from '@angular/platform-browser'
import { ComponentsModule } from '../../components/components.module'
import { ProductsComponent } from './products.component'
import { CommonModule } from '@angular/common'

import { HttpClientModule } from "@angular/common/http"

import { AppRoutingModule } from '../../app-routing.module'
import { NgxPaginationModule } from 'ngx-pagination';

import { MainPage } from '../main-page/main-page.component'
import { SearchPage } from '../../pages/search-page/search-page.component'
import { ProductPage } from '../../pages/product-page/product-page.component'

@NgModule({
  declarations: [
    ProductsComponent, MainPage, SearchPage, ProductPage
  ],
  imports: [
    BrowserModule, 
    CommonModule,
    AppRoutingModule, 
    ComponentsModule, 
    HttpClientModule,
    NgxPaginationModule
  ],
  providers:[],
  bootstrap: [ProductsComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class ProductsModule {}

