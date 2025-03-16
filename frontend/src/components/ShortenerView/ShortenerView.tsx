import { Input } from "./Input";
import { Search } from "lucide-react";
import { forwardRef, LegacyRef } from "react";
import { testCSSBorders } from "../../lib/utils";
import { ShortenerViewProps } from "./ShortenerView.types";

export const ShortenerView = forwardRef(
  ({ isCollapsed }: ShortenerViewProps, ref): React.ReactElement => {
    console.log(isCollapsed);
    return (
      <>
        <div className="h-[45vh]" aria-hidden="true" />
        <section
          ref={ref as LegacyRef<HTMLElement> | undefined}
          className={`z-20 sticky top-0 w-full pt-[5px] ${testCSSBorders(
            "red-500"
          )}`}
        >
          <div className="w-[50%] mx-auto relative mt-auto">
            <Input
              type="search"
              placeholder="Search..."
              className="h-14 pl-12 pr-4 text-lg rounded-full shadow-lg focus:ring-2 focus:ring-blue-500"
              aria-label="Search"
            />
            {/* Search Icon */}
            <Search
              className="absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400"
              size={24}
              aria-hidden="true"
            />
          </div>
        </section>
        <div className="h-[55vh]" aria-hidden="true" />
      </>
    );
  }
);
