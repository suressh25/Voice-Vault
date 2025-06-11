# streamlit_app.py
import streamlit as st
from converter import text_to_speech
from upload import upload_to_s3

st.title("🎧 Notes to Podcast Converter")

text = st.text_area("Enter your notes")

if st.button("Convert and Upload"):
    text_to_speech(text, "output.mp3")
    url = upload_to_s3("output.mp3", "voice-vault-suresh")
    st.success("Podcast uploaded!")
    st.audio(url)
    st.markdown(f"[Listen here]({url})")
