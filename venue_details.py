import streamlit as st

def create_amenity_card(amenity_type, description, quantity):
    with st.container(border=True):
        st.write(f"Type: {amenity_type}")
        st.write(f"Quantity: {quantity}")
        st.write(description)

col1, col2 = st.columns([0.8,0.2])
col1.title("State Spaces :material/location_city:")
if col2.button("Change User"):
    st.switch_page("change_user.py")

venue_id = st.session_state.get("selected_venue")
conn = st.connection("postgresql", type="sql")

# venue query
venue_query = f"SELECT v.venue_id, v.venue_name, vt.venue_type, v.capacity, v.floor, v.floor_area, v.renovating, b.building_name, CONCAT(b.street, ' Street, ', b.district), b.city FROM venue v JOIN building b ON v.building_id = b.building_id JOIN venue_type vt ON v.venue_id = vt.venue_id WHERE v.venue_id = {venue_id};"
venue_info = conn.query(venue_query)

venue_name = venue_info["venue_name"][0]
venue_type = venue_info["venue_type"][0]
capacity = venue_info["capacity"][0]
floor = venue_info["floor"][0]
floor_area = venue_info["floor_area"][0]
renovating = venue_info["renovating"][0]
building_name = venue_info["building_name"][0]
address = venue_info["concat"][0]
city = venue_info["city"][0]

st.header(venue_name)
venue_cont = st.container()
with venue_cont:
    col1, col2, col3 = st.columns([1,1,0.5])
    col1.metric(label="Venue ID",value=venue_id)
    col2.metric(label="Venue Type",value=venue_type)
    col3.metric(label="Capacity :material/person:",value=capacity)
    col1.metric(label="Floor",value=floor)
    col2.metric(label="Floor Area (sq. m)",value=floor_area)
    col3.metric(label="Renovating",value=renovating)
    st.metric(label="Location",value=address)
    col1, col2 = st.columns([1,1])
    col1.metric(label="Building",value=building_name)
    col2.metric(label="City",value=city)


st.subheader("Amenities")

# amenity query
amenities_query = f"SELECT a.amenity_type, a.description, a.quantity, a.venue_id FROM amenity a JOIN venue v ON a.venue_id = v.venue_id WHERE v.venue_id = {venue_id};"
amenities_info = conn.query(amenities_query)
amenities_cont = st.container()
with amenities_cont:
    col1, col2, col3 = st.columns([1,1,1])
    for i, row in amenities_info.iterrows(): # for column, row
        amenity_type = row["amenity_type"]
        description = row["description"]
        quantity = row["quantity"]

        if i%3 == 0:
            with col1:
                create_amenity_card(amenity_type, description, quantity)
        elif i%3 == 1:
            with col2:
                create_amenity_card(amenity_type, description, quantity)
        else:
            with col3:
                create_amenity_card(amenity_type, description, quantity)

if st.button("Back to Venues"):
    st.switch_page("select_venue.py")


