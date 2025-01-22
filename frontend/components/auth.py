import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

def login_or_signup():
    # Choose between Login and Signup
    choice = st.radio("Choose Action", ["Login", "Signup"])
    
    if choice == "Login":
        st.subheader("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            response = requests.post(f"{BASE_URL}/login/", json={"email": email, "password": password})
            if response.status_code == 200:
                user_data = response.json()
                st.session_state["logged_in"] = True
                st.session_state["user_id"] = user_data["id"]
                st.success(f"Welcome {user_data['name']}!")
                st.rerun()
            else:
                st.error("Invalid credentials. Please try again.")

    elif choice == "Signup":
        st.subheader("Signup")
        name = st.text_input("Name")
        email = st.text_input("Email")
        role = st.text_input("Role")
        location = st.text_input("Location")
        password = st.text_input("Password", type="password")
        
        # Multiselect box for skills
        skills = st.multiselect(
            "Select Your Skills",
            ["Python", "SQL", "FastAPI", "Streamlit", "JavaScript", "React", "Machine Learning", "DevOps", "UI/UX"],
        )
        
        if st.button("Signup"):
            if not all([name, email, role, location, password, skills]):
                st.error("Please fill in all the details")
            else:
                response = requests.post(f"{BASE_URL}/signup/", json={
                    "name": name,
                    "email": email,
                    "role": role,
                    "location": location,
                    "password": password,
                    "skills": skills
                })
                if response.status_code == 200:
                    st.success("Signup successful! Please log in.")
                    st.rerun()
                else:
                    st.error("Signup failed. Please try again.")
