import streamlit as st
import joblib
import pandas as pd
import numpy as np

model = joblib.load("random_forest_model.pkl")


st.title("🏠 House Price Prediction System")

bathroom = st.number_input("Bathrooms", 1, 10, 2)
balcony = st.number_input("Balcony", 0, 5, 1)
bhk = st.number_input("BHK", 1, 10, 2)
carpet_area = st.number_input("Carpet Area (sqft)", 200, 5000, 800)
current_floor = st.number_input("Current Floor", 0, 50, 2)
total_floors = st.number_input("Total Floors", 1, 50, 10)


furnishing = st.selectbox(
    "Furnishing",
    ["Furnished", "Semi-Furnished", "Unfurnished"]
)

furnishing_furnished = 1 if furnishing == "Furnished" else 0
furnishing_semi = 1 if furnishing == "Semi-Furnished" else 0
furnishing_unfurnished = 1 if furnishing == "Unfurnished" else 0


facing = st.selectbox(
    "Facing",
    ["East", "North", "North - East", "North - West",
     "South", "South - East", "South -West", "West"]
)

facing_map = {
    "East": [1,0,0,0,0,0,0,0],
    "North": [0,1,0,0,0,0,0,0],
    "North - East": [0,0,1,0,0,0,0,0],
    "North - West": [0,0,0,1,0,0,0,0],
    "South": [0,0,0,0,1,0,0,0],
    "South - East": [0,0,0,0,0,1,0,0],
    "South -West": [0,0,0,0,0,0,1,0],
    "West": [0,0,0,0,0,0,0,1]
}

facing_values = facing_map[facing]



input_data = pd.DataFrame([[
    bathroom,
    balcony,
    bhk,
    carpet_area,
    current_floor,
    total_floors,
    furnishing_furnished,
    furnishing_semi,
    furnishing_unfurnished,
    *facing_values
]], columns=[
    'Bathroom', 'Balcony', 'BHK', 'Carpet_Area_sqft',
    'Current_Floor', 'Total_Floors',
    'Furnishing_Furnished', 'Furnishing_Semi-Furnished',
    'Furnishing_Unfurnished',
    'facing_East', 'facing_North', 'facing_North - East',
    'facing_North - West', 'facing_South',
    'facing_South - East', 'facing_South -West',
    'facing_West'
])



if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ₹ {prediction[0]:,.0f}")
