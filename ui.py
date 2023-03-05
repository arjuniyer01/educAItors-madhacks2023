import streamlit as st
import ai
import db
import time
import avatar

result_text = ""
result_images = []


def process_result(prompt: str):
    global result_text
    global result_images
    result_images.clear()
    result_text = ai.generate_response(prompt)
    for i in range(2):
        result_images.append(ai.generate_image(ai.generate_image_prompt(prompt)))


def display_result():
    global result_text
    global result_images
    st.markdown(f"## :speech_balloon: Summarized Text")
    col1, col2 = st.columns([1, 1])
    with col1:
        for i in result_images:
            st.image(i)
    with col2:
        st.markdown(f"#### {result_text}")
    avatar.generate_voice(result_text)


def save_result():
    global result_text
    global result_images
    save_time = int(time.time())
    progress = db.get_progress(st.session_state.user_id)
    progress[f"{save_time}"] = result_text
    db.update_progress(st.session_state.user_id, progress)


def about(expanded: bool = False):
    with st.expander("About", expanded=expanded):
        st.markdown("## :wave: Welcome to educAIte!")
        st.markdown(
            "A powerful language agnostic education tool leveraging AI and computer vision."
        )
        st.markdown("## How does it work?")
        st.markdown(
            """
                    Provide skim and detailed summaries of text, pdfs, docx, images, and voice in any language to aid students with their quest to learn
Provide AI generated visual learning tools to help children learn languages or topics.
Provide a mini-podcast where you can listen to what you are learning.
Provide object detection computer vision tools for younger children to help them learn about the world around them
Completely language and age customizable.
"""
        )
        st.markdown("## How can I use it?")
        st.markdown(
            """
        Upload textbook/notes/book in any format and get a skim or detailed summary with images and voice to aid learning.
Upload recording of lecture to get a skim or detailed summary with images and voice to aid learning.
Learn a new language visually by getting labeled images
        """
        )
