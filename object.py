import streamlit as st
import torch
import torchvision
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

# Define Streamlit app
def app():
    st.title('Object Detection')
    st.write('Upload an image and I will try to detect the objects in it!')

    # Allow user to upload an image
    uploaded_file = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        # Load image and perform object detection
        image = Image.open(uploaded_file)
        labels, labelled_image = detect_objects(image)

        # Output results
        st.write('The objects in the image are:')
        st.write(labels)
        st.image(labelled_image, caption='Labelled image', use_column_width=True)

# Run app
if __name__ == '__main__':
    app()



#streamlit run object.py
