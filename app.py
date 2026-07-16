import os
from google import genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

st.title("Streamlit First App")
st.write("This app demonstrates a conversational agent.")

user_input = st.text_input("Ask a question:")

if st.button("Submit"):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )
    st.write(response.text)