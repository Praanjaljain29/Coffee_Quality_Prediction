#This is a script to move the csv files to raw_data folder 
#The purpose of this script is to create a folder raw_data and move all the csv files starting from coffee_
import os
import shutil

SOURCE_DIR = "."          # current folder
TARGET_DIR = "raw_data"

# create target folder if it doesn't exist
os.makedirs(TARGET_DIR, exist_ok=True)

moved = 0

for file in os.listdir(SOURCE_DIR):
    if file.startswith("coffee_") and file.endswith(".csv"):
        src_path = os.path.join(SOURCE_DIR, file)
        dst_path = os.path.join(TARGET_DIR, file)

        if not os.path.exists(dst_path):
            shutil.move(src_path, dst_path)
            moved += 1

print(f"Moved {moved} CSV files to '{TARGET_DIR}'")
