from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def get_inertia(scaled_data):
    inertia = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(scaled_data)
        inertia.append(kmeans.inertia_)
    return inertia

def get_sil_scores(scaled_data):
    sil_scores = []
    for k in range(2, 11):
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(scaled_data)
        score = silhouette_score(scaled_data, labels)
        sil_scores.append(score)
    return sil_scores

def run_Kmeans(scaled_data):
    kmeans = KMeans(n_clusters=2, random_state=1)
    kmeans.fit(scaled_data)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    return labels, centroids