import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { StarWarsMoviesModule } from './star-wars-movies.module';
import { StarWarsMoviesComponent } from './star-wars-movies/star-wars-movies.component';
import { MovieCardComponent } from './movie-card/movie-card.component';

@NgModule({
  declarations: [
    AppComponent,
    StarWarsMoviesComponent,
    MovieCardComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    StarWarsMoviesModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
