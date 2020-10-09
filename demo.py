from typing import Dict
import streamlit as st
import pandas as pd
import numpy as np
# import cv2 as cv

st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader(
    "Choose a base image",
    type=['png', 'jpg', 'gif'],
    encoding="test"
)

sidebar = st.sidebar.file_uploader('Multiple Sidebar', accept_multiple_files=True)

txt = st.file_uploader('Multiple Files', accept_multiple_files=True)

csv = st.file_uploader('CSV', type="csv")

def create_df(buffer):
    st.write(buffer.tell())
    dataframe = pd.read_csv(buffer)
    st.write(buffer.tell())

    st.write(dataframe)


"""
-------
"""
excel = st.file_uploader('Excel')

if excel is not None:
    st.write(excel)

"""
-------
"""

video = st.file_uploader('Video')

if video is not None:
    st.video(video)
