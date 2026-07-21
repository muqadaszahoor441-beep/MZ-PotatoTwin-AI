import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import st_folium
import streamlit.components.v1 as components
from functions import data
import functions




API_KEY = "794876783d3644a6b1d150548260307"

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# Page Configuration
st.set_page_config(
    page_title="Smart Potato Advisor",
    page_icon="🥔",
    layout="wide"
)

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

div[data-testid="stMetric"]{
    background:#E8F5E9;
    border-radius:12px;
    padding:15px;
}
            
 /* Sidebar */
section[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#1B5E20,#2E7D32,#388E3C);
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Buttons */
.stButton>button{
    background:#2E7D32;
    color:white;
    border-radius:12px;
    border:none;
    padding:10px 18px;
    font-weight:bold;
    transition:0.3s;
}

.stButton>button:hover{
    background:#1B5E20;
    transform:scale(1.05);
}

/* Cards */
.feature-card{
    background:white;
    border-radius:18px;
    padding:20px;
    box-shadow:0px 6px 18px rgba(0,0,0,0.15);
    text-align:center;
    transition:0.4s;
    margin-bottom:15px;
}

.feature-card:hover{
    transform:translateY(-8px);
    box-shadow:0px 10px 25px rgba(0,0,0,0.25);
}

/* Gradient Title */
.main-title{
    text-align:center;
    font-size:48px;
    font-weight:800;
    background:linear-gradient(90deg,#2E7D32,#66BB6A,#A5D6A7);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}
</style>
""", unsafe_allow_html=True)      




# ---------------- HEADER ----------------

st.markdown("""
<h1 style='text-align:center;color:#2E8B57;font-size:55px;'>
🥔 Smart Potato Advisor
</h1>

<h3 style='text-align:center;color:#666666;'>
AI Powered Smart Potato Recommendation System
</h3>
""", unsafe_allow_html=True)

st.markdown("---")





# ---------------- SIDEBAR ----------------

st.sidebar.image("images/potato.png", width=170)

st.sidebar.title("🥔 Smart Potato Advisor")

st.sidebar.success("🌱 Smart Farming Assistant")

st.sidebar.markdown("---")

# Sidebar


option = st.sidebar.radio(
    "Select Feature",
    [
        "🏠 Home",
        "🔍 Search Potato Variety",
        "📍 District Recommendation",
        "🌱 Season Recommendation",
        "🌾 Soil Recommendation",
        "🦠 Disease Information",
        "🌿 Fertilizer Recommendation",
        "🤖 AI Smart Recommendation",
        "🌦️ Live Weather & Climate",
        "📋 View All Varieties",
        "📖 Research Project",
        "📈 Yield Prediction",
        "💰 Economic Analysis",
        "💧 Irrigation Schedule",
        "🌱 Seed Rate Recommendation",
        "🗺️ Pakistan Recommendation Map",
        "🦠 Disease Prediction AI",
        "📄 AI Farmer Report",
        
    
    ]
)

# ---------------- HOME ----------------

if option == "🏠 Home":


    st.image("images/field.jpg", use_container_width=True)

    st.markdown("""
# 🌾 Welcome to Smart Potato Advisor

### Making Potato Farming Smarter with Artificial Intelligence
""")


    st.success("Helping Farmers with AI + Live Weather + Climate Advisory")
    st.markdown("""
    <div style="background:linear-gradient(90deg,#2E8B57,#66BB6A);
    padding:25px;
    border-radius:15px;
    color:white;
    text-align:center;">

    <h2>🥔 Welcome to Smart Potato Advisor </h2>

    <p style="font-size:18px;">
    AI-Based Potato Recommendation • Live Weather • Climate Advisory
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1,2])

    with col1:
        st.image("images/potato.png", width=250)

    with col2:

        st.markdown("""
### 🚀 What can this system do?

✅ Search Potato Variety

✅ AI Smart Recommendation

✅ Live Weather

✅ Climate Advisory

✅ Disease Information

✅ Fertilizer Recommendation

✅ District Recommendation

✅ Season Recommendation

✅ Soil Recommendation
""")

    st.markdown("---")

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.metric("🥔 Potato", "50+")

    with c2:
        st.metric("🤖 AI", "Active")

    with c3:
        st.metric("🌦 Weather", "Live")

    with c4:
        st.metric("🌱 Farmers", "Supported")

    st.markdown("---")

    st.header("✨ Why Choose Smart Potato Advisor?")

    col1,col2,col3=st.columns(3)

    with col1:
        st.success("🤖 Artificial Intelligence")

    with col2:
        st.success("🌦 Live Weather")

    with col3:
        st.success("📈 Better Decision Making")

    st.markdown("---")


    st.info("""
### 🎯 Project Objective

Our mission is to help potato farmers select the best potato variety using:

🌦 Live Weather

🤖 Artificial Intelligence

🌍 Climate Advisory

📈 Smart Recommendation

🦠 Disease Awareness
""")
    
    st.markdown("---")
    st.header("🚀 Smart Features")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="feature-card">
        <h2>🤖</h2>
        <h4>AI Recommendation</h4>
        <p>Find the best potato variety using AI.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="feature-card">
        <h2>🌦️</h2>
        <h4>Live Weather</h4>
        <p>Real-time weather with climate advisory.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="feature-card">
        <h2>🦠</h2>
        <h4>Disease Guide</h4>
        <p>Know disease risks and resistant varieties.</p>
        </div>
        """, unsafe_allow_html=True)

    c4, c5, c6 = st.columns(3)

    with c4:
        st.markdown("""
        <div class="feature-card">
        <h2>🌱</h2>
        <h4>Season Match</h4>
        <p>Choose the right planting season.</p>
        </div>
        """, unsafe_allow_html=True)

    with c5:
        st.markdown("""
        <div class="feature-card">
        <h2>🌾</h2>
        <h4>Soil Analysis</h4>
        <p>Recommend varieties based on soil type.</p>
        </div>
        """, unsafe_allow_html=True)

    with c6:
        st.markdown("""
        <div class="feature-card">
        <h2>🌿</h2>
        <h4>Fertilizer Guide</h4>
        <p>Smart fertilizer recommendations.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style="text-align:center;
    padding:20px;
    background:#E8F5E9;
    border-radius:10px;
    color:#2E7D32;">

    <h3>👩‍💻 Developed by Muqadas Zahoor</h3>

    <p>Smart Potato Advisor </p>

    <p>🌱 AI-Based Smart Farming Platform for Potato Growers</p>

    </div>
    """, unsafe_allow_html=True)
    
    
# ---------------- SEARCH VARIETY ----------------

elif option == "🔍 Search Potato Variety":

    st.header("🔍 Search Potato Variety")

    st.info("Search complete information about any potato variety.")

    variety = st.text_input("🥔 Enter Potato Variety Name")

    if st.button("🔍 Search Variety"):

        result = data[data["Variety name"].str.lower() == variety.lower()]

        if result.empty:

            st.error("❌ Potato Variety Not Found")

        else:

            row = result.iloc[0]

            st.success("✅ Variety Found Successfully")

            st.dataframe(
                row.to_frame(name="Information"),
                use_container_width=True
            )
# ---------------- DISTRICT RECOMMENDATION ----------------

elif option == "📍 District Recommendation":

    st.header("📍 District Recommendation")

    st.info("Find the best potato varieties for your district.")

    district = st.text_input("📍 Enter District")

    if st.button("🌱 Recommend Varieties"):

        district_result = data[
            data["Suitable area"].str.contains(district, case=False, na=False)
        ]

        if district_result.empty:

            st.error("❌ No Variety Found")

        else:

            st.success("✅ Recommended Varieties")

            st.dataframe(
                district_result[["Variety name"]],
                use_container_width=True
            )
# ---------------- SEASON RECOMMENDATION ----------------

elif option == "🌱 Season Recommendation":

    st.header("🌱 Season Recommendation")

    season = st.text_input("🌱 Enter Season")

    if st.button("🌿 Recommend"):

        result = data[
            data["Suitable Season"].str.contains(season, case=False, na=False)
        ]

        if result.empty:

            st.error("❌ No Variety Found")

        else:

            st.success("✅ Recommended Varieties")

            st.dataframe(
                result[["Variety name"]],
                use_container_width=True
            )

# ---------------- SOIL RECOMMENDATION ----------------

elif option == "🌾 Soil Recommendation":

    st.header("🌾 Soil Recommendation")

    soil = st.text_input("🌾 Enter Soil Type")

    if st.button("🌱 Find Variety"):

        result = data[
            data["Soil type"].str.contains(soil, case=False, na=False)
        ]

        if result.empty:

            st.error("❌ No Variety Found")

        else:

            st.success("✅ Recommended Varieties")

            st.dataframe(
                result[["Variety name"]],
                use_container_width=True
            )
# ---------------- DISEASE INFORMATION ----------------

elif option == "🦠 Disease Information":

    st.header("🦠 Disease Risk Information")

    st.info("Check disease resistance and risks for a potato variety.")

    variety = st.text_input("🥔 Enter Potato Variety")

    if st.button("🦠 Check Disease Risk"):

        result = data[data["Variety name"].str.lower() == variety.lower()]

        if result.empty:

            st.error("❌ Potato Variety Not Found")

        else:

            row = result.iloc[0]

            st.success("✅ Disease Information")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Late Blight", row["late blight risk"])
                st.metric("Early Blight", row["early blight risk"])
                st.metric("Common Scab", row["common scab risk"])

            with col2:
                st.metric("Black Scurf", row["black scurf risk"])
                st.metric("Bacterial Wilt", row["bacterial wilt risk"])
                st.metric("Disease Resistant", row["disease resistant"])

            st.markdown("### 🧬 Major Diseases")
            st.info(row["major diseases"])

# ---------------- FERTILIZER RECOMMENDATION ----------------

elif option == "🌿 Fertilizer Recommendation":

    st.header("🌿 Fertilizer Recommendation")

    variety = st.text_input("🥔 Enter Potato Variety")

    if st.button("🌿 Show Recommendation"):

        result = data[data["Variety name"].str.lower() == variety.lower()]

        if result.empty:

            st.error("❌ Potato Variety Not Found")

        else:

            row = result.iloc[0]

            st.success("✅ Fertilizer Recommendation")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Nitrogen", row["nitrogen"])

            with col2:
                st.metric("Phosphorus", row["phosphorus"])

            with col3:
                st.metric("Potassium", row["potassium"])

            st.markdown("### 🌱 Recommendation")

            st.success(row["fertilizer recommendation"])

# ---------------- VIEW ALL VARIETIES ----------------

elif option == "📋 View All Varieties":

    st.header("📋 Available Potato Varieties")

    st.success(f"Total Varieties: {len(data)}")

    st.dataframe(
        data[["Variety name"]],
        use_container_width=True,
        hide_index=True
    )

# ---------------- RESEARCH PROJECT ----------------

elif option == "📖 Research Project":

    st.title("📖 Research Project")

    st.markdown("""
# 🥔 Smart Potato Advisor

### Artificial Intelligence-Based Smart Potato Recommendation System

---

## 🎯 Project Overview

Smart Potato Advisor is an Artificial Intelligence-powered decision support system developed to assist farmers in selecting the most suitable potato varieties based on environmental and agronomic conditions.

The system integrates:

- 🤖 Artificial Intelligence
- 🌦️ Live Weather API
- 🌱 Climate Advisory
- 🌿 Fertilizer Recommendation
- 🦠 Disease Information
- 📊 Smart Variety Recommendation

---

## 🎯 Research Objectives

- Develop an AI-powered potato recommendation system.
- Improve farmers' decision-making.
- Support precision agriculture.
- Integrate real-time weather information.
- Promote sustainable potato production.

---

## 💻 Technologies Used

- Python
- Streamlit
- Pandas
- WeatherAPI
- Microsoft Excel
- GitHub

---

## 📂 Dataset Information

**Current Dataset:** Demonstration Dataset

**Original Institutional Dataset:** Confidential

The original research dataset is not publicly available because it is reserved for ongoing research and future publication.

---

## 🚀 Current Version

**Smart Potato Advisor Version 1.0**

---

## 🔮 Future Enhancements

- Machine Learning Integration
- Yield Prediction
- Disease Prediction
- Mobile Application
- GIS Mapping
- Satellite Data
- IoT Sensors
- Climate Change Prediction

---

© 2026 Muqadas Zahoor

All Rights Reserved.
""")
    
# ---------------- YIELD PREDICTION ----------------

elif option == "📈 Yield Prediction":

    st.header("📈 AI Yield Prediction")

    variety = st.selectbox(
        "Select Potato Variety",
        data["Variety name"].unique()
    )

    city = st.text_input("Enter District / City")

    if st.button("Predict Yield"):

        weather = get_weather(city)

        if weather:

            temperature = weather["current"]["temp_c"]
            humidity = weather["current"]["humidity"]

            row = data[data["Variety name"] == variety].iloc[0]

            st.success("Yield Prediction Generated")

            st.metric("🌾 Expected Yield", row["yield potential"])

            if temperature >= 18 and temperature <= 24:
                st.success("🟢 High Yield Expected")

            elif temperature >= 15 and temperature < 18:
                st.warning("🟡 Moderate Yield Expected")

            else:
                st.error("🔴 Low Yield Expected")

            st.subheader("🤖 AI Suggestions")

            if humidity > 80:
                st.warning("High humidity may increase disease risk.")

            elif humidity >= 60:
                st.success("Humidity is suitable for potato growth.")

            else:
                st.info("Additional irrigation may be required.")

            st.write("🌡 Temperature:", temperature, "°C")
            st.write("💧 Humidity:", humidity, "%")

            st.progress(0.90)

        else:

            st.error("Unable to retrieve weather information.")


# ---------------- ECONOMIC ANALYSIS ----------------

elif option == "💰 Economic Analysis":

    st.header("💰 AI Economic Analysis")

    variety = st.selectbox(
        "Select Potato Variety",
        data["Variety name"].unique(),
        key="eco_variety"
    )

    area = st.number_input(
        "Farm Area (Hectare)",
        min_value=0.1,
        value=1.0,
        step=0.1
    )

    if st.button("Calculate Economic Analysis"):

        row = data[data["Variety name"] == variety].iloc[0]

        # Read values from Excel
        seed_rate = float(str(row["seed rate"]).split()[0])
        fertilizer_cost = float(row["fertilizer cost"])
        irrigation_cost = float(row["irrigation cost"])
        labour_cost = float(row["labour cost"])
        expected_yield = float(row["expected yield"])
        market_price = float(row["market price"])

        # Seed Cost (Demo)
        seed_cost = seed_rate * 35

        total_cost = (
            seed_cost +
            fertilizer_cost +
            irrigation_cost +
            labour_cost
        ) * area

        total_income = (
            expected_yield *
            market_price *
            area
        )

        net_profit = total_income - total_cost

        bcr = total_income / total_cost

        st.success("✅ Economic Analysis Completed")

        col1, col2 = st.columns(2)

        with col1:

            st.metric("🌱 Seed Cost", f"Rs. {seed_cost:,.0f}")

            st.metric("🌿 Fertilizer Cost", f"Rs. {fertilizer_cost:,.0f}")

            st.metric("💧 Irrigation Cost", f"Rs. {irrigation_cost:,.0f}")

            st.metric("👨‍🌾 Labour Cost", f"Rs. {labour_cost:,.0f}")

        with col2:

            st.metric("💰 Total Cost", f"Rs. {total_cost:,.0f}")

            st.metric("💵 Expected Income", f"Rs. {total_income:,.0f}")

            st.metric("📈 Net Profit", f"Rs. {net_profit:,.0f}")

            st.metric("📊 Benefit Cost Ratio", f"{bcr:.2f}")

        st.subheader("🤖 AI Economic Advice")

        if bcr >= 2:

            st.success("🟢 Excellent profitability expected.")

        elif bcr >= 1.5:

            st.info("🟡 Good profitability expected.")

        else:

            st.warning("🔴 Profitability is relatively low.")

        st.progress(min(bcr / 3, 1.0))


# ---------------- IRRIGATION SCHEDULE ----------------

elif option == "💧 Irrigation Schedule":

    st.header("💧 Smart Irrigation Schedule")

    variety = st.selectbox(
        "Select Potato Variety",
        data["Variety name"].unique(),
        key="irrigation"
    )

    city = st.text_input("Enter District / City")

    if st.button("Show Irrigation Schedule"):

        weather = get_weather(city)

        row = data[data["Variety name"] == variety].iloc[0]

        st.success("✅ Irrigation Schedule Generated")

        st.write("🌱 **First Irrigation:**", row["first irrigation"])
        st.write("🌿 **Vegetative Stage:**", row["vegetative irrigation"])
        st.write("🥔 **Tuber Initiation:**", row["tuber initiation"])
        st.write("📈 **Tuber Bulking:**", row["tuber bulking"])
        st.write("🏁 **Last Irrigation:**", row["last irrigation"])
        st.write("💧 **Total Water Requirement:**", row["Total water need"])

        if weather:

            condition = weather["current"]["condition"]["text"]

            st.subheader("🌦 Weather Advisory")

            if "rain" in condition.lower():

                st.warning("🌧 Rain is expected. Delay irrigation.")

            else:

                st.success("✅ Weather is suitable for irrigation.")

        st.subheader("🤖 AI Recommendation")

        st.info(
            "Maintain proper irrigation intervals to improve tuber development and maximize potato yield."
        )


# ---------------- SEED RATE RECOMMENDATION ----------------

elif option == "🌱 Seed Rate Recommendation":

    st.header("🌱 Seed Rate Recommendation")

    variety = st.selectbox(
        "Select Potato Variety",
        data["Variety name"].unique(),
        key="seedrate"
    )

    area = st.number_input(
        "Farm Area (Hectare)",
        min_value=0.1,
        value=1.0,
        step=0.1
    )

    if st.button("Calculate Seed Requirement"):

        row = data[data["Variety name"] == variety].iloc[0]

        seed_rate = float(row["seed rate"])

        total_seed = seed_rate * area

        bags = total_seed / 50

        st.success("✅ Seed Recommendation Generated")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("🌱 Seed Rate", f"{seed_rate:.0f} kg/ha")
            st.metric("🥔 Total Seed Required", f"{total_seed:.0f} kg")

        with col2:
            st.metric("🛍 Seed Bags (50 kg)", f"{bags:.1f}")
            st.metric("📏 Plant Spacing", row["plant spacing"])

        st.write("📏 Row Spacing:", row["row spacing"])
        st.write("🌱 Planting Depth:", row["planting depth"])

        st.subheader("🤖 AI Recommendation")

        st.info(
            "Use certified disease-free seed and maintain recommended spacing for maximum yield."
        )



# ---------------- PAKISTAN RECOMMENDATION MAP ----------------

elif option == "🗺️ Pakistan Recommendation Map":

    st.title("🗺️ Pakistan Potato Recommendation Map")

    district_locations = {
        "Okara": [30.81, 73.45],
        "Sahiwal": [30.66, 73.11],
        "Pakpattan": [30.34, 73.39],
        "Kasur": [31.12, 74.45],
        "Faisalabad": [31.41, 73.08],
        "Depalpur": [30.67, 73.65],
        "Bahawalpur": [29.39, 71.68],
        "Sialkot": [32.49, 74.53]
    }

    district = st.selectbox(
        "Select District",
        list(district_locations.keys())
    )

    m = folium.Map(location=[30.8, 72.8], zoom_start=7)

    lat, lon = district_locations[district]

    folium.Marker(
        [lat, lon],
        popup=district,
        tooltip=district,
        icon=folium.Icon(color="green", icon="leaf")
    ).add_to(m)

    st_folium(m, width=900, height=500)

    result = data[
        data["Suitable area"].str.contains(
            district,
            case=False,
            na=False
        )
    ]

    st.subheader("🥔 Recommended Potato Varieties")

    if result.empty:
        st.warning("No variety available.")
    else:
        st.dataframe(
            result[["Variety name", "Suitable Season", "Soil type"]],
            use_container_width=True
        )

# ---------------- DISEASE PREDICTION AI ----------------

elif option == "🦠 Disease Prediction AI":

    st.title("🦠 AI Disease Prediction")

    variety = st.selectbox(
        "Select Potato Variety",
        data["Variety name"].unique()
    )

    temperature = st.number_input(
        "Temperature (°C)",
        value=22.0
    )

    humidity = st.slider(
        "Humidity (%)",
        30,
        100,
        70
    )

    weather = st.selectbox(
        "Weather Condition",
        [
            "Sunny",
            "Cloudy",
            "Rainy"
        ]
    )

    if st.button("Predict Disease Risk"):

        result = data[
            data["Variety name"] == variety
        ].iloc[0]

        st.subheader("🦠 Disease Prediction Result")

        if humidity > 85 and weather == "Rainy":
            st.error("🔴 High Risk of Late Blight")

        elif humidity > 70:
            st.warning("🟠 Medium Disease Risk")

        else:
            st.success("🟢 Low Disease Risk")

        st.write("Late Blight:", result["late blight risk"])
        st.write("Early Blight:", result["early blight risk"])
        st.write("Common Scab:", result["common scab risk"])
        st.write("Black Scurf:", result["black scurf risk"])
        st.write("Bacterial Wilt:", result["bacterial wilt risk"])

        st.markdown("---")

        st.subheader("💊 Prevention Advice")

        st.info("""
✅ Use certified seed.

✅ Avoid over irrigation.

✅ Maintain proper spacing.

✅ Monitor humidity.

✅ Spray fungicide if necessary.

✅ Remove infected plants immediately.
""")
        

# ---------------- AI FARMER REPORT ----------------

elif option == "📄 AI Farmer Report":

    st.title("📄 AI Farmer Recommendation Report")

    variety = st.selectbox(
        "Select Potato Variety",
        data["Variety name"].unique(),
        key="report"
    )

    city = st.text_input("District / City")

    if st.button("Generate Report"):

        weather = get_weather(city)

        if weather:

            row = data[data["Variety name"] == variety].iloc[0]

            temperature = weather["current"]["temp_c"]
            humidity = weather["current"]["humidity"]
            condition = weather["current"]["condition"]["text"]

            st.success("✅ Report Generated Successfully")

            st.markdown("## 🥔 Potato Variety")
            st.write(row["Variety name"])

            st.markdown("## 🌦 Live Weather")
            st.write("Temperature:", temperature, "°C")
            st.write("Humidity:", humidity, "%")
            st.write("Weather:", condition)

            st.markdown("## 🌱 Yield")
            st.write(row["yield potential"])

            st.markdown("## 🌿 Fertilizer")
            st.write("Nitrogen:", row["nitrogen"])
            st.write("Phosphorus:", row["phosphorus"])
            st.write("Potassium:", row["potassium"])

            st.markdown("## 💧 Irrigation")
            st.write(row["first irrigation"])
            st.write(row["vegetative irrigation"])
            st.write(row["tuber initiation"])
            st.write(row["tuber bulking"])

            st.markdown("## 🦠 Disease Resistance")
            st.write(row["disease resistant"])

            st.markdown("## 📊 AI Recommendation")

            st.info("""
✔ Suitable Variety

✔ Suitable Weather

✔ Follow Fertilizer Recommendation

✔ Monitor Disease Risk

✔ Follow Irrigation Schedule
""")
            

# ---------------- POTATO AI CHATBOT ----------------

elif option == "🤖 Potato AI Chatbot":

    st.title("🤖 Potato AI Chatbot")

    st.write("Ask anything about potato farming.")

    question = st.text_input("Ask your question")

    if st.button("Ask AI"):

        q = question.lower()

        if "best variety" in q:
            st.success("Sante, Asterix and Lady Rosetta are among the best recommended potato varieties.")

        elif "fertilizer" in q:
            st.info("Apply the recommended Nitrogen, Phosphorus and Potassium according to your selected variety.")

        elif "irrigation" in q:
            st.info("Potato requires regular irrigation, especially during tuber initiation and bulking stages.")

        elif "late blight" in q:
            st.warning("Late Blight risk increases under cool and humid weather. Use resistant varieties and recommended fungicides.")

        elif "yield" in q:
            st.success("Yield depends on variety, soil, weather and management practices.")

        elif "season" in q:
            st.info("Autumn and Spring are the major potato growing seasons in Pakistan.")

        elif "weather" in q:
            st.info("Use the Live Weather & Climate module to check current weather conditions.")

        else:
            st.write("🤖 Sorry, I don't know that yet. This feature will be improved in future versions.")

# ---------------- AI SMART RECOMMENDATION ----------------

elif option == "🤖 AI Smart Recommendation":

    st.title("🤖 AI Smart Recommendation")

    st.success("AI analyzes your farm conditions and recommends the best potato varieties.")

    district = st.text_input("📍 Enter District")

    season = st.selectbox(
        "🌱 Select Season",
        ["Autumn", "Spring"]
    )

    soil = st.selectbox(
        "🌾 Select Soil Type",
        sorted(data["Soil type"].dropna().unique())
    )

    ph = st.number_input(
        "🧪 Soil pH",
        min_value=3.0,
        max_value=10.0,
        value=6.0,
        step=0.1
    )

    city = st.text_input("🌦 Enter City")

    if st.button("🚀 Generate AI Recommendation"):

        weather = get_weather(city)

        if weather is None:
            st.error("Unable to retrieve weather information.")
            st.stop()

        temperature = weather["current"]["temp_c"]
        humidity = weather["current"]["humidity"]
        wind = weather["current"]["wind_kph"]
        condition = weather["current"]["condition"]["text"]

        st.success("✅ Live Weather Loaded")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("🌡 Temp", f"{temperature} °C")

        with c2:
            st.metric("💧 Humidity", f"{humidity}%")

        with c3:
            st.metric("💨 Wind", f"{wind} km/h")

        with c4:
            st.metric("☁ Weather", condition)

        recommendations = []
        
        for _, row in data.iterrows():

            score = 0
            reasons = []

            # District Match
            if district.strip().lower() in str(row["Suitable area"]).lower():
                score += 25
                reasons.append("✅ Suitable for your district")

            # Season Match
            if season.strip().lower() in str(row["Suitable Season"]).lower():
                score += 20
                reasons.append("✅ Suitable planting season")

            # Soil Match
            if soil.strip().lower() in str(row["Soil type"]).lower():
                score += 20
                reasons.append("✅ Suitable soil type")

            # pH Match
            try:
                ph_min = float(row["Ideal pH minimum"])
                ph_max = float(row["Ideal pH maximum"])

                if ph_min <= ph <= ph_max:
                    score += 15
                    reasons.append("✅ Ideal soil pH")
            except:
                pass

            # Temperature Match
            try:
                temp_min = float(row["Ideal temprature minimum"])
                temp_max = float(row["ideal temprature maximum"])

                if temp_min <= temperature <= temp_max:
                    score += 15
                    reasons.append("✅ Current temperature is suitable")
            except:
                pass

            # Humidity Bonus
            if 60 <= humidity <= 80:
                score += 5
                reasons.append("✅ Good humidity")

            # Weather Bonus
            weather_text = condition.lower()

            if "clear" in weather_text or "sunny" in weather_text:
                score += 5

            elif "cloud" in weather_text:
                score += 3

            elif "rain" in weather_text:
                score -= 5

            # Score Limits
            score = max(0, min(score, 100))

            recommendations.append({
                "Variety": row["Variety name"],
                "Score": score,
                "Yield": row["yield potential"],
                "Disease": row["disease resistant"],
                "Rainfall": row["Rainfall requirement"],
                "Irrigation": row["recommended irrigation stages"],
                "Reasons": reasons
            })

        recommendations = sorted(
            recommendations,
            key=lambda x: x["Score"],
            reverse=True
        )
        st.subheader("🥔 Top 3 AI Recommendations")

        for rec in recommendations[:3]:

            st.markdown("---")

            st.subheader(rec["Variety"])

            st.progress(rec["Score"] / 100)

            st.write(f"🎯 **AI Match Score:** {rec['Score']}%")
            st.write(f"🌾 **Yield Potential:** {rec['Yield']}")
            st.write(f"🦠 **Disease Resistance:** {rec['Disease']}")
            st.write(f"🌧 **Rainfall Requirement:** {rec['Rainfall']}")
            st.write(f"💧 **Recommended Irrigation:** {rec['Irrigation']}")

            st.write("### ✅ Why this variety?")
            for reason in rec["Reasons"]:
                st.write(reason)
# ---------------- LIVE WEATHER & CLIMATE ----------------

elif option == "🌦️ Live Weather & Climate":

    st.header("🌦️ Live Weather & Climate")

    city = st.text_input("Enter District / City")

    if st.button("Get Live Weather"):

        weather = get_weather(city)

        if weather:

            temp = weather["current"]["temp_c"]
            humidity = weather["current"]["humidity"]
            wind = weather["current"]["wind_kph"]
            condition = weather["current"]["condition"]["text"]

            st.success("🌦 Live Weather Dashboard")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("🌡️ Temperature", f"{temp} °C")
                st.metric("💧 Humidity", f"{humidity}%")

            with col2:
                st.metric("💨 Wind Speed", f"{wind} km/h")
                st.metric("☁️ Weather", condition)

            st.subheader("🌍 Climate Advisory")

            if temp > 30:
                st.warning("🔥 High temperature. Heat stress risk for potato crop.")

            elif 18 <= temp <= 24:
                st.success("✅ Temperature is ideal for potato growth.")

            else:
                st.info("🌱 Temperature is acceptable.")

            if humidity > 80:
                st.warning("🦠 High humidity. Late blight risk may increase.")

            if "rain" in condition.lower():
                st.warning("🌧️ Rain expected. Delay irrigation if possible.")

            else:
                st.info("💧 Irrigation can be scheduled normally.")


        else:

            st.error("City not found or API request failed.")

        st.markdown("---")

        st.info("""
        ### 🌱 Smart Farming Tips

        ✅ Use certified seed.

        💧 Avoid over irrigation.

        🌦 Monitor weather regularly.

        🦠 Inspect crop every week.

        🌿 Apply balanced fertilizer.
        """)

