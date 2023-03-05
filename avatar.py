import os
from google.cloud import texttospeech
import streamlit as st
import json
from dotenv import load_dotenv

load_dotenv('.env')

# set up credentials for Google Cloud TTS
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = json(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])

def generate_voice(text: str):
    # create a client object for Google Cloud TTS
    client = texttospeech.TextToSpeechClient()
    # set up default voice configuration
    voice = texttospeech.VoiceSelectionParams(
        language_code='en-US', ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )
    # set up default audio configuration
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    # set up the synthesis input object
    synthesis_input = texttospeech.SynthesisInput(text=text)
    # generate the audio file
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    # stream the audio file to the user's browser
    st.audio(response.audio_content, format='audio/mp3')

