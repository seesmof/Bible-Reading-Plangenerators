from data import PLAN_LISTS_WITH_BOOK_NUMBERS as lists_data
from data import BIBLE_BOOK_NUMBER_TO_NUMBER_OF_CHAPTERS as chapter_counts
from data import BIBLE_BOOK_NUMBER_TO_UKRAINIAN_NAME as Ukrainian_Book_names

def get_next_reading_for_list(
    list_index:int,
    Book_index:int,
    chapter_number:int
):
    # Get a list of Book numbers for current list
    list_data=lists_data[list_index]

    # Get a Book number from the selected list
    Book_number = list_data[Book_index]

    # Get a number of available chapters for the current Book
    available_chapters = chapter_counts[Book_number]

    # Check if there are more chapters to read for this Book
    if chapter_number < available_chapters:
        # If so, move to the next chapter
        chapter_number += 1

    # If there are no more chapters for the current Book
    else:
        # Then set a chapter into 1 since wee will be moving to the next Book
        chapter_number = 1

        # Now check if there are move Books in a list
        if Book_index < len(list_data)-1:
            # If so then move to the next Book
            Book_index += 1
        
        # If there are no more Books to read from in a list
        else:
            # Then restart the list and read the first Book
            Book_index = 0

    return Book_index,chapter_number

def get_next_reading_for_day(
    day_number:int,
):
    data=[]
    for li in range(10):
        cd=0
        bi,cn=0,0
        while cd!=day_number:
            bi,cn=get_next_reading_for_list(li,bi,cn)
            ld=lists_data[li]
            bn=ld[bi]

            cd+=1
            if cd==day_number:
                data.append((bn,cn))
    return data

data=get_next_reading_for_day(68)
for r in data:
    bn,cn=r
    print(Ukrainian_Book_names[bn],cn)