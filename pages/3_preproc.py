import streamlit as st
from utils import trans_write


st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>📝 Preprocessing</h2>",
    unsafe_allow_html=True,
)


st.subheader(
    ":red[Removing duplicates]",
    divider=True,
)

text = "18 duplicate pairs were identified, 17 from dataset 1 and 1 from dataset 3"
trans_write(text, st.session_state.lang.split("-")[0])


with st.expander("🕵️ Display duplicates"):
    st.image(
        "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/blood_cells/duplicates.png"
    )

st.subheader(
    ":red[Segmentation]",
    divider=True,
)

text = """In computer vision, segmentation is a task that involves dividing an image into meaningful regions to facilitate its analysis.
The goal is to isolate objects or areas of interest, for example, separating an object from the background. There are different segmentation methods.  
For our Machine Learning models, we used a thresholding method to further highlight the cell from which the model will extract its features during training.  
This method will not be used for training Deep Learning models because they rely on CNN-based approaches."""
trans_write(text, st.session_state.lang.split("-")[0])

text = """Thresholding is a simple image processing technique used to separate objects from the background.  
  
How it works (in simple terms):  
• Each pixel in the image has an intensity value (e.g., from 0 to 255 for grayscale images).  
• You choose a threshold value (e.g., 128).  
• If the pixel value is higher than the threshold, it is set to white (255).  
• If the pixel value is lower, it is set to black (0).  
This converts the image into a binary image (black and white), making objects easier to detect.  
"""
trans_write(text, st.session_state.lang.split("-")[0])

st.image(
    "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/thresholding.png",
    caption="Example of binarization with different thresholds",
)


_, _, col = st.columns(3)
with col:
    st.write("")
    st.write("")
    st.page_link(
        st.Page(
            "pages/4_ml.py",
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
