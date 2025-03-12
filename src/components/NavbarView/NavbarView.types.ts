
export type Item = {
    text: string;
    link?: string;
    onClick?: () => void;
};

export type ItemViewProps = {
    allItems: Item[];
};

export type NavbarViewProps = {
    navbarItemsProps: ItemViewProps;
};
