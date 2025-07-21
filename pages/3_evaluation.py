import streamlit as st


st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>📝 Evaluation</h2>",
    unsafe_allow_html=True,
)


st.subheader(
    (
        ":red[Entraînement]"
        if st.session_state.lang.startswith("fr")
        else ":red[Training]"
    ),
    divider=True,
)


st.subheader(":red[Evaluation]", divider=True)

_, col, _ = st.columns(3)
with col:
    st.write("")
    st.write("")
    st.page_link(
        st.Page(
            "pages/4_optimization.py",
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
    © 2023 Jonathan CAMBON, Didier FLAMM, Mamadou HASSIMIOU BAH, Ilyass SAIDI, supervised by Khalil OUERTANI<br>
    © 2025 Didier FLAMM, Pavithra BHASKAR
    </div>
    """,
    unsafe_allow_html=True,
)
