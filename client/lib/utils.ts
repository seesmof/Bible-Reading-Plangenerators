import { HornerData } from "./data";

export const calculateDay = (day: number) => {
  for (const [key, value] of Object.entries(HornerData)) {
    console.log(key);
  }
};
