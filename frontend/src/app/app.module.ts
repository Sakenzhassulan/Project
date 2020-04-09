import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule} from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { BannerComponent } from './banner/banner.component';
import { ShortcutComponent } from './shortcut/shortcut.component';
import { AboutUsComponent } from './about-us/about-us.component';
import { UniversitiesComponent } from './universities/universities.component';
import { ReviewAboutUsComponent } from './review-about-us/review-about-us.component';
import { FooterComponent } from './footer/footer.component';
import { PartnersComponent } from './partners/partners.component';
import { MainNewsComponent } from './main-news/main-news.component';
import {LazyLoadScriptService} from './lazy-load-script.service';
import { ProfessorsComponent } from './professors/professors.component';
import { MainComponent } from './main/main.component';
import { SubHeaderComponent } from './sub-header/sub-header.component';
import { ProfessorDetailComponent } from './professor-detail/professor-detail.component';
import {FormsModule} from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    BannerComponent,
    ShortcutComponent,
    AboutUsComponent,
    UniversitiesComponent,
    ReviewAboutUsComponent,
    FooterComponent,
    PartnersComponent,
    MainNewsComponent,
    ProfessorsComponent,
    MainComponent,
    SubHeaderComponent,
    ProfessorDetailComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [LazyLoadScriptService],
  bootstrap: [AppComponent]
})
export class AppModule { }
