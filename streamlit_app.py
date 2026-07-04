import streamlit as st
import pandas as pd
import requests

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
    page_title="MZ PotatoTwin AI",
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

</style>
""", unsafe_allow_html=True)

# Read Excel Database
data = pd.read_excel("data/Potato_database.xlsx")
data.columns = data.columns.str.strip()

# ---------------- HEADER ----------------

st.markdown("""
<h1 style='text-align:center;color:#2E8B57;font-size:55px;'>
🥔 MZ PotatoTwin AI
</h1>

<h3 style='text-align:center;color:#666666;'>
AI Powered Smart Potato Recommendation System
</h3>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SIDEBAR ----------------

st.sidebar.image("images/potato.png", width=170)

st.sidebar.title("🥔 MZ PotatoTwin AI")

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
        "📋 View All Varieties"
    ]
)

# ---------------- HOME ----------------

if option == "🏠 Home":

    st.image("images/field.jpg", use_container_width=True)

    st.markdown("""
# 🌾 Welcome to MZ PotatoTwin AI

### Making Potato Farming Smarter with Artificial Intelligence
""")

    st.success("Helping Farmers with AI + Live Weather + Climate Advisory")

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

    st.header("✨ Why Choose MZ PotatoTwin AI?")

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

    st.caption("👩‍💻 Developed by Muqadas Zahoor")
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

# ---------------- AI SMART RECOMMENDATION ----------------

elif option == "🤖 AI Smart Recommendation":

    st.header("🤖 AI Smart Recommendation")
    st.success("🤖 AI has analyzed your location, weather and soil conditions.")

    city = st.text_input("District / City")
    district = city

    season = st.text_input("Season")
    soil = st.text_input("Soil Type")
    ph = st.number_input("Soil pH", value=6.0)
    rainfall = st.text_input("Expected Rainfall")

    if st.button("Get AI Recommendation"):

        weather = get_weather(city)

        if weather:

            temperature = weather["current"]["temp_c"]
            humidity = weather["current"]["humidity"]
            wind = weather["current"]["wind_kph"]
            condition = weather["current"]["condition"]["text"]

            st.success("🌦 Live Weather Loaded")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("🌡 Temperature", f"{temperature} °C")

            with col2:
                st.metric("💧 Humidity", f"{humidity}%")

            with col3:
                st.metric("💨 Wind Speed", f"{wind} km/h")

            data["Ideal pH minimum"] = pd.to_numeric(data["Ideal pH minimum"], errors="coerce")
            data["Ideal pH maximum"] = pd.to_numeric(data["Ideal pH maximum"], errors="coerce")
            data["Ideal temprature minimum"] = pd.to_numeric(data["Ideal temprature minimum"], errors="coerce")
            data["ideal temprature maximum"] = pd.to_numeric(data["ideal temprature maximum"], errors="coerce")

            recommendations = []

            for index, row in data.iterrows():

                score = 0

                if district.lower() in str(row["Suitable area"]).lower():
                    score += 20

                if season.lower() in str(row["Suitable Season"]).lower():
                    score += 20

                if soil.lower() in str(row["Soil type"]).lower():
                    score += 20

                if row["Ideal pH minimum"] <= ph <= row["Ideal pH maximum"]:
                    score += 20

                if row["Ideal temprature minimum"] <= temperature <= row["ideal temprature maximum"]:
                    score += 20

                # Humidity Bonus
                if 60 <= humidity <= 80:
                    score += 10

                # Weather Bonus
                if "sunny" in condition.lower():
                    score += 5
                elif "cloud" in condition.lower():
                    score += 3
                elif "rain" in condition.lower():
                    score -= 5

                recommendations.append((score, row))

            recommendations.sort(reverse=True, key=lambda x: x[0])

            st.subheader("🥔 Top AI Recommendations")

            for score, row in recommendations[:3]:

                st.subheader("🥔 " + row["Variety name"])

                st.progress(min(score, 100) / 100)

                st.write("**AI Match Score:**", str(score) + "%")
                if score >= 90:
                    st.success("🏆 Excellent Match")

                elif score >= 70:
                    st.info("✅ Good Match")

                else:
                    st.warning("⚠ Moderate Match")
                st.write("🌡️ Live Temperature:", str(temperature) + " °C")
                st.write("💧 Live Humidity:", str(humidity) + "%")
                st.write("💨 Wind Speed:", str(wind) + " km/h")
                st.write("☁️ Weather Condition:", condition)

                st.write("**Rainfall Requirement:**", row["Rainfall requirement"])
                st.write("**Recommended Irrigation:**", row["recommended irrigation stages"])
                st.write("**Yield Potential:**", row["yield potential"])
                st.write("**Disease Resistant:**", row["disease resistant"])
                st.subheader("🤖 Why This Variety?")
                st.markdown("### 👨‍🌾 Farmer Advice")

                if score >= 90:
                    st.success("Highly recommended for cultivation under current conditions.")

                elif score >= 70:
                    st.info("Suitable variety. Follow proper irrigation and fertilizer schedule.")

                else:
                    st.warning("Suitable with careful crop management.")


                reasons = []

                if district.lower() in str(row["Suitable area"]).lower():
                   reasons.append("✅ Suitable for your selected district")

                if season.lower() in str(row["Suitable Season"]).lower():
                   reasons.append("✅ Suitable for the selected season")

                if soil.lower() in str(row["Soil type"]).lower():
                   reasons.append("✅ Compatible with your soil type")

                if row["Ideal pH minimum"] <= ph <= row["Ideal pH maximum"]:
                   reasons.append("✅ Soil pH is ideal")

                if row["Ideal temprature minimum"] <= temperature <= row["ideal temprature maximum"]:
                   reasons.append("✅ Current temperature is suitable")

                if humidity >= 60 and humidity <= 80:
                   reasons.append("✅ Humidity is favorable")

                if row["disease resistant"] != "No":
                   reasons.append("✅ Good disease resistance")

                for reason in reasons:
                    st.write(reason)

                st.divider()

            st.subheader("🌍 Climate Advisory")

            if temperature > 30:
                st.warning("🔥 High temperature. Heat stress risk for potato crop.")
            elif 18 <= temperature <= 24:
                st.success("✅ Temperature is ideal for potato growth.")
            else:
                st.info("🌱 Temperature is acceptable.")

            if humidity > 80:
                st.warning("🦠 High humidity. Late blight risk may increase.")

            if "rain" in condition.lower():
                st.warning("🌧 Rain expected. Delay irrigation if possible.")
            else:
                st.info("💧 Irrigation can be scheduled normally.")

        else:
            st.error("City not found or API request failed.")

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