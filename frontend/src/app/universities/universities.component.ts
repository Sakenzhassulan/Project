import { Component, OnInit } from '@angular/core';
import {ApiService} from '../api.service';
import {University} from '../university';

@Component({
  selector: 'app-universities',
  templateUrl: './universities.component.html',
  styleUrls: ['./universities.component.css']
})
export class UniversitiesComponent implements OnInit {

  universities: University;

  ngOnInit(): void {
    this.getUniversities();
  }


  constructor(private api: ApiService) { }

  getUniversities() {
    this.api.getAllUniversities().subscribe(
      data => {
        this.universities = data;
      },
      error => {
        console.error(error);
      });
  }

}
