import pandas as pd
import numpy as np
import plotly.express as px


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
        value_vars=["cholesterol", "gluc" , "smoke", "alco", "active", "overweight"],
    )

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(
        df_cat.groupby([split_by, "variable", "value"]).size().reset_index(name="total")
    ).astype({"value": "category"})

    # Draw the catplot with 'sns.catplot()'
    fig = px.bar(
        df_cat,
        x="variable",
        y="total",
        facet_col=split_by,
        color="value",
        barmode="group",
    )

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

    fig = px.imshow(
        corr.where(~mask),
        text_auto=".1f",
    )
    return fig
