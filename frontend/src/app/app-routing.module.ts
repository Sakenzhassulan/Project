import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {AppComponent} from './app.component';
import {ProfessorsComponent} from './professors/professors.component';
import {MainComponent} from './main/main.component';
import {ProfessorDetailComponent} from './professor-detail/professor-detail.component';


const routes: Routes = [
  { path: '', component: MainComponent },
  { path: 'professors', component: ProfessorsComponent },
  { path: 'professors/:id', component: ProfessorDetailComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
