import streamlit as st
import pandas as pd

df = pd.read_csv("good_tree_coords.csv")

st.title("Vancouver Hammock Map")
st.write("This map shows the locations of tree pairs suitable for hammocks in Vancouver, Canada.")
st.write("Data Source: https://opendata.vancouver.ca/explore/dataset/public-trees")

st.map(df,size=1)