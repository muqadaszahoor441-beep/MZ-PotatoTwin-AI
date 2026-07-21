import pandas as pd

data = pd.read_excel(
    "data/Potato_database.xlsx",
    sheet_name="potato varieties"
)

def search_variety():

    print("\nSearch Potato Variety")

    variety = input("\nEnter Potato Variety: ")

    result = data[data["Variety name"].str.lower() == variety.lower()]

    if result.empty:
        print("\nPotato variety not found!")

    else:
        row = result.iloc[0]

        print("\n========== POTATO INFORMATION ==========\n")

        for column in data.columns:
            print(f"{column}: {row[column]}")


def district_recommendation():

    print("\nDistrict Recommendation")

    district = input("\nEnter District: ")

    district_result = data[
        data["Suitable area"].str.contains(district, case=False, na=False)
    ]

    if district_result.empty:
        print("\nNo potato variety found for this district.")

    else:
        print("\nRecommended Potato Varieties:\n")

        for variety in district_result["Variety name"]:
            print("-", variety)


def season_recommendation():

    print("\nSeason Recommendation")

    season = input("\nEnter Season: ")

    season_result = data[
        data["Suitable Season"].str.contains(season, case=False, na=False)
    ]

    if season_result.empty:
        print("\nNo potato variety found for this season.")

    else:
        print("\nRecommended Potato Varieties:\n")

        for variety in season_result["Variety name"]:
            print("-", variety)


def soil_recommendation():

    print("\nSoil Recommendation")

    soil = input("\nEnter Soil Type: ")

    soil_result = data[
        data["Soil type"].str.contains(soil, case=False, na=False)
    ]

    if soil_result.empty:
        print("\nNo potato variety found for this soil type.")

    else:
        print("\nRecommended Potato Varieties:\n")

        for variety in soil_result["Variety name"]:
            print("-", variety)


def disease_information():

    print("\nDisease Risk Information")

    variety = input("\nEnter Potato Variety: ")

    result = data[data["Variety name"].str.lower() == variety.lower()]

    if result.empty:
        print("\nPotato variety not found!")

    else:
        row = result.iloc[0]

        print("\nDisease Information:\n")

        print("Late Blight Risk:", row["late blight risk"])
        print("Early Blight Risk:", row["early blight risk"])
        print("Common Scab Risk:", row["common scab risk"])
        print("Black Scurf Risk:", row["black scurf risk"])
        print("Bacterial Wilt Risk:", row["bacterial wilt risk"])
        print("Disease Resistant:", row["disease resistant"])
        print("Major Diseases:", row["major diseases"])


def fertilizer_recommendation():

    print("\nFertilizer Recommendation")

    variety = input("\nEnter Potato Variety: ")

    result = data[data["Variety name"].str.lower() == variety.lower()]

    if result.empty:
        print("\nPotato variety not found!")

    else:
        row = result.iloc[0]

        print("\n========== FERTILIZER RECOMMENDATION ==========\n")

        print("Nitrogen:", row["nitrogen"])
        print("Phosphorus:", row["phosphorus"])
        print("Potassium:", row["potassium"])
        print("Fertilizer Recommendation:", row["fertilizer recommendation"])

    
def ai_smart_recommendation():

    print("\n========== AI SMART RECOMMENDATION ==========\n")

    district = input("Enter District: ")
    season = input("Enter Season: ")
    soil = input("Enter Soil Type: ")
    ph = float(input("Enter Soil pH: "))
    temperature = float(input("Enter Average Temperature (°C): "))
    rainfall = input("Enter Expected Rainfall (mm): ")
   
    # Convert numeric columns
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

        recommendations.append((score, row))

    recommendations.sort(reverse=True, key=lambda x: x[0])

    print("\n========== TOP RECOMMENDATIONS ==========\n")

    for score, row in recommendations[:3]:

        print("Variety:", row["Variety name"])
        print("AI Match Score:", str(score) + "%")
        print("Rainfall Requirement:", row["Rainfall requirement"])
        print("Recommended Irrigation Stages:", row["recommended irrigation stages"])
        print("Yield Potential:", row["yield potential"])
        print("Disease Resistant:", row["disease resistant"])
        print("-" * 50)