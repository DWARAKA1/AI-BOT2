import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="AI-BOT2",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "groq_client" not in st.session_state:
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        st.error("Please set your GROQ_API_KEY in the .env file")
        st.stop()
    st.session_state.groq_client = Groq(api_key=api_key)

# App header
st.title("🤖 AI-BOT2")
st.markdown("*Powered by Groq API*")

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    model = st.selectbox(
        "Model",
        ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768"]
    )
    max_tokens = st.slider("Max Tokens", 100, 2000, 1000)
    temperature = st.slider("Temperature", 0.0, 2.0, 0.7)
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Prepare messages for API
                api_messages = [{"role": msg["role"], "content": msg["content"]} 
                               for msg in st.session_state.messages]
                
                # Create chat completion
                response = st.session_state.groq_client.chat.completions.create(
                    model=model,
                    messages=api_messages,
                    max_tokens=max_tokens,
                    temperature=temperature
                )
                
                assistant_response = response.choices[0].message.content
                st.markdown(assistant_response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": assistant_response
                })
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Please check your API key and try again.")
