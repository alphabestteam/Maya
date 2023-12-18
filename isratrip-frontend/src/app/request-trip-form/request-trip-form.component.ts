import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';


@Component({
  selector: 'app-request-trip-form',
  templateUrl: './request-trip-form.component.html',
  styleUrls: ['./request-trip-form.component.css']
})
export class RequestTripFormComponent {
  tripForm!: FormGroup;
  formSubmitted = false;
  cities: string[] = [];
  value!: string;
  ages: string[] = ["ALL", "13+", "16+", "18+"];
  weathers: string[] = ["winter", "spring", "summer", "autumn"];

  constructor(private formBuilder: FormBuilder) { }
  ngOnInit(): void {
    this.tripForm = this.formBuilder.group({
      location_name: ['', Validators.required],
      category: ['', [Validators.required]],
      trip_title: ['', [Validators.required]],
      age_limit: ['', [Validators.required]],
      best_weather: ['', [Validators.required]],
      opening_days: ['', [Validators.required]],
    });
  }

  onSubmit() {
    this.formSubmitted = true;
    if (this.tripForm.invalid) {
      return;
    }
    else {
      console.log(this.tripForm.value);
    }
  }
  // async getLocationApi(): Promise<string>{
  //   const url = 'https://referential.p.rapidapi.com/v1/city?fields=iso_a2%2Cstate_code%2Cstate_hasc%2Ctimezone%2Ctimezone_offset&iso_a2=il&lang=hebrew&state_code=IL&limit=250';
  //   const options = {
  //     method: 'GET',
  //     headers: {
  //       'X-RapidAPI-Key': '70b4207fe2msh44fcd20aed003aep1484c2jsnb1962095186a',
  //       'X-RapidAPI-Host': 'referential.p.rapidapi.com'
  //     }
  //   };  
  //   const response = await fetch(url, options);
  //   const result = await response.text();
  //   return result;
  // }
//   async getCitiesFromApi(): Promise<string[]> {
//     const locations: string = await this.getLocationApi();
//     const citiesArr: string[] = JSON.parse(locations);
//     const values = citiesArr.map(city => city.value);
//     return values
//   }
  // myMap() {
  //   const mapProp: google.maps.MapOptions = {
  //     center: new google.maps.LatLng(51.508742, -0.120850),
  //     zoom: 5,
  //   };
  //   const map: google.maps.Map = new google.maps.Map(
  //     document.getElementById("googleMap")!,
  //     mapProp
  //   );
  // }
}