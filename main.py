import streamlit as st
from sqlalchemy.sql import text
import pandas as pd

st.set_page_config(page_title="State Spaces")

venues = st.Page("select_venue.py", title="Venues")
create_reservation = st.Page("create_reservation.py", title="Create Reservation")
venue_details = st.Page("venue_details.py", title="Venue Details")

pg = st.navigation([venues, create_reservation, venue_details])
pg.run()


