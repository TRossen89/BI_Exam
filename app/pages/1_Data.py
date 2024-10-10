import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write("# Data")

data_source = st.sidebar.selectbox("Select a dataset:", ["World Happiness Data", "GDP, Happiness, Social Expenditure, Taxation and Unemployment"])


file_name = "../dataframes.h5"
hap_key = "happiness_df"
all_key = "all_df"
hap_box_key = "hap_box_df"
#hap_cor_key = "hap_cor_df"


hap_df = pd.read_hdf(file_name, hap_key)
all_df = pd.read_hdf(file_name, all_key)
hap_box_df = pd.read_hdf(file_name, hap_box_key)
#hap_cor_df = pd.read_hdf(file_name, hap_cor_key)

# Load Data
if data_source == "World Happiness Data":

    st.write("### World Happiness Data")

    st.write("This data contain yearly measures of the happiness of different countries, where the happiness is measured through different 9 different features (GDP per capita is one of them). The data is extracted from the worldhappiness.report webpage. The data is from 2023. The data presented here has been cleaned after extraction. You can get the raw data from the link below.")
    
    st.write("Link: https://worldhappiness.report/data/")
    st.write("")
    st.write("")
    st.write("#### General info about the dataset:")
    st.write("- Number of columns: 11")
    st.write("- Number of rows: 1958")
    st.write("- Number of countries: 156")
    st.write("- Years: 2005-2022")
    st.write("")
    st.write("Further down you can see visualizations of some of the statistical features of the data")
    st.write("")
    st.dataframe(hap_df)
    st.write("")
    st.write("")
    
    st.write("### Box Plots of All 9 Happiness Features")
    
    # Displaying box plots
    plt.figure(figsize=(20, 16))
    sns.boxplot(x='variable', y='value', data=hap_box_df)
    
    plt.xticks(rotation=45)

    st.pyplot(plt)

    st.write("")
    st.write("")
    st.write("### Histograms of All 9 Happiness Features")
    
    # Displaying histograms
    hap_df.drop(columns=["Country", "Year"]).hist(bins=50, figsize=(20, 12))

    st.pyplot(plt)

    st.write("")
    st.write("")
    st.write("### Correlation Matrix of All 9 Happiness Features")

    correlation_matrix = hap_df.drop(columns=["Country", "Year"]).corr()
    
    # Displaying histograms
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    

    st.pyplot(plt)
    
    
else:
    st.write("Aggregated data: GDP, Happiness, Social Expenditure, Taxation and Unemployment")
    st.dataframe(all_df)


