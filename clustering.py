import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("diabetes.csv")
print(df.head())

# First we visualize each column to identify potential outliers and 0 values in data.
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

# Next we identify specific outliers to remove with z-score method
def detect_outliers_zscore(data):
    outliers = []
    thres = 3
    mean = np.mean(data)
    std = np.std(data)
    for i in data:
        z_score = (i-mean)/std
        if (np.abs(z_score) > thres):
            outliers.append(i)
    return outliers

# All outliers removed
df = df[~df['SkinThickness'].isin(detect_outliers_zscore(df['SkinThickness']))]
df = df[~df['BloodPressure'].isin(detect_outliers_zscore(df['BloodPressure']))]
df = df[~df['Insulin'].isin(detect_outliers_zscore(df['Insulin']))]
df = df[~df['BMI'].isin(detect_outliers_zscore(df['BMI']))]
plot_histograms(df, ['SkinThickness', 'BloodPressure', 'Insulin', 'BMI'])

# Scaling the data before elbow method
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# KMeans for a range of cluster numbers and store the inertia (SSE)
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

# Plotting elbow curve
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia (SSE)')
plt.grid(True)
plt.show()