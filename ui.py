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
    col1, col2 = st.columns([1,1])
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
        st.markdown("educAIte is a platform for teachers and students to learn and teach using AI.")
        st.markdown("## :question: How does it work?")
        st.markdown("educAIte uses AI to summarize text and images, while translating text to your preferred language.")
        st.markdown("## :question: How can I use it?")
        st.markdown("<Add text here>")
        st.markdown("## :question: How can I contribute?")
        st.markdown("educAIte is open source, and you can contribute to the project on [GitHub](https://github.com/arjuniyer01/educAItors-madhacks2023)")
