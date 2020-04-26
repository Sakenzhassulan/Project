import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {ApiService} from '../api.service';
import {Comment} from '../comment';
import {AuthService} from '../auth.service';

@Component({
  selector: 'app-professor-detail',
  templateUrl: './professor-detail.component.html',
  styleUrls: ['./professor-detail.component.css']
})
export class ProfessorDetailComponent implements OnInit {

  professor;
  ratings;
  comment = new Comment();

  constructor(
    private route: ActivatedRoute,
    public router: Router,
    private apiService: ApiService,
    private authService: AuthService,
  ) { }

  ngOnInit(): void {
    this.getUserData();
    this.getProfessor();
    this.getProfessorRatingFilter();
  }

  getProfessor() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.apiService.getProfessor(id).subscribe(professor => this.professor = professor);
  }

  getProfessorRatingFilter() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.apiService.getProfessorRatingCount(id).subscribe(ratings => this.ratings = ratings);
  }

  addComment(): void {
    if (this.authService.loggedIn()) {
      this.comment.professor = this.professor.id;
      this.apiService.addComment(this.comment)
        .subscribe( comment => {
          this.professor.ratings.push(comment);
          this.getProfessorRatingFilter();
          console.log(comment.value);
        });
    }
    else alert('Вам нужно войти')
  }

  statsReviews(total, value) {
    return value * 100 / total;
  }

  convertDate(date) {
    let convertedDateString = date.toLocaleString();
    convertedDateString = convertedDateString.replace('at ', '');
    return new Date(convertedDateString);
  }

  range(n) {
      return Array(Math.max(0, Math.min(5, n)));
  }

  getUserData() {
    if (this.authService.loggedIn()) {
      this.authService.getUserData()
        .subscribe(
          user => {
            // @ts-ignore
            return this.comment.email = user.email;
          },
          error => console.log(error)
        );
    }
  }


}
