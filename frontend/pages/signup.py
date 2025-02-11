import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

m = st.markdown("""
<style>
div[class*="stTextInput"] label p {
  font-size: 23px;
}
div[class*="stMultiSelect"] label p {
  font-size: 23px;
}
div.stButton > button:first-child {
  background-image: linear-gradient(#42A1EC, #0070C9);
  border: 1px solid #0077CC;
  border-radius: 4px;
  box-sizing: border-box;
  color: #FFFFFF;
  cursor: pointer;
  direction: ltr;
  display: block;
  font-family: "SF Pro Text","SF Pro Icons","AOS Icons","Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size: 19px;
  font-weight: 400;
  letter-spacing: -.022em;
  line-height: 1.47059;
  min-width: 30px;
  overflow: visible;
  padding: 4px 15px;
  text-align: center;
  vertical-align: baseline;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  white-space: nowrap;
}
</style>""", unsafe_allow_html=True)

st.title(":rainbow[Signup]")
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

col1, col2 = st.columns([3,1])

with col1:
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
            st.switch_page("pages/login.py")
        else:
            st.error("Signup failed. Please try again.")
with col2:
   if st.button("Already have an Account"):
      st.switch_page("pages/login.py")