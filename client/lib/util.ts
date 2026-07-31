import { HornerData } from "./data";

export const calculateDay = (day: number): string => {
  for (const [key, value] of Object.entries(HornerData)) {
    console.log(key, value);
  }
  return "";
};
