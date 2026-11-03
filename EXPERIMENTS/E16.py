from sklearn.neural_network import MLPClassifier
if __name__ == "__main__":
    n = int(input("Enter number of training samples: "))
    f = int(input("Enter number of features per sample: "))
    X, y = [], []
    for i in range(n):
        X.append(list(map(float, input(f"Features for sample {i+1} (space separated): ").split())))
        y.append(input(f"Class for sample {i+1}: "))
    mlp = MLPClassifier(hidden_layer_sizes=(5,), max_iter=1000)
    mlp.fit(X, y)
    test = list(map(float, input("Enter features for a test sample: ").split()))
    print("Predicted Class:", mlp.predict([test])[0])