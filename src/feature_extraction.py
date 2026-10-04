from urllib.parse import urlparse
import re


SUSPICIOUS_WORDS = [
    "login",
    "verify",
    "verification",
    "account",
    "secure",
    "update",
    "signin",
    "confirm",
    "password",
    "bank"
]


def extract_features(url):
    features = {}

    # Basic URL features
    features["url_length"] = len(url)
    features["num_dots"] = url.count(".")
    features["num_hyphens"] = url.count("-")
    features["num_at"] = url.count("@")
    features["num_question"] = url.count("?")
    features["num_equal"] = url.count("=")
    features["num_slashes"] = url.count("/")

    # HTTPS feature
    features["has_https"] = int(url.lower().startswith("https://"))

    # Check whether the URL contains an IP address
    ip_pattern = r"^(?:https?://)?(?:\d{1,3}\.){3}\d{1,3}"

    features["has_ip"] = int(bool(re.search(ip_pattern, url)))

    # Check for suspicious words
    url_lower = url.lower()

    features["has_suspicious_words"] = int(
        any(word in url_lower for word in SUSPICIOUS_WORDS)
    )

    # Count subdomains
    parsed_url = urlparse(url if "://" in url else "http://" + url)

    hostname = parsed_url.hostname or ""

    hostname_parts = hostname.split(".")

    features["num_subdomains"] = max(0, len(hostname_parts) - 2)

    return features
if __name__ == "__main__":
    test_url = "https://example.com/login"

    result = extract_features(test_url)

    print("URL:", test_url)
    print("\nExtracted Features:")

    for feature, value in result.items():
        print(f"{feature}: {value}")