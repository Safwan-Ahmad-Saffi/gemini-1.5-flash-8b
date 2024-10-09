import os
import streamlit as st
import google.generativeai as genai

# Set your API key (you can also set this via Hugging Face environment settings for security)
os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

# Configure the Google Generative AI SDK with your API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Define the model and generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-8b",
    generation_config=generation_config,
)
# Initialize a chat session
chat_session = model.start_chat(history=[])
# Streamlit app setup
st.title("Gemini 1.5 Chatbot")
st.write("Ask anything, and the Gemini 1.5 model will respond!")

# Create a text input for the user
user_input = st.text_input("Enter your message:", "")

# If the user provides input, send it to the chatbot
if user_input:
    # Send message to the model
    response = chat_session.send_message(user_input)
    
    # Display the response
    st.write("Gemini 1.5 says:")
    st.write(response.text)
