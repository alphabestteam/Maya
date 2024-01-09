import { Component } from '@angular/core';
import { never } from 'rxjs';

interface Record{
  recordName: string, 
  artistName: string,
  description: string,
  image: string
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  records: Record[] = [{
    "recordName": "Good Kid M.a.a.d City",
    "artistName": "Kendrick Lamar",
    "description": "Kendrick Lamar- Good Kid M.a.a.d City record",
    "image": "assets/kendrick_lamar_maad_city.png"
  },
  {
    "recordName": "To Pimp A Butterfly",
    "artistName": "Kendrick Lamar",
    "description": "Kendrick Lamar- To Pimp A Butterfly record",
    "image": "assets/to_pimp_butterfly.png"
  },
  {
    "recordName": "Damn.",
    "artistName": "Kendrick Lamar",
    "description": "Kendrick Lamar- Damn.",
    "image": "assets/damn_record.png"
  }]
  title = 'shopping-cart-storage';
  finalCart: string[] = []
  ngOnInit(){
  }
  addToShoppingCart(record: Record){
    const recordName: string = record.recordName
    const chosenRecord: string = JSON.stringify(record);
    localStorage.setItem(`${recordName}`, chosenRecord);
  }
  deleteCart(){
    localStorage.clear();
    this.finalCart.splice(0, this.finalCart.length);
  }

  printCart(){
    Object.keys(localStorage).forEach(key => {
      let value = `${key} - ${localStorage.getItem(key)}`;
      this.finalCart.push(key)
      console.log(value);
    });

  }
}
