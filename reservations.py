import streamlit as st
from sqlalchemy import text 

st.title("State Spaces :material/location_city:")

st.header("Reservations")
conn = st.connection("postgresql", type="sql")

if st.button("Create Reservation"):
    st.write("Creating reservation...")

# fetching data from db
query = "SELECT * FROM users;"  # postgres query

# displaying as dataframe
df = conn.query(query, ttl="5s")
st.table(df)
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

if st.button("Back"):
    st.switch_page("select_venue.py")
