# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd

# set_page_config() can only be called once per app page, and must be called as the first Streamlit command in your script.
st.set_page_config(
    menu_items={
        "Get Help": None,
        "Report a bug": "mailto:contact@diveintodata.ai?subject=Reporting%20a%20bug&body=Project:%0AOS%20(Windows,%20macOS,%20Linux,%20Android,%20iOS):%0ABrowser:%0ABug%20you%20encountered:%0A%0AThanks!",
        "About": """## Blood Cells Classification 
Project using computer vision and deep learning to automatically identify different cell types (healthy or pathological) from microscopic images.  

© 2025 Didier FLAMM & Pavithra BHASKAR  

📦 Source code: [GitHub](https://github.com/DidierFlamm/titanic-survival-predictor)  
📂 Portfolio: [Streamlit Cloud](https://share.streamlit.io/user/didierflamm)  
✉️ [contact@diveintodata.ai](mailto:contact@diveintodata.ai)  
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
        "🍁 Canada Pale Ale",
        "🇨🇦 French Version 📛",
        "🕌 India Pop Ale",
        "💿 Welcome to Gattaca",
        "💲 Your ad here for...",
    ),
    label_visibility="collapsed",
)


if ambiance.startswith("🍁"):

    video_url = "https://www.youtube.com/watch?v=ekwf5IAFLhQ"
    st.sidebar.video(video_url, autoplay=True, muted=False)

    st.sidebar.markdown(
        """
    <div style='text-align: center; font-size: small; color: gray;'>
    Charlotte Cardin - Confetti<br>
    Live at The 2024 JUNO Awards on CBC
    </div>
    """,
        unsafe_allow_html=True,
    )

elif ambiance.startswith("🇨🇦"):

    video_url = "https://www.youtube.com/watch?v=lNfAtaURtBI"
    st.sidebar.video(video_url, autoplay=True, muted=False)

    st.sidebar.markdown(
        """
    <div style='text-align: center; font-size: small; color: gray;'>
    © 2023 Charlotte Cardin - Confetti (VF)<br>
    [Official Lyric Video]
    </div>
    """,
        unsafe_allow_html=True,
    )

elif ambiance.startswith("🕌"):
    st.balloons()
    video_url = "https://youtu.be/6w67NOaRe-w?si=GvtoD5rbshLG1vaf"
    st.sidebar.video(video_url, autoplay=True, muted=False)

    st.sidebar.markdown(
        """
    <div style='text-align: center; font-size: small; color: gray;'>
    © 2013 Yeh Jawaani Hai Deewani - Illahi <br>
    [Official Video]
    </div>
    """,
        unsafe_allow_html=True,
    )

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
    © and your copyright here (or not)
    </div>
    """,
        unsafe_allow_html=True,
    )

st.sidebar.subheader("Join us on Discord", divider=True)

st.sidebar.markdown(
    """
    <a href="https://www.worldofdatacraft.com" target="_blank">
        <img src="https://github.com/DidierFlamm/DidierFlamm/raw/main/WoD_nobg.png" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)

st.sidebar.subheader("View all apps", divider=True)

st.sidebar.markdown(
    """
    <a href="https://share.streamlit.io/user/didierflamm" target="_blank">
        <img src="https://github.com/DidierFlamm/DidierFlamm/raw/main/DID.png" width="100%"; />
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
        st.Page("pages/2_viz.py", title="Visualisation", icon="📊"),
        st.Page("pages/3_preproc.py", title="Preprocessing", icon="🛠️"),
        st.Page("pages/4_ml.py", title="Machine Learning", icon="🤖"),
        st.Page("pages/5_dl.py", title="Deep Learning", icon="🧠"),
        st.Page("pages/6_pred.py", title="Predictions", icon="🎯"),
        st.Page("pages/7_end.py", title="The End", icon="🏁"),
    ]

pg = st.navigation(st.session_state.pages, position="top")
pg.run()
