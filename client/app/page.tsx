"use client";

import { calculateDay } from "@/lib/util";
import React, { useState } from "react";

export default function IndexPage() {
  const [day, setDay] = useState<number>(1);
  const [result, setResult] = useState<string>("");

  const handleDaySubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const result = calculateDay(day);
    setResult(result);
  };

  return (
    <div className="min-h-screen bg-sky-50">
      <div className="mx-auto max-w-md p-3 flex flex-col gap-3">
        <div className="bg-white p-3 rounded-md shadow">
          <form className="flex gap-1" onSubmit={handleDaySubmit}>
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
          {result}
        </div>
      </div>
    </div>
  );
}
