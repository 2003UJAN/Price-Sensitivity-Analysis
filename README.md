# 📉 Price Sensitivity Analysis Dashboard

Analyze how price changes affect customer order volume across grocery categories like fruits, snacks, and dairy.

## Features
- 📊 Regression modeling (Price → Order Volume)
- 🧪 A/B testing for discount effectiveness
- 📈 Interactive Streamlit dashboard
- 🧬 Use sample synthetic data or upload your own CSV

## 📁 Dataset Format
Expected CSV columns:
- `category`, `price`, `discount`, `order_volume`

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run src/dashboard.py
