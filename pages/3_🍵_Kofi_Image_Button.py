import streamlit as st

st.set_page_config(
    page_title="Donations",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None,
)

with st.echo():
    st.markdown(
        """
        <a href='https://ko-fi.com/X7X47Q0EG' target='_blank'><img height='36' style='border:0px;height:36px;' 
        src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>        
        """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.markdown(
            """
        <a href='https://ko-fi.com/X7X47Q0EG' target='_blank'><img height='36' style='border:0px;height:36px;' 
        src='https://storage.ko-fi.com/cdn/kofi5.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>        
        """,
            unsafe_allow_html=True,
        )
