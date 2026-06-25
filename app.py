import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="ChitoChar AI Platform", page_icon="🌱", layout="wide")

# Inject Custom Elegant Fonts and Styling (Emerald Sustainable Theme)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght=300;400;600;700&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    
    .main-title { font-size: 44px; font-weight: 700; color: #1b4332; text-align: center; margin-top: -10px; }
    .tagline { font-size: 18px; font-weight: 300; color: #40916c; text-align: center; margin-bottom: 20px; font-style: italic; }
    
    /* Metric Card Styling */
    .metric-card {
        background: #f4f9f4;
        border: 1px solid #d8f3dc;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        height: 100%;
    }
    .metric-val { font-size: 30px; font-weight: 700; color: #2d6a4f; margin: 5px 0; }
    .metric-lbl { font-size: 13px; color: #52b788; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
    .metric-desc { font-size: 12px; color: #74c69d; }
    
    /* Risk Badge Styling */
    .risk-badge {
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 13px;
        display: inline-block;
        margin-top: 5px;
    }
    .risk-low { background-color: #d8f3dc; color: #1b4332; }
    .risk-med { background-color: #fefae0; color: #b5842e; }
    .risk-high { background-color: #f8d7da; color: #721c24; }
    
    /* Bulletproof Custom Chart Styling */
    .chart-container { display: flex; justify-content: space-around; align-items: flex-end; height: 200px; padding: 20px; background: #fafafa; border-radius: 12px; border: 1px solid #eee; margin-top: 15px; }
    .chart-bar-wrapper { display: flex; flex-direction: column; align-items: center; width: 40%; }
    .chart-bar { width: 100%; border-radius: 6px 6px 0 0; text-align: center; color: white; font-weight: bold; padding-top: 10px; font-size: 15px; }
    .bar-normal { background: #e63946; box-shadow: 0 4px 10px rgba(230, 57, 70, 0.2); }
    .bar-chito { background: #2d6a4f; box-shadow: 0 4px 10px rgba(45, 106, 79, 0.2); }
    .chart-label { margin-top: 10px; font-weight: 600; font-size: 14px; color: #333; }
    </style>
""", unsafe_allow_html=True)

# Top Header Area
st.markdown('<div class="main-title">ChitoChar AI</div>', unsafe_allow_html=True)
st.markdown('<div class="tagline">Preserving the food, Restoring the planet</div>', unsafe_allow_html=True)

# Simulation Mode Toggle & Legal Disclaimer
st.write("---")
col_sim_left, col_sim_right = st.columns([1, 4])
with col_sim_left:
    sim_mode = st.toggle("Simulation Mode", value=True)
with col_sim_right:
    if sim_mode:
        st.caption("⚠️ *Preliminary predictions based on published research regarding biochar-based ethylene scavenging technologies. Values will be continuously updated as experimental validation data become available.*")
st.write("---")

# Display Hero Image Banner
st.image("hero_banner.png.jpg", use_container_width=True)
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

# Sidebar Sachet Image Display
st.sidebar.markdown("---")
st.sidebar.image("sachet_product.png.jpg", caption="ChitoChar Smart Sachet Prototype", use_container_width=True)

# Smart AI Recommendations Assistant Block
st.sidebar.markdown("---")
st.sidebar.subheader("🤖 Smart AI Assistant")
c_meta = crop_data[selected_crop]
sachet_needed = int(c_meta["sachets_per_ton"] * shipment_volume)

st.sidebar.warning(f"💡 **Recommendation:** Deploy **{sachet_needed} Sachets** for this shipment size.")

# Dynamic Warnings
if selected_crop == "Banana" and storage_temp < 10:
    st.sidebar.error("⚠️ **Critical Warning:** Temperatures below 10°C trigger **Chilling Injury** in bananas. Maintain optimal transit at 13°C.")
elif storage_temp > 26:
    st.sidebar.error("⚠️ **High Spoilage Alert:** Elevated thermal environment accelerates sudden ethylene release surges.")
else:
    st.sidebar.success(f"💎 **Storage Tip:** Maintain target temperature close to {c_meta['optimal_temp']}°C for maximum lifespan expansion.")

if selected_crop in ["Tomato", "Banana"]:
    st.sidebar.info("🚫 **Compatibility Hint:** Avoid cross-storing Tomatoes and Bananas directly next to each other to block compound ripening spikes.")

# Dynamic Calculations Setup
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

# PLATFORM TABS LAYOUT
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Predictive Analytics", 
    "♻️ Circular Economy Module", 
    "🇪🇬 National Impact Simulator", 
    "📦 Solutions Ecosystem"
])

# --- TAB 1: PREDICTIVE ANALYTICS ---
with tab1:
    st.subheader("Real-Time Analytics Dashboard")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-lbl">Spoilage Risk Score</div>
            <div class="metric-val">{calculated_risk}%</div>
            <span class="risk-badge {risk_class}">{risk_label} Level</span>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-lbl">⏳ Expected Range (Shelf Life)</div>
            <div class="metric-val">{shelf_normal} - {shelf_chito} Days</div>
            <div class="metric-desc"><b>Predicted Shelf Life:</b> Up to {shelf_chito} Days</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-lbl">Days Saved Counter</div>
            <div class="metric-val">+{days_saved} Days Saved</div>
            <div class="metric-desc">Ethylene Sensitivity: <b>{c_meta['sensitivity']}</b></div>
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
    
    # ChitoChar ROI Calculator Block
    st.subheader("💰 ChitoChar ROI Calculator")
    saved_kg = c_meta["saved_kg_per_ton"] * shipment_volume
    gross_savings = saved_kg * c_meta["price_per_kg"]
    total_sachet_cost = sachet_needed * 2  
    net_profit = gross_savings - total_sachet_cost
    
    f_col1, f_col2, f_col3, f_col4 = st.columns(4)
    f_col1.metric("Food Loss Prevented", f"{saved_kg:,.1f} kg", f"Reduction: {c_meta['reduction']}%")
    f_col2.metric("Gross Revenue Saved", f"EGP {gross_savings:,.0f}")
    f_col3.metric("Total Sachet Cost", f"EGP {total_sachet_cost:,.0f}", "At EGP 2.00 / unit")
    f_col4.metric("Net Financial Profit", f"EGP {net_profit:,.0f}", "Direct Value Generated", delta_color="inverse")
    
    st.write("---")
    
    # Climate & Carbon Metrics
    st.subheader("🌍 Atmospheric & Climate Impact Metrics")
    co2_avoided = c_meta["co2_factor"] * saved_kg
    trees_equivalent = round(co2_avoided / 22)
    
    st.error(f"📉 **Methane Emission Mitigation:** Preventing the rotting cycle of **{saved_kg:,.1f} kg** of active organic mass cuts off dangerous anaerobic landfill breakdown, halting **Methane (CH₄)** release—a gas documented as **25 times more destructive** to global atmospheric warming than standard CO₂ structures.")
    st.success(f"🌱 **Carbon Offset Equivalency:** This atmospheric salvage saves roughly **{co2_avoided:,.1f} kg CO₂-eq**, directly mirroring the impact of **growing {trees_equivalent} mature trees** over a full 12-month calendar year.")

# --- TAB 2: CIRCULAR ECONOMY MODULE ---
with tab2:
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

# --- TAB 3: NATIONAL IMPACT SIMULATOR ---
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

# --- TAB 4: SOLUTIONS ECOSYSTEM ---
with tab4:
    st.subheader("ChitoChar Solutions Portfolio")
    st.markdown("*Transforming agricultural waste into smart solutions for food preservation and sustainable agriculture.*")
    
    with st.expander("🌿 ChitoChar Preserve (Smart Biochar Sachets for Post-Harvest Protection)"):
        st.write("ChitoChar Preserve is a biochar-based active packaging solution designed to help reduce post-harvest losses in fruits and vegetables. The sachets are placed inside storage boxes, packaging, or transportation containers, where they help manage ripening-related gases that accelerate spoilage. This helps maintain freshness for longer periods, reduce food losses, and improve produce quality during storage and transportation.")
        st.write("**Key Benefits:**\n* ✔ Helps extend produce freshness and shelf life\n* ✔ Reduces post-harvest losses\n* ✔ No direct food contact\n* ✔ Low-cost and easy to use\n* ✔ Made from agricultural waste\n* ✔ Suitable for tomatoes, bananas, mangoes, and other climacteric crops")
        st.caption("*♻️ After use, the biochar content can be safely incorporated into soil, helping improve soil quality and supporting a circular agricultural system.*")
        
    with st.expander("📦 ChitoChar Shield (Active Biochar Carton Liners - Future Product)"):
        st.write("ChitoChar Shield is an advanced active-packaging solution currently under development, designed for highly perishable fruits and vegetables that require enhanced protection during storage and transportation. The carton liners are manufactured from biochar and chitosan-based materials, combining gas-management capabilities with natural antimicrobial properties.")
        st.write("**Key Benefits:**\n* ✔ Helps extend shelf life of highly perishable produce\n* ✔ Reduces spoilage during transportation and storage\n* ✔ Natural antimicrobial properties\n* ✔ Adaptable for export packaging\n* Target Applications: berries, grapes, strawberries, fresh-cut produce.")
        
    with st.expander("🌱 ChitoChar Grow (Sustainable Soil Amendment for Pre-Harvest Improvement)"):
        st.write("ChitoChar Grow is a soil-enhancement solution developed from recycled bio-based materials and nutrient-rich agricultural residues. It is designed to improve soil quality, support plant growth, enhance crop resilience, and improve fruit quality before harvest.")
        st.write("**Key Benefits:**\n* ✔ Improves soil health and nutrient availability\n* ✔ Enhances crop resilience to environmental stress\n* ✔ Helps improve post-harvest quality and shelf life starting from the cultivation stage")
        
    with st.expander("🤖 ChitoChar AI (Smart Shelf-Life & Loss Prediction Platform)"):
        st.write("ChitoChar AI helps farmers, distributors, and food businesses make better storage and logistics decisions. Using crop information, storage conditions, and environmental data, the platform predicts shelf life, estimates spoilage risk, and provides recommendations to reduce food loss and maximize product value across the supply chain.")
        
    with st.expander("📖 Vision, Innovation Background & Milestones"):
        st.write("Our startup is tackling one of the most critical challenges in global food systems: post-harvest food loss. Every year, a significant percentage of fresh fruits and vegetables are lost before reaching consumers due to rapid ripening, spoilage, and inefficient preservation methods.")
        st.write("Our core innovation is a low-cost, eco-friendly active preservation sachet developed from bio-based and waste-derived materials. Unlike conventional preservation methods, our sachets do not come into direct contact with food. Instead, they are placed inside packaging where they absorb ripening-related gases, helping slow the deterioration process.")
        st.write("In one of our key trials, we successfully extended the shelf life of tomatoes from 6 days to 19 days at room temperature, highlighting the potential of the solution to significantly reduce food waste across the supply chain.")
        st.write("Our journey has been accelerated through participation in the Ready for Tomorrow program delivered by Plan International, which helped us strengthen our business model and prepare for commercialization. We are currently working toward launching our first products and entering the market in early 2027.")
        st.write("Our work has already gained international recognition, including winning Falling Walls Lab Cairo, organized by DAAD, for our breakthrough contribution to reducing food loss through sustainable packaging innovation.")

# ==========================================
# 🔥 END OF FILE - MAKE SURE THIS LINE IS COPIED 🔥
# ==========================================
