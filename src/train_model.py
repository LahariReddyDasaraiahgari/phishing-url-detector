from pathlib import Path

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# File paths
INPUT_PATH = Path("dataset/features.csv")
MODEL_PATH = Path("model/phishing_url_model.pkl")


# Load the feature dataset
df = pd.read_csv(INPUT_PATH)

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)


# Separate features (X) and target (y)
X = df.drop("label", axis=1)
y = df["label"]


print("\nFeatures used for training:")
print(X.columns.tolist())


# Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# Create the Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)


# Train the model
print("\nTraining Random Forest model...")
model.fit(X_train, y_train)

print("Model training completed!")


# Make predictions on the test data
y_pred = model.predict(X_test)


# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy:.4f}")


# Display classification report
print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Legitimate", "Phishing"]
))


# Display confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# Save the trained model
MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

joblib.dump(model, MODEL_PATH)

print("\nModel saved successfully!")
print("Saved to:", MODEL_PATH)