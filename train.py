from ultralytics import YOLO
model= YOLO()
model.train(data="data.yaml", epochs = 5 )