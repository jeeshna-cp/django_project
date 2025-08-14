import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutUs } from './about-us/about-us';
import { ContactUs } from './contact-us/contact-us';
import { Home } from './home/home';

const routes: Routes = [
  {path:'Home',component:Home},
  {path:'About-us',component:AboutUs},
  {path:'Contact-us',component:ContactUs}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
