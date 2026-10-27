import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import sys
from urllib.parse import urlparse


# --------------------------------------------------
# Find project files
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "phishing_url_model.pkl"

SRC_DIR = BASE_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from feature_extraction import extract_features


# --------------------------------------------------
# Load trained model
# --------------------------------------------------

if not MODEL_PATH.exists():
    st.error("The trained model file was not found.")
    st.info("Check that model/phishing_url_model.pkl exists.")
    st.stop()

model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Phishing URL Detector")

st.write(
    "A machine learning tool that analyzes URL characteristics "
    "and predicts whether a URL is likely to be legitimate or phishing."
)

st.caption(
    "Educational tool only. A prediction does not guarantee that "
    "a website is safe or malicious."
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


def is_valid_url(value):
    """Check for a basic, well-formed web URL."""
    value = value.strip()

    if not value or any(char.isspace() for char in value):
        return False

    candidate = value if "://" in value else "https://" + value

    try:
        parsed = urlparse(candidate)
        hostname = parsed.hostname

        return (
            parsed.scheme in ("http", "https")
            and hostname is not None
            and "." in hostname
            and not hostname.startswith(".")
            and not hostname.endswith(".")
        )
    except ValueError:
        return False


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("🔍 Analyze URL", use_container_width=True):

    if not url.strip():
        st.warning("Please enter a URL first.")

    elif not is_valid_url(url):
        st.warning(
            "Please enter a valid web address, such as "
            "https://example.com."
        )

    else:
        try:
            features = extract_features(url.strip())
            feature_df = pd.DataFrame([features])

            prediction = model.predict(feature_df)[0]
            probabilities = model.predict_proba(feature_df)[0]
            estimated_probability = probabilities[prediction] * 100

            st.divider()
            st.subheader("📊 Detection Result")

            if prediction == 1:
                st.error("🚨 LIKELY PHISHING")
                st.write(
                    "The model classified this URL as likely phishing. "
                    "Avoid entering sensitive information unless you "
                    "have independently verified the website."
                )
            else:
                st.success("✅ CLASSIFIED AS LIKELY LEGITIMATE")
                st.write(
                    "The model classified this URL as likely legitimate. "
                    "This does not guarantee that the website is safe."
                )

            st.metric(
                "Model Probability for This Prediction",
                f"{estimated_probability:.2f}%"
            )

            st.caption(
                "This percentage is the model's estimated probability "
                "for its predicted class, not a guarantee of correctness."
            )

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

        except Exception:
            st.error(
                "The URL could not be analyzed. Please check the input "
                "and try again."
            )


# --------------------------------------------------
# About the project
# --------------------------------------------------

st.divider()
st.subheader("ℹ️ About This Project")

st.write(
    "This project uses machine learning to analyze URL characteristics "
    "such as URL length, dots, suspicious words, IP-address patterns, "
    "HTTPS usage, and subdomains."
)

st.write(
    "**Final Model:** Decision Tree  \n"
    "**Dataset:** 235,370 URLs  \n"
    "**Engineered Features:** 11  \n"
    "**Reported Test Accuracy:** 99.49%  \n"
    "**Reported F1 Score:** 99.40%"
)

st.caption(
    "This tool provides a machine-learning prediction and should not "
    "be treated as a definitive security verdict."
)
