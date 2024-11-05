from data import PLAN_LISTS_WITH_BOOK_NUMBERS as lists_data
from data import BIBLE_BOOK_NUMBER_TO_NUMBER_OF_CHAPTERS as chapter_counts

def get_next_reading_for_list(
    list_index:int,
    Book_index:int,
    chapter_number:int
):
    # Get data with Book numbers for currently selected Bible reading list
    current_list_data=lists_data[list_index]

    # Get a Book number from a selected Book index
    selected_Book_number = current_list_data[Book_index]

    # Get a number of existing chapters for currently selected Bible Book
    available_chapters = chapter_counts[selected_Book_number]

    print(current_list_data)
    print(selected_Book_number)
    print(available_chapters)

    if chapter_number < available_chapters:
        chapter_number += 1

get_next_reading_for_list(0,0,0)