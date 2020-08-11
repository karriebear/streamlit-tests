import streamlit as st
import pandas as pd

page_config = {
    "icon": "🌟",
    "layout": "wide",
    "sidebar":"collapsed"
}

feature_contents = {
    "Page Config": {
        "docs": 'url',
        "text":"""
Now you can configure your page. Current options include:
- Page title: Text displayed by your browser tab
- Page icon: Icon displayed by your browser tab
- Layout: Change page layout to wide or centered mode
- Initial Sidebar State: Collapse or expand the sidebar by default
""",
        "code":'''
st.beta_set_page_config(
    page_title="Streamlit Releasing v0.65!",
    page_icon="{0}",
    layout="{1}",
    initial_sidebar_state="collapsed"
)
'''.format(page_config["icon"], page_config["layout"], page_config["sidebar"]),
    },
    "Query Params": {
        "text":"We have added to our experiemental namespace the ability to get and set query parameters. With these query params, you can bookmark or share your app in various states. Thanks [@zhaoooyue](https://github.com/zhaoooyue) for the contribution!",
        "code":'''
radio_list = ['Eat', 'Sleep', 'Both']
query_params = st.experimental_get_query_params()
# Query parameters are returned as a list to support multiselect.
# Get the first item in the list if the query parameter exists.
default = int(query_params["activity"][0]) if "activity" in query_params else 0
activity = st.radio(
    "What are you doing at home during quarantine?",
    radio_list,
    index = default
)
if activity:
    st.experimental_set_query_params(activity=radio_list.index(activity))
        ''',
    },
    "Improved Dataframe Support": {
        "text":"""
With 0.65, there is additional support for pandas dataframes. These components can now take in a panda dataframe as a list of options:
- `st.radio`
- `st.multiselect`
- `st.selectbox`
        """,
        "code":'''
options = pd.DataFrame({'Options': ['radio', 'multiselect', 'selectbox']})
st.write("Input", options)

st.radio("Dataframe as input for radio buttons", options)
st.multiselect("Dataframe as input for multiselect", options)
st.selectbox("Dataframe as input for selectbox", options)
        ''',
    },
    "st.stop": {
        "text":"",
        "code":'''''',
    },
}


st.beta_set_page_config(
    page_title="Introducing Streamlit Page Config",
    page_icon=page_config["icon"],
    layout=page_config["layout"],
    initial_sidebar_state=page_config["sidebar"]
)


st.sidebar.header("New features in 0.65")
feature = st.sidebar.radio(
    "",
    [*feature_contents]
)

st.header("Introducing {0} in v0.65!".format(feature))
st.write(feature_contents[feature]["text"])
if ("docs" in feature_contents[feature]):
    st.write("See our [docs]({0}) for more information!".format(feature_contents[feature]["docs"]))
code = feature_contents[feature]["code"]
if code:
    if (feature != "Page Config"):
        exec(code)
    st.subheader("Example:")
    st.code(code, language="python")
