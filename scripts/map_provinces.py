import pandas as pd
import json
import plotly.express as px
from utils import get_smaller_data, save_or_display_html
import topojson as tp
from io import StringIO

df_map_all = pd.read_csv("../data/covid19za_provincial_cumulative_timeline_confirmed.csv")

# Get only one date per week
df_map = get_smaller_data(df_map_all, 7).fillna(method="ffill")

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

df_map = df_map.melt(id_vars = ["date"], value_vars=["EC","FS","GP","KZN","LP","MP","NC","NW","WC"])

df_map["location"] = df_map["variable"].map(provinces_codes)

"""GEO_DATA = 'geojson.json'
#Load GeoJson 
with open('za_prov.json') as f:
    provinces = json.load(f)

topo = tp.Topology(provinces, object_name='layer1')
# convert to geojson, store in GEO_DATA
topo.to_geojson(GEO_DATA)
"""
#provinces=rewind(provinces,rfc7946=False)
with open('geojson.json', 'r') as data:
    geojson = json.load(StringIO(data.read()))
     
fig = px.choropleth_mapbox(df_map, geojson=geojson, locations='location', featureidkey="properties.PROVINCE", 
                     color_continuous_scale="algae", color="value", range_color=(0,1500000),
                    animation_frame="date",  hover_name='variable',
                    labels={'value': 'Confirmed cases'},
                    zoom=3.5, center = {"lat": -28, "lon": 24},
                    mapbox_style="carto-positron",
                    title = "Number of confirmed cases in South African provinces")

fig.update_layout(geo_resolution=50,  title_x=0.5,
                      title=dict(font=dict(size=25)))   
                    

save_or_display_html(fig, "map_provinces_cases")