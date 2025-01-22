import streamlit as st

BASE_URL = "http://127.0.0.1:8000"

# Initialize session state for user login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["user_id"] = None

# Adjust the menu based on login state
if st.session_state["logged_in"]:
    menu_options = ["Home", "About", "Jobs", "Visualization", "Logout"]
else:
    menu_options = ["Home", "About", "Login/Signup"]

# Sidebar for navigation
menu = st.sidebar.radio("Navigation", menu_options)

if menu == "Home":
    st.title("Announcements")

elif menu == "About":
    st.title("About Us")
    st.write("Welcome to the Job Recommendation Platform! This platform helps users find jobs based on their skills and preferences.")

elif menu == "Jobs":
    if st.session_state["logged_in"]:
        st.title("Job Recommendations")
        st.write("Here are your job recommendations...")
        # Add job-related functionality (fetch jobs via API)
        from components.jobs import display_jobs
        display_jobs()
    else:
        st.warning("Please log in to view job recommendations.")

elif menu == "Login/Signup":
    st.title("Login or Signup")
    from components.auth import login_or_signup
    login_or_signup()

elif menu == "Visualization":
    if st.session_state["logged_in"]:
        st.title("Visualization")
        st.write("Here is a graphical representation of your skills and job matches.")
        from components.visualization import render_visualization
        render_visualization()
    else:
        st.warning("Please log in to access visualizations.")

elif menu == "Logout":
    st.session_state["logged_in"] = False
    st.session_state["user_id"] = None
    st.success("You have been logged out.")
    st.rerun()  # Refresh to show the updated menu
