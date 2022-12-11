import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
import { CommonModule } from '@angular/common'
import { ComponentsModule } from '../../components/components.module'
import { SearchPage } from './search-page.component'

import { BrowserModule } from '@angular/platform-browser'
import { HttpClientModule } from "@angular/common/http"

import { AppRoutingModule } from '../../app-routing.module'
import { AppComponent } from '../../app.component'

import { NgxPaginationModule } from 'ngx-pagination';

@NgModule({
  declarations: [SearchPage],
  imports: [ 
    BrowserModule, 
    CommonModule,
    AppRoutingModule, 
    ComponentsModule, 
    HttpClientModule, 
    NgxPaginationModule
  ],
  exports: [SearchPage],
  //bootstrap:[SearchPage],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class SearchPageModule {}

