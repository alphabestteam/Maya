import { Component, Input } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-reviews-form',
  templateUrl: './reviews-form.component.html',
  styleUrls: ['./reviews-form.component.css']
})

export class ReviewsFormComponent {
  max: number = 5;
  value!: number;
  reviewForm!: FormGroup;
  constructor(private formBuilder: FormBuilder) {
    this.reviewForm = this.formBuilder.group({
      value: [null]
    });
  }

  ngOnInit() {
    this.reviewForm = this.formBuilder.group({
      value: ['', Validators.required],
      review: ['', Validators.required]
    });
  }
}