import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import sys


# --------------------------------------------------
# Find the src folder
# --------------------------------------------------

sys.path.append(str(Path(__file__).parent / "src"))

from feature_extraction import extract_features


# --------------------------------------------------
# Load trained model
# --------------------------------------------------

MODEL_PATH = Path("model/phishing_url_model.pkl")

model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🛡️",
    layout="centered"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🛡️ Phishing URL Detector")

st.write(
    "A machine learning system that analyzes URL characteristics "
    "and predicts whether a URL is likely to be legitimate or phishing."
)

st.divider()


# --------------------------------------------------
# Model information
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Dataset", "235K+ URLs")

with col2:
    st.metric("Features", "11")

with col3:
    st.metric("Model", "Decision Tree")


st.divider()


# --------------------------------------------------
# URL input
# --------------------------------------------------

st.subheader("🔎 Check a URL")

url = st.text_input(
    "Enter website URL",
    placeholder="https://example.com"
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("🔍 Analyze URL", use_container_width=True):

    if not url.strip():

        st.warning("Please enter a URL first.")

    else:

        # Extract URL features
        features = extract_features(url)

        # Convert features into DataFrame
        feature_df = pd.DataFrame([features])

        # Make prediction
        prediction = model.predict(feature_df)[0]

        # Get model probabilities
        probabilities = model.predict_proba(feature_df)[0]

        confidence = probabilities[prediction] * 100


        st.divider()


        # --------------------------------------------------
        # Prediction result
        # --------------------------------------------------

        st.subheader("📊 Detection Result")

        if prediction == 1:

            st.error(
                "🚨 PHISHING URL DETECTED"
            )

            st.write(
                "The machine learning model classified this URL "
                "as likely phishing."
            )

        else:

            st.success(
                "✅ LEGITIMATE URL"
            )

            st.write(
                "The machine learning model classified this URL "
                "as likely legitimate."
            )


        st.metric(
            "Model Confidence",
            f"{confidence:.2f}%"
        )


        # --------------------------------------------------
        # Feature analysis
        # --------------------------------------------------

        st.subheader("🔍 URL Feature Analysis")

        feature_display = pd.DataFrame({
            "Feature": feature_df.columns,
            "Value": feature_df.iloc[0].values
        })

        st.dataframe(
            feature_display,
            use_container_width=True,
            hide_index=True
        )


# --------------------------------------------------
# About the project
# --------------------------------------------------

st.divider()

st.subheader("ℹ️ About This Project")

st.write(
    """
    This project uses machine learning to detect potentially phishing
    URLs based on characteristics such as URL length, number of dots,
    suspicious words, IP addresses, HTTPS usage, and subdomains.
    """
)

st.write(
    "**Final Model:** Decision Tree  \n"
    "**Dataset:** 235,370 URLs  \n"
    "**Engineered Features:** 11  \n"
    "**Test Accuracy:** 99.49%  \n"
    "**F1 Score:** 99.40%"
)

st.caption(
    "This tool provides a machine-learning prediction and should not "
    "be treated as a definitive security verdict."
)