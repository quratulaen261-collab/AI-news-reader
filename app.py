import streamlit as st
import pyttsx3
from news_fetcher import get_news

st.set_page_config(page_title="AI News Reader", page_icon="📰")

st.title("AI News Reader")
st.write("Click below to fetch and listen to the latest news headlines ")

category = st.selectbox(
    "Select News Category:",
    ["technology", "sports", "health", "business", "entertainment"]
)

if st.button("🎙 Fetch & Read News"):
    with st.spinner("Fetching latest news..."):
        headlines = get_news(category)
        for idx, headline in enumerate(headlines[:5], start=1):
            st.write(f"{idx}. {headline}")
        
        engine = pyttsx3.init()
        for headline in headlines[:5]:
            engine.say(headline)
        engine.runAndWait()

st.success("Ready to deliver your daily dose of news!")

