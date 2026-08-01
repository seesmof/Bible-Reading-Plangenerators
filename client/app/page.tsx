"use client";

import { Point } from "@/lib/data";
import { calculateDay } from "@/lib/utils";
import React, { useState } from "react";

export default function IndexPage() {
  const [day, setDay] = useState<number>(1);
  const [results, setResults] = useState<{ book: Point; chapter: number }[]>([
    {
      book: { id: 1, engAbbr: "GEN", ukrName: "Буття", chaptersNum: 50 },
      chapter: 1,
    },
    {
      book: { id: 40, engAbbr: "MAT", ukrName: "Матей", chaptersNum: 28 },
      chapter: 1,
    },
  ]);

  const handleDaySubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const result = calculateDay(day);
  };

  return (
    <div className="min-h-screen bg-sky-50">
      <div className="mx-auto max-w-md p-3 flex flex-col gap-3">
        <div className="bg-white p-3 rounded-md shadow">
          <form className="flex gap-3" onSubmit={handleDaySubmit}>
            <input
              type="number"
              className="px-2 py-1 rounded-md border w-full border-sky-600"
              min={1}
              value={day}
              onChange={(e) => setDay(Number.parseInt(e.target.value))}
            />
            <button
              type="submit"
              className="bg-sky-600 text-white px-4 rounded-md hover:bg-sky-700 cursor-pointer"
            >
              Show
            </button>
          </form>
        </div>
        <div className="bg-white p-3 rounded-md shadow flex flex-col">
          {results.map((result, index) => (
            <div className="flex gap-3" key={index}>
              <input type="checkbox" id={result.book.id.toString()}></input>
              <label htmlFor={result.book.id.toString()}>
                {result.book.ukrName} {result.chapter}
              </label>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
