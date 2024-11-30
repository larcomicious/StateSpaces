import streamlit as st
from sqlalchemy import text
import datetime

col1, col2 = st.columns([0.8,0.2])
col1.title("State Spaces :material/location_city:")
if col2.button("Change User"):
    st.switch_page("change_user.py")

st.header("Make Reservation")
conn = st.connection("postgresql", type="sql")

# user id
customer_id = st.session_state.get("user_id")

# venue details
venue_id = st.session_state.get("selected_venue")
venue_query = f"SELECT v.venue_id, v.venue_name, vt.venue_type, v.capacity, v.renovating FROM venue v JOIN venue_type vt ON v.venue_id = vt.venue_id WHERE v.venue_id = {venue_id};"
venue_info = conn.query(venue_query)

venue_name = venue_info["venue_name"][0]
venue_type = venue_info["venue_type"][0]
capacity = venue_info["capacity"][0]
renovating = venue_info["renovating"][0]

venue_cont = st.container()
with venue_cont:
    col1, col2 = st.columns([1,0.6])
    col1.metric(label="Venue Name",value=venue_name)
    col2.metric(label="Venue ID",value=venue_id)
    col1, col2, col3 = st.columns([0.5,1,1])
    col1.metric(label="Capacity :material/person:",value=capacity)
    col2.metric(label="Venue Type",value=venue_type)
    col3.metric(label="Renovating",value=renovating)

# reservation details
st.write("### Reservation Details")
reservation_cont = st.container(border=True)
with reservation_cont:
    col1, col2 = st.columns([1,1])
    date_from = col1.date_input("Date From")
    time_from = col1.time_input("Time From")
    date_to = col2.date_input("Date To")
    time_to = col2.time_input("Time To")
    number_of_participants = st.number_input("No. of Participants", min_value=0, max_value=capacity, step=1)

col1, col2 = st.columns([0.8,0.22])
today = datetime.datetime.today().date()

if col2.button("Make Reservation", disabled=renovating):
    # check for existing reservations of users to venue
    reserv_query = f"SELECT reserved_from, reserved_to FROM reservation WHERE venue_id = {venue_id};"
    reserv_info = conn.query(reserv_query)

    # validation              # multi-day              # single day
    if today <= date_from and ((date_from < date_to) or (date_from == date_to and time_from <= time_to)):
        input_from = datetime.datetime.combine(date_from, time_from)
        input_to = datetime.datetime.combine(date_to, time_to)

        intersect = False # for checking 

        for i, row in reserv_info.iterrows(): # for column, row
            reserved_from = row["reserved_from"]
            reserved_to = row["reserved_to"]

            if input_from <= reserved_to and input_to >= reserved_from: 
                intersect = True
                break 
        
        if not intersect:
            insert_query = text("INSERT INTO reservation (reserved_from, reserved_to, number_of_participants, venue_id, customer_id) VALUES (:reserved_from, :reserved_to, :number_of_participants, :venue_id, :customer_id);")
            with conn.session as session:
                session.execute(insert_query, params={"reserved_from": input_from, "reserved_to": input_to, "number_of_participants": number_of_participants, "venue_id":venue_id, "customer_id":customer_id})
                session.commit()
            st.success(f"Reservation to {venue_name} made successfully!")
        else:
            st.error("Error: The given date and time range intersects with an existing reservation.")
    else:
        st.error("Error: Invalid date range. Ensure the start date is today or later, and the end date and end time is after the start date and start time respectively.")

if col1.button("Back to Venues"):
    st.switch_page("select_venue.py")
