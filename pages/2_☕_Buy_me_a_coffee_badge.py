import streamlit as st

st.set_page_config(
    page_title="Donations",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None,
)

st.info(
    "Documentation: https://arnaudmiribel.github.io/streamlit-extras/extras/badges/",
    icon="💡",
)


with st.echo():
    from streamlit_extras.badges import badge  # pip install streamlit-extras

    badge(type="buymeacoffee", name="CodingIsFun")

    with st.sidebar:
        badge(type="buymeacoffee", name="CodingIsFun")
