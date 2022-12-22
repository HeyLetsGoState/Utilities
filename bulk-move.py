import os, shutil
from datetime import datetime
from pathlib import Path
from PIL import Image


dirpath = '%MAIN_SOURCE'
paths = sorted(Path(dirpath).iterdir(), key=os.path.getctime)
date_format = '%Y:%m:%d %H:%M:%S'

# Create the directory
parent_dir = '%FINAL_DESTINATION'
if not os.path.isdir(parent_dir):
    os.mkdir(parent_dir)

for path in paths:
    try:
        # The exif code 36867 is the time the file was created (meta data on the actual picture)
        date_created =  Image.open(path)._getexif()[36867]  
        date = datetime.strptime(date_created, date_format)
        formatted_date = date.strftime('%Y-%m-%d')

        # see if the directory exists
        tmp_dir = parent_dir + "/" + formatted_date
        if not os.path.isdir(tmp_dir):
            os.mkdir(tmp_dir)
        shutil.copy(path, tmp_dir)
    except:
        # misc ones are tossed in one folder (burst photos/videos/misc)
        shutil.copy(path, parent_dir)
