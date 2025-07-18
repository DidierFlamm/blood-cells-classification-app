import time
import json
import streamlit as st
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account


# stream function
def stream_data(text, word_by_word=False, sleep=0.03):
    if word_by_word:
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.1)
    else:
        for char in text:
            yield char
            time.sleep(sleep)


# Get Google credentials from st.secrets (Streamlit Cloud)
if "google_credentials" in st.secrets:
    creds_attrdict = st.secrets["google_credentials"]
    creds_dict = dict(creds_attrdict)
    # Create JSON string from dict
    creds_json = json.dumps(creds_dict)
    # Load Google credentials from JSON string
    credentials = service_account.Credentials.from_service_account_info(
        json.loads(creds_json)
    )
    translate_client = translate.Client(credentials=credentials)
else:

    st.warning(
        "Traduction won't work because google_credentials was not found in st.secrets. Please add it to your .streamlit/secrets.toml or app settings.",
        icon="🔒",
    )


# translation function using Google Cloud Translation API
@st.cache_data
def translate_text(text: str, language: str):
    if "google_credentials" in st.secrets and not language.startswith("en"):
        return translate_client.translate(text, target_language=language)[
            "translatedText"
        ]
    else:
        return text
