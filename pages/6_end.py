import streamlit as st
from utils import stream_data

st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>🏁 The end</h2>",
    unsafe_allow_html=True,
)


st.subheader("🚨  SPOILER ALERT 🫣")

# URL de la vidéo
video_url = "https://youtu.be/M26WayJWXCM?si=Ur2NimIhUimfaHSz"

st.video(video_url, autoplay=True, muted=True)

st.subheader("🎉")

st.write_stream(
    stream_data(
        """Au nom de tous les membres de l’équipage, nous souhaitons vous adresser nos plus sincères félicitations et remerciements pour avoir bravé avec succès cet océan de données. Nous espérons que ce projet vous a apporté autant de plaisir que d’apprentissage, et nous avons hâte de vous retrouver très bientôt pour de nouvelles expériences passionnantes avec DID — Dive Into Data. 
"""
    )
)


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
