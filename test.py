import streamlit as st
import pandas as pd
import SessionState

st.beta_set_page_config(
    page_title="{0}",
    page_icon="{1}",
    layout="wide",
    initial_sidebar_state="collapsed"
)

options = pd.DataFrame({'Options': ['radio', 'multiselect', 'selectbox']})

st.radio("Dataframe as input for radio buttons", options)


"""query params"""
query_params = st.experimental_get_query_params()
number = st.slider("slider")
st.write(number)

st.hello.hello.run()
