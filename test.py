import streamlit as st
import pandas as pd
from SessionState import SessionState
from SessionState import get as get_session_state

st.beta_set_page_config(
    page_title="{0}",
    page_icon="{1}",
    layout="wide",
    initial_sidebar_state="collapsed"
)

options = pd.DataFrame({'Options': ['radio', 'multiselect', 'selectbox']})

st.radio("Dataframe as input for radio buttons", options)

st.slider("Slider")

session_state = SessionState(user_name='', favorite_color='black')
session_state.user_name

session_state.user_name = 'Mary'

session_state = get_session_state(user_name='', favorite_color='black')
session_state.user_name
