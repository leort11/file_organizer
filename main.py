import os
from tkinter.filedialog import askdirectory

path = askdirectory(title="Select a folder")

file_list = os.listdir(path)

locals = {
    "images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"],
    "spreadsheets": [".xlsx", ".xls", ".ods"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
    "documents": [".doc", ".docx", ".txt", ".odt"],
    "presentations": [".ppt", ".pptx", ".odp"],
    "archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "audio": [".mp3", ".wav", ".aac", ".flac"],
    "videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"]
}

for file in file_list:
    name, extention = os.path.splitext(f"{path}/{file}")
    for folder in locals:
        if extention in locals[folder]:
            if not os.path.exists(f"{path}/{folder}"):
                os.mkdir(f"{path}/{folder}")

            os.rename(f"{path}/{file}", f"{path}/{folder}/{file}")