import streamlit as st
from openai import OpenAI

# 1. Setup OpenAI Client gamit ang Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Premium Marketing Suite", page_icon="💎")

st.title("💎 Premium Marketing Suite")
st.subheader("Professional Captions & Elegant Visuals")

# User Inputs
business_name = st.text_input("Business Name", placeholder="e.g., Zionlife, RAK, or MC Petrofuel")
business_type = st.selectbox("Industry", ["Real Estate", "Fuel & Energy", "Food & Beverage", "Retail", "Services"])
details = st.text_area("Anong promo o details ang isasama?", placeholder="Describe the offer or the vibe you want...")

st.divider()

# Para makatipid, hiwalay ang logic ng Text at Image
col1, col2 = st.columns(2)

with col1:
    if st.button("Generate Elegant Caption ✍️"):
        if business_name:
            with st.spinner('Writing a lucrative copy...'):
                text_prompt = f"""
                Act as a high-end Digital Marketing Consultant in the Philippines.
                Create a sophisticated Taglish Facebook post for {business_name} in the {business_type} industry.
                Goal: {details}.
                
                Guidelines:
                - Use an elegant, professional, and trustworthy tone.
                - Use natural 'Taglish' (not forced).
                - Highlight a 'lucrative' opportunity or benefit.
                - Avoid generic AI phrases like 'In a world where...' or 'Unlock your potential'.
                - Include 3 minimalist emojis.
                - Structure: Catchy Header, 3 Bullet points of benefits, and a Clear CTA.
                """
                
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": text_prompt}]
                )
                st.success("Caption Created!")
                st.write(response.choices[0].message.content)
        else:
            st.error("Input business name first.")

with col2:
    if st.button("Generate Professional Image 📸"):
        if business_name:
            with st.spinner('Generating high-end visual...'):
                # IMAGE PROMPT: Focused on realism and professional photography
                image_prompt = f"""
                Professional commercial photography of {business_type} theme related to {details}. 
                Style: Minimalist, elegant, cinematic lighting, shot on 35mm lens, f/1.8, natural soft light. 
                Vibe: Clean, premium, high-end lifestyle. 
                Strictly NO text in the image. NOT digital art, NOT 3D render. 
                Must look like a real photo for a premium magazine advertisement.
                """
                
                img_response = client.images.generate(
                    model="dall-e-3",
                    prompt=image_prompt,
                    size="1024x1024",
                    quality="hd",
                    n=1,
                )
                st.image(img_response.data[0].url, caption="Premium Generated Visual")
        else:
            st.error("Input business name first.")