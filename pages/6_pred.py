import streamlit as st
from PIL import Image

st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>🎯 Predictions</h2>",
    unsafe_allow_html=True,
)

# URL de la vidéo
video_url = "https://youtu.be/W_KruQhfvW4?si=xYCw-vPowiZdz8jy"

st.video(video_url, autoplay=True, muted=False)

st.subheader("🔮 :red[Try the classifier]", divider=True)

# Create a widget to upload a file
uploaded_file = st.file_uploader("Choose a blood cell image", type=["png", "jpg"])

if uploaded_file is not None:
    try:
        img = Image.open(uploaded_file)
        st.image(img)
    except Exception:
        st.error(f"{uploaded_file.name} is not a supported image", icon="❌")

#######################################################################################
# Faire la prédiction
########################################################################################

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
