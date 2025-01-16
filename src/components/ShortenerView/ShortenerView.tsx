// import React, { useState, useEffect, useRef, useCallback } from "react";
// import { Input } from "@/components/ui/input"
import { Input } from "./Input";
import { Search } from "lucide-react";
import { ShortenerViewProps } from "./ShortenerView.types";
import { forwardRef, LegacyRef } from "react";
import { testCSSBorders } from "../../lib/utils";

export const ShortenerView = forwardRef(
  (
    { isCollapsed = false }: ShortenerViewProps,
    ref: LegacyRef<HTMLDivElement>
  ): React.ReactElement => {
    return (
      <>
        <div className="h-[45vh]" aria-hidden="true"></div>
        <section
          ref={ref}
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
      </>
    );
  }
);
