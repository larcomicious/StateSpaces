import streamlit as st
st.title("State Spaces :material/location_city:")
st.header("Change User")
conn = st.connection("postgresql", type="sql")

new_id = st.number_input("Customer ID", step=1, min_value=1, max_value=5)
if st.button("Confirm"):
    st.session_state["user_id"] = new_id
    st.session_state["selected_venue"] = ""
    st.session_state["page"] = ""
    st.success(f"Changed user successfully!")

if st.button("Go to Venues"):
    st.switch_page("select_venue.py")