from ultralytics import YOLO
import cv2
# Load model

coco_model = YOLO('./models/yolov8n.pt') #To detect Cars
license_plate_detector = YOLO('./models/license_plate_detector.pt') #To detect Liscence Plates

#Load Vedio
cap = cv2.VideoCapture('sample.mp4')

# read frames
frame_number = -1
ret = True
while ret and frame_number < 10:
    frame_number += 1
    ret, frame = cap.read()
    if ret:
        pass
        
        #detect vehicles
        results = coco_model(frame)

