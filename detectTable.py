import os, time, ocr_functions
from pdf2image import convert_from_path
import pandas as pd

def detect_table(pdf_path):
    try:
        time_begin = time.time()
        detect_info = []
        file_name = pdf_path.split('\\')[-1]
        SAVE_IMG_FOLDER = os.path.join(r'C:\Users\patcharapol.y\Desktop\Projects\New folder\VS code\OCR', 'pictures')
        if not os.path.exists(SAVE_IMG_FOLDER):
            os.mkdir(SAVE_IMG_FOLDER)
        detect_info.append(file_name)
        dpi=300
        first_page, last_page = 5, 7
        for loop in range(0,6):
            pages = convert_from_path(pdf_path=pdf_path, dpi=300, first_page=first_page, last_page=last_page)
            index, page_table = ocr_functions.find_table(pages)
            page_num = [idx+first_page for idx in index]
            if len(page_table) > 0:
                detect_info.append(page_num)
                # for k, p in enumerate(page_table):
                #     p.save(r"{}".format(os.path.join(SAVE_IMG_FOLDER, file_name[:-4] + '_' + str(k+1) + '.jpg')))
                page_table[0].save(r"{}".format(os.path.join(SAVE_IMG_FOLDER, file_name[:-4] + '_1.jpg')))
                time_finish = time.time()
                detect_info.append(round(time_finish - time_begin, 2))
                
                note_path = os.path.join(SAVE_IMG_FOLDER, 'found_table.txt')
                with open(note_path, 'a', encoding="utf-8") as f:
                    for text in detect_info:
                        f.write(str(text))
                        f.write(',')
                    f.write('\n')
                print(f'Saved {detect_info}')
                
                break
            else:
                first_page, last_page = last_page + 1, last_page + 3
        
        if not page_table:
            note_path = os.path.join(SAVE_IMG_FOLDER, 'not_found_table.txt')
            print('Not Found Table Images')
            with open(note_path, 'a', encoding="utf-8") as f:
                f.write(pdf_path)
                f.write('\n')
    except:
        print(f'{file_name} Not found')