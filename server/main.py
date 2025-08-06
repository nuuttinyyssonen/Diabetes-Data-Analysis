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

def get_cleaned_df():
    df = dp.handle_zeros(orig_df.copy())
    df = df[~df['SkinThickness'].isin(dp.detect_outliers_zscore(df['SkinThickness']))]
    df = df[~df['BloodPressure'].isin(dp.detect_outliers_zscore(df['BloodPressure']))]
    df = df[~df['Insulin'].isin(dp.detect_outliers_zscore(df['Insulin']))]
    df = df[~df['BMI'].isin(dp.detect_outliers_zscore(df['BMI']))]
    return df

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
        df = dp.handle_zeros(orig_df.copy())
        image_base64 = viz.plot_histograms(df, ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI'])
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        print("Error in /zeroValuesRemoved:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get('/outliersRemoved')
def outliersRemoved():
    try:
        df = get_cleaned_df()
        image_base64 = viz.plot_histograms(df, ['SkinThickness', 'BloodPressure', 'Insulin', 'BMI'])
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        print("Error in /outliersRemoved:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.get('/elbowMethod')
def get_elbow_method():
    try:
        df = get_cleaned_df()
        scaled_data = dp.data_scale(df)
        inertia = clus.get_inertia(scaled_data)
        image_base64 = viz.plot_elbow(inertia)
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        print("Error in /elbowMethod:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get('/silhouetteScores')
def get_silhouette_scores():
    try:
        df = get_cleaned_df()
        scaled_data = dp.data_scale(df)
        sil_scores = clus.get_sil_scores(scaled_data)
        image_base64 = viz.plot_silhouette(sil_scores)
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        print("Error in /silhouetteScores")
        return JSONResponse(content={"error": str(e)}, status_code=500)

# # KMeans
@app.get('/kmeansPlot')
def getKmeansPlot():
    try:
        df = get_cleaned_df()
        scaled_data = dp.data_scale(df)
        labels, centroids = clus.run_Kmeans(scaled_data)
        pca = PCA(n_components=2)
        reduced_data = pca.fit_transform(scaled_data)
        centroids_2d = pca.transform(centroids)
        images_base64 = viz.plot_clusters(reduced_data, centroids_2d, labels)
        return JSONResponse(content={"image": images_base64})
    except Exception as e:
        print("Error in /kmeansPlot")
        return JSONResponse(content={"error": str(e)}, status_code=500)

# # Comparing cluster assignments to the outcome variable
# comparison = pd.crosstab(orig_df['Cluster'], orig_df['Outcome'], rownames=['Cluster'], colnames=['Actual Outcome'])
# print(comparison)

# # KNN
@app.get('/KNN')
def getKNN():
    try:
        df = get_cleaned_df()
        X = df.drop(columns=['Outcome'])
        y = df['Outcome']
        X_scaled_data = dp.data_scale(df)
        accuracies, X_train, X_test, y_train, y_test = clas.run_knn(X_scaled_data, y)

        # Training final model with best k
        best_k = 1 + accuracies.index(max(accuracies))
        knn = KNeighborsClassifier(n_neighbors=best_k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)

        # Convert to list for JSON serialization
        y_pred_list = y_pred.tolist()
        y_test_list = y_test.tolist()

        # Base64 image
        image_base64 = viz.plot_knn(accuracies)
        return JSONResponse(content={
            'image': image_base64,
            'y_pred': y_pred_list,
            'y_test': y_test_list
        })
    except Exception as e:
        print("Error in KNN")
        return JSONResponse(content={'message': str(e)}, status_code=500)
    

# # Plot accuracy vs k
# viz.plot_knn(accuracies)

# most_accurate_k = 12
# knn = KNeighborsClassifier(n_neighbors=most_accurate_k)
# knn.fit(X_train, y_train)

# y_pred = knn.predict(X_test)

# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# print("\nClassification Report:\n", classification_report(y_test, y_pred))