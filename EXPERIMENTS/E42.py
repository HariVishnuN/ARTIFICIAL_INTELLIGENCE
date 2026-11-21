import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score


def main():
    X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.8, random_state=42)

    k = 4
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = kmeans.fit_predict(X)

    score = silhouette_score(X, labels)
    print(f"Number of clusters (K): {k}")
    print(f"Inertia (WCSS): {kmeans.inertia_:.4f}")
    print(f"Silhouette Score: {score:.4f}")
    print("Cluster Centers:\n", np.round(kmeans.cluster_centers_, 3))
    print("Samples per cluster:", np.bincount(labels))


if __name__ == "__main__":
    main()