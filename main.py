import streamlit as st
from sqlalchemy.sql import text
import pandas as pd


st.title("State Spaces")

menu = ["View Users", "Add User"]
choice = st.sidebar.selectbox("Menu", menu)

# connecting to postgres db
conn = st.connection("postgresql", type="sql")

if choice == "View Users":
    st.subheader("User List")

    # fetching data from db
    query = "SELECT * FROM users;"  # postgres query

    # displaying as dataframe
    df = conn.query(query, ttl="5s")
    st.dataframe(df)


elif choice == "Add User":
    st.subheader("Add New User")

    # user input
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, step=1)
    email = st.text_input("Email")

    if st.button("Add User"):
        # insert data into table
        insert_query = text("INSERT INTO users (name, age, email) VALUES (:name, :age, :email);")
        with conn.session as session:
            session.execute(insert_query, params={"name": name, "age": age, "email":email})
            session.commit()
        st.success(f"User {name} added successfully!")

