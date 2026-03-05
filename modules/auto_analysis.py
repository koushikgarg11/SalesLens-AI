import pandas as pd

def detect_columns(df):

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    cat_cols = df.select_dtypes(include="object").columns.tolist()

    return numeric_cols, cat_cols


def basic_stats(df):

    stats = {}

    for col in df.select_dtypes(include="number").columns:
        stats[col] = {
            "sum": df[col].sum(),
            "mean": df[col].mean(),
            "max": df[col].max(),
            "min": df[col].min(),
        }

    return stats
