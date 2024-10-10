# <div align='center'> GDP and Happiness </div>
## <div align='center'> - an investigation into connections between nations' Happiness, Social Expenditure, Taxation, Unemployment and GDP </div>

### Introduction

The distribution of wealth within a country and the strategies to ensure its future prosperity are critical issues for both politicians and citizens. My objective with this project has been to generate insights that can help inform these stakeholders' decisions based on objective analysis. I consider this project a preliminary investigation that, through further research, will develop machine learning models capable of predicting GDP with sufficient accuracy to assist politicians in making informed decisions about wealth distribution in their respective countries. My focus in this preliminary project has been on factors such as happiness, social expenditure, taxation, and unemployment as predictors of GDP. These variables are of particular interest to me, and I hypothesized that they are interconnected with GDP in such a way that GDP can be predicted with a reasonable degree of certainty based on these features.   

My problem formulation for this project has been:

- "Does the happiness of nations influence their GDP and can a machine learning model predict GDP from happiness indicators?"  
  
Additionally:  
  
- "Can data on happiness, health, unemployment, social expenditure, taxation, and GDP provide insights into what enhances or diminishes the GDP of nations?"
  


### Guide to the repository:

#### Extraction and cleaning of data
I have used 4 different data sets from 4 different sources. The extraction and basic cleaning of the different dataset happens in four different Jupyter Notebooks which names all starts with 'Extracting...'. In all of these Notebooks one or two data frames has been saved in the 'dataframes.h5' file. In the Notebook called 'Merging_data_frames' I have loaded the cleaned data frames from  'dataframes.h5' and merged them into different data frames and saved then them in the 'dataframes.h5' file as well.  

All data frames in 'dataframes.h5' has been cleaned and follow a specific structure: 
- There are no missing values
- There are no duplicates
- They all have a 'Country' (type: object) and a 'Year' (type: int64) column identifying each row, and then a set of features (type: float64)
- Outliers are included

This cleaning and structure was to make it easy to merge the data and to have different data sets to work with without being concerned of their structure and whether they had been cleaned.
Outliers were included because I judged that the inclusion or exclusion of outliers depended what I wanted to do with the data. 

#### Working with the data and creating models
I have chosen to work with two data frames of the several data frames saved in 'dataframes.h5'. 

 



