import os
import util
from util.const import BIBLE_BOOK_NUMBER_TO_NUMBER_OF_CHAPTERS as chapter_numbers
from util.const import BIBLE_BOOK_NUMBER_TO_UKRAINIAN_NAME as Book_names
from Grant_Horner_Bible_Reading_Plan import get_eBible_reading_link

res=[]
for B in range(1,66+1):
    Bn=Book_names[B]
    for c in range(1,chapter_numbers[B]+1):
        l=get_eBible_reading_link(B,c)
        t=f'[{Bn} {c}]({l})'
        res.append(t)

target_file=os.path.join(util.root_folder_path,'out.md')
try:
    with open(target_file,encoding='utf-8',mode='w') as f:
        f.write('\n'.join(res))
except: pass
