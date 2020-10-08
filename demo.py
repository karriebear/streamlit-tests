from typing import Dict
import streamlit as st
import pandas as pd
import numpy as np
# import cv2 as cv

# @st.cache
# def get_image(uploaded_file):
# 	file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
# 	img = cv.imdecode(file_bytes, cv.IMREAD_COLOR)
# 	return img

uploaded_file = st.file_uploader("Choose a base image", type=['png', 'jpg', 'gif'])
# if uploaded_file is not None:
	# st.write(type(uploaded_file))
	# img = get_image(uploaded_file)
	# img_width, img_height = img.shape[:2]
	# mask_width = st.slider('Mask width', 0, img_width // 2, img_width // 10)
	#
	# # """Here is the image you uploaded:"""
	# st.write(type(img), img.shape)
	# st.image(img, use_column_width=True, channels='BGR')
# else:
	# """The uploader has no images right now."""


sidebar = st.sidebar.file_uploader('Multiple Sidebar', accept_multiple_files=True)

# txt = st.file_uploader('Multiple Files', accept_multiple_files=True)
x = st.file_uploader("Pick a file", accept_multiple_files=True)
st.write(x)
st.write("length:", len(x))

csv = st.file_uploader('CSV', type="csv")

def create_df(buffer):
    st.write(buffer.tell())
    dataframe = pd.read_csv(buffer)
    st.write(buffer.tell())

    st.write(dataframe)


"""
-------
"""
# st.set_option('deprecation.v00_063_showfileUploaderEncoding', False)
excel = st.file_uploader('Excel')

if excel is not None:
    st.write(excel)
    # data = pd.read_excel(excel)
    # st.dataframe(data.head(10))

"""
-------
"""

video = st.file_uploader('Video')

if video is not None:
    st.video(video)

"""
-------
"""
import pdfplumber

def extract_data(feed):
    data = []
    page_count = 0
    with pdfplumber.load(feed) as pdf:
        pages = pdf.pages
        page_count = len(pdf.pages)
        for p in pages:
            data.append(p.extract_tables())
    return page_count # build more code to return a dataframe

pdf = st.file_uploader('PDF')

if pdf is not None:
    df = extract_data(pdf)
    st.write(df)


#
# @st.cache(allow_output_mutation=True)
# def get_static_store() -> Dict:
#     """This dictionary is initialized once and can be used to store the files uploaded"""
#     return {}
#
#
# def main():
#     """Run this function to run the app"""
#     static_store = get_static_store()
#
#     st.info(__doc__)
#     result = st.file_uploader("Upload", type="py")
#     if result:
#         # Process you file here
#         value = result.getvalue()
#
#         # And add it to the static_store if not already in
#         if not value in static_store.values():
#             static_store[result] = value
#     else:
#         static_store.clear()  # Hack to clear list if the user clears the cache and reloads the page
#         st.info("Upload one or more `.py` files.")
#
#     if st.button("Clear file list"):
#         static_store.clear()
#     if st.checkbox("Show file list?", True):
#         st.write(list(static_store.keys()))
#     if st.checkbox("Show content of files?"):
#         for value in static_store.values():
#             st.code(value)
#
#
# main()
# st.file_uploader("Choose a CSV file")
