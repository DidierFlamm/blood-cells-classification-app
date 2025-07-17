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

default_language = 'fr-FR'
disabled = True
languages_csv = "https://raw.githubusercontent.com/DidierFlamm/titanic-survival-predictor/refs/heads/main/data/languages.csv"
languages = pd.read_csv(languages_csv)

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
    disabled=disabled,
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
    ("🔇 Silent mode", "😎 Summer version", "💿 Titanic OST"),
    label_visibility="collapsed",
)

video_url = "https://www.youtube.com/watch?v=KiBQR7jKlzM"

if ambiance.startswith("😎"):
    st.sidebar.video(video_url, autoplay=True, muted=False)

    st.sidebar.markdown(
        """
    <div style='text-align: center; font-size: small; color: gray;'>
    © 2019 Diva Faune feat. Clara Doxal
    </div>
    """,
        unsafe_allow_html=True,
    )

elif ambiance.startswith("💿"):
    tracks = {
        "1. Never an Absolution": "https://archive.org/download/TitanicMusicfromtheMotionPicture/01%20Never%20an%20Absolution.mp3",
        "2. Distant Memories": "https://archive.org/download/TitanicMusicfromtheMotionPicture/02%20Distant%20Memories.mp3",
        "3. Southampton": "https://archive.org/download/TitanicMusicfromtheMotionPicture/03%20Southampton.mp3",
        "4. Rose": "https://archive.org/download/TitanicMusicfromtheMotionPicture/04%20Rose.mp3",
        "5. Leaving Port": "https://archive.org/download/TitanicMusicfromtheMotionPicture/05%20Leaving%20Port.mp3",
        '6. "Take Her to Sea, Mr. Murdoch"': "https://archive.org/download/TitanicMusicfromtheMotionPicture/06%20%22Take%20Her%20to%20Sea%2C%20Mr.%20Murdoch%22.mp3",
        '7. "Hard to Starboard"': "https://archive.org/download/TitanicMusicfromtheMotionPicture/07%20Track07.mp3",
        "8. Unable to Stay, Unwilling to Leave": "https://archive.org/download/TitanicMusicfromtheMotionPicture/08%20Unable%20to%20Stay%2C%20Unwilling%20to%20Leave.mp3",
        "9. The Sinking": "https://archive.org/download/TitanicMusicfromtheMotionPicture/09%20The%20Sinking.mp3",
        "10. Death of Titanic": "https://archive.org/download/TitanicMusicfromtheMotionPicture/10%20Death%20of%20Titanic.mp3",
        "11. A Promise Kept": "https://archive.org/download/TitanicMusicfromtheMotionPicture/11%20A%20Promise%20Kept.mp3",
        "12. A Life So Changed": "https://archive.org/download/TitanicMusicfromtheMotionPicture/12%20A%20Life%20So%20Changed.mp3",
        "13. An Ocean of Memories": "https://archive.org/download/TitanicMusicfromtheMotionPicture/13%20An%20Ocean%20of%20Memories.mp3",
        "14. My Heart Will Go On": "https://archive.org/download/TitanicMusicfromtheMotionPicture/14%20My%20Heart%20Will%20Go%20On.mp3",
        "15. Hymn to the Sea": "https://archive.org/download/TitanicMusicfromtheMotionPicture/15%20Hymn%20to%20the%20Sea.mp3",
    }

    if "track_index" not in st.session_state:
        st.session_state.track_index = 0

    track = st.sidebar.selectbox(
        "Select track",
        list(tracks.keys()),
        index=st.session_state.track_index,
    )

    st.session_state.track_index = list(tracks.keys()).index(track)

    st.sidebar.audio(
        tracks[track],
        format="audio/mpeg",
        autoplay=True,
    )

    st.sidebar.markdown(
        """
    <div style='text-align: center; font-size: small; color: gray;'>
    © 1997 James Horner
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
            icon="🏡",
            default=True,
        ),
        st.Page("pages/2_vizualisation.py", title="Vizualisation", icon="📊"),
        st.Page("pages/3_evaluation.py", title="Evaluation", icon="📝"),
        st.Page("pages/4_optimization.py", title="Optimization", icon="📈"),
        st.Page("pages/5_predictions.py", title="Predictions", icon="🎯"),
        st.Page("pages/6_end.py", title="End", icon="🏁"),
    ]

pg = st.navigation(st.session_state.pages, position="top")
pg.run()
