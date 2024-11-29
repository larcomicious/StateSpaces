import streamlit as st
from sqlalchemy import text

col1, col2 = st.columns([0.8,0.2])
col1.title("State Spaces :material/location_city:")
if col2.button("Change User"):
    st.switch_page("change_user.py")

st.header("Make Reservation")
conn = st.connection("postgresql", type="sql")

# venu details
venue_id = st.session_state.get("selected_venue")
venue_query = f"SELECT venue_id, venue_name, capacity, floor_area FROM venue WHERE venue_id = {venue_id};"
venue_info = conn.query(venue_query)

venue_name = venue_info["venue_name"][0]
capacity = venue_info["capacity"][0]
floor_area = venue_info["floor_area"][0]

venue_cont = st.container()
with venue_cont:
    st.header(venue_name)
    st.write(f":material/person: {capacity}")
    st.write(f"Floor Area: {floor_area} sqm")


# customer details
st.write("### Customer Details")
customer_cont = st.container(border=True)
# with customer_cont:
#     # col1, col2 = st.columns([0.7,0.3])
#     # customer_name = col1.text_input("Name")
#     # birth_date = col2.date_input("Birth Date")
#     # contact_no = st.text_input("Contact No.")
#     customer_id = st.text_input("Customer ID")

# reserv details
st.write("### Reservation Details")
reservation_cont = st.container(border=True)
with reservation_cont:
    col1, col2 = st.columns([1,1])
    date_from = col1.date_input("Date From")
    time_from = col1.time_input("Time From")
    date_to = col2.date_input("Date To")
    time_to = col2.time_input("Time To")
    number_of_participants = st.number_input("No. of Participants", min_value=0, max_value=capacity, step=1)

reserved_from = str(date_from)+' '+str(time_from)
reserved_to = str(date_from)+' '+str(time_from)

# st.write(reserved_from)
# st.write(reserved_to)

# def is_available():
#     query = f"SELECT reserved_from, reserved_to FROM reservation WHERE venue_id = {venue_id};"
#     query_info = conn.query(query)
#     for i, row in query_info.iterrows(): # for column, row
#         dt_from = row["reserved_from"]
#         dt_to = row["reserved_to"]

# query = f"SELECT reserved_from, reserved_to FROM reservation WHERE venue_id = {venue_id};"
# query_info = conn.query(query)
# for i, row in query_info.iterrows(): # for column, row
#     dt_from = row["reserved_from"]
#     dt_to = row["reserved_to"]
#     st.write(dt_from)
#     st.write(dt_to)

if st.button("Make Reservation"):
    # check if available
    check_query = f"SELECT EXISTS(SELECT 1 FROM reservation WHERE venue_id = {venue_id} AND ('{reserved_from}' < reserved_to AND '{reserved_to}' > reserved_from));"
    check_reserv = conn.query(check_query)
    st.write(check_reserv)
    # insert data into table
    # insert_query = text("INSERT INTO users (name, age, email) VALUES (:name, :age, :email);")
    # with conn.session as session:
    #     session.execute(insert_query, params={"name": name, "age": age, "email":email})
    #     session.commit()
    # st.success(f"User {name} added successfully!")

if st.button("Back to Venues"):
    st.switch_page("select_venue.py")
