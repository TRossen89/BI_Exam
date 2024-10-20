import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "../dataframes.h5"
high_key = "high_gdp_df"
low_key = "low_gdp_df"
feat_import_key = "feat_import_df"
clust1_key = "clust1_df"
clust2_key = "clust2_df"
clust3_key = "clust3_df"


highest_gdp = pd.read_hdf(file_name, high_key)
lowest_gdp = pd.read_hdf(file_name, low_key)
feat_import_df = pd.read_hdf(file_name, feat_import_key)

clust1_df = pd.read_hdf(file_name, clust1_key)
clust2_df = pd.read_hdf(file_name, clust2_key)
clust3_df = pd.read_hdf(file_name, clust3_key)



st.write("# Charts")

st.write("In this section you can see 3 different charts")
st.write("")
st.write("1) The first chart is a chart made from the aggregated dataset (Social Expenditure, Taxation etc.). The features of the 3 countries with the highest GDP accross 10 years are compared with the features of the 3 countries with the lowest GDP accross 10 years (2012-2022)")
st.write("")
st.write("2) The second chart is also using the aggregated dataset. It's a chart based on a machine learning model using a decision tree regressor. It shows the importance score of four different features used to predict GDP.")
st.write("")
st.write("3) The third chart is a chart of 3 different clusters made from the World Happiness dataset. It visualize the percentage of continents represented in each cluster")
st.write("---")
st.write("")
st.write("### 1. Highest and lowest GDP ")
st.write("These bar charts were made from the aggregated data. The average of GDP per capita, Social Expenditure, Taxation and Unemployment per country over 10 years were calculated and then bar charts showing the average Social Expenditure, Taxation and Unemployment of the 3 countries with highest and lowest average GDP were created")

bar_colors = ['purple', 'darkblue', 'pink']

st.write("#### The 3 countries with highest average GDP over 10 years")
highest_gdp.plot(x='Country', y=['Social expenditure as % of GDP', 'Main aggregated taxation as % of GDP', 'Unemployment as % of labour force'], kind='bar', figsize=(6,5), color=bar_colors)

plt.ylim(0, 50)

plt.ylabel('Amount')
plt.xlabel('')
plt.xticks(rotation=0)
plt.legend(title='Metrics')
plt.axhline(0, color='grey', lw=0.8)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
st.pyplot(plt)

st.write("")

st.write("#### The 3 countries with lowest average GDP over 10 years")
lowest_gdp.plot(x='Country', y=['Social expenditure as % of GDP', 'Main aggregated taxation as % of GDP', 'Unemployment as % of labour force'], kind='bar', figsize=(6,5), color=bar_colors)

plt.ylim(0, 50)

plt.ylabel('Amount')
plt.xlabel('')
plt.xticks(rotation=0)
plt.legend(title='Metrics')
plt.axhline(0, color='grey', lw=0.8)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
st.pyplot(plt)

st.write("")
st.write("---")
st.write("### 2. Importance score predicting GDP ")

st.write("")
st.write("This bar chart shows the importance score of")
st.write("- Life Ladder*") 
st.write("- Main aggregated taxation as % of GDP")
st.write("- Unemployment as % of labour force")
st.write("- Social expenditure as % of GDP") 
st.write("in a Decision Tree Regressor machine learning model. The model was trained from the aggregated dataset where only the above columns were included. The other features (columns) were excluded because there was a high correlation between a summarization of the excluded features and Life Ladder")
st.write("")
st.write("**Life Ladder*:** Life Ladder is a measure of peoples perception of the quality of their life at the time they were asked. They could rank their quality of life from 1 to 10, where 10 is indicating the highest possible quality of life. The values in the Life Ladder column are the country averages")
st.write("")

st.write("#### Feature importance score predicting GDP ")
feat_import_df.plot(kind='bar', x='Feature', y='Importance', legend=False)
plt.xlabel('')
plt.xticks(rotation=45)
st.pyplot(plt)

st.dataframe(feat_import_df)


st.write("---")
st.write("### 3. Continents in different happiness clusters")
st.write("")
st.write("3 clusters were created with a K-Means model from the happiness features in the World Happiness dataset. These were created to see if some clusters of countries were better at predicting GDP from their happiness values than other clusters. The happiness features of cluster 3 were somewhat good at predicting GDP through a Linear Regression machine learning model. The model's R-Squared value was 0.808 from a test of the cluster. The happiness features of cluster 1 and 2 weren't that great. Their R-squared values was around 0.6.")
st.write("Beneath are 3 pie charts of the percentage of continents represented in the different clusters")


st.write("#### Cluster 1")
st.write("R-Squared of this cluster's linear model: 0.578")
value_counts1 = clust1_df['Continent'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(value_counts1, labels=value_counts1.index, autopct='%1.1f%%', startangle=140)

plt.axis('equal') 
st.pyplot(plt)

st.write("")

st.write("#### Cluster 2")
st.write("R-Squared of this cluster's linear model: 0.620")
value_counts2 = clust2_df['Continent'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(value_counts2, labels=value_counts2.index, autopct='%1.1f%%', startangle=140)

plt.axis('equal') 
st.pyplot(plt)

st.write("")
st.write("#### Cluster 3")
st.write("R-Squared of this cluster's linear model: 0.808")
value_counts3 = clust3_df['Continent'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(value_counts3, labels=value_counts3.index, autopct='%1.1f%%', startangle=140)

plt.axis('equal') 
st.pyplot(plt)


         