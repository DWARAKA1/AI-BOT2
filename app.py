import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Streamlit app
st.title("AI-BOT")

# User input
user_input = st.text_input("Enter your message:")

if st.button("Submit"):
    # Create chat completion
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
    )

    # Display the response
    st.write("Response:")
    st.write(chat_completion.choices[0].message.content)
