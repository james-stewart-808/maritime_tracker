from collections import defaultdict
from pathlib import Path
import sqlite3

import streamlit as st
import altair as alt
import pandas as pd


# Set the title and favicon that appear in the Browser's tab bar.
#st.set_page_config(
#    page_title="Inventory tracker",
#    page_icon=":shopping_bags:",  # This is an emoji shortcode. Could be a URL too.
#)




import streamlit as st
import pandas as pd

# Define the pages
main = st.Page("main.py", title="Home", icon="🏡")
#inventories = st.Page("inventories/inventories.py", title="Voyage-based Inventories", icon="🚢")
#trade = st.Page("trade/trade.py", title="Merchandise Trade Portfolios", icon="📦")
#impact_tracking = st.Page("impact_tracking/impact_tracking.py", title="Impact Tracking Results", icon="💵")
#example_page = st.Page("streamlit_example.py", title="Streamlit Example", icon="❄️")


# Set up navigation
pg = st.navigation([main])#, inventories, trade, impact_tracking]) #, example_page])

# Run the selected page
pg.run()
