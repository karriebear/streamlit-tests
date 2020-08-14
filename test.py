import streamlit as st
import pandas as pd
import SessionState

st.beta_set_page_config(
    page_title="{0}",
    page_icon="{1}",
    layout="wide",
    initial_sidebar_state="collapsed"
)

with st.echo():
    options = pd.DataFrame({'Options': ['radio', 'multiselect', 'selectbox']})

    st.radio("Dataframe as input for radio buttons", options)


"""query params"""
with st.echo():
    query_params = st.experimental_get_query_params()
    session_state = SessionState.get(first_query_params=query_params)
    first_query_params = session_state.first_query_params
    app_state = st.experimental_get_query_params()

    radio_list = ['Eat', 'Sleep', 'Both']
    default_index = eval(first_query_params["radio"][0]) if "radio" in app_state else 0
    genre = st.radio("What are you doing at home during quarantine?", radio_list, index=default_index)
    app_state["radio"] = radio_list.index(genre)

    default_slider = eval(first_query_params["slider"][0]) if "slider" in query_params else 0
    app_state["slider"] = st.slider("slider", value=default_slider)
    st.experimental_set_query_params(**app_state)
