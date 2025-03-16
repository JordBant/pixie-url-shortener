import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn (...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
/**
 * To use for testing
 * 
 * @param borderColor 
 * @param borderWidth 
 * @returns 
 */
export function testCSSBorders (borderColor: string = "blue-500", borderWidth: number = 2) {
  const reconciledStyles = borderColor.split('').indexOf('-') >= 0 ? borderColor : `[${borderColor}]`;
  return `border-[${borderWidth}px] border-solid border-${reconciledStyles}`;
}