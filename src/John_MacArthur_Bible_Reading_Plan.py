'''
JESUS CHRIST IS LORD

From some of his sermons, pastor John MacArthur recommended reading the Holy Bible in this way: for the Old Testament to read simply from Genesis until Matthew chapter by chapter; for the New Testament to read one smaller Book for a month reading It each day, and then moving onto a larger Book, dividing it into smaller parts and reading those parts each for 30 days. He recommended starting with 1 John, then moving onto John (3 times reading 7 new chapters for 30 days each), then Philippians, and then go to Matthew, then to Colossians, then to Acts, and so on.
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
for k,v in smaller_Books.items():
    link=get_eBible_reading_link(k,1)
    markdown_link=f'[{Book_names[k]}]({link})'
    local=[markdown_link for _ in range(1,REPEAT_BOOK_TIMES+1)]
    lines.append('\n'.join(local))

print()
bigger_Books={k:v for k,v in from_least_to_most_chapters_dict.items() if v>6}
for k,v in bigger_Books.items():
    Book_reference=f"{Book_names[k]} {v}"
    link=get_eBible_reading_link(k,1)
    markdown_link=f'[{Book_reference}]({link})'
    # lines.append(markdown_link)

    print(Book_names[k],v)
    if v//2>6:
        if v//3>6:
            if v//4>6:
                print(v//4,5)

target_file=os.path.join(root_folder_path,'out.md')
try:
    with open(target_file,encoding='utf-8',mode='w') as f:
        f.write('\n'.join(lines))
except: pass
