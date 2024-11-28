import streamlit as st

venue_id = st.session_state.get("selected_venue")
conn = st.connection("postgresql", type="sql")

venue_query = f"SELECT venue_id, venue_name, capacity, floor_area FROM venue WHERE venue_id = {venue_id};"  # postgres query

venue_info = conn.query(venue_query)

venue_name = venue_info["venue_name"][0]
capacity = venue_info["capacity"][0]
floor_area = venue_info["floor_area"][0]

st.subheader(venue_name)
st.text(f"Capacity: {capacity}")
st.text(f"Floor Area: {floor_area} sqm")


if st.button("Back"):
    st.switch_page("select_venue.py")
