import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Compass - FIFA World Cup 2026 Assistant", page_icon="⚽")

st.title("⚽ Compass")
st.subheader("Multilingual Stadium Assistant - FIFA World Cup 2026")

api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

language = st.selectbox("Language / భాష ఎంచుకోండి:", ["English", "Telugu", "Hindi", "Spanish", "Portuguese"])

user_input = st.text_input("Mee question అడగండి (navigation, seating, facilities, transport):")

if st.button("Ask Compass") and user_input:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are Compass, a helpful multilingual assistant for FIFA World Cup 2026 stadium visitors. Answer in {language}. Help with navigation, seating, facilities, transportation, and general stadium information."},
                {"role": "user", "content": user_input}
            ]
        )
        answer = response.choices[0].message.content
        st.write(answer)
