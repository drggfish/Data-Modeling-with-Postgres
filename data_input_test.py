import os
import glob
import pandas as pd
import numpy as np

filepath="log_data/2018/11"

all_files = []

print((filepath))
    
for root, dirs, files in os.walk(filepath):
    files = glob.glob(os.path.join(root, "*.json"))
    for f in files:
        all_files.append(os.path.abspath(f))

# get total number of files found
num_files = len(all_files)
print(f"{num_files} files found in {filepath}")

for i, datafile in enumerate(all_files, 1):
    print(f"{i}/{num_files} files processed.")