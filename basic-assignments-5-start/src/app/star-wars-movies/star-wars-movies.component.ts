import { Component } from '@angular/core';
import { FILMS } from '../star-wars-fake-db/film-data';
import { StarWarsMovie } from '../star-wars-movies-interface';

@Component({
  selector: 'app-star-wars-movies',
  templateUrl: './star-wars-movies.component.html',
  styleUrls: ['./star-wars-movies.component.scss']
})
export class StarWarsMoviesComponent {
  starWars: StarWarsMovie[] = FILMS;
}
