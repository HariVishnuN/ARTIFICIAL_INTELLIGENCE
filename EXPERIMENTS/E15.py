from sklearn.tree import DecisionTreeClassifier
if __name__ == "__main__":
    n = int(input("Enter number of training samples: "))
    f = int(input("Enter number of features per sample: "))
    X, y = [], []
    for i in range(n):
        X.append(list(map(float, input(f"Features for sample {i+1} (space separated): ").split())))
        y.append(input(f"Class for sample {i+1}: "))
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    test = list(map(float, input("Enter features for a test sample: ").split()))
    print("Predicted Class:", clf.predict([test])[0])