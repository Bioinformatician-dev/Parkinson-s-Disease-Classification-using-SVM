import os
!mkdir -p ~/.kaggle
!mv kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets download -d vikasukani/parkinsons-disease-data-set
import zipfile
zip_file = "parkinsons-disease-data-set.zip"
extract_folder = "parkinsons_data"

with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

print("Dataset extracted successfully!")
os.listdir(extract_folder)
