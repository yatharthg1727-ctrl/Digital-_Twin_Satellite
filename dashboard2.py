import streamlit as st
import pandas as pd

st.title("Satellite Digital Twin Dashboard")

data = pd.read_csv("data.csv")

st.line_chart(data["Battery"])

st.line_chart(data["Temperature"])

st.line_chart(data["Fuel"])

st.line_chart(data["Signal"])