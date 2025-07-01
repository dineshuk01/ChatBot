# filename: app.py
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI()

st.set_page_config(page_title="AI Agent", layout="centered")
st.title("🤖 Your AI Agent")

user_input = st.text_area("Ask me anything:")

if st.button("Submit") and user_input:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        st.markdown("### 💬 Response:")
        st.write(response.choices[0].message.content)
