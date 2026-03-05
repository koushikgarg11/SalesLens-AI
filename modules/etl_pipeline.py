import pandas as pd

def clean_data(df):

    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    df = df.drop_duplicates()

    df = df.dropna(how="all")

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()

    return df
