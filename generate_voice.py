import streamlit as st
from espeakng import ESpeakNG

# Set up espeak-ng
esng = ESpeakNG()
esng.voice = 'english'

# Define available languages
languages = {
    'English': 'english',
    'French': 'french',
    'German': 'german',
    'Italian': 'italian',
    'Spanish': 'spanish'
}

# Define Streamlit app
def app():
    st.title('Text-to-Speech App')

    # Get user input
    text = st.text_input('Enter your text here')

    # Get selected language
    lang = st.selectbox('Select a language', list(languages.keys()))

    # Set language for espeak-ng
    esng.voice = languages[lang]

    # Generate audio from text
    if text:
        audio = esng.synth_wav(text)

        # Play audio
        st.audio(audio, format='audio/wav')

if __name__ == '__main__':
    app()

#streamlit run generate_voice.py
