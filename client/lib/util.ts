import { BibleData, HornerData, Point } from "./data";

// Тип для результату денного читання
export type ReadingItem = {
  listName: string;
  book: Point;
  chapter: number;
};

/**
 * Генерує плоский список усіх розділів для конкретного списку Горнера
 */
function generateFlatListForGroup(
  bookIds: number[],
): { book: Point; chapter: number }[] {
  const flatList: { book: Point; chapter: number }[] = [];

  for (const id of bookIds) {
    const book = BibleData.find((b) => b.id === id);
    if (!book) continue;

    // Додаємо кожен розділ книги у загальний масив списку
    for (let ch = 1; ch <= book.chaptersNum; ch++) {
      flatList.push({ book, chapter: ch });
    }
  }

  return flatList;
}

// Попередньо генеруємо та кешуємо всі 10 списків для швидкого доступу
const HORNER_FLAT_LISTS = Object.entries(HornerData).map(
  ([groupName, bookIds]) => ({
    groupName,
    chapters: generateFlatListForGroup(bookIds),
  }),
);

/**
 * Повертає 10 розділів для читання на заданий день
 * @param dayNumber Порядковий день плану (починаючи з 1)
 */
export function getHornerReadingForDay(dayNumber: number): ReadingItem[] {
  if (dayNumber < 1) {
    throw new Error("Day number must be 1 or greater");
  }

  return HORNER_FLAT_LISTS.map(({ groupName, chapters }) => {
    // Важливий момент: робимо зсув на -1, оскільки масиви починаються з 0 індексу, а дні з 1
    const targetIndex = (dayNumber - 1) % chapters.length;
    const reading = chapters[targetIndex];

    return {
      listName: groupName,
      book: reading.book,
      chapter: reading.chapter,
    };
  });
}

// --- ПРИКЛАД ВИКОРИСТАННЯ ---
const day = 1; // Перший день плану
const readings = getHornerReadingForDay(day);

console.log(`=== ЧИТАННЯ НА ДЕНЬ ${day} ===`);
readings.forEach((item) => {
  console.log(
    `[${item.listName}] -> ${item.book.ukrName} (${item.book.engAbbr}), розділ ${item.chapter}`,
  );
});
