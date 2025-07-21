import streamlit as st
from utils import stream_data

st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>🏁 The end</h2>",
    unsafe_allow_html=True,
)


st.balloons()

st.subheader("🚨 ¡ SPOILER ALERT ! 🚨")

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

st.divider()

st.markdown(
    """_📦 Le code source du projet Titanic Survival Predictor est disponible sur <a href="https://github.com/DidierFlamm/titanic-survival-predictor" target="_blank">GitHub</a>.  
    🧩 Découvrez toutes mes applications interactives sur <a href="https://share.streamlit.io/user/didierflamm" target="_blank">Streamlit Community Cloud</a>.  
    N’hésitez pas à y faire un tour puis me faire part de vos impressions via  
    ✉️ [contact@diveintodata.fr](mailto:contact@diveintodata.fr)  ou 💬 [LinkedIn](https://www.linkedin.com/in/didier-flamm)._""",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style='text-align: center; font-size: small; color: gray;'>
    © 2023 Jonathan CAMBON, Didier FLAMM, Mamadou HASSIMIOU BAH, Ilyass SAIDI, supervised by Khalil OUERTANI<br>
    © 2025 Didier FLAMM, Pavithra BHASKAR
    </div>
    """,
    unsafe_allow_html=True,
)
