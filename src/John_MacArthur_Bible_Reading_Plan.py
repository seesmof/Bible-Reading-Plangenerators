'''
JESUS CHRIST IS LORD

From some of his sermons, pastor John MacArthur recommended reading the Holy Bible in this way: for the Old Testament to read simply from Genesis until Matthew chapter by chapter; for the New Testament to read one smaller Book for a month reading It each day, and then moving onto a larger Book, dividing it into smaller parts and reading those parts each for 30 days. He recommended starting with 1 John, then moving onto John (3 times reading 7 new chapters for 30 days each), then Philippians, and then go to Matthew, then to Colossians, then to Acts, and so on.
'''

from util import *

from util.const import BIBLE_BOOK_NUMBER_TO_NUMBER_OF_CHAPTERS as chapters_data
from util.const import BIBLE_BOOK_NUMBER_TO_UKRAINIAN_NAME as Book_names

only_New_Testament=[e for e in chapters_data.items() if e[0]>=40]
only_New_Testament_dict=dict(only_New_Testament)
from_least_to_most_chapters=sorted(only_New_Testament_dict.items(),key=lambda d:d[-1])
from_least_to_most_chapters_dict=dict(from_least_to_most_chapters)

'''
for k,v in from_least_to_most_chapters_dict.items():
    print(Book_names[k],v)
'''