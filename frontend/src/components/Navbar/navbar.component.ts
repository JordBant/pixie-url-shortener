import { Component } from "@angular/core";

@Component({
    selector: 'pxy-navbar',
    standalone: true,
    template: `
    <header
      className="fixed w-full bg-zinc-900 z-10"
    >
      <section className="w- full mx - auto px - 4">
        <nav className="flex h-16 items-center justify-between">
          <div className="flex items-center space-x-2">
            <!-- <Droplet className="h-6 w-6 text-white" /> -->
            <span className="text-xl font-semibold text-white">Pixie</span>
          </div>
          <!-- <NavbarItems {...navbarItemsProps} /> -->
        </nav>
      </section>
    </header>
    `
})


export class Navbar {
    constructor () { }
}