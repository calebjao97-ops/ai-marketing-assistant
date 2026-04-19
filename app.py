import streamlit as st
from openai import OpenAI

# ILAGAY MO DITO YUNG API KEY MO
client = OpenAI(api_key="PASTE_YOUR_API_KEY_HERE")

st.set_page_config(page_title="AI Marketing Pro", page_icon="🎨")

st.title("Caleb AI Marketing & Image Generator")
st.subheader("Caption + Visuals sa isang pindutan!")

business = st.text_input("Ano ang business mo?")
details = st.text_area("Anong promo o vibes ang gusto mo? (e.g. Buy 1 Take 1, Aesthetic, Modern)")

if st.button("Generate Marketing Package 🚀"):
    if business:
        with st.spinner('Generating your viral content and image...'):
            # 1. GENERATE CAPTION
            text_prompt = f"Create a viral Taglish Facebook post for a {business} business. Promo details: {details}. Use emojis and a friendly tone."
            text_response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": text_prompt}]
            )
            caption = text_response.choices[0].message.content
            
            # 2. GENERATE IMAGE
            image_prompt = f"A high-quality, professional commercial photography of {business} product, {details} theme, cinematic lighting, 4k, marketing style."
            img_response = client.images.generate(
                model="dall-e-3",
                prompt=image_prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            image_url = img_response.data[0].url

            # DISPLAY RESULTS
            st.divider()
            st.image(image_url, caption=f"AI Generated Image for {business}")
            st.success("Heto na ang Caption mo:")
            st.write(caption)
    else:
        st.error("Lagay mo muna yung business details!")
