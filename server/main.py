import pandas as pd
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

import visualization as viz
import data_processing as dp
import clustering as clus
import classification as clas

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

orig_df = pd.read_csv("diabetes.csv")
print(orig_df.head())

@app.get('/startingColumns')
def get_starting_columns():
    try:
        image_base64 = viz.plot_histograms(orig_df, ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        print("Error in /startingColumns:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get('/zeroValuesRemoved')
def zeroValuesRemoved():
    try:
        df_without_zeros = dp.handle_zeros(orig_df.copy())
        image_base64 = viz.plot_histograms(df_without_zeros, ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI'])
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        print("Error in /zeroValuesRemoved:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get('/outliersRemoved')
def outliersRemoved():
    try:
        # Remove outliers from the specified columns
        new_df = dp.handle_zeros(orig_df.copy())
        new_df = new_df[~new_df['SkinThickness'].isin(dp.detect_outliers_zscore(new_df['SkinThickness']))]
        new_df = new_df[~new_df['BloodPressure'].isin(dp.detect_outliers_zscore(new_df['BloodPressure']))]
        new_df = new_df[~new_df['Insulin'].isin(dp.detect_outliers_zscore(new_df['Insulin']))]
        new_df = new_df[~new_df['BMI'].isin(dp.detect_outliers_zscore(new_df['BMI']))]
        image_base64 = viz.plot_histograms(new_df, ['SkinThickness', 'BloodPressure', 'Insulin', 'BMI'])
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        print("Error in /outliersRemoved:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)
    

# # Visualizing columns
# viz.plot_histograms(df, ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

# # Next we handle zero values with median
# df = dp.handle_zeros(df)
# viz.plot_histograms(df, ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI'])

# # All outliers removed
# df = df[~df['SkinThickness'].isin(dp.detect_outliers_zscore(df['SkinThickness']))]
# df = df[~df['BloodPressure'].isin(dp.detect_outliers_zscore(df['BloodPressure']))]
# df = df[~df['Insulin'].isin(dp.detect_outliers_zscore(df['Insulin']))]
# df = df[~df['BMI'].isin(dp.detect_outliers_zscore(df['BMI']))]
# viz.plot_histograms(df, ['SkinThickness', 'BloodPressure', 'Insulin', 'BMI'])

# # Scaling the data before elbow method
# scaled_data = dp.data_scale(df)

# # Elbow method
# intertia = clus.get_inertia(scaled_data)
# viz.plot_elbow(intertia)

# # Silhouette method to support the decision of clusters
# sil_scores = clus.get_sil_scores(scaled_data)
# viz.plot_silhouette(sil_scores)

# # KMeans
# labels, centroids = clus.run_Kmeans(scaled_data)
# df['Cluster'] = labels
# pca = PCA(n_components=2)
# reduced_data = pca.fit_transform(scaled_data)
# centroids_2d = pca.transform(centroids)

# # Plotting clusters
# viz.plot_clusters(reduced_data, centroids_2d, labels)

# # Comparing cluster assignments to the outcome variable
# comparison = pd.crosstab(df['Cluster'], df['Outcome'], rownames=['Cluster'], colnames=['Actual Outcome'])
# print(comparison)

# # KNN
# accuracies, X_train, X_test, y_train, y_test = clas.run_knn(df)

# # Plot accuracy vs k
# viz.plot_knn(accuracies)

# most_accurate_k = 12
# knn = KNeighborsClassifier(n_neighbors=most_accurate_k)
# knn.fit(X_train, y_train)

# y_pred = knn.predict(X_test)

# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# print("\nClassification Report:\n", classification_report(y_test, y_pred))