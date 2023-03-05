import streamlit as st
import time
from streamlit_echarts import st_echarts
import db
import auth
import webbrowser
import comms
from PIL import Image
import io

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
    st.markdown(f"[Google Login]({auth.get_login_str()})")
    st.warning("Please login to access this page")
    st.stop()
elif st.session_state.user_email:
    st.markdown(f"`{st.session_state.user_email}`")

st.markdown('# :house: Dashboard')

# TODO: Get array from DB
content = db.get_progress(st.session_state.user_id)

# TODO: Get user's role from DB
role = db.get_role(st.session_state.user_id)

st.write(f"{len(content.items())}")

if role == 'student':
    # TODO: Get progress from DB
    st.markdown('## Progress')
    if len(content.items() == 0):
        st.warning('No progress yet')
        st.stop()
    for key, value in content.items():
        # {value[0:10]}
        with st.expander(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(key)))}: {value[0:10]}..."):
            st.write(value)
            st.button('Email to me', on_click=comms.send_email, args=[st.session_state.user_email, value, key], key=key)