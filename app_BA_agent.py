import streamlit as st
from main_BA_agent import run_pipeline

st.title("Autonomous Business Analyst Agent")
st.write("Upload a CSV file to get cleaning, analysis, visualizations and a business report.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    with open("temp_uploaded.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded. Running analysis...")

    with st.spinner("Analyzing your data..."):
        report, analysis = run_pipeline("temp_uploaded.csv")

    df = analysis["dataframe"]
    numeric_cols = analysis["numeric_cols"]
    categorical_cols = analysis["categorical_cols"]

    st.subheader("Cleaned Data Preview")
    st.dataframe(df.head(10))

    if numeric_cols:
        st.subheader("Numeric Trends")
        st.line_chart(df[numeric_cols])

    if categorical_cols and numeric_cols:
        st.subheader("Top Category Breakdown")
        top_col = categorical_cols[0]
        group = df.groupby(top_col)[numeric_cols[0]].sum()
        st.bar_chart(group)

    st.subheader("Business Report")
    st.text(report)