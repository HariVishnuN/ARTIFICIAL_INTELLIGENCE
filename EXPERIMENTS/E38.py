from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Generate synthetic binary dataset
X, y = make_classification(n_samples=100, n_features=4, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Implement Support Vector Classifier
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

predictions = svm_model.predict(X_test)
print(classification_report(y_test, predictions))
