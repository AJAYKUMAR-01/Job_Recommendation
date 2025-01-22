import streamlit as st

BASE_URL = "http://127.0.0.1:8000"

# Initialize session state for user login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["user_id"] = None
    st.session_state["email"] = None

# Adjust the menu based on login state
if st.session_state["logged_in"]:
    menu_options = ["Home", "About", "Jobs", "Visualization", "Logout"]
else:
    menu_options = ["Home", "About", "Login/Signup"]

# Sidebar for navigation
menu = st.sidebar.radio("Navigation", menu_options)

if menu == "Home":
    st.title("Welcome to the Job Recommendation Platform 🎯")
    st.subheader("Your career starts here!")
    st.write("""
        Discover job opportunities tailored to your skills, experience, and preferences. 
        Whether you're looking for your first job or planning your next career move, 
        our platform is here to help you succeed.
    """)
    
    st.markdown("---")
    st.subheader("🌟 Key Features")
    st.write("- **Personalized Job Recommendations**: Get suggestions based on your profile.")
    st.write("- **Advanced Search & Filters**: Find the perfect job with ease.")
    st.write("- **Interactive Visualizations**: Explore connections between jobs, skills, and industries.")
    
    st.markdown("---")
    st.subheader("📖 Getting Started")
    st.write("""
        1. **Sign Up**: Create your profile with details like skills and job preferences.
        2. **Explore**: Check out job recommendations tailored to you.
        3. **Search**: Use filters to find exactly what you're looking for.
    """)
    
    st.markdown("---")
    st.subheader("Ready to start ?")
    
    st.markdown("---")
    st.caption("Empowering careers, one match at a time.")



elif menu == "About":
    st.title("About Us")
    st.write("""
        ### Welcome to the Job Recommendation Platform
        Our platform is designed to help users find job opportunities tailored to their 
        skills, experiences, and preferences. We believe in leveraging technology to 
        bridge the gap between job seekers and the roles they aspire to.

        #### Key Features:
        - Personalized job recommendations based on your profile.
        - Interactive visualizations to explore relationships between jobs, skills, and industries.
        - An intuitive and user-friendly interface.

        #### Our Mission:
        To empower individuals by connecting them with the best career opportunities 
        and helping them grow professionally.

        #### Contact Us:
        - Email: support@jobrecommendation.com
        - Phone: +1-800-123-4567
        - Address: 123 Job Lane, Career City, Workland

        Thank you for choosing our platform. Together, let's build your career!
    """)

elif menu == "Jobs":
    if st.session_state["logged_in"]:
        st.title("Job Recommendations")
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
