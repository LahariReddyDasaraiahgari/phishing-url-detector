from pathlib import Path
import pandas as pd

from feature_extraction import extract_features


# Input and output file paths
INPUT_PATH = Path("dataset/phishing_urls.csv")
OUTPUT_PATH = Path("dataset/features.csv")


# Load the cleaned URL dataset
df = pd.read_csv(INPUT_PATH)

print("Dataset loaded successfully!")
print("Number of URLs:", len(df))


# Extract features from every URL
feature_rows = []

for url in df["URL"]:
    features = extract_features(url)
    feature_rows.append(features)


# Convert extracted features into a DataFrame
features_df = pd.DataFrame(feature_rows)


# Add the original label
features_df["label"] = df["label"].values


# Save the feature dataset
features_df.to_csv(OUTPUT_PATH, index=False)


print("\nFeature extraction completed!")
print("Feature dataset saved to:", OUTPUT_PATH)

print("\nFeature dataset shape:")
print(features_df.shape)

print("\nFeatures:")
print(features_df.columns.tolist())

print("\nFirst 5 rows:")
print(features_df.head())

print("\nClass distribution:")
print(features_df["label"].value_counts())