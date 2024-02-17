import streamlit as st


st.set_page_config(
    page_title="Donations",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items=None,
)

st.title("💰 Get Donations for Your App!", anchor=False)
st.subheader(
    "Let's add donation buttons to support your app. Quick and easy!", anchor=False
)
st.write(" ")

with st.container(border=True):
    st.page_link(
        "https://www.buymeacoffee.com/", label="**BuyMeACoffee Website**", icon="🌍"
    )
    st.page_link(
        "pages/1_☕_Buy_me_a_coffee_button.py",
        label="Buy Me A Coffee - Button",
        icon="1️⃣",
    )
    st.page_link(
        "pages/2_☕_Buy_me_a_coffee_badge.py", label="Buy Me A Coffee - Badge", icon="2️⃣"
    )
    with st.expander("Getting started with BuyMeACoffee"):
        st.video(
            "https://youtu.be/D6jDmCQIink?si=zV6bpIo9L0rccTVV",
            format="video/mp4",
            start_time=0,
        )


with st.container(border=True):
    st.page_link("https://ko-fi.com/", label="**Ko-Fi Website**", icon="🌍")
    st.page_link(
        "pages/3_🍵_Kofi_Image_Button.py", label="Kofi - Image Button", icon="1️⃣"
    )
    st.page_link(
        "pages/4_🍵_Kofi_Wiggle_Button.py", label="Kofi - Wiggle Button", icon="2️⃣"
    )
    st.page_link(
        "pages/5_🍵_Kofi_Donation_Form.py", label="Kofi - Donation Form", icon="3️⃣"
    )

    with st.expander("Getting started with Ko-Fi"):
        st.video(
            "https://youtu.be/Xvd4KgV4g-0?si=FobB6xKekcHcMaCY",
            format="video/mp4",
            start_time=0,
        )
