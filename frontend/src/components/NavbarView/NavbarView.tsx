import React, { forwardRef, LegacyRef } from "react";
import { Droplet } from "lucide-react";
import NavbarItems from "./ItemsView";
import { NavbarViewProps } from "./NavbarView.types";
import { testCSSBorders } from "../../lib/utils";
import Shortener from "../../containers/Shortener/Shortener";

const NavbarView = forwardRef(({ navbarItemsProps }: NavbarViewProps, ref) => {
  return (
    <header
      className="fixed w-full bg-zinc-900 z-10"
      ref={ref as LegacyRef<HTMLElement> | undefined}
    >
      <section className={`w-full mx-auto px-4`}>
        <nav className="flex h-16 items-center justify-between">
          <div className="flex items-center space-x-2">
            <Droplet className="h-6 w-6 text-white" />
            <span className="text-xl font-semibold text-white">Pixie</span>
          </div>
          <NavbarItems {...navbarItemsProps} />
        </nav>
      </section>
    </header>
  );
});

export default NavbarView;
