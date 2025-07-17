import streamlit as st


st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>📈 Optimisation</h2>",
    unsafe_allow_html=True,
)


st.subheader("🔧 :red[Fine tuning]", divider=True)


st.subheader(
    (
        "🏆 :red[Classement]"
        if st.session_state.lang.startswith("fr")
        else "🏆 :red[Ranking]"
    ),
    divider=True,
)

_, col, _ = st.columns(3)
with col:
    st.write("")
    st.write("")
    st.page_link(
        st.Page(
            "pages/5_predictions.py",
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
    © 2025 World of Datacraft
    </div>
    """,
    unsafe_allow_html=True,
)
