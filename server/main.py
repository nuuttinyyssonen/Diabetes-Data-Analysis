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
from fastapi.staticfiles import StaticFiles
from pathlib import Path

import os

app = FastAPI()

# Get allowed origins from environment, or use defaults for local development
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,http://localhost:8000").split(",")
# Strip whitespace from origins
allowed_origins = [origin.strip() for origin in allowed_origins]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
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

# Cache the cleaned dataframe at startup to avoid reprocessing on every request
print("Pre-processing and caching cleaned dataframe...")
cached_cleaned_df = get_cleaned_df()
cached_scaled_data = dp.data_scale(cached_cleaned_df)
print("Cache complete!")

@app.get('/startingColumns')
def get_starting_columns():
    try:
        image_base64 = viz.plot_histograms(orig_df, ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        print("Error in /startingColumns:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get('/columnsWithoutZeros')
def zeroValuesRemoved():
    try:
        df = dp.handle_zeros(orig_df.copy())
        image_base64 = viz.plot_histograms(df, ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI'])
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        print("Error in /zeroValuesRemoved:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get('/columnsWithoutOutliers')
def outliersRemoved():
    try:
        # Use cached cleaned dataframe instead of reprocessing
        image_base64 = viz.plot_histograms(cached_cleaned_df, ['SkinThickness', 'BloodPressure', 'Insulin', 'BMI'])
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        print("Error in /outliersRemoved:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.get('/correlationHeatMap')
def correlationHeatMap():
    try:
        # Use cached cleaned dataframe
        image_base64 = viz.plot_correlation_heatmap(cached_cleaned_df)
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        print("Error in /correlationHeatMap:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get('/outcomeDistribution')
def outcomeDistribution():
    try:
        df = orig_df.copy()
        image_base64 = viz.plot_outcome_distribution(df)
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        print("Error in /outcomeDistribution:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get('/elbowMethodPlot')
def get_elbow_method():
    try:
        # Use cached scaled data instead of reprocessing
        inertia = clus.get_inertia(cached_scaled_data)
        image_base64 = viz.plot_elbow(inertia)
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        print("Error in /elbowMethodPlot:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get('/silhouetteScoresPlot')
def get_silhouette_scores():
    try:
        # Use cached scaled data
        sil_scores = clus.get_sil_scores(cached_scaled_data)
        image_base64 = viz.plot_silhouette(sil_scores)
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        print("Error in /silhouetteScoresPlot:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

# KMeans
@app.get('/kmeansPlot')
def getKmeansPlot():
    try:
        # Use cached scaled data and cleaned dataframe
        labels, centroids = clus.run_Kmeans(cached_scaled_data)
        pca = PCA(n_components=2)
        reduced_data = pca.fit_transform(cached_scaled_data)
        centroids_2d = pca.transform(centroids)
        images_base64 = viz.plot_clusters(reduced_data, centroids_2d, labels)
        return JSONResponse(content={"image": images_base64})
    except Exception as e:
        print("Error in /kmeansPlot:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.get('/clusterOutcomeHeatmap')
def cluster_outcome_heatmap():
    try:
        # Use cached data
        labels, _ = clus.run_Kmeans(cached_scaled_data)
        df = cached_cleaned_df.copy()
        df['Cluster'] = labels + 1
        ct = pd.crosstab(df['Cluster'], df['Outcome'], rownames=['Cluster'], colnames=['Actual Outcome'])
        image_base64 = viz.plot_heatmap(ct)
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        print("Error in /clusterOutcomeHeatmap:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

# KNN
@app.get('/KNN')
def getKNN():
    try:
        # Use cached cleaned dataframe and scaled data
        X = cached_cleaned_df.drop(columns=['Outcome'])
        y = cached_cleaned_df['Outcome']
        accuracies, X_train, X_test, y_train, y_test = clas.run_knn(cached_scaled_data, y)

        # Training final model with best k
        best_k = 1 + accuracies.index(max(accuracies))
        knn = KNeighborsClassifier(n_neighbors=best_k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)

        # Base64 image
        image_base64 = viz.plot_knn(accuracies)
        cm_image_base64 = viz.plot_confusion_matrix(y_test, y_pred)
        return JSONResponse(content={
            'image': image_base64,
            'confusion_matrix': cm_image_base64
        })
    except Exception as e:
        print("Error in KNN:", e)
        return JSONResponse(content={'message': str(e)}, status_code=500)

# Serve static files (React frontend)
static_dir = Path(__file__).parent / "static"
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")