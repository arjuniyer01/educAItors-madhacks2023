import openai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv('.env')

# openai.api_key = os.environ['OPENAI_API_KEY']
openai.api_key = st.secrets["OPENAI_API_KEY"]

# openai.error.InvalidRequestError:

#Generate GPT response and return in string format
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}])

    message = response.choices[0]["message"]["content"]
    return message.strip()  

#Generate prompt for image:
def generate_image_prompt(response):
    image_prompt = generate_response("Generate a 50 word description for a non-violent image that aligns with the time period and the following text: " + response)
    return image_prompt

#Generate dall-e image:
def generate_image(image_prompt):
    image_url = openai.Image.create(prompt=f"{image_prompt}, hd, oil painting", n=1, size="1024x1024")['data'][0]['url']
    return image_url

def get_text_from_whisper():
    return openai.Audio.transcribe("whisper-1", open("audio.mp3", "rb"))




