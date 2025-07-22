import streamlit as st
from utils import trans_write
import pandas as pd

st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>🤖 Machine Learning</h2>",
    unsafe_allow_html=True,
)


text_0 = "😬 To our great regret, we will not be able to give you a live demonstration of the training and fine-tuning of the models on the training set, for two reasons:"

text_1 = "1. Even resized to 100x100 pixels, RGB image has 30,000 features. With 17,000 images, the model must process over 500 million data points. Traditional Machine Learning trains in a reasonable time but Deep Learning, excelling in feature extraction, requires much longer training times (tens of minutes to hours)."
text_2 = "2. Streamlit Cloud cannot host the full 300MB dataset, nor download it fast enough from an external host to provide a smooth user experience."
text_3 = "As a result, we will be showcasing only the results from the training and fine-tuning of the 3 models that was completed in advance."

for text in [text_0, text_1, text_2, text_3]:
    trans_write(text, st.session_state.lang.split("-")[0])

results = pd.DataFrame(
    {
        "Model": ["Random Forest", "SVM", "XGBoost"],
        "Accuracy with raw images": ["85%", "83%", "91%"],
        "Accuracy after segmentation": ["73%", "57%", "74%"],
    }
)
results.set_index("Model", inplace=True)

st.dataframe(results)

text = "🧐 We find that segmentation by thresholding did not deliver the expected results: while training was much faster, the performance loss does not justify its use. The best-performing Machine Learning model is XGBoost trained on the raw images with **91%** accuracy."
trans_write(text, st.session_state.lang.split("-")[0])

_, _, col = st.columns(3)
with col:
    st.write("")
    st.write("")
    st.page_link(
        st.Page(
            "pages/5_dl.py",
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
