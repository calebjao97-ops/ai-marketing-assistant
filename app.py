import streamlit as st

# Configuration for a high-end dashboard feel
st.set_page_config(
    page_title="RAK Group | Strategic Management Suite",
    page_icon="⚖️",
    layout="wide"
)

# Custom Elegant Styling
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #FAFAFA;
    }
    
    /* Executive Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0A192F;
        color: white;
    }
    
    /* Professional Headers */
    h1, h2, h3 {
        color: #0A192F;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    /* Premium Button Styling */
    .stButton>button {
        width: 100%;
        border: none;
        border-radius: 4px;
        padding: 0.6rem;
        background-color: #0A192F;
        color: #FFFFFF;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #112240;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        color: #64FFDA;
    }
    
    /* Input Box refinement */
    .stTextInput>div>div>input {
        border-radius: 4px;
    }
    </style>
    """, unsafe_allow_set_body_with_html=True)

# --- SIDEBAR: EXECUTIVE NAVIGATION ---
with st.sidebar:
    st.markdown("## RAK GROUP")
    st.markdown("---")
    st.markdown("### Strategic Pillars")
    module = st.radio(
        "Select Operation Wing:",
        ["Executive Communication", "Visual Asset Development", "Strategic Planning", "Procurement & Logistics"]
    )
    st.markdown("---")
    st.caption("Authenticated Access: Executive Level")

# --- MAIN INTERFACE: RAK GROUP DASHBOARD ---
st.title("RAK Group of Companies")
st.markdown(f"### {module}")
st.write("---")

if module == "Executive Communication":
    st.markdown("#### Strategic Copywriting & Narrative Synthesis")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        campaign_theme = st.text_input("Campaign Designation", placeholder="e.g., Annual Logistics Overview")
        key_objectives = st.text_area("Key Strategic Objectives", placeholder="Define the primary value proposition...")
    
    with col2:
        tone_profile = st.select_slider(
            "Communication Tone",
            options=["Conservative", "Professional", "Visionary", "Aggressive"]
        )
        audience = st.selectbox("Target Stakeholder", ["Institutional Partners", "High-Net-Worth Individuals", "Industrial Clients"])

    if st.button("Synthesize Executive Brief"):
        st.info("Structure locked. Awaiting AI Brain Integration.")
        st.markdown(f"""
        **DRAFT PREVIEW:**
        
        **RAK Group Strategic Communication** *Subject: {campaign_theme}*
        
        Our commitment to excellence within the {audience} sector remains paramount. 
        As we leverage our core competencies in {key_objectives}, RAK Group 
        continues to set the benchmark for operational efficiency and 
        market leadership...
        """)

elif module == "Visual Asset Development":
    st.markdown("#### High-End Creative Direction")
    col_a, col_b = st.columns(2)
    
    with col_a:
        asset_type = st.selectbox("Asset Format", ["Corporate Profile Image", "Industrial Showcase", "Commercial Ad Background"])
        art_direction = st.text_area("Creative Directives", placeholder="Minimalist, cinematic lighting, professional focus...")
    
    with col_b:
        quality_preset = st.radio("Resolution Quality", ["Standard Definition", "High-Definition Portfolio", "Raw Photographic Print"])

    if st.button("Initialize Visual Generation"):
        st.warning("Visual System on Standby. Credits preserved.")
        st.image("https://via.placeholder.com/1200x500.png?text=RAK+Group+Visual+Architecture", use_container_width=True)

elif module == "Strategic Planning":
    st.markdown("#### Data-Driven Decision Support")
    st.info("This module is designed for synthesizing market data into actionable intelligence.")
    st.text_input("Project Valuation / Target Market Cap")
    st.multiselect("Risk Factors", ["Market Volatility", "Logistical Constraint", "Regulatory Change"])
    
    if st.button("Generate Risk Assessment"):
        st.write("Generating strategic overview for RAK Group decision-makers...")

elif module == "Procurement & Logistics":
    st.markdown("#### Global Supply Chain Coordination")
    col_x, col_y = st.columns(2)
    with col_x:
        commodity_spec = st.text_input("Material/Service Specification")
        volume_req = st.text_input("Volume / Capacity Requirements")
    with col_y:
        origin_point = st.text_input("Logistical Origin")
        destination_point = st.text_input("Final Destination")

    if st.button("Draft Master Agreement"):
        st.success("Drafting formal procurement terms...")

# --- EXECUTIVE FOOTER ---
st.write("---")
footer_col1, footer_col2 = st.columns([4, 1])
with footer_col1:
    st.caption("© 2026 RAK Group of Companies. All Rights Reserved. Proprietary Strategic Information.")
with footer_col2:
    st.caption("System Status: **Live**")