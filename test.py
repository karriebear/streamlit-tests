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
st.write(session_state.user_name)

session_state.user_name = 'Mary'
session_state = get_session_state(user_name='', favorite_color='black')
st.write(session_state.user_name)


"""query params"""
query_params = st.experimental_get_query_params()
app_state = st.experimental_get_query_params()

session_state = SessionState.get(first_query_params=query_params)
first_query_params = session_state.first_query_params

radio_list = ['Eat', 'Sleep', 'Both']

# The trick here is you can't change the default index based on query params on every run!
# The *only time* you do that is on the *first* run.
default_index = eval(first_query_params["radio"][0]) if "radio" in app_state else 0

genre = st.radio("What are you doing at home during quarantine?", radio_list, index=default_index)
app_state["radio"] = radio_list.index(genre)

st.experimental_set_query_params(**app_state)
