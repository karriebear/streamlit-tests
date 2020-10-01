import streamlit as st
from PIL import Image
import numpy as np

# clear the deprecation warning for the file uploader
st.set_option('deprecation.showfileUploaderEncoding', False)

"# Image Viewer"

IMAGE_EXTENSIONS = ['jpg', 'png', 'jpeg']
image_data = st.file_uploader('Upload an image', IMAGE_EXTENSIONS)

if not image_data:
    raise RuntimeError('Please upload a file.')

st.write(image_data.name)
image = np.array(Image.open(image_data))
st.image(image, use_column_width=True)

'---'
if st.checkbox('Show help'):
    st.help(st.file_uploader)
