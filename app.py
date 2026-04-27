import streamlit as st

# Executive Configuration
st.set_page_config(
    page_title="RAK Group | Strategic Management Suite",
    page_icon="⚖️",
    layout="wide"
)

# Custom Elegant Styling (Corrected Parameter)
st.markdown("""
    <style>
    .stApp { background-color: #FAFAFA; }
    [data-testid="stSidebar"] { background-color: #0A192F; color: white; }
    h1, h2, h3 { color: #0A192F; font-family: 'Helvetica Neue', sans-serif; font-weight: 700; }
    
    .stButton>button {
        width: 100%;
        border-radius: 4px;
        background-color: #0A192F;
        color: white;
        font-weight: 600;
        height: 3em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: NAVIGATION ---
with st.sidebar:
    st.markdown("## RAK GROUP")
    st.markdown("---")
    module = st.radio(
        "Select Operation Wing:",
        ["Executive Communication", "Visual Asset Development", "Strategic Planning", "Procurement & Logistics"]
    )
    st.markdown("---")
    st.caption("Authenticated Access: Executive Level")

# --- MAIN INTERFACE ---
st.title("RAK Group of Companies")
st.markdown(f"### {module}")
st.write("---")

if module == "Executive Communication":
    st.markdown("#### Strategic Copywriting & Narrative Synthesis")
    col1, col2 = st.columns([2, 1])
    with col1:
        campaign = st.text_input("Campaign Designation")
        objectives = st.text_area("Key Strategic Objectives")
    with col2:
        audience = st.selectbox("Target Stakeholder", ["Institutional Partners", "Industrial Clients", "Internal Management"])
    
    if st.button("Synthesize Executive Brief"):
        st.info("System Ready. Structure for executive narrative is initialized.")

elif module == "Visual Asset Development":
    st.markdown("#### High-End Creative Direction")
    st.selectbox("Asset Format", ["Corporate Profile", "Industrial Showcase", "Commercial Ad"])
    st.text_area("Creative Directives")
    if st.button("Initialize Visual Generation"):
        st.warning("Visual System on Standby. Interface confirmed.")

elif module == "Strategic Planning":
    st.markdown("#### Data-Driven Decision Support")
    st.text_input("Project Valuation / Target Market Cap")
    if st.button("Generate Risk Assessment"):
        st.write("Analyzing strategic vectors for RAK Group...")

elif module == "Procurement & Logistics":
    st.markdown("#### Global Supply Chain Coordination")
    c1, c2 = st.columns(2)
    with c1:
        st.text_input("Commodity Specification")
    with c2:
        st.text_input("Destination Point")
    if st.button("Draft Master Agreement"):
        st.success("Procurement framework initialized.")

# --- FOOTER ---
st.write("---")
st.caption("© 2026 RAK Group of Companies. Proprietary Strategic Information.")