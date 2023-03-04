import streamlit as st
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

st.markdown("# Quiz")

if 'question_number' not in st.session_state:
    st.session_state.question_number = 0

def get_question(question_number):
    questions = [
        ("What is 1 + 1?", "2", ["1", "2", "3"]),
        ("What is 2 + 2?", "4", ["2", "4", "6"]),
        ("What is 3 + 3?", "6", ["3", "6", "9"]),
        ("What is 4 + 4?", "8", ["4", "8", "12"]),
        ("What is 5 + 5?", "10", ["5", "10", "15"]),
    ]
    return questions[question_number]

if st.button('Start quiz'):   
    q, ans, choices = get_question(st.session_state.question_number)

    st.markdown(f"## {q}")
    a = st.radio('Answer:', choices)

    if a != "Please select an answer":
        st.write(f"You chose {a}")
        if (ans == a):
            st.write("Correct!")
        else:
            st.write(f"Wrong!, the correct answer is {ans}")
                
    if st.button('Next question'):
        st.session_state.question_number += 1