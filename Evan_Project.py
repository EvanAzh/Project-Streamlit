''' Toulouse Business School MSc AIBA

Course: Advanced Python for Data Science -- PROJECT
Author: Evan Brahma Hughie Azhabur
Version: v1.0

Project Description and Goal
1. Data Import; this can be an Excel spreadsheet, CSV file, Database query or data streaming.
2. Data Visualisation; the data app displays one or more charts.
3. User Input; at least one; this can be text/number input, file upload, selection from choices, …
4. (Bonus) External Interaction; this can be calling a machine learning model served with a
REST API for example.

'''

# Importing Libraries needed
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Function for loading and clean the data

@st.cache_data
def load_data():
    data = pd.read_csv(
        "D:/Local Disk D/TBS/Semester 1/Module 3 Programming/3.3. Advanced Python for Data Science - Samia Drappeau/Project/Project_Evan/Evan Brahma_Advanced Python for Data Science_Project/University1.csv",
        sep=";")
    data_clean = data.dropna()
    return data_clean

# Function for showing the data

@st.cache_data
def get_univ(data):
    return sorted(data['Name'].unique().tolist())[:30]

# Function for horizontal graph of qualification rate

def qualification_rate():
    st.write("Qualification rate Analysis")
    st.write("Comparison between the number of applicant, eligibles and qualified entering the university")
    dfqr = load_data()
    xqr = (
        dfqr['Total.applicants'],
        dfqr['Total.eligibles'],
        dfqr['Total.qualified'])
    x_pos = np.arange(len(xqr))
    bar = px.bar(x_pos,
                 x=dfqr[['Total.applicants', 'Total.eligibles', 'Total.qualified']].sum(),
                 y=['Total Applicants', 'Total Eligibles', 'Total Qualified'],
                 orientation='h',
                 labels={'x': 'Sum of the data value', 'y': 'Category'},
                 title='Qualification Analysis')
    return(bar)

# Function for scatter plot graph of tuition vs enrollment

def tuition_vs_enrollment():
    st.write("The Relationship Between Fee and Enrollment")
    st.write("Searching for trend and pattern within the tuition fee and number of applicant that want to enroll in a university")
    dftve = load_data()
    fil_dftve = dftve[dftve['Tuition.fees'] <= 50000]
    scat = st.scatter_chart(data=fil_dftve, x='Tuition.fees',
                            y='Total.applicants',
                            color='#FF0000',
                            use_container_width=True)
    return(scat)

# Main Function

def main():
    st.title("University Analysis")
    st.subheader("Glimpse of the Data")
    df = load_data()

    univ_list = ['All University'] + get_univ(df)
    selected_univ = st.selectbox('Choose a University', univ_list)

    if selected_univ == 'All University':
        st.write('Here is every University!')
        st.write(df.head(30))
    else:
        st.write(f'You Selected {selected_univ}')
        univ = df[df['Name'] == selected_univ]
        st.write(univ)

    st.sidebar.header(("The Analysis begin!"))
    st.sidebar.markdown(
        "Here is the visualization of the University data, pick the type of analysis below!")
    selected_option = st.sidebar.selectbox(
        "Select Desired Analysis", [
            "Qualification Rate", "Fee vs Enrollment Relationship"])

    if selected_option == "Qualification Rate":
        qr = qualification_rate()
        st.write(qr)
        st.write(
            "Based on the analysis results, out of a total of 8 million applicants across all universities, only 4.38 million were deemed eligible, and 1.28 million were qualified for university admission."
            "Consequently, the acceptance rate is calculated to be 15.9%")
    elif selected_option == "Fee vs Enrollment Relationship":
        tuition_vs_enrollment()
    else:
        st.write("none")


if __name__ == '__main__':
    main()
