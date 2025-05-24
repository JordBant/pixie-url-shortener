import { useCallback, useEffect, useRef, useState } from "react";
import { ShortenerView } from "../../components/ShortenerView/ShortenerView";

export default function Shortener() {
  const [shouldCollapse] = useState(false);
  const shortenerRef = useRef<HTMLDivElement>();

  // const memoizedVH = useMemo(
  //   () => convertToViewportHeight(pixelHeight),
  //   [convertToViewportHeight, pixelHeight]
  // );

  const handleScroll = useCallback(() => {
    // if (shortenerRef.current) {
    //   const client = shortenerRef.current;
    //   const wind = window.innerHeight;
    // setShouldCollapse(spaceFromTop <= heightOfInput);
    // console.log({ client, wind });
    // console.log(convertToViewportHeight(spaceFromTop));
    // }
  }, []);

  useEffect(() => {
    document.addEventListener("scroll", handleScroll);
    console.log(shouldCollapse);

    return () => {
      document.removeEventListener("scroll", handleScroll);
    };
  }, [handleScroll]);

  return <ShortenerView ref={shortenerRef} isCollapsed={shouldCollapse} />;
}
