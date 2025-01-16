import { useRef } from "react";
import NavbarView from "../../components/NavbarView/NavbarView";
import { Item } from "../../components/NavbarView/NavbarView.types";

export default function Navbar() {
  const headerRef = useRef<HTMLElement | null>(null);
  const items: Item[] = [
    { text: "Pricing" },
    { text: "Visualization" },
    { text: "Username" },
  ];

  return <NavbarView ref={headerRef} navbarItemsProps={{ items }} />;
}
