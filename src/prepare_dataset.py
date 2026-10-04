from ucimlrepo import fetch_ucirepo
import pandas as pd
from pathlib import Path


# Download the PhiUSIIL dataset from UCI
dataset = fetch_ucirepo(id=967)

# Get the feature data and target labels
features = dataset.data.features
target = dataset.data.targets

# Combine them into one DataFrame
df = pd.concat([features, target], axis=1)

# Keep only the raw URL and original label
df = df[["URL", "label"]]

# Remove duplicate URLs
df = df.drop_duplicates(subset="URL")

# Remove rows with missing URLs or labels
df = df.dropna(subset=["URL", "label"])

# Convert UCI labels:
# UCI: 1 = legitimate, 0 = phishing
# Our project: 0 = legitimate, 1 = phishing
df["label"] = df["label"].map({
    1: 0,
    0: 1
})

# Create dataset folder if it does not exist
output_path = Path("dataset/phishing_urls.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Save our cleaned dataset
df.to_csv(output_path, index=False)

print("Dataset prepared successfully!")
print("Number of URLs:", len(df))
print("\nClass distribution:")
print(df["label"].value_counts())

print("\nFirst 5 rows:")
print(df.head())