import numpy as np
from collections import Counter
X_train = np.array([[1, 2], [2, 3], [3, 1], [6, 5], [7, 8], [8, 6]])
y_train = np.array([0, 0, 0, 1, 1, 1])  # Binary Classes: 0 or 1
def knn_classify(sample, X, y, k=3):
    distances = [np.sqrt(np.sum((sample - x) ** 2)) for x in X]
    k_indices = np.argsort(distances)[:k]
    k_labels = [y[i] for i in k_indices]
    return Counter(k_labels).most_common(1)[0][0]
new_sample = np.array([2, 2])
prediction = knn_classify(new_sample, X_train, y_train, k=3)
print(f"Predicted Class for sample {new_sample}: {prediction}")
