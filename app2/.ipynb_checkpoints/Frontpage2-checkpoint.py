import streamlit as st

st.write("## Happiness, GDP and more")

st.write("In this app you can explore and get insights from data about the happiness, GDP, social expenditure, taxation and unemployment of different countries. You can also get predictions of nations' GDP from a machine learning model trained on this data. That is you can enter certain measures of well-being of a country and then a trained model will give you a prediction of the GDP of that country with some certainty")



st.write("### Guide:")

st.write("- **Data:** In the 'data' section you can view the data used for charts and model training. You can get some information about the data and how it's aggregated and you can view some visualizations of the datasets' statistical features")

st.write("- **Charts:** In the 'charts' section you can view a few charts visualizing some interesting comparisons between the countries, between the different data features' predictive power related to GDP and bewteen some clusters of countries based on happiness features")

st.write("- **A predictive model:** In the predictive model section you can enter values of different happiness measures and get a prediction of a countries GDP")   
st.write("")
st.write("Go to https://github.com/TRossen89/BI_Exam to see further details about how the data was prepared for the charts and model in this app and how the charts and model were created")
st.write("")