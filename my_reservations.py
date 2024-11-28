import streamlit as st

st.title("State Spaces :material/location_city:")
st.header("My Reservations")
conn = st.connection("postgresql", type="sql")



customer_id = st.text_input("Customer ID")
customer_query = f"SELECT v.venue_name, vt.venue_type, CONCAT(b.street, ' ', b.district, ' ', b.city), r.number_of_participants, r.reserved_from, r.reserved_to FROM building b JOIN venue v ON b.building_id = v.building_id JOIN amenity a ON v.venue_id = a.venue_id JOIN reservation r ON v.venue_id = r.venue_id JOIN customer c ON c.customer_id = r.customer_id JOIN venue_type vt ON vt.venue_id = v.venue_id WHERE c.customer_id = {customer_id};"

customer_reservations = conn.query(customer_query)

st.write(customer_reservations["concat"][0])

st.table(customer_reservations)

if st.button("Back to Venues"):
    st.switch_page("select_venue.py")
