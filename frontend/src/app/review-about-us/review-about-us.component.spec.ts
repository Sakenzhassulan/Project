import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ReviewAboutUsComponent } from './review-about-us.component';

describe('ReviewAboutUsComponent', () => {
  let component: ReviewAboutUsComponent;
  let fixture: ComponentFixture<ReviewAboutUsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ReviewAboutUsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReviewAboutUsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
