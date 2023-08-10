from ultralytics import YOLO
model= "C:\\Users\\tanis\\Desktop\\yolo\\runs\\detect\\train22\\weights\\best.pt"
model.val(data="data.yaml", epochs = 5 )