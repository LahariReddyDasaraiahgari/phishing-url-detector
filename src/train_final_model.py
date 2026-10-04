from pathlib import Path

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# File paths
INPUT_PATH = Path("dataset/features.csv")
MODEL_PATH = Path("model/phishing_url_model.pkl")


# Load the feature dataset
df = pd.read_csv(INPUT_PATH)

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)


# Separate features and target
X = df.drop("label", axis=1)
y = df["label"]


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# Create the final Decision Tree model
model = DecisionTreeClassifier(
    random_state=42
)


# Train the model
print("\nTraining final Decision Tree model...")

model.fit(X_train, y_train)

print("Training completed!")


# Make predictions
y_pred = model.predict(X_test)


# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nFinal Model Accuracy:")
print(f"{accuracy:.4f}")


# Classification report
print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Legitimate", "Phishing"]
    )
)


# Confusion matrix
print("\nConfusion Matrix:")

print(confusion_matrix(y_test, y_pred))


# Create model directory if it doesn't exist
MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)


# Save the final trained model
joblib.dump(model, MODEL_PATH)

print("\nFinal model saved successfully!")
print("Saved to:", MODEL_PATH)