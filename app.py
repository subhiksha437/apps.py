def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")
import streamlit as st
st.header("STAGE PREDICTION ASESSMENT")

nl(1)

# Text Prompt
st.markdown("""
            1. This quiz contains 15 questions and all the questions must be answered.
            2. Based on the answers given, your current stage will be decided.
            3. Analyse each question and answer. ALL THE BEST!!!
            """)

# Create Placeholder to print test score
scorecard_placeholder = st.empty()

# Activate Session States
ss = st.session_state
# Initializing Session States
if 'counter' not in ss:
    ss['counter'] = 0
if 'start' not in ss:
    ss['start'] = False
if 'stop' not in ss:
    ss['stop'] = False
if 'refresh' not in ss:
    ss['refresh'] = False
if "button_label" not in ss:
    ss['button_label'] = ['START', 'SUBMIT', 'RELOAD']
if 'current_quiz' not in ss:
    ss['current_quiz'] = {}
if 'user_answers' not in ss:
    ss['user_answers'] = []
if 'grade' not in ss:
    ss['grade'] = 0
