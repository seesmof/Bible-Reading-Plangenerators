import os
import util
from util.const import BIBLE_BOOK_NUMBER_TO_NUMBER_OF_CHAPTERS as chapter_numbers
from util.const import BIBLE_BOOK_NUMBER_TO_KULISH_BIBLE_NAME as Book_names
from Grant_Horner_Bible_Reading_Plan import get_Bolls_reading_link, get_eBible_reading_link

res=[]
for B in range(1,40):
    Bn=Book_names[B]
    for c in range(1,chapter_numbers[B]+1):
        l=get_Bolls_reading_link(B,c)
        t=f'[{Bn} {c}]({l})'
        res.append(t)

target_file=os.path.join(util.results_folder_path,'OT.md')
try:
    with open(target_file,encoding='utf-8',mode='w') as f:
        f.write('\n'.join(res))
except: pass
