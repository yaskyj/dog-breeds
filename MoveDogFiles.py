import pandas as pd
import os, fnmatch, csv, re

files = pd.read_csv('labels.csv')

# Create folders for each breed
breeds = files['breed'].sort_values().unique()
for i in breeds:
    directory = './train/train/' + i
    if not os.path.exists(directory):
        os.makedirs(directory)
        
