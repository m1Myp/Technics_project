import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
import { RouterModule } from '@angular/router'
import { CommonModule } from '@angular/common'
import { ComponentsModule } from '../../components/components.module'
import { ProductPage } from './product-page.component'

import { BrowserModule } from '@angular/platform-browser'
import { HttpClientModule } from "@angular/common/http"
import { AppRoutingModule } from '../../app-routing.module'
import { NgxPaginationModule } from 'ngx-pagination';

@NgModule({
  declarations: [ProductPage],
  imports: [ 
    BrowserModule, 
    CommonModule,
    AppRoutingModule, 
    ComponentsModule, 
    HttpClientModule, 
    NgxPaginationModule
  ],
  exports: [ProductPage],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class ProductPageModule {}
