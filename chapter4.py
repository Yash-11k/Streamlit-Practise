import streamlit as st
import pandas as pd 

st.title("Chai Dashboard")

file = st.file_uploader("Ipload your csv file", type = ["csv"]) #file uploader

if file:
    df = pd.read_csv(file)
    st.subheader("Data Prieview")
    st.dataframe(df)


if file:
    st.subheader("Summary Stats")
    st.write(df.describe())