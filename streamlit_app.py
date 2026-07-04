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

# Read Excel Database
data = pd.read_excel("data/Potato_database.xlsx")
data.columns = data.columns.str.strip()

# Title
st.title("🥔 MZ PotatoTwin AI")
st.subheader("Smart Potato Recommendation System")

# Sidebar
st.sidebar.title("Menu")

option = st.sidebar.selectbox(
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

    st.header("Welcome to MZ PotatoTwin AI")

    st.write("""
This AI system helps farmers choose the best potato variety based on:

- District
- Season
- Soil Type
- Disease Information
- Fertilizer Recommendation
- AI Smart Recommendation
""")

# ---------------- SEARCH VARIETY ----------------

elif option == "🔍 Search Potato Variety":

    st.header("Search Potato Variety")

    variety = st.text_input("Enter Potato Variety Name")

    if st.button("Search"):

        result = data[
            data["Variety name"].str.lower() == variety.lower()
        ]

        if result.empty:

            st.error("Potato Variety Not Found!")

        else:

            row = result.iloc[0]

            st.success("Potato Variety Found")

            for column in data.columns:

                st.write(f"**{column}:** {row[column]}")


# ---------------- DISTRICT RECOMMENDATION ----------------

elif option == "📍 District Recommendation":

    st.header("District Recommendation")

    district = st.text_input("Enter District Name")

    if st.button("Find Varieties"):

        district_result = data[
            data["Suitable area"].str.contains(district, case=False, na=False)
        ]

        if district_result.empty:

            st.error("No potato variety found for this district.")

        else:

            st.success("Recommended Potato Varieties")

            for variety in district_result["Variety name"]:

                st.write("🥔", variety)


# ---------------- SEASON RECOMMENDATION ----------------

elif option == "🌱 Season Recommendation":

    st.header("Season Recommendation")

    season = st.text_input("Enter Season")

    if st.button("Recommend"):

        season_result = data[
            data["Suitable Season"].str.contains(season, case=False, na=False)
        ]

        if season_result.empty:

            st.error("No potato variety found.")

        else:

            st.success("Recommended Potato Varieties")

            for variety in season_result["Variety name"]:

                st.write("🥔", variety)


# ---------------- SOIL RECOMMENDATION ----------------

elif option == "🌾 Soil Recommendation":

    st.header("Soil Recommendation")

    soil = st.text_input("Enter Soil Type")

    if st.button("Search"):

        soil_result = data[
            data["Soil type"].str.contains(soil, case=False, na=False)
        ]

        if soil_result.empty:

            st.error("No potato variety found.")

        else:

            st.success("Recommended Potato Varieties")

            for variety in soil_result["Variety name"]:

                st.write("🥔", variety)


# ---------------- DISEASE INFORMATION ----------------

elif option == "🦠 Disease Information":

    st.header("Disease Information")

    variety = st.text_input("Enter Potato Variety")

    if st.button("Show Disease Information"):

        result = data[data["Variety name"].str.lower() == variety.lower()]

        if result.empty:

            st.error("Potato Variety Not Found!")

        else:

            row = result.iloc[0]

            st.success("Disease Information")

            st.write("**Late Blight Risk:**", row["late blight risk"])
            st.write("**Early Blight Risk:**", row["early blight risk"])
            st.write("**Common Scab Risk:**", row["common scab risk"])
            st.write("**Black Scurf Risk:**", row["black scurf risk"])
            st.write("**Bacterial Wilt Risk:**", row["bacterial wilt risk"])
            st.write("**Disease Resistant:**", row["disease resistant"])
            st.write("**Major Diseases:**", row["major diseases"])


# ---------------- FERTILIZER RECOMMENDATION ----------------

elif option == "🌿 Fertilizer Recommendation":

    st.header("Fertilizer Recommendation")

    variety = st.text_input("Enter Potato Variety")

    if st.button("Show Fertilizer Recommendation"):

        result = data[data["Variety name"].str.lower() == variety.lower()]

        if result.empty:

            st.error("Potato Variety Not Found!")

        else:

            row = result.iloc[0]

            st.success("Fertilizer Recommendation")

            st.write("**Nitrogen:**", row["nitrogen"])
            st.write("**Phosphorus:**", row["phosphorus"])
            st.write("**Potassium:**", row["potassium"])
            st.write("**Recommendation:**", row["fertilizer recommendation"])


# ---------------- VIEW ALL VARIETIES ----------------

elif option == "📋 View All Varieties":

    st.header("Available Potato Varieties")

    st.dataframe(data[["Variety name"]], use_container_width=True)


# ---------------- AI SMART RECOMMENDATION ----------------

elif option == "🤖 AI Smart Recommendation":

    st.header("🤖 AI Smart Recommendation")

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
                st.write("🌡️ Live Temperature:", str(temperature) + " °C")
                st.write("💧 Live Humidity:", str(humidity) + "%")
                st.write("💨 Wind Speed:", str(wind) + " km/h")
                st.write("☁️ Weather Condition:", condition)

                st.write("**Rainfall Requirement:**", row["Rainfall requirement"])
                st.write("**Recommended Irrigation:**", row["recommended irrigation stages"])
                st.write("**Yield Potential:**", row["yield potential"])
                st.write("**Disease Resistant:**", row["disease resistant"])
                st.subheader("🤖 Why This Variety?")

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

            st.success("Live Weather Information")

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