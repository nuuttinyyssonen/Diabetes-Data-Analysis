import numpy as np
from sklearn.preprocessing import StandardScaler

def handle_zeros(df):
    # We convert them into NaN first
    zero_value_cols = ['Glucose', "SkinThickness", "BMI", "BloodPressure", "Insulin"]
    df[zero_value_cols] = df[zero_value_cols].replace(0, np.nan)

    # Now we replace NaN with mean
    df.fillna(df.median(), inplace=True)
    return df

# z-score method to detect outliers
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

def data_scale(df):
    data_without_outcome = df.drop(columns=['Outcome'])
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data_without_outcome)
    return scaled_data