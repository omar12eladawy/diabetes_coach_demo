import streamlit as st
from datetime import datetime, date

from streamlit.legacy_caching.caching import clear_cache

now = datetime.now().time()
st.write(now)

def is_authenticated(password):
    # return password == "mediwell-2021"
    return True

def generate_login_block():
    block1 = st.empty()
    block2 = st.empty()

    return block1, block2


def clean_blocks(blocks):
    for block in blocks:
        block.empty()


def login(blocks):
    blocks[0].markdown("""
            <style>
                input {
                    -webkit-text-security: disc;
                }
            </style>
        """, unsafe_allow_html=True)
    return blocks[1].text_input('Password')

@st.cache(allow_output_mutation=True)
def get_data():
    return []

def convert_time_to_decimal(time):
    return time.hour + time.min/60

def get_insulin_on_board(active_time, insulin_dict: list):
    insulin_onboard = 0
    for dic in insulin_dict:
        insulin_onboard += dic["units"] * ( dic["duration"]/active_time )
    return insulin_onboard


def main():
    with st.form(key="child_form"):
        active_time = st.number_input('How long is your Rapid Insulin active (range is 3-5)', min_value=1)
        units = st.slider('How many units of Insulin? ', 1, 20)
        time_insulin = st.time_input('when did you take this insulin dose?')
        submitted_child = st.form_submit_button()

    if submitted_child:
        duration = datetime.combine(date.min, now) - datetime.combine(date.min, time_insulin)
        duration_total_seconds = duration.total_seconds()
        dura = float(duration_total_seconds / 3600)

        dict_to_append = {
            'duration': dura,
            'units': units,
        }
        get_data().append(dict_to_append)
        cols = st.columns(4)
        cols[0].write(f'Units')
        cols[1].write(f'Time Elapsed')
        for dic in get_data():
            cols[0].write(f'{dic["units"]}')
            cols[1].write(f'{dic["duration"]}')

    if st.button('calculate the insulin on board'):
        iob = get_insulin_on_board(active_time, get_data())
        st.success('your insulin on board is {}'.format(iob))
        clear_cache()


login_blocks = generate_login_block()
password = login(login_blocks)

if is_authenticated(password):
    clean_blocks(login_blocks)
    main()
elif password:
    st.info("Please enter a valid password")