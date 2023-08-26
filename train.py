from ultralytics import YOLO
model= YOLO()
# model.to("cuda")
model.train(data="data.yaml", epochs = 15 )