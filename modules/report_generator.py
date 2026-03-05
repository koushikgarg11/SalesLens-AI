import pandas as pd

def generate_report(df):

    report = {}

    report["rows"] = len(df)

    report["columns"] = len(df.columns)

    report["missing_values"] = df.isna().sum().sum()

    report["summary"] = df.describe().to_dict()

    return report
