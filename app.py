# app.py
import asyncio
import streamlit as st
from agent import AskAgent  # Import the Agent function

st.set_page_config(page_title="YouTube GPT Agent", layout="wide")
st.title("YouTube GPT Agent")
st.write("Enter a YouTube video URL and ask a question or request a summary.")

# User inputs
url_input = st.text_input("YouTube Video URL")
query_input = st.text_input("Question or Summary Request", "Summarize the video in 2 sentences.")

# Run Agent button
if st.button("Run Agent") and url_input.strip():
    with st.spinner("Agent is processing..."):
        try:
            result = asyncio.run(AskAgent(url_input.strip(), query_input.strip()))
            st.success("Agent Finished")
            st.text_area("Agent Output", value=result, height=400)
        except Exception as e:
            st.error(f"Error running agent: {e}")
else:
    st.info("Enter a URL and click 'Run Agent'.")
