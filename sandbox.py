import streamlit as st
from execbox import execbox

# expander = st.beta_expander("Codepad", expanded=True)

try:
    demo = open('demo2.py', 'r')
    starting_code = demo.read()
    demo.close()
except:
    starting_code = "import streamlit as st"

execbox(starting_code, autorun=False)
