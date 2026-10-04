from pathlib import Path

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Load the feature dataset
INPUT_PATH = Path("dataset/features.csv")

df = pd.read_csv(INPUT_PATH)

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)


# Separate features and target
X = df.drop("label", axis=1)
y = df["label"]


# Use the same train-test split for every model
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# Create the models
models = {
    "Logistic Regression": LogisticRegression(
        max_iter=1000
    ),

    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )
}


# Store results
results = []


# Train and evaluate every model
for name, model in models.items():

    print(f"\nTraining {name}...")

    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    })

    print(f"{name} completed!")


# Create results table
results_df = pd.DataFrame(results)

print("\n" + "=" * 70)
print("MODEL COMPARISON")
print("=" * 70)

print(results_df.to_string(index=False))


# Show the model with the highest F1 score
best_model = results_df.loc[
    results_df["F1 Score"].idxmax()
]

print("\nBest model based on F1 Score:")
print(best_model["Model"])