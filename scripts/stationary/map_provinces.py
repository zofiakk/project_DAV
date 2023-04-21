"""Map provinces

Script which creates stationary map showing
number of cases in South African provinces
"""


import pandas as pd
import json
import plotly.express as px
from io import StringIO
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import save_stationary_plotly

# Add tokens to use specific style
mapboxtoken = "pk.eyJ1IjoiemsxMTExIiwiYSI6ImNsZ2pyNHIyYTBrcHUzaGx2aDRpYWl0OXcifQ.1Bm1k4WL57wSmV7MW5kT-g"
mapboxstyle = "mapbox://styles/zk1111/clgjrbb3l008001pk6hysb21t"

# Read the cases data
df_map = pd.read_csv(
    "../data/covid19za_provincial_cumulative_timeline_confirmed.csv")

# Dictionary showing provinces codes
provinces_codes = {
    'Western Cape': 'WC',
    'Northern Cape': 'NC',
    'Eastern Cape': 'EC',
    'Gauteng': 'GP',
    'KwaZulu-Natal': 'KZN',
    'Mpumalanga': 'MP',
    'Free State': 'FS',
    'Limpopo': 'LP',
    'North West': 'NW',
}
provinces_codes = {v: k for k, v in provinces_codes.items()}

# Modify the data to have it in a needed format
df_map = df_map.melt(id_vars=["date"],
                     value_vars=["EC", "FS", "GP", "KZN", "LP", "MP", "NC", "NW", "WC"])

df_map["PROVINCE"] = df_map["variable"].map(provinces_codes)

# Load the geojson file
with open('geojson.json', 'r') as data:
    geojson = json.load(StringIO(data.read()))


# Create the basemap showing number of cases
fig = px.choropleth_mapbox(
    df_map,
    geojson=geojson,
    color="value",
    locations="PROVINCE",
    featureidkey="properties.PROVINCE",
    center={"lat": -29, "lon": 24},
    mapbox_style=mapboxstyle,
    color_continuous_scale="algae",
    range_color=(0, 1500000),
    zoom=4.3,
    labels={'value': 'Confirmed cases'},
    title="Number of confirmed cases in South African provinces")

# Change fifure margins
fig.update_layout(margin={"r": 0, "t": 50, "l": 10, "b": 10},
                  mapbox={"accesstoken": mapboxtoken})

# Modify map layout
fig.update_layout(geo_resolution=50,
                  title_x=0.5,
                  title_y=0.96,
                  title=dict(font=dict(size=25)))

save_stationary_plotly(fig, "map_provinces")
