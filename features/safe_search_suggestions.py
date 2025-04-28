import streamlit as st

def safe_search_suggestions():
    st.title("🔒 Safe Search Suggestions")

    st.markdown("""
    **1.** Always check for **HTTPS** (secure connection) before entering sensitive information.  
    **2.** Be cautious when clicking on links in emails or texts.  
    **3.** Use trusted search engines like **Google** or **DuckDuckGo**.  
    **4.** Consider using browser extensions to block ads and pop-ups.  
    """)

    st.info("These tips can help improve your safety while browsing the web.")
