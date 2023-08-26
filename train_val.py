import os
import shutil

image_files= os.listdir("raw_images")
# image_files=[x[:-4:] for x in image_files]
label_files= os.listdir("labels")
# label_files=[x[:-4:] for x in label_files]
image_files.sort()
label_files.sort()

train_files= image_files[:1561:]
valid_files= image_files[1561:]
train_labels = label_files[:1561:]
valid_labels = label_files[1561:]
# print(len(train_files))
# print(len(valid_files))
print(image_files[:4])

for img_files in train_files:
    shutil.move(os.path.join("raw_images", img_files), "datasets/train/images")
    
for labels_files in train_labels:
    shutil.move(os.path.join("labels", labels_files), "datasets/train/labels")
    
for img_files in valid_files:
    shutil.move(os.path.join("raw_images", img_files), "datasets/val/images")
    
for labels_files in valid_labels:
    shutil.move(os.path.join("labels", labels_files), "datasets/val/labels")



