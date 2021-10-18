import time
import os
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from src.decisionTree import DecisionTree
from aenum import enum as Enum
from src.trends import Trends


class Exercise_Level(Enum):
    EX_1 = 'Level 1 - High Hypo risk'
    EX_2 = 'Level 2 - Medium Hypo risk'
    EX_3 = 'Level 3 - Low Hypo risk'


ex_enum = Exercise_Level()
trends_enum = Trends()
st.title('Mediwell Demo board')

with st.form(key="Form"):
    exercise_level = st.radio(
         "What is your current exercise level or hypoglycemia risk",
        (ex_enum.EX_1, ex_enum.EX_2, ex_enum.EX_3))

    if exercise_level == ex_enum.EX_1:
        ex_level = 'ex_1'
    elif exercise_level == ex_enum.EX_2:
        ex_level = 'ex_2'
    elif exercise_level == ex_enum.EX_3:
        ex_level = 'ex_3'
    else:
        raise AssertionError
    # st.write('hello')
    # components.iframe("https://giphy.com/gifs/reaction-wwe-wrestling-UiBmJv6Hh6FfW/fullscreen")

    # st.write('What is your current glucose level in mg/dl')
    current_glucose = st.number_input('What is your current glucose value in mg/dl')

    current_trend = st.radio(
        'What is your current glucose trend',
        (trends_enum.UP,
         trends_enum.GOING_UP,
         trends_enum.STABLE,
         trends_enum.GOING_DOWN,
         trends_enum.DOWN)
    )

    submitted = st.form_submit_button()

# st.button('Are you ready for your training')
dt = DecisionTree('ex_1')
res = dt.eval_glucose(current_glucose, current_trend)
new_line = '\n'
if submitted:
    dt = DecisionTree('ex_1')
    res = dt.eval_glucose(current_glucose, current_trend)
    with st.spinner("🤓 Getting Recommendation"):
        time.sleep(1)
    col1, col2 = st.columns(2)
    col1.subheader('Expecting increase in glucose?')
    col2.subheader('Expecting decrease in glucose?')
    if res['color'] == 'green':
        col1.success(
            f"➡️ {res['case_increase']}"
        )
        col2.success(
            f" ➡️ {res['case_increase']}"
        )
    elif res['color'] == 'yellow' or res['color'] == 'dark_yellow':
        col1.warning(
            f" ➡️ {res['case_increase']}"
        )
        col2.warning(
            f" ➡️ {res['case_increase']}"
        )
    elif res['color'] == 'red':
        col1.error(
            f" ➡️ {res['case_increase']}"
        )
        col2.error(
            f" ➡️ {res['case_increase']}"
        )

