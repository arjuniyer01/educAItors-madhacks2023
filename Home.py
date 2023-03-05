import streamlit as st
from streamlit_webrtc import webrtc_streamer
from PIL import Image
import auth
import webbrowser
import db
import ui
# import ocr
# import object

if 'user_email' not in st.session_state:
    st.session_state.user_email = None

if 'user_id' not in st.session_state:
    st.session_state.user_id = None

if 'result_mode' not in st.session_state:
    st.session_state.result_mode = False

if not st.session_state.user_email:
    if st.button("Login"):
        webbrowser.open_new_tab(auth.get_login_str())
elif st.session_state.user_email:
    # st.balloons()
    st.markdown(f"`{st.session_state.user_email}`")
    db.set_user(st.session_state.user_email)
    st.session_state.user_id = db.get_user_id(st.session_state.user_email)
    settings = db.get_settings(st.session_state.user_id)

try:
    st.session_state.user_email = auth.get_user()
except Exception as e:
    pass

col1, col2, col3 = st.columns([1,1,1])
with col2:
    st.title(":book: educAIte")


user_input = st.text_input("User Input", label_visibility='hidden', placeholder="Paste text here to summarize")
uploaded_file = st.file_uploader("File Upload", label_visibility='hidden', type=["png", "jpeg", "jpg"])
webrtc_streamer(key="sample")
if user_input:
    with st.spinner("Summarizing input text..."):
        st.session_state.result_mode = True
        ui.process_result(user_input, settings)
        ui.display_result()
        ui.save_result()
elif uploaded_file:
    selected = st.selectbox("Select an option", ["OCR", "Object detection"])
    if selected == "Object detection":
        with st.spinner("Summarizing using object detection..."):
            st.session_state.result_mode = True
            # img = Image.open(uploaded_file)
            # labels, img = object.detect_objects(img.copy())
            # st.image(img)
            # st.write(labels)
            # ui.process_result(" ".join(labels), settings)
            # ui.display_result()
            # ui.save_result()
    elif selected == "OCR":
        with st.spinner("Summarizing using OCR..."):
            st.session_state.result_mode = True
            # img = Image.open(uploaded_file)
            # ocr_text = ocr.run_ocr(img.copy())
            # st.write(ocr_text)
            # ui.process_result(ocr_text, settings)
            # ui.display_result()
            # ui.save_result()
    
ui.about()