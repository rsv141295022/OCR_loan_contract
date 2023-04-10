from ocr_functions import *
import os, pytesseract, time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def table_to_text(jpg_path, paid_installment, excel_name):
    try:
        if paid_installment == 0:
            pass
        else:
            file_name = jpg_path.split('\\')[-1]
            EXCEL_FOLDER = os.path.join(r'C:\Users\patcharapol.y\Desktop\Projects\New folder\VS code\OCR', 'excels')
            if not os.path.exists(EXCEL_FOLDER):
                os.mkdir(EXCEL_FOLDER)
            
            time_begin = time.time()
            detect_info=[]
            detect_info.append(file_name)

            processed_img = process_image_for_ocr(r'{}'.format(jpg_path))
            vertical_horizontal_lines = get_vertical_horizontal_lines(processed_img)
            _, boundingBoxes = find_contours_boxes(vertical_horizontal_lines)
            filter_boxes = filter_proper_boxes(boundingBoxes)
            all_row_col_boxes, n_cols, n_rows = rearrange_boxes_row_col(filter_boxes)
            img_for_roi = bitwise_img(processed_img, vertical_horizontal_lines)
            n_rows = int(paid_installment) + 5
            row_col_boxes = all_row_col_boxes[:n_rows]
            text_outputs = img_to_text(row_col_boxes, img_for_roi)
            text_outputs = clean_text(text_outputs)
            
            arr = np.array(text_outputs)
            df = pd.DataFrame(arr.reshape(n_rows, n_cols))
            df.to_excel(r'{}'.format(os.path.join(EXCEL_FOLDER, str(excel_name) + '.xlsx')), index=False)
            time_finish = time.time()
            detect_info.append(round(time_finish - time_begin, 2))
            
            note_path = os.path.join(EXCEL_FOLDER, 'found_table.txt')
            with open(note_path, 'a', encoding="utf-8") as f:
                for text in detect_info:
                    f.write(str(text))
                    f.write(',')
                f.write('\n')
            
            print(f'Saved {detect_info}')
    except:
        print('Error')