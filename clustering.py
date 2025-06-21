import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans

df = pd.read_csv("diabetes.csv")
print(df.head())

# First we create histogram of each colmun to visualie distribution and potential outliers.
fig, axes = plt.subplots(2, 4, figsize=(12, 5))

# Pregnancies
axes[0][0].hist(df['Pregnancies'], bins=range(df['Pregnancies'].min(), df['Pregnancies'].max() + 2), 
         edgecolor='black', align='left')
axes[0][0].set_title('Distribution of Pregnancies')
axes[0][0].set_xlabel('Number of Pregnancies')
axes[0][0].set_ylabel('Number of Patients')

# Glucose
axes[0][1].hist(df['Glucose'], bins=50, color='skyblue', edgecolor='black')
axes[0][1].set_title('Distribution of Glucose Levels')
axes[0][1].set_xlabel('Glucose')
axes[0][1].set_ylabel('Number of Patients')

# BloodPressure
axes[0][2].hist(df['BloodPressure'], bins=50, color="skyblue", edgecolor="black")
axes[0][2].set_title("Distribution of BloodPressure levels")
axes[0][2].set_xlabel("BloodPressure (mmHg)")
axes[0][2].set_ylabel("Number of Patients")

# SkinThickness
axes[0][3].hist(df['SkinThickness'], bins=50, color="skyblue", edgecolor="black")
axes[0][3].set_title("Distribution of SkinThickness levels")
axes[0][3].set_xlabel("SkinThickness (mm)")
axes[0][3].set_ylabel("Number of Patients")

# Insulin
axes[1][0].hist(df['Insulin'], bins=50, color="skyblue", edgecolor="black")
axes[1][0].set_title("Distribution of Insulin levels")
axes[1][0].set_xlabel("Insulin")
axes[1][0].set_ylabel("Number of Patients")

# BMI
axes[1][1].hist(df['BMI'], bins=50, color="skyblue", edgecolor="black")
axes[1][1].set_title("Distribution of BMI levels")
axes[1][1].set_xlabel("BMI")
axes[1][1].set_ylabel("Number of Patients")

# DiabetesPedigreeFunction
axes[1][2].hist(df['DiabetesPedigreeFunction'], bins=50, color="skyblue", edgecolor="black")
axes[1][2].set_title("Distribution of DiabetesPedigreeFunction levels")
axes[1][2].set_xlabel("DiabetesPedigreeFunction")
axes[1][2].set_ylabel("Number of Patients")

# Age
axes[1][3].hist(df['Age'], bins=50, color="skyblue", edgecolor="black")
axes[1][3].set_title("Distribution of Age")
axes[1][3].set_xlabel("Age")
axes[1][3].set_ylabel("Number of Patients")

plt.tight_layout()
plt.show()