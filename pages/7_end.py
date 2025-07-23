import streamlit as st
from utils import translate_text, stream_data

st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>🏁 The end</h2>",
    unsafe_allow_html=True,
)


st.subheader("🚨  SPOILER ALERT 🫣")

# URL de la vidéo
video_url = "https://youtu.be/M26WayJWXCM?si=Ur2NimIhUimfaHSz"

st.video(video_url, autoplay=False, muted=False)
st.markdown(
    """<p style='text-align: center; font-size: 0.8rem; color: gray;'>
    Right Handed Men Don't Hold It With Their Left | Gattaca Ending Scene<br>
    <em>🌐 Auto-generated subtitles can be activated by clicking ⚙️ at the bottom right of the video.</em>
    </p>""",
    unsafe_allow_html=True,
)


st.subheader("🎉")

OUTRO = """On behalf of all the crew members, we would like to extend our sincerest congratulations and thanks for successfully navigating this ocean of data. We hope this project brought you as much enjoyment as learning, and we look forward to seeing you very soon for more exciting experiences with DID — Dive Into Data."""

OUTRO = translate_text(OUTRO, st.session_state.lang.split("-")[0])

st.write_stream(stream_data(OUTRO))


st.write_stream(stream_data("A bientôt !"))

st.write_stream(stream_data("Didier & Pavithra 🫡🫡", sleep=0.7))

st.balloons()
st.image(
    "https://raw.githubusercontent.com/DidierFlamm/blood-cells-classification-app/main/data/MAIHA.png",
    caption="""MAKE AI H🔥T AGAIN  
    © 2025 ChatGPT feat. MS Copilot""",
)

st.divider()

st.markdown(
    """📦 Source code: <a href="https://github.com/DidierFlamm/titanic-survival-predictor" target="_blank">GitHub</a>  
    📂 Portfolio: <a href="https://share.streamlit.io/user/didierflamm" target="_blank">Streamlit Cloud</a>  
    🅦 Discord: <a href="https://www.worldofdatacraft.com" target="_blank">World of Datacraft</a>  
    ✉️ [contact@diveintodata.ai](mailto:contact@diveintodata.ai)  
    💬 LinkedIn: [Didier](https://www.linkedin.com/in/didier-flamm) - [Pavithra](https://www.linkedin.com/in/pavithrabhaskar)""",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style='text-align: center; font-size: small; color: gray;'>
    © 2023 Jonathan CAMBON, Didier FLAMM, Mamadou HASSIMIOU BAH, Ilyass SAIDI, supervised by Khalil OUERTANI<br>
    © 2025 Didier FLAMM feat. Pavithra BHASKAR
    </div>
    """,
    unsafe_allow_html=True,
)
