import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RegisterFormComponent } from './register-form/register-form.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatButtonModule} from '@angular/material/button';
import { LoginFormComponent } from './login-form/login-form.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import { ReviewsFormComponent } from './reviews-form/reviews-form.component';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import {MatDatepickerModule} from '@angular/material/datepicker';
import { BsDatepickerModule } from 'ngx-bootstrap/datepicker';
import { RatingModule, RatingConfig } from 'ngx-bootstrap/rating';
import { FormsModule } from '@angular/forms';
import { RequestTripFormComponent } from './request-trip-form/request-trip-form.component';
import {MatSelectModule} from '@angular/material/select';
@NgModule({
  declarations: [
    AppComponent,
    RegisterFormComponent,
    LoginFormComponent,
    NavBarComponent,
    ReviewsFormComponent,
    RequestTripFormComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    MatDatepickerModule,
    BsDatepickerModule.forRoot(),
    RatingModule,
    FormsModule,
    MatSelectModule
  ],
  providers: [RatingConfig],
  bootstrap: [AppComponent]
})
export class AppModule { }
