import streamlit as st
import time
from streamlit_echarts import st_echarts
import db
import auth
import webbrowser
import comms

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

st.markdown('# :house: Dashboard')

# TODO: Get array from DB
content = db.get_progress(st.session_state.user_id)

# TODO: Get user's role from DB
role = db.get_role(st.session_state.user_id)

if role == 'student':
    # TODO: Get progress from DB
    st.markdown('## Progress')
    for key, value in content.items():
        with st.expander(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(key)))}: {value[0:10]}..."):
            st.write(value)
            st.button('Email to me', onclick=comms.send_email, args=[st.session_state.user_email, value])
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