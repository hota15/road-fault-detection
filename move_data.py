import os
import shutil

image_path ="raw_images"
label_path ="annotations"
main_path = "Final/Final"

for file in os.listdir(main_path):
    file =os.path.join(main_path,file)
    # if file.endswith(".xml"): 
    #     shutil.move(file , label_path)
    if file.endswith(".jpg"):
        shutil.move(file, image_path)
