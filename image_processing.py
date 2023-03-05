import torch
import ssl
import pytesseract

ssl._create_default_https_context = ssl._create_unverified_context

# Load YOLOv5 model
model = torch.hub.load("ultralytics/yolov5", "yolov5s")

# Define function to perform object detection
def detect_objects(image):
    results = model(image)
    labels = results.pandas().xyxy[0]["name"].tolist()
    return labels, results.render()[0]


def run_ocr(image):
    return pytesseract.image_to_string(image)
