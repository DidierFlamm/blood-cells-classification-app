# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as components

st.markdown(
    "<h1 style='text-align: center; '>🌊 Dive into Computer Vision 👁️</h1>",
    unsafe_allow_html=True,
)

st.write("")
st.write("")

st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>🩸 Blood Cells Classification 🔬</h2>",
    unsafe_allow_html=True,
)

st.image(
    "https://towardsdatascience.com/wp-content/uploads/2022/05/1k3oWPNpDC5tvok-04QAKVw.jpeg",
    caption=(
        """Image by Colin Behrens"""
    ),
)


st.subheader(":red[Introduction]", divider=True)


# Textes à lire

INTRO = """
Bla bla bla... et voilà !

Vos capitaines Flamm Didier et Bhaskar Pavithra, et vos matelots James et Charlize, vous souhaitent la bienvenue à bord du projet 'Blood Cells'. Embarquez pour un voyage serein et passionnant à travers le vaste océan des données !
"""

OUTRO = """WoD — World of Datacraft"""


script = f"""
<script>
    var msgINTRO = new SpeechSynthesisUtterance({INTRO!r});
    msgINTRO.lang = {st.session_state.lang!r};
    msgINTRO.rate = 1.1;

    var msgOUTRO = new SpeechSynthesisUtterance({OUTRO!r});
    msgOUTRO.lang = 'en-GB';
    msgOUTRO.rate = 1.1;

    function speak() {{
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(msgINTRO);
        window.speechSynthesis.speak(msgOUTRO);
    }}

    function stop() {{
        window.speechSynthesis.cancel();
    }}
</script>
"""

(col1, col2, *_) = st.columns(4, vertical_alignment="center")

with col1:
    components.html(
        script
        + f"""<button onclick="speak()">🎧 {st.session_state.flag}<br>Audio Guide</button>""",
        height=45,
    )

with col2:
    components.html(
        script + """<button onclick="stop()">🔇<br>Stop</button>""",
        height=45,
    )

st.write(INTRO)

_, col, _ = st.columns(3)
with col:
    st.write("")
    st.write("")
    st.page_link(
        st.Page(
            "pages/2_vizualisation.py",
            title=(
                "Passer à l'étape suivante"
                if st.session_state.lang.startswith("fr")
                else "Go to the next step"
            ),
            icon="➡️",
        )
    )

st.divider()

st.markdown(
    """
    <div style='text-align: center; font-size: small; color: gray;'>
    © 2025 World of Datacraft
    </div>
    """,
    unsafe_allow_html=True,
)
