import streamlit as st
from execbox import execbox

# expander = st.beta_expander("Codepad", expanded=True)
demo = open('demo2.py', 'r')
execbox(demo.read(), autorun=False)
demo.close()
