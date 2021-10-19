import time
import os
import streamlit as st
import numpy as np
import pandas as pd
import streamlit.components.v1 as components

from PIL import Image
from aenum import enum as Enum

from src.decisionTree import DecisionTree
from src.trends import Trends

class Exercise_Level(Enum):
    EX_1 = 'Level 1 - High Hypo risk'
    EX_2 = 'Level 2 - Medium Hypo risk'
    EX_3 = 'Level 3 - Low Hypo risk'

ex_enum = Exercise_Level()
trends_enum = Trends()
dt = DecisionTree()
image = Image.open('Pre_ex.png')
st.title('Mediwell Demo board')

with st.form(key="Form"):
    exercise_level = st.radio(
         "What is your current exercise level or hypoglycemia risk",
        (ex_enum.EX_1, ex_enum.EX_2, ex_enum.EX_3))

    if exercise_level == ex_enum.EX_1:
        ex_level = 'ex_1'
        print('ex_level = ', ex_level)
    elif exercise_level == ex_enum.EX_2:
        ex_level = 'ex_2'
        print('ex_level = ', ex_level)
    elif exercise_level == ex_enum.EX_3:
        ex_level = 'ex_3'
        print('ex_level = ', ex_level)

    else:
        raise AssertionError
    # components.iframe("https://giphy.com/gifs/reaction-wwe-wrestling-UiBmJv6Hh6FfW/fullscreen")

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
    dt.set_exercise_level(ex_level)

if submitted:
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
            f" ➡️ {res['case_decrease']}"
        )
    elif res['color'] == 'yellow' or res['color'] == 'dark_yellow':
        col1.warning(
            f" ➡️ {res['case_increase']}"
        )
        col2.warning(
            f" ➡️ {res['case_decrease']}"
        )
    elif res['color'] == 'red':
        col1.error(
            f" ➡️ {res['case_increase']}"
        )
        col2.error(
            f" ➡️ {res['case_decrease']}"
        )


# components.html("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """)
with st.sidebar.expander("See Reference Chart"):
    st.image(image)
