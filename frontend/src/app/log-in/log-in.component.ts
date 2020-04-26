import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {AuthService} from '../auth.service';

@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css']
})
export class LogInComponent implements OnInit {
  username;
  password;

  constructor(
    private authService: AuthService,
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  login() {
    this.authService.loginUser(this.username, this.password)
      .subscribe(
        response => {
          // @ts-ignore
          localStorage.setItem('token', response.token);
          this.router.navigate(['/']);
        },
        error => console.log(error)
      );
  }




}
