from ultralytics import YOLO
model= "C:/Users/tanis/Desktop/yolo/runs/detect/train7/weights/best.pt"
model.val(data="data.yaml")