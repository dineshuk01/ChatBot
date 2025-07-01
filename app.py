import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

st.set_page_config(page_title="Bot", layout="centered", page_icon="🤖")
st.title("💬 AI Chat Agent")

st.markdown("""
    <style>
    /* Hide Streamlit Main Menu */
    #MainMenu {visibility: hidden;}
    
    /* Hide footer ("Made with Streamlit") */
    footer {visibility: hidden;}
    
    /* Hide header (the top deploy bar) */
    header {visibility: hidden;}

    /* Optional: remove whitespace above the app */
    .block-container {
        padding-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)




# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Scrollable chat container using st.container()
with st.container():
    for msg in st.session_state.messages[1:]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# Chat input stays "at the bottom" after messages
prompt = st.chat_input("Type your message...")

if prompt:
    # Add user input
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    # Save AI response
    st.session_state.messages.append({"role": "assistant", "content": reply})