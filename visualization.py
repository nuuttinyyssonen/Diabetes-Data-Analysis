import math
import matplotlib.pyplot as plt

# We use this to visualize each column to identify potential outliers and 0 values in data.
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

def plot_elbow(inertia):
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, 11), inertia, marker='o')
    plt.title('Elbow Method for Optimal k')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Inertia (SSE)')
    plt.grid(True)
    plt.show()

def plot_silhouette(sil_scores):
    plt.plot(range(2, 11), sil_scores, marker='o')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Analysis For Optimal k')
    plt.grid(True)
    plt.show()

def plot_clusters(reduced_data, centroids_2d, labels):
    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=labels, cmap='viridis', alpha=0.6)
    plt.scatter(centroids_2d[:, 0], centroids_2d[:, 1], c='red', marker='X', s=200, label='Centroids')
    plt.title('Patients colored by cluster (PCA projection)')
    plt.xlabel('PCA 1')
    plt.ylabel('PCA 2')
    plt.show()

def plot_knn(accuracies):
    plt.plot(range(1, 21), accuracies, marker='o')
    plt.title("KNN Accuracy for different k values")
    plt.xlabel("k (Number of Neighbors)")
    plt.ylabel("Accuracy")
    plt.show()