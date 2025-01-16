
export type Item = {
    text: string;
    link?: string;
    onClick?: () => void;
};

export type ItemViewProps = {
    items: Item[];
};

export type NavbarViewProps = {
    navbarItemsProps: ItemViewProps;
};
