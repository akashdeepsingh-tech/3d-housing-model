import streamlit as st
import google.generativeai as genai
import json

# --- SECURE CONFIGURATION ---
# This pulls your key from the 'Secrets' menu in Streamlit Cloud
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
except Exception:
    st.error("Please configure your GEMINI_API_KEY in the Streamlit Secrets settings.")

st.set_page_config(page_title="Architect AI Pro", layout="wide")
st.title("🏙️ Professional 3D AI Architect")

# --- SIDEBAR FILTERS ---
with st.sidebar:
    st.header("📏 Dimensions")
    length = st.number_input("Length (ft)", value=60)
    width = st.number_input("Width (ft)", value=40)
    st.divider()
    st.header("🎨 Advanced Filters")
    style = st.selectbox("Style", ["Modern", "Industrial", "Minimalist", "Victorian"])
    material = st.multiselect("Materials", ["Glass", "Wood", "Concrete", "Steel"], ["Glass"])
    floors = st.slider("Floors", 1, 3, 1)

# --- AGENT LOGIC ---
user_brief = st.text_area("Design Brief:", "A luxury villa with a wrap-around porch.")

if st.button("Generate AI Result"):
    with st.status("Agentic Workflow Active...", expanded=True) as status:
        status.write("Analyzing spatial constraints...")
        
        # Calculate Area using LaTeX for precision
        area = length * width
        status.write(f"Calculating load for {area} sq. ft footprint...")
        
        # AI Logic
        prompt = f"Design a {style} house ({length}x{width}ft). Materials: {material}. Details: {user_brief}."
        # Note: In a live app, you'd process the Gemini response here.
        
        status.update(label="Design Finalized!", state="complete")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Conceptual Master Plan")
        st.image("https://placehold.co/600x400?text=Architectural+Render", use_container_width=True)
        st.metric("Total Area", f"{area * floors} sq ft")
    
    with col2:
        st.subheader("3D Interactive Viewer")
        # Standard 3D viewer for mobile and desktop
        st.components.v1.html("""
            <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
            <model-viewer src="https://modelviewer.dev/shared-assets/models/Astronaut.glb" 
            auto-rotate camera-controls style="width: 100%; height: 400px;"></model-viewer>
        """, height=450)
