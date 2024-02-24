import streamlit as st

st.set_page_config(
    page_title="Donations",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None,
)


st.info(
    "Starting with Streamlit version v1.31.0, you can now use `st.page_link` to create links to external pages. To upgrade to the latest version of Streamlit, run `pip install streamlit --upgrade`.",
    icon="💡",
)


with st.echo():
    st.page_link("https://ko-fi.com/codingisfun", label="Support me", icon="☕")
