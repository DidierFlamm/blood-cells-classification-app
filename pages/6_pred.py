import streamlit as st
import numpy as np
from PIL import Image
from utils import trans_write
import joblib


st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>🎯 Predictions</h2>",
    unsafe_allow_html=True,
)

# URL de la vidéo
video_url = "https://youtu.be/W_KruQhfvW4?si=xYCw-vPowiZdz8jy"

st.video(video_url, autoplay=True, muted=False)

st.subheader("🔮 :red[Classifier choice]", divider=True)

text = "Due to their size, deep learning models cannot be hosted or imported on Streamlit Cloud. To strike the right balance between accuracy and usability, we opted for the Random Forest model: while it reaches 83% accuracy compared to 99% for deep learning, it’s only 40 MB, which makes it much easier to deploy."
trans_write(text, st.session_state.lang.split("-")[0])

with st.expander("📊 Show the model performance evaluation"):
    st.image(
        "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/models/confusion_matrix.png",
        caption="Confusion matrix",
    )
    st.image(
        "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/models/classification_report.png",
        caption="Classification report",
    )


st.subheader("👁️ :red[Try it out: Image classification]", divider=True)


@st.cache_resource
def load_model():
    return joblib.load("models/random_forest.joblib")


model = load_model()

# Create a widget to upload a file
uploaded_file = st.file_uploader("Choose a blood cell image", type=["png", "jpg"])

if uploaded_file is not None:
    try:
        img = Image.open(uploaded_file)
        img = img.resize((100, 100), resample=Image.BILINEAR)  # type: ignore
        st.image(img)

        # Convert to numpy
        img_array = np.array(img)
        # flatten
        img_array = img_array.flatten()
        # Add dimension for batch
        img_array = img_array.reshape(1, -1)
        prediction = model.predict(img_array)
        st.info(prediction[0], icon="👁️")
    except Exception:
        st.error(f"{uploaded_file.name} is not a supported image", icon="❌")

text = "💡 Try it with the suspicious duplicates: does the model predict Neutrophil, Eosinophil, or another type? Save the image below to your device and drop it into the box above."
trans_write(text, st.session_state.lang.split("-")[0])

st.image(
    "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/blood_cells/suspicious/EO_225902.jpg",
    caption="Is this duplicate a Neutrophil or an Eosinophil ?",
)

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
