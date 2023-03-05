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

if role == 'student':
    # TODO: Get progress from DB
    st.markdown('## Progress')
    for key, value in content.items():
        # {value[0:10]}
        with st.expander(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(key)))}: {value.summary[0:10]}..."):
            st.image(Image.open(io.BytesIO(value["images"][0])))
            st.image(Image.open(io.BytesIO(value["images"][1])))
            st.write(value["summary"])
            st.button('Email to me', on_click=comms.send_email, args=[st.session_state.user_email, value["summary"], key], key=key)





elif role == 'teacher':
    # TODO: Get teacher's dashboarding info from DB
    option1 = {
        "xAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {"type": "value"},
        "series": [{"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}],
    }
    st_echarts(
        options=option1, height="400px",
    )
    option2 = {
        "legend": {"top": "bottom"},
        "toolbox": {
            "show": True,
            "feature": {
                "mark": {"show": True},
                "dataView": {"show": True, "readOnly": False},
                "restore": {"show": True},
                "saveAsImage": {"show": True},
            },
        },
        "series": [
            {
                "name": "面积模式",
                "type": "pie",
                "radius": [50, 250],
                "center": ["50%", "50%"],
                "roseType": "area",
                "itemStyle": {"borderRadius": 8},
                "data": [
                    {"value": 40, "name": "rose 1"},
                    {"value": 38, "name": "rose 2"},
                    {"value": 32, "name": "rose 3"},
                    {"value": 30, "name": "rose 4"},
                    {"value": 28, "name": "rose 5"},
                    {"value": 26, "name": "rose 6"},
                    {"value": 22, "name": "rose 7"},
                    {"value": 18, "name": "rose 8"},
                ],
            }
        ],
    }
    st_echarts(
        options=option2, height="600px",
    )
