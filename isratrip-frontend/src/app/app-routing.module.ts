import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegisterFormComponent } from './register-form/register-form.component';
import { LoginFormComponent } from './login-form/login-form.component';
import { RequestTripFormComponent } from './request-trip-form/request-trip-form.component';

const routes: Routes = [];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
const appRoutes: Routes = [
  { path: 'request-new-trip', component: RequestTripFormComponent },
  { path: 'register',        component: RegisterFormComponent },
  { path: 'login',   component: LoginFormComponent}
];