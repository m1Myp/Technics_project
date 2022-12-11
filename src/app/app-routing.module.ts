import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { SearchPage } from './pages/search-page/search-page.component';
import { MainPage } from './pages/main-page/main-page.component';
import { ProductPage } from './pages/product-page/product-page.component';
import { ComponentsModule } from './components/components.module';

const routes: Routes = [
  {
    path: 'search-page',
    component: SearchPage
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
