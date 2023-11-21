import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  printAlert: boolean = false;
  options: Array<number> = [1, 2, 3, 4, 5, 6, 7];
  selectedOption: number = 0;
  successBtn():void{
    this.printAlert = true;
  }
  warningBtn(): void {
    this.printAlert = false;
  }

  numOfTimes(): number[]{
    return this.options.slice(0, this.selectedOption);
  }
}

