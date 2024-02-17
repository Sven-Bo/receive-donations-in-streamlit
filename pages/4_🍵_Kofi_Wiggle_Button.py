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

    components.html(
        """
        <script type='text/javascript' src='https://storage.ko-fi.com/cdn/widget/Widget_2.js'></script>
        <script type='text/javascript'>kofiwidget2.init('Support Me on Ko-fi', '#29abe0', 'X7X47Q0EG');kofiwidget2.draw();</script>
        """,
    )

    with st.sidebar:
        components.html(
            """
            <script type='text/javascript' src='https://storage.ko-fi.com/cdn/widget/Widget_2.js'></script>
            <script type='text/javascript'>kofiwidget2.init('Support Me on Ko-fi', '#29abe0', 'X7X47Q0EG');kofiwidget2.draw();</script>
            """,
        )
