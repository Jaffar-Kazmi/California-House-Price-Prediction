import streamlit as st
import joblib
import pandas as pd

model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Predictor")

# Numeric inputs
longitude = st.number_input("Longitude", value=-122.23)
latitude = st.number_input("Latitude", value=37.88)
housing_median_age = st.number_input("Housing Median Age", value=20)
total_rooms = st.number_input("Total Rooms", value=1000)
total_bedrooms = st.number_input("Total Bedrooms", value=200)
population = st.number_input("Population", value=800)
households = st.number_input("Households", value=300)
median_income = st.number_input("Median Income", value=3.5)

# Categorical input
ocean_proximity = st.selectbox(
    "Ocean Proximity",
    ["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"]
)

# Create input dataframe
input_data = pd.DataFrame([{
    "longitude": longitude,
    "latitude": latitude,
    "housing_median_age": housing_median_age,
    "total_rooms": total_rooms,
    "total_bedrooms": total_bedrooms,
    "population": population,
    "households": households,
    "median_income": median_income,
    "ocean_proximity": ocean_proximity
}])

input_data["rooms_per_household"] = input_data["total_rooms"] / input_data["households"]
input_data["bedrooms_per_room"] = input_data["total_bedrooms"] / input_data["total_rooms"]
input_data["population_per_household"] = input_data["population"] / input_data["households"]

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")