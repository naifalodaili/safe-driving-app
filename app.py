import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="حاسبة القيادة الآمنة والبيئية", page_icon="🚗", layout="centered")

# إضافة تنسيق CSS لدعم اللغة العربية (RTL)
st.markdown("""
    <style>
    body, div, p, h1, h2, h3, h4 {
        direction: RTL;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stMetric {
        background-color: #f0f8ff;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #dcdcdc;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌱 حاسبة القيادة الآمنة والبيئية")
st.subheader("احسب أثرك البيئي ومدى إسهامك في السلامة المرورية")

st.divider()

# قسم المدخلات
st.header("1. البيانات الأساسية")

distance_per_day = st.number_input("المسافة المقطوعة يومياً (كم):", min_value=1, max_value=500, value=40, step=5)
driving_style = st.selectbox(
    "أسلوب القيادة الحالي:",
    ["قيادة متزنة وهادئة", "قيادة سريعة / تسارع وفرملة مفاجأة"]
)
idle_minutes = st.number_input("دقائق انتظار المركبة والمحرك يعمل يومياً (Idling):", min_value=0, max_value=120, value=15, step=5)

# الحسابات الهندسية والبيئية
annual_distance = distance_per_day * 365 # المسافة السنوية
base_fuel_rate = 0.09 # معدل الاستهلاك الأسياسي: 9 لتر / 100 كم

# إضافة زيادة بسبب نمط القيادة
if driving_style == "قيادة سريعة / تسارع وفرملة مفاجأة":
    effective_fuel_rate = base_fuel_rate * 1.25 # زيادة 25% في الاستهلاك
else:
    effective_fuel_rate = base_fuel_rate

# حساب استهلاك الوقود والانبعاثات
fuel_consumption_driving = (annual_distance / 100) * (effective_fuel_rate * 100)
fuel_consumption_idling = (idle_minutes / 60) * 0.6 * 365 # المحرك يهدر ~0.6 لتر/ساعة أثناء الانتظار
total_fuel_liters = fuel_consumption_driving + fuel_consumption_idling

# معامل انبعاث الكربون: 1 لتر بنزين = 2.31 كجم CO2
total_co2_kg = total_fuel_liters * 2.31

# الوفر المتوقع عند تطبيق القيادة البيئية الآمنة (وفر ~20%)
potential_savings_co2 = total_co2_kg * 0.20
trees_equivalent = int(potential_savings_co2 / 20) # كل شجرة تمتص ~20 كجم CO2 سنوياً

st.divider()

# عرض النتائج
st.header("2. بطاقة الأثر البيئي الخاص بك")

col1, col2 = st.columns(2)

with col1:
    st.metric("الانبعاثات الكربونية السنوية الحالية", f"{int(total_co2_kg)} كجم CO2")
    st.metric("الوفر الكربوني عند القيادة الآمنة", f"{int(potential_savings_co2)} كجم CO2")

with col2:
    st.metric("إجمالي استهلاك الوقود التقديري", f"{int(total_fuel_liters)} لتر/سنة")
    st.metric("المكافئ البيئي للوفر السنوي", f"{trees_equivalent} شجرة 🌲")

# قسم السلامة المرورية
st.subheader("🛡️ أثر السرعة على السلامة")
if driving_style == "قيادة سريعة / تسارع وفرملة مفاجأة":
    st.warning("⚠️ خفض السرعة من 100 كم/س إلى 80 كم/س يوفر لك أكثر من **25 متراً** في مسافة التوقف عند الفرملة المفاجأة!")
else:
    st.success("✅ أسلوبك المتزن يوفر مسافة أمان كافية ويقلل إجهاد المكابح والإطارات بنسبة تصل إلى 30%.")

st.divider()

# التعهد والالتزام
st.header("3. التعهد بالقيادة الخضراء والآمنة")
pledge = st.checkbox("أتعهد بتبني أساليب القيادة الآمنة والبيئية لدعم سلامة الطرق وخفض البصمة الكربونية.")

if pledge:
    st.balloons()
    st.success("شكراً لالتزامك! تم تسجيل تعهدك بنجاح والدخول في سحب جوائز أسبوع السلامة والبيئة.")
