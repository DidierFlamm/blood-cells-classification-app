import streamlit as st
from utils import trans_write


st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>🧠 Deep Learning</h2>",
    unsafe_allow_html=True,
)

st.subheader(":red[VGG16]", divider=True)

text = "This neural network consists of 16 deep layers, composed of two main parts: the first is a set of convolutional layers for feature extraction, and the second is a series of dense layers aimed at classifying the cell types."
trans_write(text, st.session_state.lang.split("-")[0])

st.image(
    "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/deep_learning/VGG16.png",
    caption="Detailed diagram of the VGG16 network with its 16 layers",
)

text = "To enhance the performance of the VGG16 model, data is extracted from intermediate layers before being classified by a Machine Learning model. This approach is known as Feature Extraction. The fine-tuning of VGG16 is carried out using a grid search over various parameters, summarized below."
trans_write(text, st.session_state.lang.split("-")[0])

st.image(
    "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/deep_learning/VGG16_results.png",
    caption="Accuracy results for different hyperparameter configurations",
)

text = "The best-performing configuration, with an accuracy of **98.89%**, was achieved using the following hyperparameters:"
trans_write(text, st.session_state.lang.split("-")[0])

params = {
    "Trained layers": 21,
    "Batch size": 32,
    "Extraction layer": 2,
    "Classifier": "XGBoost",
}

st.json(params)

st.subheader(":red[ResNet50]", divider=True)

text_1 = """When working with deep convolutional neural networks to solve computer vision problems, machine learning experts tend to stack more layers.
These additional layers help tackle complex problems more effectively because the different layers can be trained for various tasks to achieve highly accurate results.
While increasing the number of stacked layers can enhance the model’s feature representations, a deeper network can suffer from the degradation problem.
In other words, as the number of layers in the neural network grows, accuracy levels may plateau and then gradually decline beyond a certain point.
As a result, the model’s performance deteriorates on both training and test data.
This degradation is not due to overfitting. It can result from the network initialization, the optimization function, or, more importantly, the vanishing or exploding gradients problem."""

text_2 = """ResNet was created specifically to address this issue.
Deep residual networks use residual blocks to improve model accuracy.
The concept of "skip connections," which lies at the core of residual blocks, is the key strength of this type of neural network."""

for text in [text_1, text_2]:
    trans_write(text, st.session_state.lang.split("-")[0])

st.image(
    "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/deep_learning/ResNet50.png",
    caption="Detailed diagram of the ResNet50 network with its 50 layers",
)

st.image(
    "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/deep_learning/ResNet50_results.png",
    caption="Accuracy results for different hyperparameter configurations",
)

text = "The best-performing configuration, with an accuracy of **95.58%**, was achieved using the following hyperparameters:"
trans_write(text, st.session_state.lang.split("-")[0])

params = {
    "Frozen layers": 143,
    "Learning Rate": 2e-5,
    "Configuration": 1,
    "Image size": "100x100",
}

st.json(params)


st.subheader(":red[DenseNet121]", divider=True)

text = """In a DenseNet architecture, each layer is connected to all previous layers. This means that information from all preceding layers is combined and passed on to every subsequent layer. Such dense connectivity promotes better information flow and gradient propagation, helping to mitigate the vanishing gradient problem (where gradients diminish rapidly during backpropagation) and improving the model’s performance."""
trans_write(text, st.session_state.lang.split("-")[0])

st.image(
    "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/deep_learning/DenseNet121.webp",
    caption="Diagram of the DenseNet121 network",
)

st.image(
    "https://github.com/DidierFlamm/blood-cells-classification-app/raw/main/data/deep_learning/DenseNet121_results.png",
    caption="Accuracy results for different hyperparameter configurations",
)

text = "The best-performing configuration, with an accuracy of **98.13%**, was achieved using the following hyperparameters:"
trans_write(text, st.session_state.lang.split("-")[0])

params = {
    "Frozen layers": 150,
}

st.json(params)

_, _, col = st.columns(3)
with col:
    st.write("")
    st.write("")
    st.page_link(
        st.Page(
            "pages/6_pred.py",
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
