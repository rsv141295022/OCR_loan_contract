import pandas as pd
import concurrent.futures
import detectTextTable
import os

df_info = pd.read_excel(r'C:\Users\patcharapol.y\Desktop\Projects\New folder\VS code\OCR\info_ocr.xlsx')
df = df_info[df_info['jpg_paths'].notnull()].copy()
jpg_paths = df['jpg_paths'].values
contract_id = df['contract_id'].values
paid_intstallments = df['จ่ายแล้ว (งวด)'].values

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for _, _ in zip(jpg_paths, executor.map(detectTextTable.table_to_text, jpg_paths, paid_intstallments, contract_id)):
            pass
    
if __name__ == '__main__':
    main()