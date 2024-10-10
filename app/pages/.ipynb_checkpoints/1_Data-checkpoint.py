import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write("# Data")
st.write("")
st.write("Here you can get an overview of the data used for the charts and machine learning model in the other sections. In the side bar on the left you can choose between 2 different data sets used for this app")
st.write("---")

data_source = st.sidebar.selectbox("Select a dataset:", ["World Happiness", "GDP, Happiness, Social Expenditure, Taxation and Unemployment"])


file_name = "../dataframes.h5"
hap_key = "happiness_df"
all_key = "all_df"
hap_box_key = "hap_box_df"
all_box_key = "all_box_df"


hap_df = pd.read_hdf(file_name, hap_key)
all_df = pd.read_hdf(file_name, all_key)

hap_box_df = pd.read_hdf(file_name, hap_box_key)
all_box_df = pd.read_hdf(file_name, all_box_key)


# Load Data
if data_source == "World Happiness":

    st.write("### **Dataset:** World Happiness")

    st.write("This data contain yearly measures of the happiness of different countries, where the happiness is measured through 9 different features, log GDP per capita being one of them. The data is extracted from the worldhappiness.report webpage. The data is from 2023. The data presented here has been cleaned after extraction. You can get the raw data from the link below.")
    
    st.write("Link: https://worldhappiness.report/data/")
    st.write("")
    st.write("The unit of measures are explained here: https://happiness-report.s3.amazonaws.com/2023/WHR+23_Statistical_Appendix.pdf")
    
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
    st.write("### **Dataset (aggregated):** GDP, Happiness, Social Expenditure, Taxation and Unemployment")

    st.write("This dataset contains yearly measures of the Social Expenditure, Taxation, Unemployment and Happiness of different countries, where the happiness is measured through 9 different features, GDP per capita being one of them. The data is extracted and aggregated from four different sources. The data has been cleaned and aggregated after extraction. You can get the raw data in the four links below.")
    
    st.write("Happiness (and GDP per capita) data: https://worldhappiness.report/data/")
    st.write("Social Expenditure data: https://data-explorer.oecd.org/vis?tm=Social%20expenditure&pg=0&snb=139&vw=tb&df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_SOCX_AGG%40DF_SOCX_AGG&df[ag]=OECD.ELS.SPD&df[vs]=1.0&dq=AUS%2BAUT%2BBEL%2BCZE%2BDNK%2BEST%2BFIN%2BDEU%2BFRA%2BGRC%2BHUN%2BISL%2BIRL%2BISR%2BITA%2BLVA%2BLTU%2BLUX%2BNLD%2BNZL%2BNOR%2BPOL%2BPRT%2BSVK%2BSVN%2BESP%2BSWE%2BCHE%2BTUR%2BGBR%2BUSA.A..PT_OTE_S13%2BPT_B1GQ.ES10._T._T.&pd=1989%2C2022&to[TIME_PERIOD]=false&ly[cl]=TIME_PERIOD&ly[rw]=REF_AREA%2CCOMBINED_UNIT_MEASURE")
    st.write("Taxation data: https://taxation-customs.ec.europa.eu/taxation/economic-analyses/taxation-trends-eu/data-taxation-trends_en")
    st.write("Unemployment data: https://ec.europa.eu/eurostat/databrowser/view/tps00203/default/table?lang=en&category=t_labour.t_employ.t_lfsi.t_une")

    st.write("")
    st.write("")
    st.write("")
    st.write("#### General info about the dataset:")
    st.write("- Number of columns: 15")
    st.write("- Number of rows: 222")
    st.write("- Number of countries: 22")
    st.write("- Years: 2012-2022")
    st.write("")
    st.write("Further down you can see visualizations of some of the statistical features of the data")
    st.write("")
    st.dataframe(all_df)
    st.write("")
    st.write("")
    
    st.write("### Box Plots of All Features")
    
    # Displaying box plots
    plt.figure(figsize=(20, 12))
    sns.boxplot(x='variable', y='value', data=all_box_df)
    
    plt.xticks(rotation=45)

    st.pyplot(plt)

    st.write("")
    st.write("")
    st.write("### Histograms of All Features")
    
    # Displaying histograms
    all_df.drop(columns=["Country", "Year"]).hist(bins=50, figsize=(20, 12))

    st.pyplot(plt)

    st.write("")
    st.write("")
    st.write("### Correlation Matrix of All Features")

    correlation_matrix = all_df.drop(columns=["Country", "Year","Tax difference 2012-2022"]).corr()
    
    # Displaying histograms
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    
    st.pyplot(plt)

    


