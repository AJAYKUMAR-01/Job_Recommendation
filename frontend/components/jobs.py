import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

def display_jobs():
    st.title(":rainbow[Recommended Jobs]")
    user_id = st.session_state.get("user_id")
    
    if user_id:
        response = requests.get(f"{BASE_URL}/recommendations/{user_id}")
        if response.status_code == 200:
            jobs = response.json()
            if jobs:
                for job in jobs:
                    st.subheader(f"Role: :blue[**{job['title']}**]")
                    st.subheader(f"Name of the Company: :orange[{job['industry']}]")
                    st.subheader(f"Location: :green[{job['location']}]")
                    st.subheader("Description:")
                    st.write(f"##### {job['description']} ")
                    st.write("---")
            else:
                st.info("No jobs match your skills at the moment.")
        else:
            st.error("Failed to fetch job recommendations. Please try again.")
    else:
        st.warning("You must log in to see job recommendations.")
