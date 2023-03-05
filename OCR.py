import streamlit as st
import pytesseract
from PIL import Image

def ocr(image):
    # Load image file
    with Image.open(image) as img:
        # Perform OCR on image and extract text
        script = pytesseract.image_to_string(img)

    return script

st.title("OCR with Streamlit")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# If an image is uploaded
if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Extract text using OCR
    text = ocr(uploaded_file)
    st.write("Extracted Text:")
    st.write(text)
else:
    st.write("Please upload an image.")


#streamlit run ocr.py