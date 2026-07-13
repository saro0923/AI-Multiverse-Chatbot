import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load Environment Variables
load_dotenv()

# Get API Key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API Key not found! Check your .env file.")
    st.stop()

# Create Gemini Client
client = genai.Client(api_key=api_key)

# Page Configuration
st.set_page_config(
    page_title="AI Multiverse Chatbot",
    page_icon="🌌",
    layout="wide"
)

# AI Personalities
personalities = {
    "Teacher": "You are a friendly teacher. Explain concepts clearly with examples.",
    "Programmer": "You are an expert Python programmer. Give coding solutions and explanations.",
    "Motivator": "You are a motivational coach. Encourage and inspire users.",
    "Comedian": "You are a funny comedian. Answer with humor and jokes.",
    "AI Engineer": "You are an AI Engineer helping with Machine Learning, Deep Learning, Generative AI, MLOps and AI Agents."
}

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize Saved Chats
if "saved_chats" not in st.session_state:
    st.session_state.saved_chats = {}

# Title
st.title("🌌 AI Multiverse Chatbot")
st.write("Chat with different AI personalities powered by Gemini AI")

# Sidebar
st.sidebar.header("⚙️ Settings")

selected_personality = st.sidebar.selectbox(
    "Choose Personality",
    list(personalities.keys())
)

# New Chat
if st.sidebar.button("➕ New Chat"):
    st.session_state.messages = []
    st.rerun()

# Save Chat
st.sidebar.subheader("💾 Save Current Chat")

chat_name = st.sidebar.text_input(
    "Chat Name",
    placeholder="Enter chat name..."
)

if st.sidebar.button("💾 Save Chat"):
    if chat_name.strip() and st.session_state.messages:
        st.session_state.saved_chats[chat_name] = st.session_state.messages.copy()
        st.sidebar.success("Chat Saved Successfully!")
    else:
        st.sidebar.warning("Enter a chat name and have at least one message.")

# Saved Chats
st.sidebar.subheader("📁 Saved Chats")

if not st.session_state.saved_chats:
    st.sidebar.info("No saved chats yet.")
else:
    for saved_chat in st.session_state.saved_chats.keys():
        if st.sidebar.button(f"📄 {saved_chat}"):
            st.session_state.messages = (
                st.session_state.saved_chats[saved_chat].copy()
            )
            st.rerun()

# Memory Vault Viewer
with st.sidebar.expander("🧠 Memory Vault"):
    st.write(st.session_state.messages)

# Clear Chat
if st.sidebar.button("🗑️ Clear Current Chat"):
    st.session_state.messages = []
    st.rerun()

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if user_input := st.chat_input("Say something..."):

    # Save User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Personality Prompt
    prompt = f"""
    {personalities[selected_personality]}

    User Question:
    {user_input}
    """

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        bot_reply = response.text

    except Exception as e:
        bot_reply = f"Error: {str(e)}"

    # Save Assistant Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_reply
        }
    )

    with st.chat_message("assistant"):
        st.markdown(bot_reply)