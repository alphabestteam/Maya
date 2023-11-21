import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  userInput:string = ``;
  isInputEmpty(){
    return this.userInput == ``;
  };
  resetUser(){
    this.userInput = ``;
  };
}
