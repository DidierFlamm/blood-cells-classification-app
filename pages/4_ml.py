import streamlit as st


st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>🤖 Machine Learning</h2>",
    unsafe_allow_html=True,
)

st.write("3 models: XGBoost, Random Forest and SVM")

st.subheader("📈 :red[Results]", divider=True)

st.write(
    "La binarization n'a pas améliorer les performances pcq les cellules étaient déjà colorisées donc facilement identifiables par les modèles..."
)

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
