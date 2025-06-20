import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans

df = pd.read_csv("diabetes.csv")
print(df.head())

# First we create histogram of each colmun to visualie distribution and potential outliers.
fig, axes = plt.subplots(1, 3, figsize=(12, 5))

# Pregnancies
axes[0].hist(df['Pregnancies'], bins=range(df['Pregnancies'].min(), df['Pregnancies'].max() + 2), 
         edgecolor='black', align='left')
axes[0].set_title('Distribution of Pregnancies')
axes[0].set_xlabel('Number of Pregnancies')
axes[0].set_ylabel('Number of Patients')

# Glucose
axes[1].hist(df['Glucose'], bins=50, color='skyblue', edgecolor='black')
axes[1].set_title('Distribution of Glucose Levels')
axes[1].set_xlabel('Glucose')
axes[1].set_ylabel('Number of Patients')

# BloodPressure
axes[2].hist(df['BloodPressure'], bins=50, color="skyblue", edgecolor="black")
axes[2].set_title("Distribution of BloodPressure levels")
axes[2].set_xlabel("BloodPressure (mmHg)")
axes[2].set_ylabel("Number of Patients")

plt.tight_layout()
plt.show()