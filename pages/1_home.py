# -*- coding: utf-8 -*-
import streamlit as st
from utils import translate_text
import streamlit.components.v1 as components

st.markdown(
    "<h1 style='text-align: center; '>🤿 Dive into Computer Vision 👁️</h1>",
    unsafe_allow_html=True,
)

st.write("")
st.write("")

st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>🔬 Blood Cells Classification 🩸</h2>",
    unsafe_allow_html=True,
)

st.image(
    "https://towardsdatascience.com/wp-content/uploads/2022/05/1k3oWPNpDC5tvok-04QAKVw.jpeg",
    caption=("""Image by Colin Behrens"""),
)


st.subheader(":red[Introduction]", divider=True)


# Textes à lire

INTRO = """
The first version of this project, conducted between April 24 and July 4, 2023, by a team of four students from the Data Scientist Bootcamp (April 2023 cohort) at DataScientest.com, focuses on applying computer vision techniques to medical imaging.

The goal is to automatically identify and classify different types of blood cells from microscopic images using state-of-the-art machine learning and deep learning algorithms. The relative density and distribution of blood cells in a smear are essential diagnostic indicators for various pathologies. For example, leukemia diagnosis often relies on the lymphocyte-to-other-cell ratio. Accurate detection of abnormal leukocytes is therefore a critical step in supporting early diagnosis and treatment planning. Our approach aims to build a pipeline capable of preprocessing, segmenting, and classifying cells, paving the way for both clinical decision support systems and research applications.

The project began with an exploratory analysis of the datasets, including data cleaning, normalization, and augmentation to address class imbalance and improve generalization. We implemented a complete machine learning workflow, starting with traditional models (Random Forest, SVM) for baseline performance, followed by convolutional neural networks (CNNs) for advanced feature extraction and classification.

Given the time constraints and computational resources, we focused this first stage on classifying healthy blood cells. This step provides a robust foundation for future work aimed at detecting abnormal cells and computing relevant clinical ratios (e.g., lymphocyte percentage) in real patient samples.

Two years later, in July 2025, a second version of the project was launched by a 'Dive Into Data' team composed of two dedicated data scientists. This iteration made the application more accessible to the general public, drawing a fascinating parallel between the futuristic technologies imagined by Andrew Niccol in his 1997 cult film 'Welcome to Gattaca' and the computer vision techniques developed in this project.

Captains Flamm Didier and Bhaskar Pavithra, together with their fearless young crew members James and Charlize, welcome you aboard the Blood Cells Project. Get ready to set sail on an exciting and insightful journey across the boundless ocean of data, where every wave of information brings us closer to uncovering the secrets hidden within blood cells.
"""

INTRO = translate_text(INTRO, st.session_state.lang.split("-")[0])

script = f"""
<script>
    var msgINTRO = new SpeechSynthesisUtterance({INTRO!r});
    msgINTRO.lang = {st.session_state.lang!r};
    msgINTRO.rate = 1.1;



    function speak() {{
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(msgINTRO);
        
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

st.subheader(":red[Data]", divider=True)

st.write(
    """
The models were trained and evaluated on three publicly available datasets:  
Dataset 1: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7182702/  
Dataset 2: https://www.kaggle.com/eugeneshenderov/acute-promyelocytic-leukemia-apl  
Dataset 3: https://www.kaggle.com/nikhilsharma00/leukemia-dataset

We also relied on prior work and scientific literature:  
https://www.sciencedirect.com/science/article/abs/pii/S0169260719303578?via%3Dihub  
https://www.sciencedirect.com/science/article/abs/pii/S0169260721000742?via%3Dihub
"""
)

_, col, _ = st.columns(3)
with col:
    st.write("")
    st.write("")
    st.page_link(
        st.Page(
            "pages/2_visualisation.py",
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
    © 2023 Jonathan CAMBON, Didier FLAMM, Mamadou HASSIMIOU BAH and Ilyass SAIDI
    © 2025 Didier FLAMM feat. Pavithra BHASKAR (Dive Into Data)
    </div>
    """,
    unsafe_allow_html=True,
)
