import streamlit as st

st.title("Venues")
conn = st.connection("postgresql", type="sql")

# fetching data from db
venues_query = "SELECT venue_id, venue_name, capacity, floor_area FROM venue;"  # postgres query

# displaying as dataframe
venues = conn.query(venues_query, ttl="0s")

for _, row in venues.iterrows():
    venue_id = row["venue_id"]
    venue_name = row["venue_name"]
    capacity = row["capacity"]
    floor_area = row["floor_area"]

    # Create a card layout
    with st.container():
        col1, col2 = st.columns([2, 1])  # Two columns: card content and buttons
        with col1:
            st.subheader(venue_name)
            st.text(f"Capacity: {capacity}")
            st.text(f"Floor Area: {floor_area} sqm")
        with col2:
            if st.button(f"View Details", key=f"details_{venue_id}"):
                st.session_state["selected_venue"] = venue_id
                st.session_state["page"] = "details"
                st.switch_page("venue_details.py")
            if st.button(f"Make Reservation", key=f"reserve_{venue_id}"):
                st.session_state["selected_venue"] = venue_id
                st.session_state["page"] = "reservation"
                st.switch_page("create_reservation.py")


# for venue in venues:
    
    # venue_id, venue_name, capacity, floor_area = venue

    # # Create a card layout
    # with st.container():
    #     col1, col2 = st.columns([2, 1])  # Two columns: card content and buttons
    #     with col1:
    #         st.subheader(venue_name)
    #         st.text(f"Capacity: {capacity}")
    #         st.text(f"Floor Area: {floor_area} sqm")
    #     with col2:
    #         if st.button(f"View Details (ID {venue_id})", key=f"details_{venue_id}"):
    #             st.session_state["selected_venue"] = venue_id
    #             st.session_state["page"] = "details"
    #         if st.button(f"Make Reservation (ID {venue_id})", key=f"reserve_{venue_id}"):
    #             st.session_state["selected_venue"] = venue_id
    #             st.session_state["page"] = "reservation"

