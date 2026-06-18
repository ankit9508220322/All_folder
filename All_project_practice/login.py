import streamlit as st
import json
import os

st.set_page_config(page_title="Login & Registration")

FILE_NAME = "users.json"


def user_info():

    # ---------------- FILE CREATE ----------------
    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w") as f:
            json.dump({}, f, indent=4)

    # ---------------- LOAD USERS ----------------
    with open(FILE_NAME, "r") as f:
        users = json.load(f)

    # ---------------- SESSION STATE ----------------
    if "page" not in st.session_state:
        st.session_state.page = "Register"

    # REGISTER PAGE
    if st.session_state.page == "Register":
        st.title("User Registration")

        name = st.text_input("Enter Name")
        email = st.text_input("Enter Email")
        password = st.text_input("Enter Password", type="password")

        if st.button("Register"):

            # Email already exists
            if email in users:
                st.error("Email already registered")

            else:

                users[email] = {
                    "name": name,
                    "password": password
                }

                with open(FILE_NAME, "w") as f:
                    json.dump(users, f, indent=4)

                st.success("Registration Successful")

                # Direct move to login page
                st.session_state.page = "Login"

                st.rerun()
    # LOGIN PAGE

    elif st.session_state.page == "Login":

        st.title("User Login")

        email = st.text_input("Enter Email")
        password = st.text_input("Enter Password", type="password")

        if st.button("Login"):

            # Email check
            if email not in users:
                st.error("Email not registered")

            else:

                # Password check
                if users[email]["password"] == password:

                    st.success(f"Welcome {users[email]['name']}")

                else:
                    st.error("Wrong Password")

        # Back to Register
        if st.button("Go To Register"):

            st.session_state.page = "Register"

            st.rerun()
user_info()