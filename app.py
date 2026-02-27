import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page title and description
st.title("Hockey Player Efficiency Analysis")
st.write("Explore the efficiency of hockey players across different months of the regular season, the playoffs, and their careers.")

#import the data
october_df = pd.read_csv("october_stats_df.csv")
november_df = pd.read_csv("november_stats_df.csv")
december_df = pd.read_csv("december_stats_df.csv")
january_df = pd.read_csv("january_stats_df.csv")
february_df = pd.read_csv("february_stats_df.csv")
march_df = pd.read_csv("march_stats_df.csv")
april_df = pd.read_csv("april_stats_df.csv")
clean_playoff_df = pd.read_csv("clean_playoff_df.csv")
clean_career_df = pd.read_csv("clean_career_df.csv")
yearly_playoff_df = pd.read_csv("yearly_playoff_df.csv")

# create a dropdown menu to select the player
dropdown = st.selectbox("Select Player", ("Martin Brodeur", "Player 2", "Player 3"))

# create a master navigation menu in the sidebar
app_view = st.sidebar.radio("Navigation", ["Regular Season", "Playoffs"])

# create tabs for each season
# define frequency
st.write("")
if app_view == "Regular Season":
    
    month = st.sidebar.selectbox("Select Month", ("All Months", "October", "November", "December", "January", "February", "March", "April"))
    
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
        st.write("November Efficiency Distribution")
        plt.figure(figsize=(10, 6))
        sns.histplot(november_df['Efficiency'], bins=20, kde=True)
        plt.xlabel("Efficiency")
        plt.ylabel("Frequency")
        plt.title("Distribution of Martin Brodeur's Efficiency in November")
        st.pyplot(plt)
    elif month == "December":
        st.write("December Stats")
        st.dataframe(december_df)
        st.write("December Efficiency Distribution")
        plt.figure(figsize=(10, 6))
        sns.histplot(december_df['Efficiency'], bins=20, kde=True)
        plt.xlabel("Efficiency")
        plt.ylabel("Frequency")
        plt.title("Distribution of Martin Brodeur's Efficiency in December")
        st.pyplot(plt)
    elif month == "January":
        st.write("January Stats")
        st.dataframe(january_df)
        st.write("January Efficiency Distribution")
        plt.figure(figsize=(10, 6))  
        sns.histplot(january_df['Efficiency'], bins=20, kde=True)
        plt.xlabel("Efficiency")
        plt.ylabel("Frequency")
        plt.title("Distribution of Martin Brodeur's Efficiency in January")
        st.pyplot(plt)
    elif month == "February":  
        st.write("February Stats")
        st.dataframe(february_df)
        st.write("February Efficiency Distribution")
        plt.figure(figsize=(10, 6))
        sns.histplot(february_df['Efficiency'], bins=20, kde=True)
        plt.xlabel("Efficiency")
        plt.ylabel("Frequency")
        plt.title("Distribution of Martin Brodeur's Efficiency in February")
        st.pyplot(plt)
    elif month == "March":
        st.write("March Stats")
        st.dataframe(march_df)
        st.write("March Efficiency Distribution")
        plt.figure(figsize=(10, 6))
        sns.histplot(march_df['Efficiency'], bins=20, kde=True)
        plt.xlabel("Efficiency")
        plt.ylabel("Frequency")
        plt.title("Distribution of Martin Brodeur's Efficiency in March")
        st.pyplot(plt)
    elif month == "April":
        st.write("April Stats")
        st.dataframe(april_df)
        st.write("April Efficiency Distribution")
        plt.figure(figsize=(10, 6))
        sns.histplot(april_df['Efficiency'], bins=20, kde=True)
        plt.xlabel("Efficiency")
        plt.ylabel("Frequency")
        plt.title("Distribution of Martin Brodeur's Efficiency in April")
        st.pyplot(plt)
    elif month == "All Months":
        st.write("All Months Stats")
        all_months_df = pd.concat([october_df, november_df, december_df, january_df, february_df, march_df, april_df])
        st.dataframe(all_months_df)
        st.write("All Months Efficiency Distribution")
        plt.figure(figsize=(10, 6))
        sns.barplot(data=all_months_df, x='Month', y='Efficiency', color='steelblue')
        plt.ylim(0.85, 1.0) 
        plt.xlabel("Month")
        plt.ylabel("Efficiency Score")
        plt.title("Martin Brodeur's Efficiency Across All Months")
        st.pyplot(plt)
        
elif app_view == "Playoffs":
    
    playoff_efficiency = st.sidebar.selectbox("Select Playoff Efficiency", ("Playoff Efficiency by Year",))
    

    if playoff_efficiency == "Playoff Efficiency by Year":
        st.write("Playoff Efficiency by Year")
        st.dataframe(yearly_playoff_df)
        st.write("Playoff Efficiency Distribution by Year")
        plt.figure(figsize=(10, 6))
        sns.histplot(yearly_playoff_df['Efficiency'], bins=20, kde=True)
        plt.xlabel("Efficiency")
        plt.ylabel("Frequency")
        plt.title("Distribution of Martin Brodeur's Playoff Efficiency by Year")
        st.pyplot(plt)





