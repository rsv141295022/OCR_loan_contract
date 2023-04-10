# import required module
import os
import pandas as pd

# assign directory
# folder_dir = r'C:\Users\patcharapol.y\Desktop\Projects\New folder\VS code\OCR\All Contract'
# iterate over files in that directory
# file_paths = []
# for sub_folder_dir in os.listdir(folder_dir):
#     if os.path.isdir(os.path.join(folder_dir, sub_folder_dir)):
#         sub_folder_dir = os.path.join(folder_dir, sub_folder_dir)
#         for file in os.listdir(sub_folder_dir):
#             file_path = os.path.join(sub_folder_dir, file)
#             file_paths.append(file_path)

#----------------------------------------- PDF file names -----------------------------------------
  
# df_info = pd.read_excel(r'C:\Users\patcharapol.y\Desktop\Projects\New folder\VS code\OCR\info_ocr.xlsx')
# contract_id = df_info['contract_id'].values
# folder_dir = r'C:\Users\patcharapol.y\Desktop\Projects\New folder\VS code\OCR\All Contract'
# file_paths = os.listdir(folder_dir)
# paths = []
# for id in contract_id:
#     similar_path = []
#     for path in file_paths:
#         if str(id) in path:
#             similar_path.append(path)
#     if similar_path:
#         paths.append(os.path.join(folder_dir, similar_path[0]))
#     else:
#         paths.append('Not Found')
# df_info['pdf_paths'] = paths
# df_info.to_excel(r'C:\Users\patcharapol.y\Desktop\Projects\New folder\VS code\OCR\info_ocr.xlsx', index=False)

#----------------------------------------- JPG file names -----------------------------------------
# df_info = pd.read_excel(r'C:\Users\patcharapol.y\Desktop\Projects\New folder\VS code\OCR\info_ocr.xlsx')
# contract_id = df_info['contract_id'].values
# folder_dir = r'C:\Users\patcharapol.y\Desktop\Projects\New folder\VS code\OCR\pictures'
# jpg_paths = os.listdir(folder_dir)
# jpg_paths = [path for path in jpg_paths if path.endswith("1.jpg")]
# paths = []
# for id in contract_id:
#     similar_path = []
#     for path in jpg_paths:
#         if str(id) in path:
#             similar_path.append(path)
#     if similar_path:
#         paths.append(os.path.join(folder_dir, similar_path[0]))
#     else:
#         paths.append('Not Found')
# df_info['jpg_paths'] = paths
# df_info.to_excel(r'C:\Users\patcharapol.y\Desktop\Projects\New folder\VS code\OCR\info_ocr.xlsx', index=False)


#----------------------------------------- Excel file names -----------------------------------------
# df_info = pd.read_excel(r'C:\Users\patcharapol.y\Desktop\Projects\New folder\VS code\OCR\info_ocr.xlsx')
# contract_id = df_info['contract_id'].values
# folder_dir = r'C:\Users\patcharapol.y\Desktop\Projects\New folder\VS code\OCR\excels'
# excel_paths = os.listdir(folder_dir)
# excel_paths = [path for path in excel_paths if path.endswith(".xlsx")]
# paths = []
# for id in contract_id:
#     similar_path = []
#     for path in excel_paths:
#         if str(id) in path:
#             similar_path.append(path)
#     if similar_path:
#         paths.append(os.path.join(folder_dir, similar_path[0]))
#     else:
#         paths.append('Not Found')
# df_info['excel_paths'] = paths
# df_info.to_excel(r'C:\Users\patcharapol.y\Desktop\Projects\New folder\VS code\OCR\info_ocr.xlsx', index=False)