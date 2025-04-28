import whois
import datetime
import streamlit as st
from urllib.parse import urlparse

def domain_age_checker():
    st.subheader("🌐 Domain Age Checker")
    url = st.text_input("Enter the domain or URL to check its age:")

    if st.button("Check Domain Age"):
        try:
            # Extract only the domain part if full URL is given
            domain = urlparse(url).netloc or url
            domain = domain.replace("www.", "")  # remove www if present

            domain_info = whois.whois(domain)
            creation_date = domain_info.creation_date

            if isinstance(creation_date, list):
                creation_date = creation_date[0]

            age = (datetime.datetime.now() - creation_date).days // 365
            st.success(f"The domain **{domain}** is {age} years old. 🎉")
        except Exception as e:
            st.error(f"Error retrieving information for domain {url}: {str(e)}")
