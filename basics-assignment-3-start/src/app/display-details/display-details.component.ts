import { Component } from '@angular/core';
import { count } from 'rxjs';

@Component({
  selector: 'app-display-details',
  templateUrl: './display-details.component.html',
  styleUrls: ['./display-details.component.css']
})

export class DisplayDetailsComponent {
  details: boolean = true;
  counter: number = 0;
  counterArray: number[] = [];
  displayDetails() {
    this.counter++;
    this.counterArray.push(this.counter);
  };
  getVisibility() {
    this.details = !this.details
    return this.details ? 'visible' : 'hidden';
  }
  isCounterBig() {
    return this.counter >= 5;
  }
}