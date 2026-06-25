import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="ChitoChar Smart Dashboard", page_icon="🌱", layout="wide")

# تصميم الواجهة بالألوان المتناسقة مع الهوية المستدامة
st.markdown("""
    <style>
    .main-title { font-size:36px; font-weight:bold; color:#1E5631; text-align:center; margin-bottom:10px; }
    .sub-title { font-size:18px; color:#4C9A2A; text-align:center; margin-bottom:30px; }
    .metric-box { background-color:#F4F9F4; padding:15px; border-radius:10px; text-align:center; border: 1px solid #E0EFE0; }
    </style>
""", unsafe_allowed_html=True)

st.markdown('<div class="main-title">🌱 ChitoChar - المنصة الرقمية الذكية</div>', unsafe_allowed_html=True)
st.markdown('<div class="sub-title">تحويل الهدر الغذائي إلى حلول مستدامة ودعم الأمن الغذائي</div>', unsafe_allowed_html=True)

# القائمة الجانبية للمدخلات (Sidebar Inputs)
st.sidebar.header("📥 مدخلات المستثمر / المزارع")

crop = st.sidebar.selectbox("اختر نوع المحصول:", ["طماطم (Tomatoes)", "فراولة (Strawberries)", "مانجو (Mangoes)"])
quantity = st.sidebar.number_input("الكمية المخزنة (بالطن):", min_value=0.1, value=1.0, step=0.5)

# تحديد ظروف التخزين بناءً على نوع المحصول
if crop == "فراولة (Strawberries)":
    storage = st.sidebar.selectbox("ظروف التخزين الحالية:", ["درجة حرارة الغرفة Room Temperature", "تبريد Refrigerated"])
else:
    storage = st.sidebar.selectbox("ظروف التخزين الحالية:", ["درجة حرارة الغرفة Room Temperature"])

# تعيين الأسعار الافتراضية لكل محصول (بالجنيه المصري للكيلو)
default_price = 12 if "طماطم" in crop else (35 if "فراولة" in crop else 40)
price_per_kg = st.sidebar.number_input("سعر بيع الكيلو المتوقع في السوق (ج.م):", min_value=1, value=default_price)

# قاعدة البيانات الحسابية (Logic Backend)
data = {
    "طماطم (Tomatoes)": {"normal": 6, "chito": 19, "reduction": 0.70, "saved_kg": 245, "co2": 147},
    "مانجو (Mangoes)": {"normal": 7, "chito": 21, "reduction": 0.65, "saved_kg": 162, "co2": 130},
    "فراولة (Strawberries)": {
        "درجة حرارة الغرفة Room Temperature": {"normal": 3, "chito": 8, "reduction": 0.75, "saved_kg": 300, "co2": 360},
        "تبريد Refrigerated": {"normal": 7, "chito": 16, "reduction": 0.75, "saved_kg": 300, "co2": 360}
    }
}

# استخراج القيم بناءً على الاختيار
if "فراولة" in crop:
    current_data = data["فراولة (Strawberries)"][storage]
else:
    current_data = data[crop]

# الحسابات الديناميكية بناءً على الكمية المدخلة
total_saved_kg = current_data["saved_kg"] * quantity
financial_roi = total_saved_kg * price_per_kg
total_co2_saved = current_data["co2"] * quantity
organic_carbon = 1.5 * quantity

# عرض النتائج في لوحة القيادة (Dashboard)
st.subheader(f"📊 نتائج التحليل الديناميكي لـ {quantity} طن من {crop}:")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<div class="metric-box"><h4>💰 العائد المالي الموفر</h4><h2>{financial_roi:,.0f} ج.م</h2><p>تم حمايتها من الخسارة المباشرة</p></div>', unsafe_allowed_html=True)
with col2:
    st.markdown(f'<div class="metric-box"><h4>🍅 كمية المحصول المنقذة</h4><h2>{total_saved_kg:,.0f} كجم</h2><p>من أصل {quantity*1000:,.0f} كجم مخزن</p></div>', unsafe_allowed_html=True)
with col3:
    st.markdown(f'<div class="metric-box"><h4>📉 نسبة تقليل الهدر</h4><h2>{current_data["reduction"]*100:.0f}%</h2><p>بناءً على تقارير الفقد المحلية</p></div>', unsafe_allowed_html=True)

st.write("---")

# القسم الخاص بمقارنة فترة الصلاحية والرسم البياني
col_left, col_right = st.columns([1, 1])

with col_left:
    st.subheader("⏳ مقارنة فترة الصلاحية (بالأيام)")
    fig, ax = plt.subplots(figsize=(5, 3))
    categories = ['بدون شيتوشار', 'مع شيتوشار']
    days = [current_data["normal"], current_data["chito"]]
    colors = ['#E63946', '#4C9A2A']
    
    bars = ax.bar(categories, days, color=colors, width=0.5)
    ax.set_ylabel('عدد الأيام')
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f'{yval} يوم', ha='center', va='bottom', fontweight='bold')
    
    st.pyplot(fig)

with col_right:
    st.subheader("🌍 الأثر البيئي والاستدامة (Circular Economy)")
    st.info(f"**📉 تقليل انبعاثات الكربون:** منع تلف هذه الكمية يمنع انبعاث ما يعادل **{total_co2_saved:,.1f} كجم من غاز $CO_2$.**")
    st.success(f"**🌱 كربون مردود للتربة:** بعد فتح الأظرف واستخدامها، ستعيدين **{organic_carbon:,.1f} كجم من الكربون العضوي النقي** لتحسين جودة التربة كسماد طبيعي.")

st.write("---")
st.caption("ChitoChar App • الفائز بالمركز الثالث في Falling Walls Lab Cairo • رؤية مستدامة لعام 2027")
  
