# 🛡️ Phishing URL Detection System

A machine learning cybersecurity project that analyzes URL characteristics and predicts whether a URL is likely to be legitimate or phishing.

## 📌 Project Overview

Phishing websites attempt to trick users into revealing sensitive information, including passwords and banking details.

This project uses a Decision Tree classifier to analyze URL-based features and predict potentially suspicious URLs. A Streamlit web application lets users enter a URL and view the prediction and extracted features.

**Note:** This is an educational tool. Its predictions cannot guarantee that a website is safe or malicious.

## 🎯 Objectives

- Detect potentially phishing URLs using machine learning.
- Extract security-related features from URLs.
- Compare machine learning algorithms.
- Evaluate model performance.
- Build an interactive web application.

## 🏗️ System Architecture

```text
PhiUSIIL Dataset
       ↓
Dataset Preparation
       ↓
URL Feature Extraction
       ↓
Feature Dataset
       ↓
Model Training and Evaluation
       ↓
Trained Decision Tree Model
       ↓
Streamlit Web Application
       ↓
Prediction and Feature Analysis
```

## 🧰 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## 📊 Dataset

The project uses the PhiUSIIL Phishing URL dataset from the UCI Machine Learning Repository.

- **Total URLs:** 235,370
- **Legitimate URLs:** 134,850
- **Phishing URLs:** 100,520
- **Input features:** 11

Labels used in this project:

- `0` — Legitimate
- `1` — Phishing

## 🔍 Features Extracted

The model uses 11 URL characteristics:

1. URL length
2. Number of dots
3. Number of hyphens
4. Number of `@` symbols
5. Number of question marks
6. Number of equal signs
7. Number of slashes
8. HTTPS indicator
9. IP-address pattern indicator
10. Suspicious-word indicator
11. Number of subdomains

These characteristics provide useful signals but do not fully establish whether a website is trustworthy.

## 🤖 Machine Learning Models

The project includes scripts to compare:

- Logistic Regression
- Decision Tree
- Random Forest

The final application uses the Decision Tree model saved in `model/phishing_url_model.pkl`.

## 📈 Model Performance

The current project reports the following results on its held-out test dataset:

| Metric | Result |
|---|---:|
| Decision Tree accuracy | 99.49% |
| F1 score | 99.40% |

Performance on new URLs may differ from these test results.

## 🖥️ Web Application

The application allows users to:

- Enter a URL.
- View the predicted classification.
- View the model's estimated probability for its prediction.
- Inspect the extracted URL features.

HTTPS alone does not guarantee that a website is safe, and the model can make incorrect predictions.

## 📁 Project Structure

```text
phishing-url-detector/
├── dataset/
│   ├── phishing_urls.csv
│   └── features.csv
├── model/
│   └── phishing_url_model.pkl
├── src/
│   ├── compare_models.py
│   ├── create_features.py
│   ├── feature_extraction.py
│   ├── prepare_dataset.py
│   ├── train_final_model.py
│   └── train_model.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/LahariReddyDasaraiahgari/phishing-url-detector.git
cd phishing-url-detector
```

### 2. Create and activate a virtual environment

For Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Run the application

```powershell
python -m streamlit run app.py
```

Open the local URL shown in the terminal.

## 🔒 Limitations

- The model analyzes URL characteristics rather than fully inspecting website content.
- New phishing techniques may not be represented in the dataset.
- Legitimate URLs may be flagged, and phishing URLs may be missed.
- Model probabilities are estimates, not guarantees.
- This tool should not replace browser security warnings or other security checks.

## 👩‍💻 Project Purpose

This project demonstrates dataset preparation, feature engineering, supervised machine learning, model evaluation, and deployment using Streamlit.
