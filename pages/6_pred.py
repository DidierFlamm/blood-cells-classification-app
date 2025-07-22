import streamlit as st


st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>🎯 Predictions</h2>",
    unsafe_allow_html=True,
)

# URL de la vidéo
video_url = "https://youtu.be/W_KruQhfvW4?si=xYCw-vPowiZdz8jy"

st.video(video_url, autoplay=True, muted=False)


_, _, col = st.columns(3)
with col:
    st.write("")
    st.write("")
    st.page_link(
        st.Page(
            "pages/7_end.py",
            title=("Next"),
            icon="➡️",
        )
    )

st.divider()

st.markdown(
    """
    <div style='text-align: center; font-size: small; color: gray;'>
    © 2023 Jonathan CAMBON, Didier FLAMM, Mamadou HASSIMIOU BAH, Ilyass SAIDI, supervised by Khalil OUERTANI<br>
    © 2025 Didier FLAMM feat. Pavithra BHASKAR
    </div>
    """,
    unsafe_allow_html=True,
)
