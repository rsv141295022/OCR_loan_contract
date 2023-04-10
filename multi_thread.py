import pandas as pd
import concurrent.futures
import detectTable
import os 

df_info = pd.read_excel(r'C:\Users\patcharapol.y\Desktop\Projects\New folder\VS code\OCR\info_ocr.xlsx')
pdf_paths = df_info[df_info['pdf_paths'] != 'Not Found']['pdf_paths'].values

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for _, _ in zip(pdf_paths, executor.map(detectTable.detect_table, pdf_paths)):
            pass
    
if __name__ == '__main__':
    main()