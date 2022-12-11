import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
import { BrowserModule } from '@angular/platform-browser'
import { ComponentsModule } from './components/components.module'
import { AppComponent } from './app.component'

import { HttpClientModule } from "@angular/common/http"

import { AppRoutingModule } from './app-routing.module'
import { NgxPaginationModule } from 'ngx-pagination';

import { MainPage } from './pages/main-page/main-page.component'
import { SearchPage } from './pages/search-page/search-page.component'
import { ProductPage } from './pages/product-page/product-page.component'

@NgModule({
  declarations: [
    AppComponent, SearchPage, MainPage
  ],
  imports: [
    BrowserModule, 
    AppRoutingModule, 
    ComponentsModule, 
    HttpClientModule,
    NgxPaginationModule
  ],
  providers: [],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class AppModule {}

