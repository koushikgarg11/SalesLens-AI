import pandas as pd

def generate_insights(df):

    insights = []

    numeric = df.select_dtypes(include="number")

    if len(numeric.columns) > 0:

        top_col = numeric.sum().idxmax()

        insights.append(
            f"Highest contributing metric is {top_col} with total {numeric[top_col].sum():,.2f}"
        )

        insights.append(
            f"Average value across numeric columns is {numeric.mean().mean():,.2f}"
        )

    if len(df) > 1000:
        insights.append("Dataset is large. Consider filtering for deeper insights.")

    return insights
