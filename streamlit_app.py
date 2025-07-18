# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd

# set_page_config() can only be called once per app page, and must be called as the first Streamlit command in your script.
st.set_page_config(
    menu_items={
        "Get Help": None,
        "Report a bug": "mailto:contact@diveintodata.fr?subject=Reporting%20a%20bug%20in%20titanic-survival-predictor%20Streamlit%20app&body=OS%20(Windows,%20macOS,%20Linux,%20Android,%20iOS):%0ABrowser:%0ABug%20you%20encountered:%0A%0AThanks!",
        "About": """## Blood Cells Classification 
This project predicts the survival chances of Titanic passengers using machine learning. The source code is available on [GitHub](https://github.com/DidierFlamm/titanic-survival-predictor)  

© 2025 Didier Flamm  
✉️ [contact@diveintodata.fr](mailto:contact@diveintodata.fr) – 💬 [LinkedIn](https://www.linkedin.com/in/didier-flamm) – 📁 [Portfolio](https://share.streamlit.io/user/didierflamm)  
""",
    }
)

st.logo(
    "https://img.icons8.com/?size=100&id=s5NUIabJrb4C&format=png&color=000000",
    size="large",
)

st.sidebar.subheader("Language", divider=True)

default_language = "en-US"
disable_language_selectbox = False
languages_csv = "https://raw.githubusercontent.com/DidierFlamm/blood-cells-classification-app/refs/heads/main/data/languages.csv"
languages = pd.read_csv(languages_csv)

if "google_credentials" not in st.secrets:
    disable_language_selectbox = True

index = languages.loc[languages["lang"] == default_language].index[0]


def format_language(x):
    row = languages.loc[languages["lang"] == x]
    row = row.iloc[0]
    return f"{row["flag"]} {row["local"]} ({row["region"]})"


st.sidebar.selectbox(
    "Select language",
    options=languages.lang,
    key="lang",
    format_func=format_language,
    label_visibility="collapsed",
    disabled=disable_language_selectbox,
    index=int(index),
)


try:
    flag = languages.loc[languages.lang == st.session_state.lang, "flag"].values[0]  # type: ignore
except Exception:
    flag = ""
st.session_state.flag = flag

st.sidebar.subheader("Ambiance", divider=True)

ambiance = st.sidebar.radio(
    "Select ambiance",
    (
        "🔇 Silent mode",
        "🎛️ French Connexion",
        "🕌 India Pop Ale",
        "💿 Welcome to Gattaca",
        "💲 Your ad here for...",
    ),
    label_visibility="collapsed",
)


if ambiance.startswith("🎛️"):

    video_url = "https://youtu.be/8xH_DijmoB8"
    st.sidebar.video(video_url, autoplay=True, muted=False)

    st.sidebar.markdown(
        """
    <div style='text-align: center; font-size: small; color: gray;'>
    © 2025 Astech
    </div>
    """,
        unsafe_allow_html=True,
    )

elif ambiance.startswith("🕌"):
    st.sidebar.write("🚧🚧🚧🚧🚧🚧🚧🚧")

elif ambiance.startswith("💿"):
    video_url = "https://youtu.be/zeNOEumJQdg?si=RSuNSwO0rVbC9wiH"
    st.sidebar.video(video_url, autoplay=True, muted=False)

    st.sidebar.markdown(
        """
    <div style='text-align: center; font-size: small; color: gray;'>
    © 1997 Michael Nyman
    </div>
    """,
        unsafe_allow_html=True,
    )

elif ambiance.startswith("💲"):

    st.sidebar.markdown(
        "<h3 style='text-align: center; color: red;'>FREE !</h3>",
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        """
    <div style='text-align: center; font-size: small; color: gray;'>
    © Your copyright here
    </div>
    """,
        unsafe_allow_html=True,
    )

st.sidebar.subheader("View all apps", divider=True)

st.sidebar.markdown(
    """
    <a href="https://share.streamlit.io/user/didierflamm" target="_blank">
        <img src="https://github.com/DidierFlamm/DidierFlamm/blob/main/WoD_nobg.png?raw=true" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)


if "pages" not in st.session_state:
    st.session_state.pages = [
        st.Page(
            "pages/1_home.py",
            title="Home",
            icon="🔬",
            default=True,
        ),
        st.Page("pages/2_visualisation.py", title="Visualisation", icon="📊"),
        st.Page("pages/3_evaluation.py", title="Evaluation", icon="📝"),
        st.Page("pages/4_optimization.py", title="Optimization", icon="📈"),
        st.Page("pages/5_predictions.py", title="Predictions", icon="🎯"),
        st.Page("pages/6_end.py", title="The End", icon="🏁"),
    ]

pg = st.navigation(st.session_state.pages, position="top")
pg.run()
