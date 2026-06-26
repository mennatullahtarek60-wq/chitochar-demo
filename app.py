import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="ChitoChar Smart Dashboard", page_icon="🌱", layout="wide")

# Custom CSS for perfect UI styling and branding
st.markdown("""
<style>
.product-tagline {
    font-size: 1.1rem;
    font-weight: bold;
    color: #2E7D32;
    margin-bottom: 15px;
    font-style: italic;
}
.metric-box {
    background-color: #F4FBF7;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #C8E6C9;
    text-align: center;
    margin-bottom: 15px;
}
.metric-title {
    font-size: 0.9rem;
    color: #555;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: bold;
}
.metric-value {
    font-size: 1.8rem;
    font-weight: bold;
    color: #1B5E20;
    margin-top: 5px;
}
.metric-sub {
    font-size: 0.85rem;
    color: #777;
    margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)

# 2. Main Header & Logo Section
try:
    st.image("logo.png", width=250)
except:
    st.title("ChitoChar")
    st.subheader("Preserving Food, Restoring the Planet")

try:
    st.image("hero_banner.png.jpg", use_container_width=True)
except:
    pass

# Our Story Intro Section
st.markdown("""
<div style="background-color: #F9F9F9; padding: 20px; border-left: 5px solid #2E7D32; border-radius: 4px; margin-bottom: 25px;">
    <h3 style="margin-top:0; color: #1B5E20;">🌱 Our Story</h3>
    <p style="font-size: 1.05rem; color: #333; line-height: 1.6;">
        Every year, millions of tons of fresh fruits and vegetables are lost before they ever reach a consumer's table, 
        while millions of tons of agricultural waste are burned or discarded. At ChitoChar, we asked ourselves how we could bridge this gap. 
        By upcycling biological and agricultural waste streams into active preservation solutions and pre-harvest updates, 
        we protect food ecosystems sustainably.
    </p>
</div>
""", unsafe_allow_html=True)

# 3. Sidebar Layout (Controls & Smart AI Assistant)
st.sidebar.header("⚙️ Control Panel")
crop = st.sidebar.selectbox("Select Crop Type:", ["Tomatoes", "Bananas", "Strawberries", "Berries", "Grapes"])
temp = st.sidebar.slider("Storage/Transit Temperature (°C):", min_value=-5, max_value=40, value=5)
shipment_size = st.sidebar.number_input("Shipment Size (kg):", min_value=1, value=500)

st.sidebar.markdown("---")
st.sidebar.subheader("🤖 Smart AI Assistant")

# Sachet calculation logic simulation
sachets_needed = int(shipment_size * 0.224)
st.sidebar.info(f"💡 **Recommendation:** Deploy **{sachets_needed} Sachets** for this shipment size.")

try:
    st.sidebar.image("sachet_product.png.jpg", caption="ChitoChar Smart Sachet Prototype", use_container_width=True)
except:
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
        <div class="metric-box" style="border: 2px solid #FFB74D;">
            <div class="metric-title">Spoilage Risk Score</div>
            <div class="metric-value" style="color: #E65100;">42%</div>
            <div class="metric-sub" style="background-color: #FFF3E0; padding: 4px 10px; border-radius: 10px; display: inline-block; color: #E65100; font-weight: bold;">Medium Level</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-title">⏳ Expected Range (Shelf Life)</div>
            <div class="metric-value">18 - 24 Days</div>
            <div class="metric-sub">Predicted Shelf Life: Up to 24 Days</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-title">📦 Days Saved Counter</div>
            <div class="metric-value" style="color: #2E7D32;">+6 Days Saved</div>
            <div class="metric-sub">Ethylene Sensitivity: <b>High</b></div>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("📅 Shelf Life Visualization Breakdown")
    chart_data = pd.DataFrame({
        'Condition': ['Control (No Sachet)', 'With ChitoChar Sachet'],
        'Days Fresh': [6, 24 if crop == "Tomatoes" else 19]
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

# --- TAB 3: SOLUTIONS ECOSYSTEM ---
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
        \n**Key Benefits:**
        * ✔ Helps extend produce freshness
        * ✔ Reduces post-harvest losses
        * ✔ No direct food contact
        * ✔ Low-cost and easy to use
        * ✔ Made from upcycled agricultural waste
        * ✔ Suitable for tomatoes, bananas, and a wide variety of fresh items
        * ♻ *After use, the biochar contents can be directly added to soil to act as an amendment.*
        """)

    with st.expander("📦 ChitoChar Shield (Active Biochar Carton Liners - Future Product)"):
        st.markdown('<div class="product-tagline">Protect Every Journey. Preserve Every Harvest.</div>', unsafe_allow_html=True)
        try:
            st.image("shield_product.jpg", width=350, caption="ChitoChar Shield Box Liners")
        except:
            pass
        st.write("""
        ChitoChar Shield is an advanced active-packaging solution integrating biochar properties directly into container and box liners. 
        The carton liners are manufactured from biochar composites to control storage conditions during long-distance shipping.
        \n**Key Benefits:**
        * ✔ Helps extend shelf life of highly perishable crops
        * ✔ Reduces spoilage during transportation and transit
        * ✔ Natural antimicrobial properties
        * ✔ Helps manage ripening-related gases
        * ✔ Suitable for export packaging and sensitive produce
        * ✔ Sustainable alternative to conventional plastic-based liners
        \n**Target Applications:** Berries, grapes, strawberries, and premium export fruits.
        """)

    with st.expander("🌱 ChitoChar Grow (Sustainable Soil Amendment for Pre-Harvest Improvement)"):
        st.markdown('<div class="product-tagline">Healthy Soil. Better Harvests.</div>', unsafe_allow_html=True)
        try:
            st.image("grow_product.jpg", width=350, caption="ChitoChar Grow Soil Solution")
        except:
            pass
        st.write("""
        ChitoChar Grow is a soil-enhancement solution developed from recycled bio-based materials and nutrient-rich agricultural residues.
        It is designed to improve soil quality, support plant growth, enhance crop resilience, and improve fruit quality before harvest.
        Unlike conventional solutions that focus only on preservation after harvest, ChitoChar Grow aims to reduce losses from the beginning by improving crop performance and helping produce maintain quality and freshness for longer periods after harvest.
        \n**Key Benefits:**
        * ✔ Improves soil health
        * ✔ Enhances nutrient availability
        * ✔ Supports root development
        * ✔ Increases crop resilience to environmental stress
        * ✔ Helps improve post-harvest quality and shelf life starting from the cultivation stage
        * ✔ Promotes sustainable farming practices
        * ✔ Converts waste into agricultural value
        """)
        
    with st.expander("🤖 ChitoChar AI (Smart Shelf-Life & Loss Prediction Platform)"):
        st.markdown('<div class="product-tagline">Predict. Protect. Preserve.</div>', unsafe_allow_html=True)
        st.write("""
        ChitoChar AI helps farmers, distributors, and food businesses make better storage and logistics decisions.
        Using crop information, storage conditions, and environmental data, the platform predicts shelf life, estimates spoilage risk, and provides recommendations to reduce food loss and maximize product value across the supply chain.
        \n**Key Features:**
        * ✔ Shelf-life prediction
        * ✔ Spoilage risk assessment
        * ✔ Smart storage recommendations
        * ✔ Economic savings estimation
        * ✔ Sustainability impact tracking
        * ✔ Product-specific guidance for ChitoChar solutions
        """)

    with st.expander("📖 Vision, Innovation Background & Milestones"):
        st.write("""
        Our startup is tackling one of the most critical challenges in global food systems: post-harvest food loss. Every year, a significant percentage of fresh fruits and vegetables are lost before reaching consumers due to rapid ripening, spoilage, and inefficient preservation methods. We are addressing this challenge through an innovative, sustainable, and science-driven solution that extends the shelf life of fresh produce while reducing environmental impact.
        \nOur core innovation is a low-cost, eco-friendly active preservation sachet developed from bio-based and waste-derived materials. Unlike conventional preservation methods, our sachets do not come into direct contact with food. Instead, they are placed inside packaging or storage environments where they absorb ripening-related gases, helping slow the deterioration process and maintain product quality for longer periods. This provides a safer, more sustainable, and more affordable alternative to many imported chemical-based preservation solutions currently used in the market.
        \nThe technology has already documented strong results in laboratory testing. In one of our key trials, we successfully extended the shelf life of tomatoes from 6 days to 19 days at room temperature, highlighting the potential of the solution to significantly reduce food waste across the supply chain. Beyond tomatoes, the technology is designed to be adaptable for a wide range of fruits and vegetables, including highly perishable crops.
        \nWhat makes our solution uniquely sustainable is its end-of-life cycle. Unlike many conventional preservation products that ultimately become waste, our sachets can be opened and their contents returned to the soil after use. The materials are rich in carbon and have the potential to contribute to soil improvement and circular resource utilization, transforming what would otherwise be waste into an additional environmental benefit.
        \nIn addition to our post-harvest solution, we are also developing a complementary pre-harvest product derived from agricultural and biological waste streams. This material is inspired by promising scientific research and is currently under testing. Our goal is to enhance crop quality and longevity before harvest, creating a more comprehensive approach to reducing losses across the entire agricultural value chain.
        \nTo maximize impact, we are also developing an AI-powered digital platform that will serve as a smart assistant for farmers, distributors, retailers, and consumers. The platform will help users predict produce shelf life, optimize storage conditions, receive personalized recommendations, and make data-driven decisions that reduce losses and improve efficiency.
        \nOur journey has been accelerated through participation in the Ready for Tomorrow program delivered by Plan International, which helped us strengthen our business model, refine our market strategy, and prepare for commercialization. We are currently working toward launching our first products and entering the market in early 2027.
        \nOur mission is to transform agricultural and food waste into high-value solutions that enhance food security, support sustainable agriculture, reduce economic losses, and contribute to a more resilient food system. By combining sustainability, biotechnology, materials innovation, and artificial intelligence, we aim to create scalable solutions capable of addressing food loss challenges both in Egypt and globally.
        \nOur work has already gained international recognition, including winning Falling Walls Lab Cairo, organized by DAAD, for our breakthrough contribution to reducing food loss through sustainable packaging innovation.
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
    
