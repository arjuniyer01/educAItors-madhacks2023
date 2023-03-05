import streamlit as st
import torch
# import torchvision
import numpy as np
from PIL import Image, ImageDraw
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Define function to perform object detection
def detect_objects(image):
    results = model(image)
    labels = results.pandas().xyxy[0]['name'].tolist()
    return labels, results.render()[0]
