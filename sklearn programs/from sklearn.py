from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Synthetic dataset: height, weight, BMI class (underweight, normal)
data = [
    [150, 45, 'underweight'],
    [160, 60, 'normal'],
    [170, 70, 'normal'],
    [155, 50, 'underweight'],
    [180, 80, 'normal'],
    [165, 55, 'normal'],
    [175, 65, 'normal'],
    [140, 40, 'underweight'],
    [190, 85, 'normal'],
]

# Split dataset into features (X) and labels (y)
X = [[row[0], row[1]] for row in data]
y = [row[2] for row in data]
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Synthetic dataset: height, weight, BMI class (underweight, normal)
data = [
    [150, 45, 'underweight'],
    [160, 60, 'normal'],
    [170, 70, 'normal'],
    [155, 50, 'underweight'],
    [180, 80, 'normal'],
    [165, 55, 'normal'],
    [175, 65, 'normal'],
    [140, 40, 'underweight'],
    [190, 85, 'normal'],
]

# Split dataset into features (X) and labels (y)
X = [[row[0], row[1]] for row in data]
y = [row[2] for row in data]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create K-NN classifier with k=3
knn_classifier = KNeighborsClassifier(n_neighbors=3)

# Train the classifier on the training data
knn_classifier.fit(X_train, y_train)

# Make predictions on the test data
predictions = knn_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy * 100:.2f}%")

# Example prediction
example_height = 170
example_weight = 75
example_data = [[example_height, example_weight]]
predicted_class = knn_classifier.predict(example_data)

print(f"Predicted BMI class for height {example_height} and weight {example_weight}: {predicted_class[0]}")

