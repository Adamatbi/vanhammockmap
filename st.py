import streamlit as st
import pandas as pd

df = pd.read_csv("good_tree_coords.csv")

st.set_page_config(
    page_title="Van Hammock Map",
)

st.title("Vancouver Hammock Map")
st.write("The map shows the locations of tree pairs suitable for hanging a hammock in Vancouver, Canada.")

st.map(df,size=1)

st.write("Was the map helpful? see a problem? send me a message [here](%s)" % "https://adamatbi.com/contact/")
st.write("Data Source: https://opendata.vancouver.ca/explore/dataset/public-trees")
