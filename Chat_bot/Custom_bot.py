import os
import requests
import streamlit as st

API_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
    "Content-Type": "application/json"
}


st.set_page_config(
    page_title="Character Saga",
    page_icon="👽",
    layout="wide"
)

st.title("🎭 Character Saga")
st.caption("Talk to any fictional or real character.")

# SESSION STATE

if "messages" not in st.session_state:
    st.session_state.messages = []

if "character" not in st.session_state:
    st.session_state.character = ""


# SIDEBAR

with st.sidebar:
    st.header("Character Settings")

    character = st.text_input(
        "Character Name",
        value=st.session_state.character
    )

    if st.button("Start New Chat"):
        st.session_state.messages = []
        st.session_state.character = character


# API FUNCTION

def get_response(user_message, character_name):
    payload = {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",
        "messages": [
            {
                "role": "system",
                "content": (
                    f"You are role-playing as {character_name}. "
                    f"From now on, you must fully embody {character_name}. "
                    f"Speak, think, and respond exactly as {character_name} would. "
                    f"Do not mention being an AI. "
                    f"Stay in character at all times."
                )
            }
        ]
        + st.session_state.messages
        + [{"role": "user", "content": user_message}],
        "max_tokens": 500,
        "temperature": 0.8
    }

    try:
        response = requests.post(
            API_URL,
            headers=HEADERS,
            json=payload,
            timeout=60
        )

        data = response.json()

        if "error" in data:
            return f"API Error: {data['error']}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {e}"

# DISPLAY CHAT HISTORY

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# CHAT INPUT

if prompt := st.chat_input("Type your message..."):

    if not character:
        st.warning("Please enter a character name first.")
        st.stop()

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner(f"{character} is thinking..."):
            reply = get_response(prompt, character)

        st.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )