import numpy as np
from sklearn.decomposition import PCA

# Matrix representing 5 samples with 4 structural features
X = np.array([
    [2.5, 2.4, 3.1, 4.0],
    [0.5, 0.7, 0.2, 1.1],
    [2.2, 2.9, 3.0, 3.8],
    [1.9, 2.2, 2.0, 2.9],
    [3.1, 3.0, 3.5, 4.4]
])

print(f"Original shape: {X.shape}")

# Reduce dimensions from 4 components down to 2 principal components
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print(f"Reduced shape: {X_reduced.shape}")
print("Explained Variance Ratio:", pca.explained_variance_ratio_)
print("Transformed Data:\n", X_reduced)
