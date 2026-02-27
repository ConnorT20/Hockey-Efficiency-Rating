import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#add a title for the app
st.title("Martin Brodeur Playoff Efficiency Analysis")
#import the data
october_df = pd.read_csv("october_stats_df.csv")
november_df = pd.read_csv("november_stats_df.csv")
december_df = pd.read_csv("december_stats_df.csv")
january_df = pd.read_csv("january_stats_df.csv")
february_df = pd.read_csv("february_stats_df.csv")
march_df = pd.read_csv("march_stats_df.csv")
april_df = pd.read_csv("april_stats_df.csv")


#sidebar to select month
month = st.sidebar.selectbox("Select Month", ("October", "November", "December", "January", "February", "March", "April"))
#display the selected month data and visualization
if month == "October":
    st.write("October Stats")
    st.dataframe(october_df)
    st.write("October Efficiency Distribution")
    plt.figure(figsize=(10, 6))
    sns.histplot(october_df['Efficiency'], bins=20, kde=True)
    plt.xlabel("Efficiency")
    plt.ylabel("Frequency")
    plt.title("Distribution of Martin Brodeur's Efficiency in October")
    st.pyplot(plt)
elif month == "November":
    st.write("November Stats")
    st.dataframe(november_df)
elif month == "December":
    st.write("December Stats")
    st.dataframe(december_df)
elif month == "January":
    st.write("January Stats")
    st.dataframe(january_df)
elif month == "February":
    st.write("February Stats")
    st.dataframe(february_df)
elif month == "March":
    st.write("March Stats")
    st.dataframe(march_df)
elif month == "April":
    st.write("April Stats")
    st.dataframe(april_df)