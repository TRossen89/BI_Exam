import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import numpy as np
import re

with open('../poly_model.pkl', 'rb') as file:
    poly_model_org = pickle.load(file)

model = poly_model_org[0]  
poly = poly_model_org[1]   
scaler = poly_model_org[2]

st.write("# A Predictive Model")
st.write("In this section, you can enter values for various happiness indicators related to a country, and based on that, you will receive a prediction of the country's GDP per capita.")
st.write("The prediction is created by a trained machine learning model. The model was trained using polynomial regression with a polynomial degree of 2. It was trained with data from the World Happiness data set (see Data). The 'Social support' and 'Healthy life expectancy at birth' features were excluded before training the model given that these features have a high correlation with the 'Life Ladder' feature.")
st.write("")
st.write("The model got an R-Squared of 0.728 from test data")

st.write("")
st.write("### Try the model:")
# Input fields for user data
ladder = st.text_input("Life Ladder (enter value between 1 and 10):")
free = st.text_input("Freedom to make life choices (enter value between 0 and 1):")
gene = st.text_input("Generosity (enter value between 0 and 1):")
corrupt = st.text_input("Perceptions of corruption (enter value between 0 and 1):")
pos = st.text_input("Positive affect (enter value between 0 and 1):")
neg = st.text_input("Negative affect (enter value between 0 and 1):")

if st.button('Calculate prediction!'):
    try:
        # Convert inputs to float
        inputs = [float(ladder), float(free), float(gene), float(corrupt), float(pos), float(neg)]
        
        # Create new data for prediction
        X_new = [inputs]  # Nested list for a single prediction
        X_new_scaled = scaler.transform(X_new)
        
        # Make prediction
        prediction = model.predict(X_new_scaled)
        st.write(prediction)

        # Converting log GDP per capita to US dollars
        pred_us_dollars = np.exp(prediction)

        # Format the prediction for display
        formatted_value = "{:.2f}".format(pred_us_dollars[0])  # Format to 2 decimal places
        st.write("Prediction in US dollars: ", formatted_value)

    except ValueError:
        st.error("Please enter valid numbers for all inputs.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

