from data import PLAN_LISTS_WITH_BOOK_NUMBERS as lists_data
from data import BIBLE_BOOK_NUMBER_TO_NUMBER_OF_CHAPTERS as chapter_counts
from data import BIBLE_BOOK_NUMBER_TO_UKRAINIAN_NAME as Ukrainian_Book_names

def get_next_reading_for_list(
    list_index:int,
    Book_index:int,
    chapter_number:int
):
    # Get data with Book numbers for currently selected Bible reading list
    list_data=lists_data[list_index]

    # Get a Book number from a selected Book index
    Book_number = list_data[Book_index]

    # Get a number of existing chapters for currently selected Bible Book
    available_chapters = chapter_counts[Book_number]

    # If there are more Chapters to be read in this Book
    if chapter_number < available_chapters:
        # Simply increment our chapter while we can
        chapter_number += 1

    # If current chapter exceeds available chapters for the current Bible Book
    else:
        # Reset the chapter number back to one since we will be switching to a next Book on a list
        chapter_number = 1

        # First check if there are any more Books further in a list
        if Book_index < len(list_data)-1:
            # Then we simply switch to the next Book in a list 
            Book_index += 1
        else:
            # If there are no more Book to read further in a list, then we restart our list
            Book_index = 0

    return Book_index,chapter_number

li=3
bi,cn=0,0
for _ in range(12):
    bi,cn=get_next_reading_for_list(li,bi,cn)
    ld=lists_data[li]
    bn=ld[bi]
    print(Ukrainian_Book_names[bn],cn)
