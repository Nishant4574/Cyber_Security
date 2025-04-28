import whois
import datetime
import streamlit as st

def domain_age_checker():
    st.title("🌐 Domain Age Checker")

    # Get user input for domain
    domain = st.text_input("Enter the domain to check its age:")

    if domain:
        try:
            # Get WHOIS info for the domain
            domain_info = whois.whois(domain)
            creation_date = domain_info.creation_date

            # Handle the case when creation_date is a list
            if isinstance(creation_date, list):
                creation_date = creation_date[0]

            # Calculate the domain age in years
            age = (datetime.datetime.now() - creation_date).days // 365
            st.success(f"The domain **{domain}** is **{age}** years old. 🎉")
        except Exception as e:
            st.error(f"Error retrieving information for domain **{domain}**: {str(e)}")
    else:
        st.info("Please enter a domain to check its age.")
