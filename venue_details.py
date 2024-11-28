import streamlit as st

st.title("State Spaces :material/location_city:")

venue_id = st.session_state.get("selected_venue")
conn = st.connection("postgresql", type="sql")

# postgres query

# venue_query = f"SELECT * WHERE venue_id = {venue_id};"  
query1 = f"SELECT v.venue_id, v.venue_name, vt.venue_type, v.capacity, f.floor, v.floor_area, b.building_name, CONCAT(b.street, ' Street, ', b.district), b.city, a.amenity_type, a.description, a.quantity FROM venue v JOIN building b ON v.building_id = b.building_id JOIN floor f ON v.venue_id = f.venue_id AND b.building_id = f.building_id JOIN venue_type vt ON v.venue_id = vt.venue_id JOIN amenity a ON v.venue_id = a.venue_id WHERE v.venue_id = {venue_id};"

# venue_info = conn.query(venue_query)
query1_info = conn.query(query1)
# st.write(query1_info["concat"][0])
# venue_name = venue_info["venue_name"][0]
# capacity = venue_info["capacity"][0]
# floor_area = venue_info["floor_area"][0]

# st.header(venue_name)
# st.write(f":material/person: {capacity}")
# st.write(f"Floor Area: {floor_area} sqm")
st.table(query1_info)

if st.button("Back to Venues"):
    st.switch_page("select_venue.py")


