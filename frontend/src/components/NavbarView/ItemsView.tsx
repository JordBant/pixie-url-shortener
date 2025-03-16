import React from "react";
import { ItemViewProps } from "./NavbarView.types";

export default function Items({ items }: ItemViewProps) {
  return (
    <ul className="flex items-center space-x-8">
      {items.map(({ link = "#", text }, idx) => {
        return (
          <li key={`${text}-${idx}`}>
            <a
              href={link}
              className="text-zinc-300 hover:text-white transition-colors"
            >
              {text}
            </a>
          </li>
        );
      })}
    </ul>
  );
}
