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

  displayDetails() {
    const counterElement = document.createElement('p');
    const displayArea = document.getElementById('clickCounter');
    const detailsElement = document.getElementById('details');
    if (this.details){
      detailsElement.style.visibility = 'hidden';
      this.details = false;
    }
    else{
      this.details = true;
      detailsElement.style.visibility = 'visible';
    }
    this.counter++;

    counterElement.textContent = `${this.counter}`;
    counterElement.style.margin = '0';

    if (this.counter >= 5){
      counterElement.style.backgroundColor = "blue";
    }
    if (displayArea) {
      displayArea.appendChild(counterElement);
    }
  };
}