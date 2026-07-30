import { BibleData, HornerData } from "@/lib/data";

export default function IndexPage() {
  return (
    <p className="p-3">
      {BibleData.find((book) => book.id === HornerData.Prophets[0])?.ukrName}
    </p>
  );
}
