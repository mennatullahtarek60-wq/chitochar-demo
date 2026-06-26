import streamlit as st
import pandas as pd

# 1. Page Configuration (Eco-Friendly Leaf Icon)
st.set_page_config(page_title="ChitoChar Smart Dashboard", page_icon="🌿", layout="wide")

# Custom CSS for Full Environmental & Sustainable Green Theme (التحضر للأخضر)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght=300;400;600;700&display=swap');
* { font-family: 'Inter', sans-serif; }

/* Main App Background & Sidebar Styling for Eco-Vibe */
.stApp {
    background-color: #F7FAF8; /* Soft organic off-white */
}
[data-testid="stSidebar"] {
    background-color: #EAF2EC !important; /* Beautiful pale sage green */
    border-right: 1px solid #CADECE;
}

/* Custom Text Logo Styling to perfectly match original brand identity */
.header-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    margin-bottom: 15px;
    margin-top: -10px;
}
.logo-text-main {
    font-size: 2.8rem;
    font-weight: 700;
    letter-spacing: -1px;
    margin: 5px 0 0 0;
    padding: 0;
    line-height: 1.1;
}
.logo-chito { color: #1B2A4A; } /* Deep Corporate Navy */
.logo-char { color: #2D6A4F; }  /* Deep Forest Green */
.logo-slogan {
    font-size: 1rem;
    color: #406343; /* Organic Olive Green */
    margin-top: 6px;
    font-weight: 500;
    letter-spacing: 0.5px;
}

/* Product Taglines inside expanders */
.product-tagline {
    font-size: 1.1rem;
    font-weight: bold;
    color: #1B5E20;
    margin-bottom: 15px;
    font-style: italic;
}

/* Sustainability Metric Boxes */
.metric-box {
    background-color: #E8F5E9; /* Light Mint Green */
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #A5D6A7;
    text-align: center;
    margin-bottom: 15px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}
.metric-title {
    font-size: 0.9rem;
    color: #2E7D32;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: bold;
}
.metric-value {
    font-size: 1.9rem;
    font-weight: bold;
    color: #1B5E20;
    margin-top: 5px;
}
.metric-sub {
    font-size: 0.85rem;
    color: #558B2F;
    margin-top: 5px;
}

/* Customizing Tabs to match the green theme */
div[data-testid="stMarkdownContainer"] p {
    color: #2C3E2B;
}
</style>
""", unsafe_allow_html=True)

# 2. Main Header & Custom Styled Logo Section
st.markdown('<div class="header-container">', unsafe_allow_html=True)

# Smooth loading for the logo (Checks for logo.png first, scales it cleanly)
try:
    st.image("logo.png", width=110)
except:
    pass

# HTML Text Logo to replicate image branding with zero vertical space waste
st.markdown("""
    <div class="logo-text-main"><span class="logo-chito">Chito</span><span class="logo-char">Char</span></div>
    <div class="logo-slogan">Preserving Food, Restoring the Planet 🍃</div>
</div>
""", unsafe_allow_html=True)

# Our Story Intro Section (Beautiful Green Border)
st.markdown("""
<div style="background-color: #E8F5E9; padding: 22px; border-left: 6px solid #2D6A4F; border-radius: 8px; margin-bottom: 25px;">
    <h3 style="margin-top:0; color: #1B5E20; font-weight:700;">🌱 Our Story</h3>
    <p style="font-size: 1.05rem; color: #2D3E2E; line-height: 1.6; margin-bottom:0;">
        Every year, millions of tons of fresh fruits and vegetables are lost before they ever reach a consumer's table, 
        while millions of tons of agricultural waste are burned or discarded. At ChitoChar, we asked ourselves how we could bridge this gap. 
        By upcycling biological and agricultural waste streams into active preservation solutions and pre-harvest updates, 
        we protect food ecosystems sustainably.
    </p>
</div>
""", unsafe_allow_html=True)

# The Circular Smart Ecosystem Banner (Right below the story - Visual Masterpiece!)
try:
    st.image("hero_banner.jpg", use_container_width=True)
except:
    try:
        st.image("hero_banner.png.jpg", use_container_width=True)
    except:
        pass

st.write(" ")

# --- DATA GENERATION ENGINE ---
crop_data = {
    "Tomatoes": {"rt_normal": 6, "rt_chito": 24},
    "Bananas": {"rt_normal": 5, "rt_chito": 19},
    "Strawberries": {"rt_normal": 3, "rt_chito": 10},
    "Berries": {"rt_normal": 4, "rt_chito": 12},
    "Grapes": {"rt_normal": 7, "rt_chito": 21}
}

# 3. Sidebar Layout (Eco-Styling Control Panel)
st.sidebar.markdown("<h2 style='color: #1B5E20; margin-top:0;'>⚙️ Control Panel</h2>", unsafe_allow_html=True)
crop = st.sidebar.selectbox("Select Crop Type:", list(crop_data.keys()))
temp = st.sidebar.slider("Storage/Transit Temperature (°C):", min_value=-5, max_value=40, value=5)
shipment_size = st.sidebar.number_input("Shipment Size (kg):", min_value=1, value=500)

st.sidebar.markdown("---")
st.sidebar.markdown("<h3 style='color: #1B5E20;'>🤖 Smart AI Assistant</h3>", unsafe_allow_html=True)

sachets_needed = int(shipment_size * 0.224)
st.sidebar.success(f"💡 **Recommendation:** Deploy **{sachets_needed} Sachets** for this shipment size.")

try:
    st.sidebar.image("preserve_product.jpg", caption="ChitoChar Smart Sachet Prototype", use_container_width=True)
except:
    pass

# 4. Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Predictive Analytics", 
    "♻️ Circular Economy Module", 
    "📦 Solutions Ecosystem", 
    "🇪🇬 National Impact Simulator"
])

# --- TAB 1: PREDICTIVE ANALYTICS ---
with tab1:
    st.header("Real-Time Analytics Dashboard")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-box" style="border: 2px solid #FFB74D; background-color: #FFF3E0;">
            <div class="metric-title" style="color: #E65100;">Spoilage Risk Score</div>
            <div class="metric-value" style="color: #E65100;">42%</div>
            <div class="metric-sub" style="color: #BF360C; font-weight: bold;">Medium Level</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-title">⏳ Expected Range (Shelf Life)</div>
            <div class="metric-value">{crop_data[crop]['rt_normal']} - {crop_data[crop]['rt_chito']} Days</div>
            <div class="metric-sub">Predicted Shelf Life: Up to {crop_data[crop]['rt_chito']} Days</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        days_saved = crop_data[crop]['rt_chito'] - crop_data[crop]['rt_normal']
        st.markdown(f"""
        <div class="metric-box" style="background-color: #E8F5E9; border: 1px solid #81C784;">
            <div class="metric-title">📦 Days Saved Counter</div>
            <div class="metric-value" style="color: #2E7D32;">+{days_saved} Days Saved</div>
            <div class="metric-sub">Ethylene Sensitivity: <b>High</b></div>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("📅 Shelf Life Visualization Breakdown")
    chart_data = pd.DataFrame({
        'Condition': ['Control (No Sachet)', 'With ChitoChar Sachet'],
        'Days Fresh': [crop_data[crop]['rt_normal'], crop_data[crop]['rt_chito']]
    })
    st.bar_chart(chart_data.set_index('Condition'))

# --- TAB 2: CIRCULAR ECONOMY MODULE ---
with tab2:
    st.header("♻️ Circular Impact & Waste Upcycling")
    st.write("""
    At ChitoChar, we believe waste should never be wasted.
    Agricultural and biological waste are transformed into innovative solutions that help extend shelf life, reduce food loss, improve agricultural productivity, and support a circular economy.
    """)
    st.success("📊 **The ChitoChar Loop:**\nAgricultural Waste ➔ Biochar Solutions ➔ Longer Shelf Life ➔ Reduced Food Loss ➔ Improved Soil Health")
    st.markdown("<p style='text-align: center; font-style: italic; font-weight: bold; color: #2E7D32; margin-top: 30px;'>Protect More Food. Waste Less. Grow Sustainably. 🌍</p>", unsafe_allow_html=True)

# --- TAB 3: SOLUTIONS ECOSYSTEM (FIXED TYPO & INDENTATION) ---
with tab3:
    st.header("ChitoChar Solutions Portfolio")
    st.caption("Transforming agricultural waste into smart solutions for food preservation and sustainable agriculture.")

    with st.expander("🌿 ChitoChar Preserve (Smart Biochar Sachets for Post-Harvest Protection)"):
        st.markdown('<div class="product-tagline">Protect Food Today. Enrich Soil Tomorrow.</div>', unsafe_allow_html=True)
        try:
            st.image("preserve_product.jpg", width=350, caption="ChitoChar Preserve Sachet")
        except:
            pass
        st.write("""
        ChitoChar Preserve is a biochar-based active preservation sachet designed for post-harvest protection. 
        The sachets are placed inside storage or packaging environments to absorb ripening gases and slow down spoilage.
        """)

    with st.expander("📦 ChitoChar Shield (Active Biochar Carton Liners - Future Product)"):
        st.markdown('<div class="product-tagline">Protect Every Journey. Preserve Every Harvest.</div>', unsafe_allow_html=True)
        try:
            st.image("shield_product.jpg", width=350, caption="ChitoChar Shield Box Liners")
        except:
            pass
        st.write("""
        ChitoChar Shield is an advanced active-packaging solution integrating biochar properties directly into container and box liners.
        """)

    with st.expander("🌱 ChitoChar Grow (Sustainable Soil Amendment for Pre-Harvest Improvement)"):
        st.markdown('<div class="product-tagline">Healthy Soil. Better Harvests.</div>', unsafe_allow_html=True)
        try:
            st.image("grow_product.jpg", width=350, caption="ChitoChar Grow Soil Solution")
        except:
            pass
        st.write("""
        ChitoChar Grow is a soil-enhancement solution developed from recycled bio-based materials and nutrient-rich agricultural residues.
        """)
        
    with st.expander("🤖 ChitoChar AI (Smart Shelf-Life & Loss Prediction Platform)"):
        st.markdown('<div class="product-tagline">Predict. Protect. Preserve.</div>', unsafe_allow_html=True)
        st.write("""
        ChitoChar AI helps farmers, distributors, and food businesses make better storage and logistics decisions.
        """)

# --- TAB 4: NATIONAL IMPACT SIMULATOR ---
with tab4:
    st.header("🇪🇬 National Impact Simulator")
    st.write("Calculate potential economic and environmental savings on a national scale using ChitoChar technologies.")
    tons_saved = st.slider("Scale of Implementation (Tons of Produce Handled Annually):", 1000, 50000, 10000)
    co2_offset = tons_saved * 1.5
    money_saved = tons_saved * 300
    
    c1, c2 = st.columns(2)
    c1.metric("💰 Economic Value Retained", f"${money_saved:,}")
    c2.metric("📉 CO2 Emissions Reduced", f"{co2_offset:,} Tons CO2e")
        
