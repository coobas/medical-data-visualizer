import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from medical_data_visualizer import load_data, draw_cat_plot, draw_heat_map


with st.sidebar:
    bmi_overweight = st.slider("BMI Overweight", 15, 35, 25)
    split_by = st.selectbox("Split by", ["cardio", "sex", "smoke", "alco", "active", "overweight"])
    outlier_quantile = st.number_input("Outlier Quantile", 0.0, 0.2, value=0.025, step=0.005, format="%.3f")

df = load_data(bmi_overweight=bmi_overweight)

st.title("Medical Data Visualizer")
st.header("Value counts")
st.write(draw_cat_plot(df, split_by=split_by))

st.header("Correlation Heat Map")
st.write(draw_heat_map(df, outlier_quantile=outlier_quantile))
