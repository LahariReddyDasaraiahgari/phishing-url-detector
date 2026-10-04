# 🛡️ Phishing URL Detection System

A Machine Learning based cybersecurity project that detects whether a website URL is likely to be **legitimate or phishing** by analyzing URL-based security features.

## 📌 Project Overview

Phishing attacks are one of the most common cybersecurity threats. Attackers create fake websites that look similar to legitimate websites and use them to steal sensitive information such as usernames, passwords and banking details.

This project uses Machine Learning to analyze the structure and characteristics of a URL and classify it as:

- ✅ Legitimate
- 🚨 Phishing

The system also provides a simple Streamlit web interface where users can enter a URL and receive a prediction.

---

## 🎯 Objectives

- Detect potentially phishing URLs using Machine Learning.
- Extract meaningful security-related features from URLs.
- Compare different Machine Learning algorithms.
- Select the best-performing model.
- Build a simple web interface for real-time prediction.
- Create an explainable cybersecurity project suitable for practical use.

---

## 🏗️ System Architecture

```text
User enters URL
       ↓
Feature Extraction
       ↓
URL Security Features
       ↓
Trained Decision Tree Model
       ↓
Prediction
       ↓
Legitimate / Phishing