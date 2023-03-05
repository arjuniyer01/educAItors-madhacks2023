import streamlit as st
import openai
import requests
import os

openai.api_key = "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"

#Generate GPT response and return in string format
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}])

    message = response.choices[0]["message"]["content"]
    return message.strip()  

#Generate prompt for image:
def generate_image_prompt(response):
    image_prompt = generate_response("generate a short and simple image description that illustrates the text. make it non-violent. text: " + response)
    return image_prompt

#Generate dall-e image:
def generate_image(image_prompt):
    image_url = openai.Image.create(prompt=image_prompt + ", hd oil painting", n=1, size="1024x1024")['data'][0]['url']
    return image_url





