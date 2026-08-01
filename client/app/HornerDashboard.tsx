"use client";

import React from "react";
import { useHornerPlan, GroupName } from "@/hooks/useHornerPlan"; // змініть шлях на ваш

// Словник для гарних українських назв категорій
const groupTitles: Record<GroupName, string> = {
  Pentateuch: "П'ятикнижжя",
  History: "Історичні книги",
  Wisdom: "Книги Мудрості",
  Psalms: "Псалми",
  Proverbs: "Приповісті",
  Prophets: "Пророки",
  Gospels: "Євангелія",
  Acts: "Діяння",
  Pauline: "Послання Павла",
  Epistles: "Загальні послання & Об'явлення",
};

export default function HornerDashboard() {
  const { readings, checkTrackAsRead, uncheckTrack, isLoaded } =
    useHornerPlan();

  if (!isLoaded) {
    return (
      <div className="text-center py-10 text-gray-500 animate-pulse">
        Завантаження плану читання...
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto p-4 md:p-8">
      <header className="mb-8 text-center">
        <h1 className="text-3xl font-extrabold text-slate-950 mb-2">
          Система читання Біблії Гранта Горнера
        </h1>
        <p className="text-sm text-gray-500">
          10 розділів щодня. Слово Христове нехай перебуває в вас рясно!
        </p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {readings.map((track) => (
          <div
            key={track.groupName}
            className="border border-slate-100 rounded-2xl p-5 bg-white shadow-sm hover:shadow-md transition-shadow flex flex-col justify-between"
          >
            {/* Верхня частина картки */}
            <div>
              <div className="flex justify-between items-start mb-2">
                <span className="text-xs font-bold uppercase tracking-wider text-amber-600 bg-amber-50 px-2.5 py-1 rounded-full">
                  {groupTitles[track.groupName]}
                </span>
                {track.completedRounds > 0 && (
                  <span className="text-xs bg-emerald-50 text-emerald-700 px-2 py-0.5 rounded-md font-medium">
                    Прочитано кіл: {track.completedRounds} 🔄
                  </span>
                )}
              </div>

              {/* Велика назва книги та розділу */}
              <h3 className="text-2xl font-bold text-slate-800 my-3">
                {track.currentBook.ukrName}{" "}
                <span className="text-amber-600">{track.currentChapter}</span>
              </h3>

              <p className="text-xs text-slate-400 mb-4">
                Код книги: {track.currentBook.engAbbr} | День у списку:{" "}
                {track.currentDayForGroup}
              </p>
            </div>

            {/* Нижня частина: Прогрес-бар та Кнопки дії */}
            <div className="mt-4">
              {/* Прогрес бар */}
              <div className="mb-4">
                <div className="flex justify-between text-xs text-slate-500 mb-1">
                  <span>Прогрес кола</span>
                  <span>
                    {track.currentRoundChapterNumber} / {track.totalChapters}{" "}
                    розд. ({track.progressPercent}%)
                  </span>
                </div>
                <div className="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
                  <div
                    className="bg-amber-500 h-full transition-all duration-300"
                    style={{ width: `${track.progressPercent}%` }}
                  />
                </div>
              </div>

              {/* Кнопки управління */}
              <div className="flex gap-2">
                <button
                  onClick={() => checkTrackAsRead(track.groupName)}
                  className="flex-1 bg-slate-900 hover:bg-slate-800 text-white text-sm font-semibold py-2.5 px-4 rounded-xl transition-colors active:scale-[0.98]"
                >
                  Прочитано ✓
                </button>
                <button
                  onClick={() => uncheckTrack(track.groupName)}
                  disabled={track.currentDayForGroup <= 1}
                  className="bg-slate-100 hover:bg-slate-200 text-slate-600 text-sm font-medium py-2.5 px-3 rounded-xl transition-colors disabled:opacity-40 disabled:hover:bg-slate-100"
                  title="Повернутися на розділ назад"
                >
                  ↩
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
