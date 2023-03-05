import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import json

# Set Streamlit page title and layout
st.set_page_config(page_title="Roblox Avatar Animation Player")

# Set Streamlit app title and header
st.title("Roblox Avatar Animation Player")
st.header("Enter an animation ID to see it in action")

# Get user input for animation ID
animation_id = st.text_input("Enter animation ID")

# Handle user input
if animation_id:
    # Construct the URL for the Roblox API request
    url = f"https://api.roblox.com/marketplace/productinfo?assetId={animation_id}"

    # Send the request to the Roblox API and parse the JSON response
    response = requests.get(url)
    data = json.loads(response.text)

    # Check if the animation is valid
    if "Name" in data:
        # Get the animation name and thumbnail image URL from the response
        animation_name = data["Name"]
        thumbnail_url = f"https://www.roblox.com/asset-thumbnail/image?assetId={animation_id}&width=420&height=420"

        # Get the thumbnail image from the URL and display it
        response = requests.get(thumbnail_url)
        thumbnail = Image.open(BytesIO(response.content))
        st.subheader(animation_name)
        st.image(thumbnail)

        # Play the animation when the user presses the "Play" button
        if st.button("Play"):
            st.info("Playing animation...")
            playback_url = f"https://assetgame.roblox.com/Asset/Animate.ashx?ID={animation_id}"
            st.video(playback_url)
    else:
        # Display an error message if the animation is not found
        st.error("Animation not found. Please enter a valid animation ID.")



#streamlit run avatar.py