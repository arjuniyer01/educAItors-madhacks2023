import streamlit as st
import pydub
import ai
from PIL import Image
import auth
import webbrowser
import db
import ui
import image_processing
import file_reader

# # Instantiation
# settings = None

if 'user_email' not in st.session_state:
    st.session_state.user_email = None

if 'user_id' not in st.session_state:
    st.session_state.user_id = None

if 'settings' not in st.session_state:
    st.session_state.settings = None

# Login
try:
    st.session_state.user_email = auth.get_user()
    db.set_user(st.session_state.user_email)
    st.session_state.user_id = db.get_user_id(st.session_state.user_email)
    st.session_state.settings = db.get_settings(st.session_state.user_id)
except Exception as e:
    pass

if not st.session_state.user_email:
    # if st.button("Login"):
    #     webbrowser.open_new_tab(auth.get_login_str())
    st.markdown(f"[Google Login]({auth.get_login_str()})")
elif st.session_state.user_email:
    # st.balloons()
    st.markdown(f"`{st.session_state.user_email}`")


# UI Begins
col1, col2, col3 = st.columns([1,1,1])
with col2:
    st.title(":book: educAIte")

user_input = st.text_input("User Input", label_visibility='hidden', placeholder="Paste text here to summarize")
uploaded_file = st.file_uploader("File Upload", label_visibility='hidden', type=["png", "jpeg", "jpg", "mp3", "pdf", "docx"])

if user_input:
    with st.spinner("Summarizing input text..."):
        ui.process_result(f"Summarize the below text in {st.session_state.settings['language']}, explain like I am {st.session_state.settings['age']} years old in one paragraph. {user_input}")
        ui.display_result()
        ui.save_result()
elif uploaded_file:
    if uploaded_file.name.endswith(".mp3"):
        with st.spinner("Summarizing audio input..."):
            audio = pydub.AudioSegment.from_mp3(uploaded_file)
            audio.export("audio.mp3", format='mp3')
            audio_bytes = open("audio.mp3", 'rb').read()
            st.audio(audio_bytes, format=f'audio/.mp3', start_time=0)
            whisper_text = ai.get_text_from_whisper()["text"]
            ui.process_result(f"Summarize the below text in {st.session_state.settings['language']}, explain like I am {st.session_state.settings['age']} years old in one paragraph. {whisper_text}")
            # ui.display_result()
            # ui.save_result()

    if uploaded_file.name.endswith(".pdf"):
        with st.spinner("Summarizing PDF input..."):
            pdf_text = file_reader.read_pdf(uploaded_file)
            ui.process_result(f"Summarize the below text in {st.session_state.settings['language']}, explain like I am {st.session_state.settings['age']} years old in one paragraph. {pdf_text}")
            # ui.display_result()
            # ui.save_result()

    if uploaded_file.name.endswith(".docx"):
        with st.spinner("Summarizing DOCX input..."):
            docx_text = file_reader.convert_docx_to_text(uploaded_file)
            ui.process_result(f"Summarize the below text in {st.session_state.settings['language']}, explain like I am {st.session_state.settings['age']} years old in one paragraph. {docx_text}")
            # ui.display_result()
            # ui.save_result()

    if uploaded_file.name.endswith(".png") or uploaded_file.name.endswith(".jpeg") or uploaded_file.name.endswith(".jpg"):
        selected = st.selectbox("Select image processing method", ["Object detection", "OCR"])
        if st.button("Process"):
            if selected == "Object detection":
                with st.spinner("Summarizing using object detection..."):
                    img = Image.open(uploaded_file)
                    labels, img = image_processing.detect_objects(img.copy())
                    st.image(img)
                    ui.process_result(f"Define the objects mentioned below in {st.session_state.settings['language']}, explain like I am {st.session_state.settings['age']} years old in one paragraph. {' '.join(labels)}")
                    # ui.display_result()
                    # ui.save_result()
            if selected == "OCR":
                with st.spinner("Summarizing using OCR..."):
                    img = Image.open(uploaded_file)
                    ocr_text = image_processing.run_ocr(img.copy())
                    st.write(ocr_text)
                    ui.process_result(f"Summarize the below text in {st.session_state.settings['language']}, explain like I am {st.session_state.settings['age']} years old in one paragraph. {ocr_text}")
                    # ui.display_result()
                    # ui.save_result()

ui.display_result()
ui.save_result()
ui.about()
