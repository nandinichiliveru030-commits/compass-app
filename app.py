import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Compass - FIFA World Cup 2026 Assistant", page_icon="⚽")

st.title("⚽ Compass")
st.subheader("Multilingual Stadium Assistant - FIFA World Cup 2026")

api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

language = st.selectbox("Language / భాష ఎంచుకోండి:", ["English", "Telugu", "Hindi", "Spanish", "Portuguese"])

user_input = st.text_input("Mee question అడగండి (navigation, seating, facilities, transport):")

if st.button("Ask Compass") and user_input:
    with st.spinner("Thinking..."):
        prompt = f"You are Compass, a helpful multilingual assistant for FIFA World Cup 2026 stadium visitors. Answer in {language}. Help with navigation, seating, facilities, transportation, and general stadium information.\n\nUser question: {user_input}"
        response = model.generate_content(prompt)
        st.write(response.text)
