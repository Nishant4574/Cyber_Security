import streamlit as st
from features import phishing_url_detector, domain_age_checker, safe_search_suggestions

st.set_page_config(page_title="Cyber Security Toolkit", page_icon="🛡️", layout="centered")
st.title("🛡️ Cyber Security Toolkit")
st.markdown("A simple app to help you browse the web safely. Choose a feature from the sidebar.")

st.sidebar.title("🧭 Navigation")
feature = st.sidebar.radio("Select a Feature", ("Phishing URL Detector", "Domain Age Checker", "Safe Search Suggestions"))

if feature == "Phishing URL Detector":
    phishing_url_detector.phishing_url_detector()

elif feature == "Domain Age Checker":
    domain_age_checker.domain_age_checker()

elif feature == "Safe Search Suggestions":
    safe_search_suggestions.safe_search_suggestions()
