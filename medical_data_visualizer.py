import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def load_data(bmi_overweight=25):
    # Import data
    df = pd.read_csv("medical_examination.csv")

    # Add 'overweight' column
    df["overweight"] = (df["weight"] / ((df["height"] / 100) ** 2) > bmi_overweight).astype(int)

    # Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

    df = df.assign(
        cholesterol=np.minimum(df["cholesterol"] - 1, 1),
        gluc=np.minimum(df["gluc"] - 1, 1),
    )
    return df


# Draw Categorical Plot
def draw_cat_plot(df, split_by="cardio"):
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(
        df,
        id_vars=[split_by],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
    )

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(
        df_cat.groupby([split_by, "variable", "value"]).size().reset_index(name="total")
    )

    # Draw the catplot with 'sns.catplot()'
    sns_plot = sns.catplot(
        df_cat,
        x="variable",
        y="total",
        hue="value",
        col=split_by,
        kind="bar",
    )

    # Get the figure for the output
    fig = sns_plot.fig

    # Do not modify the next two lines
    fig.savefig("catplot.png")
    return fig


# Draw Heat Map
def draw_heat_map(df, outlier_quantile=0.025):
    # Clean the data
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(outlier_quantile))
        & (df["height"] <= df["height"].quantile(1 - outlier_quantile))
        & (df["weight"] >= df["weight"].quantile(outlier_quantile))
        & (df["weight"] <= df["weight"].quantile(1 - outlier_quantile))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, ax=ax, annot=True, fmt=".1f")

    # Do not modify the next two lines
    fig.savefig("heatmap.png")
    return fig