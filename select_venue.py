import streamlit as st

def create_venue_card(venue_id, venue_name, venue_type, capacity):
    with st.container(border=True):
        st.subheader(venue_name)
        col1, col2 = st.columns([0.8,0.2])
        col1.write(f"Type: {venue_type}")
        col2.write(f":material/person: {capacity}")
        if st.button(f"View Details", key=f"details_{venue_id}", use_container_width=True):
            st.session_state["selected_venue"] = venue_id
            st.session_state["page"] = "details"
            st.switch_page("venue_details.py")
        if st.button(f"Make Reservation", key=f"reserve_{venue_id}", use_container_width=True):
            st.session_state["selected_venue"] = venue_id
            st.session_state["page"] = "reservation"
            st.switch_page("create_reservation.py")

col1, col2 = st.columns([0.8,0.2])
col1.title("State Spaces :material/location_city:")
if col2.button("Change User"):
    st.switch_page("change_user.py")

col1, col2 = st.columns([1,0.3])
col1.header("Venues")
if col2.button("My Reservations"):
    st.switch_page("my_reservations.py")

conn = st.connection("postgresql", type="sql")

# fetching data from db
venues_query = "SELECT v.venue_id, v.venue_name, vt.venue_type, v.capacity FROM venue v JOIN venue_type vt ON v.venue_id = vt.venue_id;"  # postgres query
col1, col2 = st.columns([1,1])
venues = conn.query(venues_query, ttl="0s")
for i, row in venues.iterrows(): # for column, row
    venue_id = row["venue_id"]
    venue_name = row["venue_name"]
    venue_type = row["venue_type"]
    capacity = row["capacity"]

    if i%2 == 0:
        with col1:
            create_venue_card(venue_id, venue_name, venue_type, capacity)
    else:
        with col2:
            create_venue_card(venue_id, venue_name, venue_type, capacity)


