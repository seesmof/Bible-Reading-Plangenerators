from data import PLAN_LISTS_WITH_BOOK_NUMBERS as lists_data

def get_next_reading_for_list(
    current_list_index:int,
    current_Book_number:int,
    current_chapter_number:int
):
    print(lists_data[current_list_index])

get_next_reading_for_list(0,0,0)