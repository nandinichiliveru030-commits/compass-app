import streamlit as st
import anthropic

st.set_page_config(page_title="Compass - FIFA World Cup 2026 Assistant", page_icon="⚽")

st.title("⚽ Compass")
st.subheader("Multilingual Stadium Assistant - FIFA World Cup 2026")

api_key = st.secrets["ANTHROPIC_API_KEY"]
client = anthropic.Anthropic(api_key=api_key)

language = st.selectbox("Language / భాష ఎంచుకోండి:", ["English", "Telugu", "Hindi", "Spanish", "Portuguese"])

user_input = st.text_input("Mee question అడగండి (navigation, seating, facilities, transport):")

if st.button("Ask Compass") and user_input:
    with st.spinner("Thinking..."):
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            system=f"You are Compass, a helpful multilingual assistant for FIFA World Cup 2026 stadium visitors. Answer in {language}. Help with navigation, seating, facilities, transportation, and general stadium information.",
            messages=[{"role": "user", "content": user_input}]
        )
        answer = response.content[0].text
        st.write(answer)
