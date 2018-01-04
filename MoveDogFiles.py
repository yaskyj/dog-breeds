import pandas as pd
import os

files = pd.read_csv('labels.csv')

# Create folders for each breed
breeds = files['breed'].sort_values().unique()
for i in breeds:
    directory = './train/train/' + i
    if not os.path.exists(directory):
        os.makedirs(directory)

for i in breeds:
    directory = './train/test/' + i
    if not os.path.exists(directory):
        os.makedirs(directory)
        
# Move pictures into corresponding breed folders 
for index, row in files.iterrows():
    match_string = './train/' + row['id'] + '.jpg'
    destination = './train/train/' + row['breed'] + '/' + row['id'] + '.jpg'
    print match_string
    print destination
    os.rename(match_string, destination)
    
# Count number of pictures in each breed folder
path = './train/train/'
folders = [name for name in os.listdir(path)]
image_counts = []
for folder in folders:
    contents = os.listdir(os.path.join(path,folder))
    image_counts.append(len(contents))
    print len(contents)
print min(image_counts)

# Delete images more than 66 for each breed
for folder in folders:
    count = 1
    for file in os.listdir(os.path.join(path,folder)):
        if count < 66:
            os.remove(os.path.join(path,folder,file))
        count += 1

# Move 10 images into another folder for testing for each breed
for folder in folders:
    count = 1
    for file in os.listdir(os.path.join(path,folder)):
        if count < 11:
            print os.path.join(path,folder,file)
            print os.path.join('./train/test/',folder,file)
            os.rename(os.path.join(path,folder,file), os.path.join('./train/test/',folder,file))
        count += 1
