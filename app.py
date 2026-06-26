import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="ChitoChar Platform", page_icon="🌱", layout="wide")

# Inject Custom Elegant Fonts and Styling (Emerald Sustainable Theme)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght=300;400;600;700&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    
    /* Center Logo styling */
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 10px;
    }
    
    /* Elegant Story Box */
    .story-box {
        background-color: #f4f9f4;
        border-left: 5px solid #2d6a4f;
        border-radius: 8px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(45, 106, 79, 0.05);
    }
    .story-title { font-size: 22px; font-weight: 700; color: #1b4332; margin-bottom: 10px; }
    .story-text { font-size: 15px; color: #2d6a4f; line-height: 1.6; font-style: italic; }
    
    /* Metric Card Styling */
    .metric-card {
        background: #ffffff;
        border: 1px solid #d8f3dc;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(45, 106, 79, 0.04);
        height: 100%;
    }
    .metric-lbl { font-size: 13px; color: #52b788; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
    
    /* Risk Badge Styling - Clean & Solid */
    .risk-badge {
        padding: 10px 20px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 18px;
        display: inline-block;
        margin-top: 15px;
    }
    .risk-low { background-color: #d8f3dc; color: #1b4332; border: 1px solid #b7e4c7; }
    .risk-med { background-color: #fefae0; color: #b5842e; border: 1px solid #e9d8a6; }
    .risk-high { background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
    
    /* Product Tagline Styling */
    .product-tagline {
        font-size: 16px;
        font-weight: 600;
        color: #2d6a4f;
        font-style: italic;
        margin-bottom: 15px;
        border-bottom: 1px dashed #d8f3dc;
        padding-bottom: 5px;
    }
    
    /* Custom Chart Styling */
    .chart-container { display: flex; justify-content: space-around; align-items: flex-end; height: 200px; padding: 20px; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; margin-top: 15px; }
    .chart-bar-wrapper { display: flex; flex-direction: column; align-items: center; width: 40%; }
    .chart-bar { width: 100%; border-radius: 6px 6px 0 0; text-align: center; color: white; font-weight: bold; padding-top: 10px; font-size: 15px; }
    .bar-normal { background: #e63946; box-shadow: 0 4px 10px rgba(230, 57, 70, 0.2); }
    .bar-chito { background: #2d6a4f; box-shadow: 0 4px 10px rgba(45, 106, 79, 0.2); }
    .chart-label { margin-top: 10px; font-weight: 600; font-size: 14px; color: #333; }
    </style>
""", unsafe_allow_html=True)

# 1. Main Premium Logo Display (Centered without redundant texts)
st.image("logo.png", use_container_width=True)

# 2. Hero Image Banner Display
st.image("hero_banner.jpg", use_container_width=True)

# 3. Our Story Section (Placed beautifully under the Banner)
st.markdown("""
<div class="story-box">
    <div class="story-title">🌱 Our Story</div>
    <div class="story-text">
        Every year, millions of tons of fresh fruits and vegetables are lost before they ever reach a consumer's table, while millions of tons of agricultural waste are burned or discarded.<br><br>
        At ChitoChar, we asked ourselves one simple question:<br>
        <b>What if the waste causing one problem could become the solution to another?</b><br><br>
        That question became our mission. We're turning agricultural waste into innovative solutions that help preserve food, reduce losses, and build a more sustainable future.<br><br>
        <i>Because every harvest deserves to reach a table—not a landfill.</i>
    </div>
</div>
""", unsafe_allow_html=True)

st.write(" ")

# --- DATA GENERATION ENGINE ---
crop_data = {
    "Tomato": {
        "sensitivity": "Medium", "suitable": "✅ Yes",
        "rt_normal": 6, "rt_chito": 10, "rt_risk": 65,
        "cold_normal": 18, "cold_chito": 24, "cold_risk": 20,
        "optimal_temp": 5, "reduction": 25, "saved_kg_per_ton": 147,
        "price_per_kg": 20, "sachets_per_ton": 50, "co2_factor": 0.6
    },
    "Banana": {
        "sensitivity": "High", "suitable": "✅ Yes",
        "rt_normal": 5, "rt_chito": 10, "rt_risk": 85,
        "cold_normal": 18, "cold_chito": 24, "cold_risk": 30,
        "optimal_temp": 13, "reduction": 65, "saved_kg_per_ton": 143,
        "price_per_kg": 15, "sachets_per_ton": 75, "co2_factor": 0.8
    },
    "Guava": {
        "sensitivity": "High", "suitable": "✅ Yes",
        "rt_normal": 3, "rt_chito": 9, "rt_risk": 90,
        "cold_normal": 8, "cold_chito": 18, "cold_risk": 35,
        "optimal_temp": 8, "reduction": 70, "saved_kg_per_ton": 210,
        "price_per_kg": 18, "sachets_per_ton": 60, "co2_factor": 0.5
    },
    "Avocado": {
        "sensitivity": "High", "suitable": "✅ Yes",
        "rt_normal": 5, "rt_chito": 15, "rt_risk": 75,
        "cold_normal": 7, "cold_chito": 18, "cold_risk": 25,
        "optimal_temp": 7, "reduction": 60, "saved_kg_per_ton": 120,
        "price_per_kg": 75, "sachets_per_ton": 60, "co2_factor": 2.5
    },
    "Blueberry": {
        "sensitivity": "Medium", "suitable": "✅ Yes",
        "rt_normal": 2, "rt_chito": 5, "rt_risk": 95,
        "cold_normal": 7, "cold_chito": 21, "cold_risk": 15,
        "optimal_temp": 4, "reduction": 75, "saved_kg_per_ton": 187,
        "price_per_kg": 200, "sachets_per_ton": 75, "co2_factor": 1.2
    }
}

# Sidebar Input Controls
st.sidebar.header("📥 Input Parameters")
selected_crop = st.sidebar.selectbox("Select Crop Type:", list(crop_data.keys()))
shipment_volume = st.sidebar.number_input("Shipment Volume (Tons):", min_value=0.1, value=1.0, step=0.5)

# Dynamic Temperature Controls
temp_min = 2 if selected_crop == "Blueberry" else 4
storage_temp = st.sidebar.slider("Storage/Transit Temperature (°C):", min_value=temp_min, max_value=38, value=25)

# Sidebar Sachet Image Display (Clean text name without prototype)
st.sidebar.markdown("---")
st.sidebar.image("preserve_product.jpg", caption="ChitoChar Smart Sachet", use_container_width=True)

# Smart AI Recommendations Assistant Block
st.sidebar.markdown("---")
st.sidebar.subheader("🤖 Smart AI Assistant")
c_meta = crop_data[selected_crop]
sachet_needed = int(c_meta["sachets_per_ton"] * shipment_volume)

# Scientific Logic for Non-Climacteric Blueberry
if selected_crop == "Blueberry":
    st.sidebar.warning("💡 **Recommendation:** Preferred: **ChitoChar Shield (Antimicrobial Carton Liners)** for this non-climacteric shipment.")
else:
    st.sidebar.warning(f"💡 **Recommendation:** Deploy **{sachet_needed} Sachets** for this shipment size.")

# Dynamic Warnings based on Crop Physiology
if selected_crop == "Banana" and storage_temp < 10:
    st.sidebar.error("⚠️ **Critical Warning:** Temperatures below 10°C trigger **Chilling Injury** in bananas. Maintain optimal transit at 13°C.")
elif storage_temp > 26:
    st.sidebar.error("⚠️ **High Spoilage Alert:** Elevated thermal environment accelerates sudden ethylene release surges.")
else:
    st.sidebar.success(f"💎 **Storage Tip:** Maintain target temperature close to {c_meta['optimal_temp']}°C for maximum lifespan expansion.")

if selected_crop in ["Tomato", "Banana"]:
    st.sidebar.info("🚫 **Compatibility Hint:** Avoid cross-storing Tomatoes and Bananas directly next to each other to block compound ripening spikes.")

# Calculations Setup
is_cold = storage_temp <= 12
shelf_normal = c_meta["cold_normal"] if is_cold else c_meta["rt_normal"]
shelf_chito = c_meta["cold_chito"] if is_cold else c_meta["rt_chito"]
base_risk = c_meta["cold_risk"] if is_cold else c_meta["rt_risk"]

temp_deviation = abs(storage_temp - c_meta["optimal_temp"])
calculated_risk = min(int(base_risk + (temp_deviation * 1.5)), 99)

if calculated_risk < 40:
    risk_class, risk_label = "risk-low", "Low"
elif calculated_risk < 75:
    risk_class, risk_label = "risk-med", "Medium"
else:
    risk_class, risk_label = "risk-high", "High"

days_saved = shelf_chito - shelf_normal


# REORGANIZED TABS LAYOUT
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌍 Why ChitoChar?",
    "📊 Predictive Analytics", 
    "♻️ Circular Economy Module", 
    "🇪🇬 National Impact Simulator", 
    "📦 Solutions Ecosystem"
])

# --- TAB 1: WHY CHITOCHAR? ---
with tab1:
    st.subheader("🌍 Why ChitoChar?")
    
    st.markdown("""
    ### 🌱 Turning Waste into Value
    We transform locally available agricultural residues into high-value preservation technologies, creating a true circular economy where waste becomes a resource.
    
    ### 💰 Affordable by Design
    Unlike many imported preservation solutions, ChitoChar is designed to be cost-effective from day one—making advanced food preservation accessible to farmers, traders, and distributors of all sizes.
    
    ### 🇪🇬 100% Locally Developed
    From raw materials to innovation, ChitoChar is proudly developed in Egypt using locally sourced agricultural waste, reducing dependence on imported preservation technologies.
    
    ### 🍅 Reduce Food Loss
    Our technologies help slow post-harvest deterioration, extend shelf life, and protect produce throughout the supply chain—reducing waste while increasing profitability.
    
    ### 🌍 Beyond Sustainability
    Our impact doesn't end after preserving food. After use, our biochar-based materials can be returned to the soil, helping improve soil health and closing the loop of a truly circular agricultural system.
    
    ### 🤖 Smart Agriculture
    ChitoChar combines sustainable materials with AI-powered decision support, helping users make smarter storage and post-harvest management decisions.
    
    ### ♻️ Built for the Future
    Our vision extends beyond a single product. We're building an integrated ecosystem of pre-harvest solutions, post-harvest preservation, active packaging, and digital intelligence to reshape how food is protected from farm to table.
    """)

# --- TAB 2: PREDICTIVE ANALYTICS ---
with tab2:
    st.subheader("Real-Time Analytics Dashboard")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        # Clean Risk Card showing ONLY text level levels
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-lbl">Spoilage Risk Score</div>
            <div style="margin-top: 15px;">
                <span class="risk-badge {risk_class}">{risk_label} Level</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-lbl">⏳ Expected Range (Shelf Life)</div>
            <div style="font-size: 28px; font-weight: 700; color: #2d6a4f; margin: 10px 0;">{shelf_normal} - {shelf_chito} Days</div>
            <div style="font-size: 12px; color: #74c69d;"><b>Predicted Shelf Life:</b> Up to {shelf_chito} Days</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-lbl">Days Saved Counter</div>
            <div style="font-size: 28px; font-weight: 700; color: #2d6a4f; margin: 10px 0;">+{days_saved} Days Saved</div>
            <div style="font-size: 12px; color: #74c69d;">Ethylene Sensitivity: <b>{c_meta['sensitivity']}</b></div>
        </div>
        """, unsafe_allow_html=True)
        
    st.write(" ")
    
    # Custom HTML/CSS Bar Chart Layout
    st.subheader("📅 Shelf Life Visualization Breakdown")
    normal_height = int((shelf_normal / 24) * 150)
    chito_height = int((shelf_chito / 24) * 150)
    st.markdown(f"""
    <div class="chart-container">
        <div class="chart-bar-wrapper">
            <div class="chart-bar bar-normal" style="height: {normal_height}px;">{shelf_normal} Days</div>
            <div class="chart-label">Without ChitoChar</div>
        </div>
        <div class="chart-bar-wrapper">
            <div class="chart-bar bar-chito" style="height: {chito_height}px;">{shelf_chito} Days</div>
            <div class="chart-label">With ChitoChar Active</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # ChitoChar ROI Calculator Block (Updated to 3 EGP per sachet)
    st.subheader("💰 ChitoChar ROI Calculator")
    saved_kg = c_meta["saved_kg_per_ton"] * shipment_volume
    gross_savings = saved_kg * c_meta["price_per_kg"]
    total_sachet_cost = sachet_needed * 3  
    net_profit = gross_savings - total_sachet_cost
    
    f_col1, f_col2, f_col3, f_col4 = st.columns(4)
    f_col1.metric("Food Loss Prevented", f"{saved_kg:,.1f} kg", f"Reduction: {c_meta['reduction']}%")
    f_col2.metric("Gross Revenue Saved", f"EGP {gross_savings:,.0f}")
    f_col3.metric("Total Sachet Cost", f"EGP {total_sachet_cost:,.0f}", "At EGP 3.00 / unit")
    f_col4.metric("Net Financial Profit", f"EGP {net_profit:,.0f}", "Direct Value Generated", delta_color="inverse")
    
    st.write("---")
    
    # Climate & Carbon Metrics
    st.subheader("🌍 Atmospheric & Climate Impact Metrics")
    co2_avoided = c_meta["co2_factor"] * saved_kg
    trees_equivalent = round(co2_avoided / 22)
    
    st.error(f"📉 **Methane Emission Mitigation:** Preventing the rotting cycle of **{saved_kg:,.1f} kg** of active organic mass cuts off dangerous anaerobic landfill breakdown, halting **Methane (CH₄)** release—a gas documented as **25 times more destructive** to global atmospheric warming than standard CO₂ structures.")
    st.success(f"🌱 **Carbon Offset Equivalency:** This atmospheric salvage saves roughly **{co2_avoided:,.1f} kg CO₂-eq**, directly mirroring the impact of **growing {trees_equivalent} mature trees** over a full 12-month calendar year.")

# --- TAB 3: CIRCULAR ECONOMY MODULE ---
with tab3:
    st.subheader("The Circular Economy Cycle")
    st.info("💡 **Sustainable Ethylene Scavenger Made from Agricultural Waste**")
    
    st.markdown("""
    **Closed-Loop Resource Matrix:**
    Agricultural Waste Streams ➡️ Biochar Synthesis ➡️ Active Packaging Protection ➡️ Food Loss Prevention ➡️ Subsurface Soil Re-Incorporation
    """)
    
    biochar_returned = 1.5 * shipment_volume
    pure_carbon_returned = 0.8 * biochar_returned
    
    c_col1, c_col2 = st.columns(2)
    with c_col1:
        st.metric("Biochar Returned to Soil Bed", f"{biochar_returned:,.1f} kg")
        st.write("**🔄 Regenerative Cycle Action:** After finishing its active post-harvest protective function, the sachet matrix is designed to be opened. Instead of joining typical commercial solid waste streams, the spent carbon core is applied directly into crop beds.")
    with c_col2:
        st.metric("Pure Organic Carbon Sequestered", f"{pure_carbon_returned:,.1f} kg")
        st.write("**🌱 Subsurface Quality Enhancements:** The applied carbon structures function as permanent soil sponges—retaining moisture fields, locking essential mineral nutrients, stopping dangerous fertilizer chemical leaching, and elevating natural yield indexes over long horizons.")
        
    st.write("---")
    st.subheader("🌱 ChitoChar Grow: Pre-Harvest Innovation Matrix")
    st.markdown("""
    Our integrated developmental roadmap introduces specialized **Eggshell Ash** frameworks into pre-harvest operations:
    * **Calcium-Rich Structural Matrix:** Actively reinforces cellular wall bonds while fruits are growing on the vine.
    * **Pre-Harvest Defensive Fortification:** Preserves early cellular water content, lowers initial environmental crop stress factors, and locks in baseline resistance before the produce ever reaches the supply chain.
    """)

# --- TAB 4: NATIONAL IMPACT SIMULATOR ---
with tab3:
    st.subheader("🇪🇬 National Impact Simulator (Egypt Scale)")
    st.write("Systemic performance metrics evaluated if a baseline **10%** of Egypt's active tomato agricultural ecosystems integrate ChitoChar technology:")
    
    st.write(" ")
    nat_col1, nat_col2, nat_col3, nat_col4 = st.columns(4)
    nat_col1.metric("🧑‍🌾 Farmers Using ChitoChar", "10%")
    nat_col2.metric("🍅 Food Saved Anually", "46,500 Tons")
    nat_col3.metric("💰 Revenue Protected", "EGP 558,000,000")
    nat_col4.metric("🌍 Systemic CO₂ Avoided", "20,000 Tons")
    
    st.write(" ")
    st.success("♻️ **Agricultural Waste Upcycled:** Thousands of tonnes of agricultural residues transformed into value-added biochar instead of being discarded or openly burned; growing every single season.")
    st.markdown("<p style='font-size:10px; color:#aaa; font-style: italic;'>Simulation based on publicly available national production statistics and published post-harvest loss estimates. Results are indicative and intended for impact visualization only.</p>", unsafe_allow_html=True)

# --- TAB 5: SOLUTIONS ECOSYSTEM (With Clean Headers, Taglines and Product Images) ---
with tab5:
    st.subheader("ChitoChar Solutions Portfolio")
    st.markdown("*Transforming agricultural waste into smart solutions for food preservation and sustainable agriculture.*")
    
    with st.expander("🌿 ChitoChar Preserve"):
        st.markdown('<div class="product-tagline">Protect Food Today. Enrich Soil Tomorrow.</div>', unsafe_allow_html=True)
        st.image("preserve_product.jpg", width=350, caption="ChitoChar Preserve Sachet Solution")
        st.write("""
        ChitoChar Preserve is a biochar-based active packaging solution designed to help reduce post-harvest losses in fruits and vegetables.
        The sachets are placed inside storage boxes, packaging, or transportation containers, where they help manage ripening-related gases that accelerate spoilage. This helps maintain freshness for longer periods, reduce food losses, and improve produce quality during storage and transportation.
        \n**Key Benefits:**
        * ✔ Helps extend produce freshness and shelf life
        * ✔ Reduces post-harvest losses
        * ✔ No direct food contact
        * ✔ Low-cost and easy to use
        * ✔ Made from agricultural waste
        * ✔ Suitable for tomatoes, bananas, mangoes, and other climacteric crops
        \n*♻️ After use, the biochar content can be safely incorporated into soil, helping improve soil quality and supporting a circular agricultural system.*
        """)
        
    with st.expander("📦 ChitoChar Shield (Future Product)"):
        st.markdown('<div class="product-tagline">Protect Every Journey. Preserve Every Harvest.</div>', unsafe_allow_html=True)
        st.image("shield_product.jpg", width=350, caption="ChitoChar Shield Design Concept")
        st.write("""
        ChitoChar Shield is an advanced active-packaging solution currently under development, designed for highly perishable fruits and vegetables that require enhanced protection during storage and transportation.
        The carton liners are manufactured from biochar and chitosan-based materials, combining gas-management capabilities with natural antimicrobial properties. They are designed to help slow quality deterioration, reduce spoilage, and maintain freshness throughout the supply chain.
        \n**Key Benefits:**
        * ✔ Helps extend shelf life of highly perishable produce
        * ✔ Reduces spoilage during transportation and storage
        * ✔ Natural antimicrobial properties
        * ✔ Helps manage ripening-related gases
        * ✔ Suitable for export packaging and sensitive fruits
        * ✔ Sustainable alternative to conventional packaging materials
        \n*Target Applications: berries, grapes, strawberries, fresh-cut produce, and other highly perishable fruits and vegetables.*
        """)
        
    with st.expander("🌱 ChitoChar Grow"):
        st.markdown('<div class="product-tagl
