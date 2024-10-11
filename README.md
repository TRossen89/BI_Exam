# <div align='center'> GDP and Happiness </div>
## <div align='center'> - an investigation into connections between nations' Happiness, Social Expenditure, Taxation, Unemployment and GDP </div>

### Introduction

The distribution of wealth within a country and the strategies to ensure its future prosperity are critical issues for both politicians and citizens. My objective with this project has been to generate insights that can help inform these stakeholders' decisions based on objective analysis. I consider this project a preliminary investigation that, through further research, will develop machine learning models capable of predicting GDP with sufficient accuracy to assist politicians in making informed decisions about wealth distribution in their respective countries. My focus in this preliminary project has been on factors such as happiness, social expenditure, taxation, and unemployment as predictors of GDP. These variables are of particular interest to me, and I hypothesized that they are interconnected with GDP in such a way that GDP can be predicted with a reasonable degree of certainty based on these features.   

 My problem formulation for this project has been:

- *"Does the happiness of nations influence their GDP and can a machine learning model predict GDP from happiness indicators?"*  
  
Additionally:  
  
- *"Can data on happiness, unemployment, social expenditure, taxation, and GDP provide insights into what enhances or diminishes the GDP of nations?"*

  
---
  
### Guide to the repository:  

#### _Extraction and cleaning of data_
I have used 4 different data sets from 4 different sources. These 4 data sets are downloaded from 4 different webpages and stored as either csv, tsv or xlsx files in the folder named 'All_data_files'.   
The basic cleaning of the different dataset happens in four different Jupyter Notebooks which names all starts with 'Extracting...'. In all of these Notebooks one or two data frames has been saved in the 'dataframes.h5' file. In the Notebook called 'Merging_data_frames.ipynb' I have loaded the cleaned data frames from  'dataframes.h5' and merged them into different data frames and saved then them in the 'dataframes.h5' file as well.  

All data frames in 'dataframes.h5' has been cleaned and follow a specific structure: 
- There are no missing values
- There are no duplicates
- Outliers are included
- They all have a 'Country' (type: object) and a 'Year' (type: int64) column identifying each row, and then a set of features (type: float64)
- Irrelevant columns (columns not being a country feature or country identifier) has been removed
  
This cleaning and structure was to make it easy to merge the data and to have different data sets to work with without being concerned about their structure and whether they had been cleaned.
Outliers were included because I judged that the inclusion or exclusion of outliers depended what I wanted to do with the data.  
  
  
#### _Working with the data and creating models_
I have chosen to work with two data frames of the several data frames saved in 'dataframes.h5': 'happines_df' and 'all_df'.  
'happines_df' contain data from one source: World Happiness Report. 'all_df' is a merged data frame which contain data from all data sets extracted.  
In 'all_data_df.ipynb' I work with 'all_df' and in 'happiness_data.ipynb' I work with 'happiness_df'. 
- 'all_data_df.ipynb': Here I explore the dataset, prepare it for machine learning, create charts showing a summarization of the features and train and test different machine learning models trying to predict GDP. 
- 'happiness_data.ipynb': Here I explore the dataset, prepare it for machine learning and train and test different machine learning models that could predict GDP from the other happiness features. I also train an unsupervised machine learning model to cluster the data from 6 of the happiness features. This was to see if some clusters of countries was better at predicting GDP from happiness features than others. In the Notebook one machine learning model is saved in the 'poly_model.pkl' file. It was the best model I trained and tested using the full happinness data set and therefore I chose to save that for the streamlit app.   
  
#### _Streamlit app_
In the folder named 'app' there is a streamlit app showing some of the data visualizations and machine learning model I have created. The two data frames I've worked with is also presented.  
  
#### _Irrelevant folder and irrelevant data sets_
The folder 'Initial_messy_research' contains a Notebook with my initial data search and exploration. Nothing from that Notebook is used two answer my problem formulation or create my streamlit app. The 'All data files' folder contains several data sets used in the Notebook in 'Initial_messy_research'.

---

### Brief Conclusions

- My data exploration in both of the used data frames show that there is a high correlation between the happiness indicator 'Life Ladder' and GDP. The correlation doesn't say anything about whether it's the Life Ladder that causes GDP or reverse, so I can't say much about whether happiness influence GDP from this. 
- My investigation into the happiness data frame and into whether the happiness features can predict GDP, I found that a polynomial regression model was the best at predicting the GDP when the whole data set was splittet in a training and testing set. It had an R-Squared of 0.728 when tested on data it wasn't trained on.  
- My clustering of the data based on 6 happiness features gave me 3 clusters (chosen from a combination of the elbow method and silhoutte score). One of these clusters produced the best model for predicting GDP based on happiness features. A linear regression model was trained with an R-Squared of 0.808 when tested on data it wasn't trained on. The other two clusters had an R-Squared around 0.6. This indicates that in a group of countries their might be a more close connection between happiness and GDP than in others, although the clusterings silhoutte score were only around .25 indicating that the clusters arend that separated.
- My investigation of my own aggregated data frame (all_df) showed that happiness, unemployment, social expenditure and taxation together couldn't predict GDP that well. All my linear regression models trained had an R-Squared under 0.55 and the decission tree regressor model had an R-Squared of 0.66. The decision tree did show that Life Ladder was by far the most important feature of those 4 features when predicting GDP. In general the investigations from this data set indicated that unemployment, social expenditure and taxation has no direct impact on GDP. This is visualized in a bar chart showing that there is no clear difference between the 3 countries with a the highest GDP over 10 years and the 3 countries with the lowest GDP over 10 years when it comes to measures of unemployment, social expenditure and taxation. 

 



