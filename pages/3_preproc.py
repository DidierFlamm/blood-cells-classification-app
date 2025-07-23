import streamlit as st
from utils import trans_write


st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>📝 Preprocessing</h2>",
    unsafe_allow_html=True,
)


st.subheader(
    ":red[Resizing and removing duplicates]",
    divider=True,
)

text = "18 duplicate pairs were identified, 17 from dataset 1 and 1 from dataset 3"
trans_write(text, st.session_state.lang.split("-")[0])


with st.expander("🕵️ Show the duplicates"):
    st.image(
        "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/blood_cells/duplicates.png"
    )

st.subheader(":red[Fun fact]", divider=True)
text = """At this point, we have a clean dataset, free of duplicates and with images of identical sizes — conditions necessary for effective models training. The images have been evaluated by pathologists, and it is impossible for us to identify any potential labeling errors that may have occurred. However, there is one exception: we can state with certainty that at least one image has been mislabeled in the dataset. Indeed, among the duplicates detected earlier, two strictly identical images (pixel by pixel) have been classified into two different categories: Neutrophil and Eosinophil. 🎭 Fun challenge: try to spot the two images in question in the duplicates grid above."""
trans_write(text, st.session_state.lang.split("-")[0])

with st.expander("🔑 Reveal the 2 suspicious duplicates"):
    col1, col2 = st.columns(2)
    col1.write("Neutrophil - BNE_191112")
    col1.image(
        "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/blood_cells/suspicious/BNE_191112.jpg"
    )
    col2.write("Eosinophil - EO_225902")
    col2.image(
        "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/blood_cells/suspicious/EO_225902.jpg"
    )

text = """🔍 By the end of the project, we will use a trained and fine-tuned model to predict the most probable cell type for this duplicate image.
    "Save one of the two identical images above, and you’ll soon have access to the model’s prediction—providing more insight to determine whether the duplicate corresponds to a Neutrophil or an Eosinophil."""

trans_write(text, st.session_state.lang.split("-")[0])

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
• Each pixel in the image has an intensity value between 0 and 1 for each RGB channel..  
• You choose a threshold value (e.g., 0.5).  
• If the pixel value is higher than the threshold, it is set to white (1).  
• If the pixel value is lower, it is set to black (0).  
This transforms the image into a binary (black and white) format, reducing file size and making object detection easier, thus shortening the model training time. 
"""
trans_write(text, st.session_state.lang.split("-")[0])

st.image(
    "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/blood_cells/thresholding.png",
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
