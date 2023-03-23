import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
import { BrowserModule } from '@angular/platform-browser'
import { ComponentsModule } from './components/components.module'
import { AppComponent } from './app.component'

import { HttpClientModule } from "@angular/common/http"

import { AppRoutingModule } from './app-routing.module'
import { NgxPaginationModule } from 'ngx-pagination';

import { ProductsModule } from './pages/products-route/products.module'
import { SearchPageModule } from './pages/search-page/search-page.module'
import { MainPageModule } from './pages/main-page/main-page.module'
import { ProductPageModule } from './pages/product-page/product-page.module'

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule, 
    AppRoutingModule, 
    ComponentsModule, 
    HttpClientModule,
    NgxPaginationModule,

    ProductsModule,
    SearchPageModule,
    MainPageModule,
    ProductPageModule
  ],
  providers: [],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class AppModule {}

