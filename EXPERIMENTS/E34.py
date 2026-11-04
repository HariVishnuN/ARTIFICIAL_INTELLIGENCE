import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Hides unnecessary TensorFlow startup logs

import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Load and preprocess the MNIST dataset (handwritten digits 0-9)
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalize pixel values to be between 0 and 1
X_train, X_test = X_train / 255.0, X_test / 255.0

# 2. Build the Neural Network Model
model = models.Sequential([
    layers.Input(shape=(28, 28)),          # Modern input layer shape definition
    layers.Flatten(),                      # Flatten 28x28 images into a 784-element vector
    layers.Dense(128, activation='relu'),  # Hidden layer with ReLU activation
    layers.Dropout(0.2),                   # Dropout layer for regularization to prevent overfitting
    layers.Dense(10, activation='softmax') # Output layer with 10 classes (digits 0-9)
])

# 3. Compile the Model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 4. Train the Model
print("Training the model...")
model.fit(X_train, y_train, epochs=5, batch_size=64)

# 5. Evaluate the Model on Test Data
print("\nEvaluating the model...")
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f"\nFinal Test Accuracy: {test_acc:.4f}")