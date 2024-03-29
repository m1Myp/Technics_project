import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { SearchPage } from './pages/search-page/search-page.component';
import { MainPage } from './pages/main-page/main-page.component';
import { ProductPage } from './pages/product-page/product-page.component';
import { ComponentsModule } from './components/components.module';
import { ProductsComponent } from './pages/products-route/products.component';
import { CatalogPage } from './pages/catalog-page/catalog-page.component';

const routes: Routes = [
  {
    path: 'products',
    component: ProductsComponent,
    children: [
      {
        path: 'catalog-page/:category',
        component: CatalogPage
      },
      {
        path: 'catalog-page',
        component: CatalogPage
      },
      {
        path: 'search-page/:search',
        component: SearchPage
      },
      {
        path: 'search-page',
        component: SearchPage
      },
      {
        path: 'product-page/:id',
        component: ProductPage
      }
    ]
  },
  { 
    path: '', 
    component: MainPage
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
