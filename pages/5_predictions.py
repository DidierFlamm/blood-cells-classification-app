import streamlit as st


st.markdown(
    "<h2 style='text-align: center; color: #DC143C;'>🎯 Predictions</h2>",
    unsafe_allow_html=True,
)

# URL de la vidéo
video_url = "https://youtu.be/vXBY6Zu46HE"

st.video(video_url, autoplay=True, muted=True)



st.write(
    "🚢 Cher passager, merci pour votre patience ! La traversée des étapes d’évaluation et d’optimisation n’est pas toujours de tout repos – surtout quand les conditions algorithmiques sont capricieuses..."
)
st.write(
    """🌟 Nous voici enfin arrivés à destination : **les prédictions**, clou du spectacle et raison d’être de tout projet en intelligence artificielle.  
    Grâce aux modèles que nous avons précédemment optimisés, nous allons enfin pouvoir répondre à **la question qui nous guide depuis le début** :  
    _“Quels types de passagers avaient le plus de chances de survivre au naufrage du Titanic ?”_"""
)
st.write(
    """🧠 Pour y répondre, le modèle sélectionné va effectuer ce qu’on appelle une **prédiction** : il va estimer – à l’aide de méthodes statistiques apprises lors de l'entraînement – **la probabilité de survie individuelle** de chaque passager."""
)


st.subheader(
    (
        ":red[Chances de survie]"
        if st.session_state.lang.startswith("fr")
        else ":red[Survival chances]"
    ),
    divider=True,
)

st.subheader(
    (
        ":red[Passager mystère]"
        if st.session_state.lang.startswith("fr")
        else ":red[Custom passenger]"
    ),
    divider=True,
)


st.write(
    """Une méthode simple et universelle pour interpréter les résultats d'un modèle consiste à **jouer avec un exemple** : on sélectionne un passager aléatoire, on observe sa probabilité de survie, puis on modifie ses caractéristiques (âge, sexe, classe…) pour voir comment cela influence la prédiction.  
    👉 **À vous de jouer !** Remplissez le formulaire ci-dessous et observez l’impact de chaque paramètre sur la chance de survie."""
)

_, col, _ = st.columns(3)
with col:
    st.write("")
    st.write("")
    st.page_link(
        st.Page(
            "pages/6_end.py",
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
