import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"  # Backend API URL

def login_or_signup():
    # Choose between Login and Signup
    choice = st.radio("Choose Action", ["Login", "Signup"])
    
    if choice == "Login":
        st.subheader("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            # Simulate login API request
            response = requests.post(f"{BASE_URL}/login/", json={"email": email, "password": password})
            if response.status_code == 200:
                user_data = response.json()
                st.session_state["logged_in"] = True
                st.session_state["user_id"] = user_data["id"]
                st.success("Login successful!")
                st.rerun()  # Redirect to the Home page
            else:
                st.error("Invalid credentials. Please try again.")

    elif choice == "Signup":
        st.subheader("Signup")
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        
        if st.button("Signup"):
            # Simulate signup API request
            response = requests.post(f"{BASE_URL}/signup/", json={"name": name, "email": email, "password": password})
            if response.status_code == 201:
                st.success("Signup successful! Please log in.")
                st.rerun()  # Redirect to the Home page
            else:
                st.error("Signup failed. Please try again.")
