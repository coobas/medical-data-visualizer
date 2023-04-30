import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from medical_data_visualizer import load_data, draw_cat_plot, draw_heat_map


df = load_data()

st.title("Medical Data Visualizer")
st.header("Value counts")
st.write(draw_cat_plot(df))

st.header("Correlation Heat Map")
st.write(draw_heat_map(df))
