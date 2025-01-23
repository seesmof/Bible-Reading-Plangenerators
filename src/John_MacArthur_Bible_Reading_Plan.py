'''
JESUS CHRIST IS LORD

From some of his sermons, pastor John MacArthur recommended reading the Holy Bible in this way: for the Old Testament to read simply from Genesis until Matthew chapter by chapter; for the New Testament to read one smaller Book for a month reading It each day, and then moving onto a larger Book, dividing it into smaller parts and reading those parts each for 30 days. He recommended starting with 1 John, then moving onto John (3 times reading 7 new chapters for 30 days each), then Philippians, and then go to Matthew, then to Colossians, then to Acts, and so on.

This program focuses specifically on the New Testament, because it's not as easy to set up as the Old Testament reading. When run, it should generate the complete New Testament Bible reading plan with each section repeating 33 times. Sections might be entire books (if under 7 chapters long) or parts of larger Books. The entire plan should take a bit over 4 years to complete if reading one reading per day.
'''

from util import *
from Grant_Horner_Bible_Reading_Plan import get_eBible_reading_link

from util.const import BIBLE_BOOK_NUMBER_TO_NUMBER_OF_CHAPTERS as chapters_data
from util.const import BIBLE_BOOK_NUMBER_TO_UKRAINIAN_NAME as Book_names

only_New_Testament={k:v for k,v in chapters_data.items() if k>=40}
from_least_to_most_chapters=sorted(only_New_Testament.items(),key=lambda d:d[-1])
from_least_to_most_chapters_dict=dict(from_least_to_most_chapters)

lines=[]
REPEAT_BOOK_TIMES=33

smaller_Books={k:v for k,v in from_least_to_most_chapters_dict.items() if v<=6}
for Book_number,chapters_count in smaller_Books.items():
    link=get_eBible_reading_link(Book_number,1)
    markdown_link=f'[{Book_names[Book_number]} 1-{chapters_count}]({link})' if chapters_count>1 else f'[{Book_names[Book_number]} 1]({link})'
    local=[markdown_link+f' {reading_counter}' for reading_counter in range(1,REPEAT_BOOK_TIMES+1)]
    lines.append('\n'.join(local))

MAX_CONSECUTIVE_CHAPTERS=7
bigger_Books={k:v for k,v in from_least_to_most_chapters_dict.items() if v>6}
for Book_number,chapters_count in bigger_Books.items():
    current_chapter=1
    number_of_chapters_for_this_Book=chapters_count
    amount_of_chapters_to_read=chapters_count//4 if chapters_count//3>MAX_CONSECUTIVE_CHAPTERS else chapters_count//3 if chapters_count//2>MAX_CONSECUTIVE_CHAPTERS else chapters_count//2

    for _ in range(4 if chapters_count//3>MAX_CONSECUTIVE_CHAPTERS else 3 if chapters_count//2>MAX_CONSECUTIVE_CHAPTERS else 2):
        link=get_eBible_reading_link(Book_number,current_chapter)
        markdown_link=f'[{Book_names[Book_number]} {current_chapter}-{current_chapter-1+amount_of_chapters_to_read if current_chapter+amount_of_chapters_to_read<number_of_chapters_for_this_Book else number_of_chapters_for_this_Book}]({link})'
        local=[markdown_link+f' {reading_counter}' for reading_counter in range(1,REPEAT_BOOK_TIMES+1)]
        lines.append('\n'.join(local))
        current_chapter+=amount_of_chapters_to_read
        chapters_count-=current_chapter

target_file=os.path.join(root_folder_path,'out.md')
try:
    with open(target_file,encoding='utf-8',mode='w') as f:
        f.write('\n'.join(lines))
except: pass
