import pandas as pd
import streamlit as st
import plotly.express as px

# Load the data
medical_data = pd.read_csv("medical_examination.csv")

st.title("Medical Data Visualizer")

st.markdown(
    """
    This web app visualizes the medical data provided in the CSV file `medical_examination.csv`.
    """
)
st.dataframe(medical_data)

st.header("Histogram visualization")

hist_variable = st.selectbox(
    "Select a variable to display as histogram", medical_data.columns, index=medical_data.columns.get_loc("smoke")
)

fig = px.histogram(
    medical_data,
    x=hist_variable,
    color="sex",
    barmode="group",
    histnorm="percent",
)
st.plotly_chart(fig)
