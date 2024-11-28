import streamlit as st

def create_venue_card(venue_id, venue_name, capacity, floor_area):
    with st.container(border=True):
        st.subheader(venue_name)
        st.write(f":material/person: {capacity}")
        if st.button(f"View Details", key=f"details_{venue_id}", use_container_width=True):
            st.session_state["selected_venue"] = venue_id
            st.session_state["page"] = "details"
            st.switch_page("venue_details.py")
        if st.button(f"Make Reservation", key=f"reserve_{venue_id}", use_container_width=True):
            st.session_state["selected_venue"] = venue_id
            st.session_state["page"] = "reservation"
            st.switch_page("create_reservation.py")

st.title("State Spaces :material/location_city:")
st.header("Venues")
conn = st.connection("postgresql", type="sql")

# fetching data from db
venues_query = "SELECT venue_id, venue_name, capacity, floor_area FROM venue;"  # postgres query
col1, col2 = st.columns([1,1])
venues = conn.query(venues_query, ttl="0s")
for i, row in venues.iterrows(): # for column, row
    venue_id = row["venue_id"]
    venue_name = row["venue_name"]
    capacity = row["capacity"]
    floor_area = row["floor_area"]

    if i%2 == 0:
        with col1:
            create_venue_card(venue_id, venue_name, capacity, floor_area)
    else:
        with col2:
            create_venue_card(venue_id, venue_name, capacity, floor_area)

if st.button("My Reservations"):
    st.switch_page("my_reservations.py")


