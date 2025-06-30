import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'selector-name',
    template: ` 
        <section className="z-20 sticky top-0 w-full pt-[5px]">
            <div className="w-[50%] mx-auto relative mt-auto">
            </div>
        </section>
    `
})

export class NameComponent implements OnInit {
    constructor () { }

    ngOnInit () { }
}