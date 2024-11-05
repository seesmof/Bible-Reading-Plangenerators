from data import PLAN_LISTS_WITH_BOOK_NUMBERS as lists_data
from data import BIBLE_BOOK_NUMBER_TO_NUMBER_OF_CHAPTERS as chapter_counts
from data import BIBLE_BOOK_NUMBER_TO_UKRAINIAN_NAME as Ukrainian_Book_names
from data import BIBLE_BOOK_NUMBER_TO_TINY_ABBREVIATION as eBible_abbreviations

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

def get_reading_for_day(
    day_number:int,
):
    # Will be forming a list of tuples
    # Each tuple will contain: Bible Book Number, and a Chapter Number
    reading_data=[]

    # Form readings for of the 10 lists
    for list_index in range(10):
        # Keep track of current day, start with 0
        current_day=0
        # Initialize Book Index and Chapter Number to zeros
        Book_index,chapter_number=0,0

        # Keep getting readings for next day until we reach the target day
        while current_day!=day_number:
            # Update Book Index and Chapter Number with each iteration
            Book_index,chapter_number=get_next_reading_for_list(list_index,Book_index,chapter_number)
            
            # Move to the next day
            current_day+=1
            # Now check if we reached our target day
            if current_day==day_number:
                # Then form a Book Number by first getting the current list, then selected the current Book by index
                Book_number=lists_data[list_index][Book_index]
                # Add Book Number and Chapter Number to the Reading List
                reading_data.append((Book_number,chapter_number))
    
    # And return the formed list
    return reading_data

def get_reading_link(
    Book_number:int,
    chapter_number:int,
):
    # This is how a typical eBible.org reading link looks like
    base_link = "https://ebible.org/study/?w1=bible&t1=local%3A"

    # Version can be later changed as a parameter
    translation_abbreviation = 'ukr1871'
    # Form a Bible Book Abbreviation specific to eBible.org, data taken from a constant variable
    Book_name_abbreviation = eBible_abbreviations[Book_number]
    # Form a link in a format that eBible.org uses
    ready_link = f'{base_link}{translation_abbreviation}&v1={Book_name_abbreviation}{chapter_number}'

    # And return it back to the user 
    return ready_link

data=get_reading_for_day(68)
for r in data:
    bn,cn=r
    print(Ukrainian_Book_names[bn],cn,get_reading_link(bn,cn))