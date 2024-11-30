import streamlit as st

col1, col2 = st.columns([0.8,0.2])
col1.title("State Spaces :material/location_city:")
if col2.button("Change User"):
    st.switch_page("change_user.py")

st.header("My Reservations")
conn = st.connection("postgresql", type="sql")

customer_id = st.session_state.get("user_id")

# customer_info
customer_query = f"SELECT * FROM customer WHERE customer_id = {customer_id};"
customer_info = conn.query(customer_query)

name = customer_info["customer_name"][0]
birth_date = str(customer_info["birth_date"][0])
contact_no = customer_info["contact_no"][0]

customer_cont = st.container(border=True)
with customer_cont:
    col1, col2 = st.columns([1,1])
    col1.metric(label="Customer Name",value=name)
    col2.metric(label="Birth Date",value=birth_date)
    col1.metric(label="Contact No.",value=contact_no)

resevations_query = f"SELECT DISTINCT r.reservation_id, v.venue_name, vt.venue_type, CONCAT(v.floor, ', ', b.street, ' ', b.district, ' ', b.city), r.number_of_participants, r.reserved_from, r.reserved_to FROM building b JOIN venue v ON b.building_id = v.building_id JOIN amenity a ON v.venue_id = a.venue_id JOIN reservation r ON v.venue_id = r.venue_id JOIN customer c ON c.customer_id = r.customer_id JOIN venue_type vt ON vt.venue_id = v.venue_id WHERE c.customer_id = {customer_id} ORDER BY r.reservation_id DESC;"
reservations_info = conn.query(resevations_query, ttl="5s")

st.write("### Reservations")
for i, row in reservations_info.iterrows(): # for column, row
    reservations_cont = st.container(border=True)
    col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])
    with reservations_cont:
        venue_name = row["venue_name"]
        venue_type = row["venue_type"]
        address = row["concat"]
        number_of_participants = row["number_of_participants"]
        reserved_from = row["reserved_from"]
        reserved_to = row["reserved_to"]
        
        col1.write(venue_name)
        col2.write(venue_type)
        col3.write(str(address))
        col4.write(str(number_of_participants))
        col5.write(str(reserved_from))
        col6.write(str(reserved_to))


if st.button("Back to Venues"):
    st.switch_page("select_venue.py")
