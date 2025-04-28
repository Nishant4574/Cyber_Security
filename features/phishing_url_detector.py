import re
import streamlit as st
from urllib.parse import urlparse

BLACKLIST = ["phishingsite.com", "fakebanklogin.com"]

def phishing_url_detector():
    st.title("🔍 Phishing URL Detector")

    url = st.text_input("Enter a URL to check:")

    if url:
        if is_blacklisted(url):
            st.error("This URL is blacklisted as a phishing site!")
            return
        
        if suspicious_structure(url):
            st.warning("This URL has a suspicious structure!")
            return
        
        if not url.startswith("https://"):
            st.warning("Warning: This URL does not use HTTPS.")
            return
        
        st.success("This URL seems safe.")
    else:
        st.info("Please enter a URL to check.")

def is_blacklisted(url):
    domain = urlparse(url).netloc
    return domain in BLACKLIST

def suspicious_structure(url):
    if len(url) > 80:
        return True

    suspicious_patterns = [r"%[0-9a-f]{2}", r"\?[^=]*="]
    for pattern in suspicious_patterns:
        if re.search(pattern, url):
            return True

    if "login" in url or "update" in url:
        return True
    
    return False
