import streamlit as st

col1, col2 = st.columns([0.8,0.2])
col1.title("State Spaces :material/location_city:")
if col2.button("Change User"):
    st.switch_page("change_user.py")

venue_id = st.session_state.get("selected_venue")
conn = st.connection("postgresql", type="sql")

# postgres query

# venue_query = f"SELECT * WHERE venue_id = {venue_id};"  
venue_query = f"SELECT v.venue_id, v.venue_name, vt.venue_type, v.capacity, v.floor, v.floor_area, b.building_name, CONCAT(b.street, ' Street, ', b.district), b.city, a.amenity_type, a.description, a.quantity FROM venue v JOIN building b ON v.building_id = b.building_id JOIN venue_type vt ON v.venue_id = vt.venue_id JOIN amenity a ON v.venue_id = a.venue_id WHERE v.venue_id = {venue_id};"

# venue_info = conn.query(venue_query)
venue_info = conn.query(venue_query)

venue_name = venue_info["venue_name"][0]
venue_type = venue_info["venue_type"][0]
capacity = venue_info["capacity"][0]
floor = venue_info["floor"][0]
building_name = venue_info["building_name"][0]
address = venue_info["concat"][0]
city = venue_info["city"][0]

st.header(venue_name)
venue_cont = st.container()
with venue_cont:
    col1, col2 = st.columns([1,1])
    col1.metric(label="Venue ID",value=venue_id)
    col2.metric(label="Venue Type",value=venue_type)
    col1.metric(label="Capacity :material/person:",value=capacity)
    col2.metric(label="Floor",value=floor)
    st.metric(label="Location",value=address)
    col1, col2 = st.columns([1,1])
    col1.metric(label="Building",value=building_name)
    col2.metric(label="City",value=city)
    # st.write(address)

# st.write(venue_type)
# st.write(capacity)
# st.write(floor)
# st.write(building_name)
# st.write(address)
# st.write(city)
# st.header(venue_name)
# st.write(f":material/person: {capacity}")
# st.write(f"Floor Area: {floor_area} sqm")
# st.write(venue_info)

if st.button("Back to Venues"):
    st.switch_page("select_venue.py")


