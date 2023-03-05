import streamlit as st
import pycountry
import db
import auth
import webbrowser

if 'user_email' not in st.session_state:
    st.session_state.user_email = None

# Login
try:
    st.session_state.user_email = auth.get_user()
    db.set_user(st.session_state.user_email)
    st.session_state.user_id = db.get_user_id(st.session_state.user_email)
    st.session_state.settings = db.get_settings(st.session_state.user_id)
except Exception as e:
    pass

if not st.session_state.user_email:
    st.markdown(f'''
    <a href={auth.get_login_str()}>
    <img src="https://lh3.googleusercontent.com/COxitqgJr1sJnIDe8-jiKhxDx1FrYbtRHKJ9z_hELisAlapwE9LUPh6fcXIfb5vwpbMl4xl9H9TRFPc5NOO8Sb3VSgIBrfRYvW6cUA" width="50" height="50">
    </a>
    ''', unsafe_allow_html=True)
    st.warning("Please login to access this page")
    st.stop()
elif st.session_state.user_email:
    st.markdown(f"`{st.session_state.user_email}`")

# TODO: get user's existing settings from DB

languages = ["English", "Spanish", "French", "Chinese", "Hindi"]
countries = [country.name for country in pycountry.countries]

# create a dictionary to store language names and countries where they are spoken
language_dict = {}

if st.session_state.user_id:
    settings = db.get_settings(st.session_state.user_id)
st.markdown("# :gear: Settings")
with st.form("my_form"):
   name = st.text_input("Name", value=settings["name"])
   phone = st.text_input("Phone", value=settings["phone"])
   age = st.slider("Age", 0, 123, value=settings["age"])
   location = st.selectbox("Location", countries, index=countries.index(settings["location"]))
   language = st.selectbox("Language", languages, index=languages.index(settings["language"]))

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
      db.update_settings(st.session_state.user_id, {"name": name, "phone": phone, "age": age, "location": location, "language": language})
      st.session_state.settings = db.get_settings(st.session_state.user_id)
      st.success("Submitted!")