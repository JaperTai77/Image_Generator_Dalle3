import hmac
import streamlit as st

def check_password():
    st.header("")
    def password_entered():
        if hmac.compare_digest(st.session_state["password"], st.secrets["adminpassword"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return True
    
    st.text_input(
        "Enter Password 🚀", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("Password incorrect 😕")
    return False