import streamlit as st
import pandas as pd

try:
    from releases.release_0_65_features import FEATURES, set_page_config
except:
    import urllib.request
    with urllib.request.urlopen('https://raw.githubusercontent.com/streamlit/release-demos/master/releases/release_0_65_features.py') as response:
       exec(response.read())

__VERSION__ = "0.65.0"

set_page_config()

st.sidebar.header("New features in {0}".format(__VERSION__))
feature = st.sidebar.radio(
    "",
    [*FEATURES]
)

# st.sidebar.header("Notable Bug fixes")
# st.sidebar.markdown("")

st.sidebar.header("Callouts")
st.sidebar.markdown("Deprecation Warning: The `st.image` parameter `format` has been renamed to `output_format`")

st.sidebar.markdown("----")
st.sidebar.markdown("""
Check out our
[github](https://github.com/streamlit/streamlit/compare/0.64.0...0.64.1.dev20200811)
to see the full list of changes or join us on our
[forum](https://discuss.streamlit.io/c/official-announcements/6) for any discussions!
""")

st.header("Introducing {0}".format(feature))
st.write(FEATURES[feature]["text"])
if ("docs" in FEATURES[feature]):
    st.write("See our [docs]({0}) for more information!".format(FEATURES[feature]["docs"]))
code = FEATURES[feature]["code"]
if (feature != "Page Configurations [beta]"):
    exec(code)
st.subheader("Example:")
st.code(code, language="python")
