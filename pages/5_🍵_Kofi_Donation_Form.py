import streamlit as st

st.set_page_config(
    page_title="Donations",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None,
)


with st.echo():
    import streamlit.components.v1 as components

    components.iframe(
        src="https://ko-fi.com/codingisfun/?hidefeed=true&widget=true&embed=true&preview=true",
        width=None,
        height=800,
        scrolling=False,
    )
