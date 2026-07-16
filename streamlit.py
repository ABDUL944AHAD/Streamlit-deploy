import os
from google import genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.title("Streamlit First App")
st.write("This app demonstrates a conversational agent. ")

user_input = st.text_input("Ask a question:")
if st.button("Submit"):
    with st.spinner("Agent is thinking..."):
        response = client.models.generate_content(
            model="gemini-2.5-flash" , contents=user_input
        )
    st.write(response.text)