import { Component, OnInit } from '@angular/core';
import {ApiService} from '../api.service';

@Component({
  selector: 'app-about-us',
  templateUrl: './about-us.component.html',
  styleUrls: ['./about-us.component.css']
})
export class AboutUsComponent implements OnInit {
  metrics;

  constructor(
    private apiService: ApiService
  ) {}

  ngOnInit(): void {
    this.apiService.getMetrics().subscribe(metrics => this.metrics = metrics);
  }


}
