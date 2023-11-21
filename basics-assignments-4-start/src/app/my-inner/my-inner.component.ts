import { Component, Output, EventEmitter }from '@angular/core';

@Component({
  selector: 'app-my-inner',
  templateUrl: './my-inner.component.html',
  styleUrls: ['./my-inner.component.css']
})
export class MyInnerComponent {
  @Output() decreasedInput: EventEmitter<number> = new EventEmitter<number>();
  @Output() increasedInput: EventEmitter<number> = new EventEmitter<number>();
  innerTotal: number = 5;
  addPoint(){
    this.innerTotal += 1;
    if (this.innerTotal == 10){
      this.innerTotal = 0;
      this.increasedInput.emit(10)
    }
  }
  removePoint(){
    this.innerTotal -= 1;
    if (this.innerTotal == -10){
      this.innerTotal = 0;
      this.decreasedInput.emit(-10)
    }
  }

}
