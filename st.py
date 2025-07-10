import streamlit as st
import pandas as pd

df = pd.read_csv("good_tree_coords.csv")

st.map(df,size=1)