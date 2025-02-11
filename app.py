import streamlit as st 
import google.generativeai as genai
import os

model = None

st.title("🤖Gemini ChatGPT")
with st.sidebar:
    gemini_api_key = st.text_input(type="password", label="Gemini API Key")
    "[Get an Gemini API key](https://ai.google.dev/gemini-api/docs)"

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
    if not gemini_api_key:
        st.info("Please add your Gemini API key to continue.")
        st.stop()
    else:
        if not model:
            os.environ["GEMINI_API_KEY"] = gemini_api_key
            genai.configure(api_key=os.environ["GEMINI_API_KEY"])
            model = genai.GenerativeModel("gemini-pro")
        
    with st.chat_message("user"): st.markdown(user_query)
    invoke_gemini(user_query)