import streamlit as st
from utils import translate_text

st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>📊 Visualisation</h2>",
    unsafe_allow_html=True,
)


st.subheader(":red[Dataset 1]", divider=True)

text = """The dataset 1 contains 17,092 images representing eight categories of healthy peripheral blood cells, collected using the CellaVision DM96 analyzer.  
These images were evaluated by pathologists with the aim of training classification models capable of distinguishing between 8 different cell types: neutrophils, eosinophils, basophils, lymphocytes, monocytes, immature granulocytes (myelocytes, metamyelocytes, and promyelocytes), erythroblasts, and platelets.  
The image size is 360 x 363 pixels."""
text = translate_text(text, st.session_state.lang.split("-")[0])
st.write(text)

st.subheader(":red[Dataset 2]", divider=True)

text = """Dataset 2 consists of 25,917 images divided into 22 classes, including 10,100 unlabeled images.  
All patients are affected by a myeloid cell cancer, Acute Myeloid Leukemia (AML), or a variant: Acute Promyelocytic Leukemia (APL), and we cannot distinguish pathological cells from normal cells. Moreover, the categories do not match those of Dataset 1.  
For these two reasons, we decided not to use this dataset."""
text = translate_text(text, st.session_state.lang.split("-")[0])
st.write(text)

st.subheader(":red[Dataset 3]", divider=True)
text = """Dataset 3 contains 368 images divided into 2 folders:  
• IDB1: 108 images with multiple lymphoblasts identified in each image — not usable because the cells are not isolated.  
• IDB2: 260 images of isolated and labeled lymphoblasts. Among these, 130 cells are labeled as healthy and come from patients in good health. These 130 images are kept for the continuation of the project."""
text = translate_text(text, st.session_state.lang.split("-")[0])
st.write(text)

st.subheader(":red[Complete dataset]", divider=True)
text = """Among the 3 proposed datasets, we have selected:  
Dataset 1: 17,092 images (complete)  
Dataset 2: no images  
Dataset 3: 130 images (isolated and healthy lymphoblasts)  
  
for a total of 17,222 labeled images according to the blood cell type."""
text = translate_text(text, st.session_state.lang.split("-")[0])
st.write(text)

st.code(
    "ℹ️ 17222 images found in 58ms, belonging to 9 classes: ['basophil', 'eosinophil', 'erythroblast', 'ig', 'lymphoblast', 'lymphocyte', 'monocyte', 'neutrophil', 'platelet']"
)

st.image(
    "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/data_viz.png",
    caption="""4 different types of charts to show the distribution of images by cell type:  
    Bar chart, Pie chart, Horizontal bar chart and Treemap.""",
)

st.subheader(":red[Examples]", divider=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.write("basophil")
    st.image(
        "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/blood_cells/BA_47.jpg"
    )
with col2:
    st.write("eosinophil")
    st.image(
        "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/blood_cells/EO_27.jpg"
    )
with col3:
    st.write("erythroblast")
    st.image(
        "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/blood_cells/ERB_685.jpg"
    )

col1, col2, col3 = st.columns(3)
with col1:
    st.write("immature granulocyte (ig)")
    st.image(
        "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/blood_cells/IG_5887.jpg"
    )
with col2:
    st.write("lymphoblast")
    st.image(
        "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/blood_cells/Im136_0.png"
    )
with col3:
    st.write("lymphocyte")
    st.image(
        "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/blood_cells/LY_3530.jpg"
    )

col1, col2, col3 = st.columns(3)
with col1:
    st.write("monocyte")
    st.image(
        "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/blood_cells/MO_4884.jpg"
    )
with col2:
    st.write("neutrophil")
    st.image(
        "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/blood_cells/BNE_840.jpg"
    )
with col3:
    st.write("platelet")
    st.image(
        "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/blood_cells/PLATELET_2806.jpg"
    )


_, _, col = st.columns(3)
with col:
    st.write("")
    st.write("")
    st.page_link(
        st.Page(
            "pages/3_preproc.py",
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
