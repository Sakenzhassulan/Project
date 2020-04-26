import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Router} from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  LOGINURL = 'http://127.0.0.1:8000/auth/login/';
  PROFILEURL = 'http://127.0.0.1:8000/auth/profile/';
  constructor(
    private http: HttpClient,
    private router: Router
  ) { }

  registerUser(user) {
    return this.http.post(this.PROFILEURL, user);
  }

  loginUser(username, password) {
    return this.http.post(this.LOGINURL, {username, password});
  }

  loggedIn() {
    return !!localStorage.getItem('token');
  }

  logoutUser() {
    localStorage.removeItem('token');
    this.router.navigate(['/']);
  }

  getUserData() {
    return this.http.get(this.PROFILEURL);
  }
}
