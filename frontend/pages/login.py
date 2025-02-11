import streamlit as st
import requests
BASE_URL = "http://127.0.0.1:8000"

st.title(":rainbow[Login]")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

col1, col2 = st.columns([3,1])

m = st.markdown("""
<style>
div[class*="stTextInput"] label p {
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
  font-size: 20px;
  font-weight: 500;
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

with col1:
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
with col2:
    if st.button("Don't have an account"):
        st.switch_page("pages/signup.py")
