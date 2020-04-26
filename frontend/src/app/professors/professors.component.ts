import {Component, Input, OnInit} from '@angular/core';
import {ApiService} from '../api.service';

@Component({
  selector: 'app-professors',
  templateUrl: './professors.component.html',
  styleUrls: ['./professors.component.css']
})
export class ProfessorsComponent implements OnInit {
  professors;
  universities;
  search = '';
  limit = 6;
  offset = 0;
  allProfessors;
  @Input() universityId = -1;

  constructor(
    private apiService: ApiService
  ) { }

  ngOnInit(): void {
    this.getProfessors();
    this.getUniversities();
    this.limit = 6;
    this.offset = 0;
  }

  getProfessors() {
    this.apiService.getProfessors().subscribe(professors => {this.allProfessors = professors; this.professors = professors; });
  }

  toStringJoin(data) {
    return data.map(r => r.abbreviation).join(', ');
  }

  getUniversities() {
    this.apiService.getAllUniversities().subscribe(universities => this.universities = universities);
  }

  getProfessorsByUniversity(universityId: any) {
    this.apiService.getProfessorsByUniversity(universityId)
      .subscribe(professors => {this.allProfessors = professors; this.professors = professors; });
  }

  getProfessorByName() {
    this.apiService.getProfessorByName(this.search)
      .subscribe(professors => {this.allProfessors = professors; this.professors = professors; });
  }

  paginate() {
    this.professors = this.allProfessors.slice(this.offset, this.offset + this.limit + 1);
  }

  next() {
    this.offset = Math.min(this.offset + this.limit, this.allProfessors.length);
    this.paginate();
  }

  prev() {
    this.offset = Math.max(0, this.offset - this.limit);
    this.paginate();
  }
}
