import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import time

st.header("Welcome to the Homepage of the International Shipping Dashboard 🏡")

# Read-in ISO Country Labels dataset and use as Standard
#country_iso_codes_cols = ["name", "alpha-2", "alpha-3", "country-code"]
#country_iso_codes_dtype = {"alpha-2":str, "alpha-3":str, "country-code":str}
#country_iso_codes_renames = {"name":"iso_country", "alpha-2":"iso_2", "alpha-3":"iso_3", "country-code":"iso_code"}
#country_iso_codes = pd.read_csv("/Users/apple/repos/datasets/national_stats/country_iso_codes.csv", usecols=country_iso_codes_cols, dtype=country_iso_codes_dtype).rename(columns=country_iso_codes_renames)
#country_iso_codes.loc[country_iso_codes.iso_country == "Namibia", "iso_2"] = "NA"

#country_choice = st.selectbox(
#    "For which country would you like to statistics related to international shipping, merchandise trade and MTM impact tracking?",
#    (country_iso_codes.iso_country.unique()))

# set as global variable
#st.session_state.iso_country = country_choice
#st.session_state.iso_2 = country_iso_codes[(country_iso_codes.iso_country == country_choice)].iso_2.values[0]
#st.session_state.iso_3 = country_iso_codes[(country_iso_codes.iso_country == country_choice)].iso_3.values[0]
#st.session_state.iso_code = country_iso_codes[(country_iso_codes.iso_country == country_choice)].iso_code.values[0]

### Placeholder for map view of country

st.header("Take me to...") # Amend with links
#st.page_link("inventories/inventories.py", label="Voyage-based Inventories", icon="🚢")
#st.page_link("trade/trade.py", label="Merchandise Trade Portfolios", icon="📦")
#st.page_link("impact_tracking/impact_tracking.py", label="Impact Tracking Results", icon="💵")



#🚢")
#trade = st.Page("trade/trade.py", title="Merchandise Trade Portfolios", icon="📦")
#impact_tracking = st.Page("impact_tracking/impact_tracking.py", title="Impact Tracking Results", icon="💵")
