import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
import { RouterModule } from '@angular/router'
import { CommonModule } from '@angular/common'
import { ComponentsModule } from '../../components/components.module'
import { MainPage } from './main-page.component'

import { BrowserModule } from '@angular/platform-browser'
import { HttpClientModule } from "@angular/common/http"
import { AppRoutingModule } from '../../app-routing.module'
import { NgxPaginationModule } from 'ngx-pagination';

@NgModule({
  declarations: [MainPage],
  imports: [ 
    BrowserModule, 
    CommonModule,
    AppRoutingModule, 
    ComponentsModule, 
    HttpClientModule, 
    NgxPaginationModule
  ],
  exports: [MainPage],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class MainPageModule {}
