import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
# from sklearn.cluster import KMeans

df = pd.read_csv("diabetes.csv")
print(df.head())

# First we visualize each column to identify potential outliers in data.
def plot_histograms(df, columns, bins=50):
    n = len(columns)
    n_cols = 4
    n_rows = math.ceil(n / n_cols)

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(12, 5))
    axes = axes.flatten()

    for i, col in enumerate(columns):
        axes[i].hist(df[col], bins=bins, color='skyblue', edgecolor='black')
        axes[i].set_title(f"{col} Distribution")
        axes[i].set_xlabel(col)
        axes[i].set_ylabel("Number of Patients")

    # Turn off any unused axes
    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()
    plt.show()

plot_histograms(df, ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

# Next we handle zero values with median
# We convert them into NaN first
zero_value_cols = ['Glucose', "SkinThickness", "BMI", "BloodPressure", "Insulin"]
df[zero_value_cols] = df[zero_value_cols].replace(0, np.nan)

# Now we replace NaN with mean
df.fillna(df.mean(), inplace=True)
plot_histograms(df, ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI'])