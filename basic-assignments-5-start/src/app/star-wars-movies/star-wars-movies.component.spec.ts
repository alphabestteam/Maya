import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StarWarsInfoComponent } from './star-wars-movies.component';

describe('StarWarsInfoComponent', () => {
  let component: StarWarsInfoComponent;
  let fixture: ComponentFixture<StarWarsInfoComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [StarWarsInfoComponent]
    });
    fixture = TestBed.createComponent(StarWarsInfoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
