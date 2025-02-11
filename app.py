import streamlit as st 
import google.generativeai as genai
import os

os.environ["GEMINI_API_KEY"] = "[YOUR_API_KEY]"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

st.title("🤖Gemini ChatGPT")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]): st.markdown(msg["content"])

def invoke_gemini(user_query):
    response = model.generate_content(user_query)
    with st.chat_message("assistant"):st.markdown(response.text)
    st.session_state.messages.append(
        {
         "role": "user",
         "content": user_query
         }
    )
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.text
        }
    )
    
user_query = st.chat_input("Message Gemini GPT")

if user_query:
    with st.chat_message("user"): st.markdown(user_query)
    invoke_gemini(user_query)