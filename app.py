import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('house_price_model.pkl')

# App title
st.title("House Price Prediction App")
st.write("Enter the details to predict the house price.")

# Inputs (Change as per your features)
area = st.number_input("Area (in sqft)", min_value=100, max_value=10000, step=50)
bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)
bathrooms = st.slider("Number of Bathrooms", 1, 10, 2)
stories = st.slider("Number of Stories", 1, 4, 1)

# Add other features here...

# Predict button
if st.button("Predict"):
    input_data = np.array([[area, bedrooms, bathrooms, stories]])  # match your model's input shape
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated House Price: ₹ {prediction:,.2f}")
