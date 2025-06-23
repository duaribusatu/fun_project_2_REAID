import streamlit as st
import requests
import time

# Page config
st.set_page_config(
    page_title="AI Chatbot by Dandi",
    page_icon="💬",
    layout="centered"
)

# Sidebar
with st.sidebar:
    st.title("📋 Menu")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Chat cleared! Start a new conversation."}
        ]
        st.rerun()

# Title
st.title("AI Chatbot 😎💬")
st.caption("Powered by Dandi Septiandi")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Ask me anything and I'll help you."}
    ]

# API call
def get_openrouter_response(user_input):
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {st.secrets['openrouter_key']}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistralai/mistral-7b-instruct:free",
                "messages": [{"role": "user", "content": user_input}],
                "temperature": 0.7
            },
            timeout=15
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: Failed to get response from OpenRouter\n\n`{e}`"

# Custom bubble style
def chat_bubble(text, align="left", bg="#f0f2f6"):
    align_css = "right" if align == "right" else "left"
    bubble_color = "#DCF8C6" if align == "right" else bg
    st.markdown(
        f"""
        <div style='text-align: {align_css}; padding: 5px 0;'>
            <div style='
                display: inline-block;
                background: {bubble_color};
                padding: 10px 15px;
                border-radius: 15px;
                max-width: 80%;
                color: black;
            '>{text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Chat input
user_input = st.chat_input("Type your message here...")

# Show previous messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        chat_bubble(msg["content"], align="right", bg="#d1edff")
    else:
        chat_bubble(msg["content"], align="left", bg="#f0f0f0")

# Handle the new prompt after displaying full history
if user_input:
    # Add and display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    chat_bubble(user_input, align="right", bg="#d1edff")

    # Get and display assistant response with typing effect
    with st.spinner("Thinking..."):
        assistant_reply = get_openrouter_response(user_input)

    placeholder = st.empty()
    typed = ""
    for char in assistant_reply:
        typed += char
        placeholder.markdown(
            f"""
            <div style='text-align: left; padding: 5px 0;'>
                <div style='
                    display: inline-block;
                    background: #f0f0f0;
                    padding: 10px 15px;
                    border-radius: 15px;
                    max-width: 80%;
                    color: black;
                '>{typed}▌</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        time.sleep(0.015)

    # Finalize bubble
    placeholder.markdown(
        f"""
        <div style='text-align: left; padding: 5px 0;'>
            <div style='
                display: inline-block;
                background: #f0f0f0;
                padding: 10px 15px;
                border-radius: 15px;
                max-width: 80%;
                color: black;
            '>{typed}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Save AI message
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
