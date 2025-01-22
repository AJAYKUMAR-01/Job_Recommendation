import streamlit as st
import requests
BASE_URL = "http://127.0.0.1:8000"

def display_jobs():
    st.subheader("Recommended Jobs")
    user_id = st.session_state.get("user_id")
    if user_id:
        response = requests.get(f"{BASE_URL}/recommendations/{user_id}")
        if response.status_code == 200:
            jobs = response.json()
            for job in jobs:
                st.write(f"**{job['title']}**")
                st.write(f"Location: {job['location']}")
                st.write(f"Industry: {job['industry']}")
                st.write("---")
        else:
            st.error("Failed to fetch jobs. Please try again.")
    else:
        st.warning("You must be logged in to see job recommendations.")
