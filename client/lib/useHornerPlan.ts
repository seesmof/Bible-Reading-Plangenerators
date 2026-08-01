import { useState, useEffect } from "react";
// Імпортуйте ваші BibleData, HornerData та функцію generateFlatListForGroup з попереднього кроку
import { BibleData, HornerData } from "./data";

export type GroupName = keyof typeof HornerData;

// Зберігаємо для кожного списку його "поточний день читання" (починаючи з 1)
type PlanProgress = Record<GroupName, number>;

const initialProgress: PlanProgress = {
  Pentateuch: 1,
  History: 1,
  Wisdom: 1,
  Psalms: 1,
  Proverbs: 1,
  Prophets: 1,
  Gospels: 1,
  Acts: 1,
  Pauline: 1,
  Epistles: 1,
};

// Заздалегідь рахуємо статичні дані списків, щоб не робити це при кожному рендері
const LIST_DETAILS = Object.entries(HornerData).reduce(
  (acc, [groupName, bookIds]) => {
    const chapters: { bookId: number; chapter: number }[] = [];
    let totalChaptersInGroup = 0;

    for (const id of bookIds) {
      const book = BibleData.find((b) => b.id === id);
      if (book) {
        totalChaptersInGroup += book.chaptersNum;
        for (let ch = 1; ch <= book.chaptersNum; ch++) {
          chapters.push({ bookId: id, chapter: ch });
        }
      }
    }

    acc[groupName as GroupName] = {
      chapters,
      totalChapters: totalChaptersInGroup,
    };
    return acc;
  },
  {} as Record<
    GroupName,
    { chapters: { bookId: number; chapter: number }[]; totalChapters: number }
  >,
);

export function useHornerPlan() {
  const [progress, setProgress] = useState<PlanProgress>(initialProgress);
  const [isLoaded, setIsLoaded] = useState(false);

  // Гідрація для Next.js (SSR безпека)
  useEffect(() => {
    const saved = localStorage.getItem("horner_progress");
    if (saved) {
      try {
        setProgress(JSON.parse(saved));
      } catch (e) {
        console.error(e);
      }
    }
    setIsLoaded(true);
  }, []);

  const saveProgress = (newProgress: PlanProgress) => {
    setProgress(newProgress);
    localStorage.setItem("horner_progress", JSON.stringify(newProgress));
  };

  // Відмітити список як прочитаний (перейти на наступний день для цієї групи)
  const checkTrackAsRead = (groupName: GroupName) => {
    const newProgress = { ...progress, [groupName]: progress[groupName] + 1 };
    saveProgress(newProgress);
  };

  // Повернутися на крок назад (якщо випадково промахнулися)
  const uncheckTrack = (groupName: GroupName) => {
    if (progress[groupName] <= 1) return;
    const newProgress = { ...progress, [groupName]: progress[groupName] - 1 };
    saveProgress(newProgress);
  };

  // Розрахунок поточних даних для інтерфейсу
  const UIReadings = Object.keys(HornerData).map((key) => {
    const groupName = key as GroupName;
    const currentDayForGroup = progress[groupName];
    const { chapters, totalChapters } = LIST_DETAILS[groupName];

    // Рахуємо індекс у колі
    const currentIndex = (currentDayForGroup - 1) % totalChapters;
    const currentChapterData = chapters[currentIndex];
    const currentBook = BibleData.find(
      (b) => b.id === currentChapterData.bookId,
    )!;

    // Розрахунок прогресу всередині поточного кола (відсотки)
    const currentRoundChapterNumber = currentIndex + 1;
    const progressPercent = Math.round(
      (currentRoundChapterNumber / totalChapters) * 100,
    );

    // Скільки повних кіл (разів) цей список вже прочитано
    const completedRounds = Math.floor(
      (currentDayForGroup - 1) / totalChapters,
    );

    return {
      groupName,
      currentDayForGroup,
      currentBook,
      currentChapter: currentChapterData.chapter,
      progressPercent,
      completedRounds,
      currentRoundChapterNumber,
      totalChapters,
    };
  });

  return {
    isLoaded,
    readings: UIReadings,
    checkTrackAsRead,
    uncheckTrack,
    progress,
  };
}
