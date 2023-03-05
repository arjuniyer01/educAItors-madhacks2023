import streamlit as st
from streamlit_webrtc import webrtc_streamer
import auth
import webbrowser
import db

if 'user_email' not in st.session_state:
    st.session_state.user_email = None

if 'user_id' not in st.session_state:
    st.session_state.user_id = None

if not st.session_state.user_email:
    if st.button("Login"):
        webbrowser.open_new_tab(auth.get_login_str())
elif st.session_state.user_email:
    # st.balloons()
    st.markdown(f"`{st.session_state.user_email}`")
    db.set_user(st.session_state.user_email)
    st.session_state.user_id = db.get_user_id(st.session_state.user_email)

try:
    st.session_state.user_email = auth.get_user()
except Exception as e:
    pass

col1, col2, col3 = st.columns([1,1,1])
with col2:
    st.title(":book: educAIte")

user_input = st.text_input("User Input", label_visibility='hidden', placeholder="Paste text here to summarize")
upload = st.file_uploader("File Upload", label_visibility='hidden', type=["txt", "pdf", "docx", "png", "jpeg"])
webrtc_streamer(key="sample")

with st.expander("About"):
    st.markdown("## :wave: Welcome to educAIte!")
    st.markdown("educAIte is a platform for teachers and students to learn and teach using AI.")
    st.markdown("## :question: How does it work?")
    st.markdown("educAIte uses AI to summarize text and images, while translating text to your preferred language.")
    st.markdown("## :question: How can I use it?")
    st.markdown("<Add text here>")
    st.markdown("## :question: How can I contribute?")
    st.markdown("educAIte is open source, and you can contribute to the project on [GitHub](https://github.com/arjuniyer01/educAItors-madhacks2023)")