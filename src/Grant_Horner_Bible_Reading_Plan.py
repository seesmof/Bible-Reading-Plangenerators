import json
import os

from util.const import BIBLE_BOOK_NUMBER_TO_ENGLISH_TINY_ABBREVIATION as eBible_abbreviations
from util.const import BIBLE_BOOK_NUMBER_TO_ENGLISH_SHORT_ABBREVIATION as English_Book_names
from util.const import BIBLE_BOOK_NUMBER_TO_HOMENKO_BIBLE_NAME as Ukrainian_Book_names
from util.const import BIBLE_BOOK_NUMBER_TO_NUMBER_OF_CHAPTERS as chapter_counts
from util.const import BIBLE_BOOK_NUMBER_TO_GERMAN_NAME as German_Book_names
from util.const import CUSTOM_HORNER_PLAN_LISTS as lists_data
import util

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

class eBibleTranslations:
    Kulish = "ukr1871"
    Freedom = "ukrfb"

def get_eBible_reading_link(
    Book_number: int = 1,
    chapter_number: int = 12,
    translation: eBibleTranslations = eBibleTranslations.Kulish,
):
    # This is how a typical eBible.org reading link looks like
    base_link = "https://ebible.org/study/?w1=bible&t1=local:"

    # Form a Bible Book Abbreviation specific to eBible.org, data taken from a constant variable
    Book_name_abbreviation = eBible_abbreviations[Book_number]
    # Form a link in a format that eBible.org uses
    ready_link = f'{base_link}{translation}&v1={Book_name_abbreviation}{chapter_number}'

    # And return it back to the user 
    return ready_link

class BollsTranslations:
    Kulish = "UKRK"
    Homenko = "HOM"

def get_Bolls_reading_link(
    Book: int = 1,
    chapter: int = 12,
    translation: BollsTranslations = BollsTranslations.Kulish,
):
    base=f'https://bolls.life/{translation}'
    ready=f'{base}/{Book}/{chapter}/'
    return ready

def get_local_reading_link(
    Book:int,
    chapter:int,
):
    # [[Біблія Куліша#GEN 1|GEN 1]]
    base=r'[[Біблія Куліша#'
    Book_abbreviation=English_Book_names[Book]
    ref=f'{Book_abbreviation} {chapter}'
    return f'{base}{ref}|{ref}]]'

def get_formatted_link(
    Book_number:int,
    chapter_number:int,
    language='UK',
    link_type='MDE',
    link_source='EBIBLE',
):
    reading_link=get_Bolls_reading_link(Book_number,chapter_number)

    if language=='UK': Book_name=Ukrainian_Book_names[Book_number]
    elif language=='Language.EN': Book_name=English_Book_names[Book_number]
    elif language=='Language.DE': Book_name=German_Book_names[Book_number]

    if link_type=='MDI': link=reading_link
    elif link_type=='MDE': link=f'[{Book_name} {chapter_number}]({reading_link})'
    elif link_type=='HTML': link=f'<a href="{reading_link}">{Book_name} {chapter_number}</a>'
    elif link_type=='NO': link=f'{Book_name} {chapter_number}'

    return link

CURRENT_DAY=238

lines=[]
for day in range(CURRENT_DAY,CURRENT_DAY+366):
    plan_for_day=get_reading_for_day(day)
    for i,reading in enumerate(plan_for_day):
        Book,chapter=reading
        link=get_formatted_link(Book,chapter)
        lines.append(link+f" день {day}" if i==0 else link)

target_file=os.path.join(util.results_folder_path,'GH.md')
with open(target_file,encoding='utf-8',mode='w') as f:
    f.writelines([l+'\n' for l in lines])