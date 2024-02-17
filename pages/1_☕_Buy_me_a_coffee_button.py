import streamlit as st

st.set_page_config(
    page_title="Donations",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None,
)


st.info(
    "Documentation: https://arnaudmiribel.github.io/streamlit-extras/extras/buy_me_a_coffee/",
    icon="💡",
)


with st.echo():
    from streamlit_extras.buy_me_a_coffee import button  # pip install streamlit-extras

    # Args:
    #     username (str): Buy Me a Coffee username
    #     floating (bool, optional): Whether the button should be floating. Defaults to True.
    #     text (str, optional): Text to show on the button. Defaults to "Buy me a coffee".
    #     emoji (str, optional): Emoji to show on the button. Defaults to "".
    #     bg_color (str, optional): Background of the button. Defaults to "#FFDD00".
    #     font (Font, optional): Font of the button. Defaults to "Cookie".
    #     font_color (str, optional): Font color. Defaults to "#000000".
    #     coffee_color (str, optional): Coffee icon color. Defaults to "#000000".
    #     width (int, optional): Width of the button. Defaults to 220.
    button(username="CodingIsFun", floating=True, width=221)

    with st.sidebar:
        button(username="CodingIsFun", floating=False)
