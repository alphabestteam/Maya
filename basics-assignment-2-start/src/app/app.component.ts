import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  userInput: string = ``;
  isInputEmpty(): boolean {
    return this.userInput == ``;
  };
  resetUser(): void {
    this.userInput = ``;
  };
}
