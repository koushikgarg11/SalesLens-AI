import streamlit as st

from modules.data_loader import load_dataset
from modules.etl_pipeline import clean_data
from modules.auto_analysis import detect_columns
from modules.charts_engine import generate_chart
from modules.semantic_search import search_dataframe
from modules.insights_engine import generate_insights

st.title("SalesLens AI - Smart Data Analyzer")

uploaded_file = st.file_uploader("Upload Dataset")

if uploaded_file:

    df = load_dataset(uploaded_file)

    df = clean_data(df)

    st.dataframe(df.head())

    numeric_cols, cat_cols = detect_columns(df)

    st.write("Numeric Columns:", numeric_cols)
    st.write("Categorical Columns:", cat_cols)

    if numeric_cols and cat_cols:

        x = st.selectbox("Category", cat_cols)
        y = st.selectbox("Metric", numeric_cols)

        st.plotly_chart(bar_chart(df, x, y))

    st.subheader("Insights")

    insights = generate_insights(df)

    for i in insights:
        st.write("•", i)

    st.subheader("Search Data")

    query = st.text_input("Search dataset")

    if query:

        results = search_dataframe(df, query)

        st.dataframe(results)
