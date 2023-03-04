import streamlit as st
import pycountry
import auth
import webbrowser

if 'user_email' not in st.session_state:
    st.session_state.user_email = None

if not st.session_state.user_email:
    if st.button("Login"):
        webbrowser.open_new_tab(auth.get_login_str())
elif st.session_state.user_email:
    # st.balloons()
    st.markdown(f"`{st.session_state.user_email}`")

try:
    st.session_state.user_email = auth.display_user()
except Exception as e:
    pass

if not st.session_state.user_email:
   st.warning("Please login to access this page")
   st.stop()

# TODO: get user's existing settings from DB

languages = []
countries = [country.name for country in pycountry.countries]

# create a dictionary to store language names and countries where they are spoken
language_dict = {}

st.markdown("# :gear: Settings")
with st.form("my_form"):
   name = st.text_input("Name")
   phone = st.text_input("Phone")
   age = st.slider("Age", 0, 123, 5)
   location = st.selectbox("Location", countries, index=0)
   language = st.selectbox("Language", languages)

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
      st.success("Submitted!")