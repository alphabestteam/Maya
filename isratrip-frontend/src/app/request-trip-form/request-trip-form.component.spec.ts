import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RequestTripFormComponent } from './request-trip-form.component';

describe('RequestTripFormComponent', () => {
  let component: RequestTripFormComponent;
  let fixture: ComponentFixture<RequestTripFormComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [RequestTripFormComponent]
    });
    fixture = TestBed.createComponent(RequestTripFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
