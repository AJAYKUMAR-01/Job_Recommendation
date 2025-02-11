import streamlit as st

BASE_URL = "http://127.0.0.1:8000"

def visualize():
    if st.session_state["logged_in"]:
        st.title(":rainbow[Visualization]")
        st.subheader("Here is a graphical representation of your :blue[skills] and :blue[job] matches.")
        from components.visualization import render_visualization
        render_visualization()

def jobs():
    from components.jobs import display_jobs
    display_jobs()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["user_id"] = None
    st.session_state["email"] = None


home = st.Page("static_pages/home.py", title="Home", icon=":material/home:")
company_policies = st.Page("static_pages/cmp.py", title="Companies Policies", icon=":material/book:")
tech_news = st.Page("static_pages/news.py", title="Tech News", icon=":material/notification_important:")
login_page = st.Page("pages/login.py", title="Login", icon=":material/login:")
settings = st.Page("pages/settings.py", title="Settings", icon=":material/settings:")
signup = st.Page("pages/signup.py", title="Sign Up", icon=":material/man:")
logout_page = st.Page(logout, title="Log Out", icon=":material/logout:")
jobs = st.Page(jobs, title="Jobs", icon=":material/man:")
visualization = st.Page(visualize, title="Visualize", icon=":material/book:")
if st.session_state["logged_in"]:
    # menu_options = ["Home", "About", "Jobs", "Visualization", "Logout"]
    
    pg = st.navigation(
        {
            "App": [home, jobs, company_policies, tech_news, visualization],
            "Account": [logout_page, settings],
            # "Tools": [search, dashboard],
        }
    )
else:
    # menu_options = [":rainbow[Home]", ":rainbow[About]", ":rainbow[Login/SignUp]"]
    pg = st.navigation(
        {
            "App": [home, company_policies, tech_news],
            "Account": [login_page, signup]
        }
    )

pg.run()




























# Sidebar for navigation
# menu = st.sidebar.radio("MENU", menu_options)

# if menu == ":rainbow[Home]":
    



# elif menu == "About":
#     st.title("About Us")
#     st.write("""
#         ### Welcome to the Job Recommendation Platform
#         Our platform is designed to help users find job opportunities tailored to their 
#         skills, experiences, and preferences. We believe in leveraging technology to 
#         bridge the gap between job seekers and the roles they aspire to.

#         #### Key Features:
#         - Personalized job recommendations based on your profile.
#         - Interactive visualizations to explore relationships between jobs, skills, and industries.
#         - An intuitive and user-friendly interface.

#         #### Our Mission:
#         To empower individuals by connecting them with the best career opportunities 
#         and helping them grow professionally.

#         #### Contact Us:
#         - Email: support@jobrecommendation.com
#         - Phone: +1-800-123-4567
#         - Address: 123 Job Lane, Career City, Workland

#         Thank you for choosing our platform. Together, let's build your career!
#     """)

# elif menu == "Jobs":
#     if st.session_state["logged_in"]:
#         st.title("Job Recommendations")
#         from components.jobs import display_jobs
#         display_jobs()
#     else:
#         st.warning("Please log in to view job recommendations.")


# elif menu == "Login/Signup":
#     st.title("Login or Signup")
#     from components.auth import login_or_signup
#     login_or_signup()

# elif menu == "Visualization":
#     if st.session_state["logged_in"]:
#         st.title("Visualization")
#         st.write("Here is a graphical representation of your skills and job matches.")
#         from components.visualization import render_visualization
#         render_visualization()
#     else:
#         st.warning("Please log in to access visualizations.")

# elif menu == "Logout":
#     st.session_state["logged_in"] = False
#     st.session_state["user_id"] = None
#     st.success("You have been logged out.")
#     st.rerun()  # Refresh to show the updated menu
