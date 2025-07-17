import streamlit as st


st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>📊 Visualisation</h2>",
    unsafe_allow_html=True,
)



st.subheader(":red[Analyse univariée]", divider=True)

st.write(
    """
    L’analyse univariée consiste à examiner **chaque variable séparément**, sans tenir compte des autres. 
    Elle permet de comprendre la **répartition** des données, de détecter d’éventuels **déséquilibres**, 
    ou encore d’identifier des **outliers**, c'est à dire des valeurs extrêmes (statistiquement éloignées) ou aberrantes (souvent erronées).

    👉 Chaque onglet ci-dessous présente une **visualisation unique** de la répartition de la **variable cible** (survie),
    ainsi que des **différentes caractéristiques** (âge, sexe, classe, tarif, etc.).

    Cette étape est essentielle pour avoir une première idée de la **structure des données** avant de passer 
    à des analyses plus complexes (bivariées ou multivariées) et enfin à la modélisation prédictive.
    """
)



st.subheader(":red[Analyse bivariée]", divider=True)

st.write(
    "L’analyse bivariée consiste à étudier la **relation entre deux variables** afin de comprendre comment elles interagissent ou sont liées. C’est une étape clé pour explorer un dataset avant de modéliser. "
)
st.write(
    "• L'analyse **target/feature** permet d’étudier comment une variable explicative (feature) est liée à la variable cible (target)."
)
st.write(
    "• L'analyse **feature/feature** permet d'explorer la relation entre 2 variables explicatives. Cela peut aider à détecter des dépendances, interactions, ou colinéarités qui influencent la modélisation."
)

st.subheader(":red[Analyse multivariée]", divider=True)

st.write(
    "L’analyse multivariée étudie simultanément les relations entre trois variables ou plus afin de mieux comprendre la structure complexe des données."
)
st.write(
    "Il existe de nombreuses méthodes d'analyse multivariée permettant de détecter les interactions, réduire la dimensionnalité ou encore segmenter les observations (ACP, AFC, clustering, etc...) mais nous n'aborderons ici que 2 visualisations multivariées par graphiques interactifs"
)


_, col, _ = st.columns(3)
with col:
    st.write("")
    st.write("")
    st.page_link(
        st.Page(
            "pages/3_evaluation.py",
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
