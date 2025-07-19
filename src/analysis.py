import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from io import BytesIO

def generate_synthetic_data():
    import numpy as np
    np.random.seed(42)
    categories = ['fruits', 'snacks', 'dairy']
    data = []
    for cat in categories:
        for i in range(50):
            price = round(np.random.uniform(1, 5), 2)
            discount = np.random.choice([0, 10, 20])
            adjusted_price = price * (1 - discount/100)
            base_volume = 200 - (adjusted_price * 30) + np.random.normal(0, 10)
            order_volume = max(10, int(base_volume))
            data.append([cat, price, discount, order_volume])
    df = pd.DataFrame(data, columns=["category", "price", "discount", "order_volume"])
    return df

def plot_price_vs_volume(df):
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x="price", y="order_volume", hue="category", ax=ax)
    ax.set_title("Price vs Order Volume")
    return fig

def run_regression(df, category):
    subset = df[df["category"] == category]
    X = sm.add_constant(subset["price"])
    y = subset["order_volume"]
    model = sm.OLS(y, X).fit()
    return model.summary().as_text()

def ab_test(df):
    group_0 = df[df["discount"] == 0]["order_volume"]
    group_20 = df[df["discount"] == 20]["order_volume"]
    t_stat, p_val, _ = sm.stats.ttest_ind(group_0, group_20)
    return {"t_statistic": t_stat, "p_value": p_val}
