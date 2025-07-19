import streamlit as st
import pandas as pd
from src.analysis import generate_synthetic_data, plot_price_vs_volume, run_regression, ab_test

st.set_page_config(page_title="Price Sensitivity Dashboard", layout="wide")

st.title("📊 Price Sensitivity Analysis")

# Upload dataset or generate sample
uploaded_file = st.file_uploader("📁 Upload your price data (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Dataset uploaded successfully!")
else:
    st.info("No file uploaded. Using synthetic dataset.")
    df = generate_synthetic_data()

st.write("### 🔍 Data Preview")
st.dataframe(df.head())

st.write("### 📉 Price vs Order Volume")
fig = plot_price_vs_volume(df)
st.pyplot(fig)

st.write("### 📌 Regression Analysis by Category")
category = st.selectbox("Choose Category", df["category"].unique())
st.code(run_regression(df, category))

st.write("### 🧪 A/B Testing (0% vs 20% Discount)")
ab = ab_test(df)
st.write(f"**T-Statistic**: `{ab['t_statistic']:.3f}`")
st.write(f"**P-Value**: `{ab['p_value']:.4f}`")
if ab['p_value'] < 0.05:
    st.success("Statistically significant difference! ✅")
else:
    st.warning("No significant difference detected. ❌")
