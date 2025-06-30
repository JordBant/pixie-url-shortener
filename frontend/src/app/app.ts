import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  // styleUrl: './app.scss',
  template: `
  <main class="text-3xl font-bold underline">
    Is my tailwind alive
  </main>
  `,
  // templateUrl: './app.html',
  imports: []
})
export class App {
  protected title = 'frontend';
}
