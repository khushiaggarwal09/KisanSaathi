import os

import streamlit as st
from google import genai
from PIL import Image

st.set_page_config(page_title="KisanSaathi", page_icon="🌾")

st.title("🌾 KisanSaathi")
st.write("Fasal ke patte ki photo daalo, AI bimaari pehchaanega aur Hindi mein ilaaj batayega.")

# API key: Streamlit secrets ya environment variable se leta hai
api_key = os.environ.get("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", None)

if not api_key:
    st.error("GEMINI_API_KEY set nahi hai. README.md dekho.")
    st.stop()

client = genai.Client(api_key=api_key)

PROMPT = """Tum ek anubhavi krishi visheshagya ho. Is photo mein fasal ke patte/paudhe ko dekho.
Hindi mein, saral bhasha mein ye batao:
1. Fasal ka naam (agar pehchaan sako)
2. Bimaari ya samasya ka naam
3. Lakshan (kaise pehchaane)
4. Ilaaj: gharelu/jaivik upay pehle, phir zaroorat ho toh dawai
5. Bachaav ke tareeke
Agar photo saaf nahi hai ya paudha nahi dikh raha, toh saaf bolo aur dobara photo maango.
Jawab chhota aur kisan ke liye samajhne layak rakho."""

uploaded = st.file_uploader("Patte ki photo chuno", type=["jpg", "jpeg", "png"])

if uploaded:
    image = Image.open(uploaded)
    st.image(image, caption="Aapki photo", use_container_width=True)

    if st.button("Bimaari pehchaano"):
        with st.spinner("Jaanch ho rahi hai..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[image, PROMPT],
                )
                st.subheader("Natija")
                st.write(response.text)
            except Exception as e:
                st.error(f"Kuch gadbad hui: {e}")

st.caption("Ye AI salah hai. Zyada nuksaan ho toh apne najdeeki krishi kendra se sampark karein.")
