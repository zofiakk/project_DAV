import pandas as pd
import json
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
import topojson as tp
from io import StringIO
mapboxtoken="pk.eyJ1IjoiemsxMTExIiwiYSI6ImNsZ2pyNHIyYTBrcHUzaGx2aDRpYWl0OXcifQ.1Bm1k4WL57wSmV7MW5kT-g"
mapboxstyle="mapbox://styles/zk1111/clgjrbb3l008001pk6hysb21t"

df_map = pd.read_csv("../data/covid19za_provincial_cumulative_timeline_confirmed.csv")

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

df_map["PROVINCE"] = df_map["variable"].map(provinces_codes)

with open('geojson.json', 'r') as data:
    geojson = json.load(StringIO(data.read()))

def basemap():
    fig = px.choropleth_mapbox(
        df_map,
        geojson=geojson,
        color="value",
        locations="PROVINCE",
        featureidkey="properties.PROVINCE",
        center = {"lat": -29, "lon": 24},
        mapbox_style=mapboxstyle,
        color_continuous_scale="algae",
        range_color=(0,1500000),
        zoom=4.3,
        labels={'value': 'Confirmed cases'},
        title = "Number of confirmed cases in South African provinces")
    fig.update_layout(margin={"r": 0, "t": 60, "l": 10, "b": 10},
                      mapbox={"accesstoken":mapboxtoken},
                      
                     )
    return fig
 
"""fig = px.choropleth_mapbox(df_map, geojson=geojson, locations='PROVINCE', featureidkey="properties.PROVINCE", 
                     color_continuous_scale="algae", color="value", range_color=(0,1500000),
                    labels={'value': 'Confirmed cases'},
                    zoom=3.5, center = {"lat": -28, "lon": 24},
                    mapbox_style="carto-positron",
                    title = "Number of confirmed cases in South African provinces")"""


gdf = (
    gpd.GeoDataFrame.from_features(geojson)
    .merge(df_map, on="PROVINCE")
    .assign(lat=lambda d: d.geometry.centroid.y, lon=lambda d: d.geometry.centroid.x)
    .set_index("PROVINCE", drop=False)
)

print(gdf.__dict__)
print(gdf.lat)
print(gdf.lon)
texttrace = go.Scattergeo(
        lat=gdf.lat,
        lon=gdf.lon,
        text="DDDDDDDDDDDDDD",
        textfont={"color":"red","size":10, "family":"Courier New"},
        mode="text",
        name='',
    )
fig = basemap()
fig.add_trace(texttrace)

fig.update_layout(geo_resolution=50,  title_x=0.5, title_y=0.98,
                      title=dict(font=dict(size=25))) 



fig.write_image("fig1.png")           
#fig.show()