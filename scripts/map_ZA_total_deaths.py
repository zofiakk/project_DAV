import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from utils import get_smaller_data, save_or_display_html

df_map_all = pd.read_csv("../data/new_covid_za.csv")

# Get only one date per week
df_map = get_smaller_data(df_map_all, 7)

# Create the animation
fig_map = go.Figure(px.choropleth(df_map,
                        locations='iso_code', color='total_deaths',
                        hover_name='location',
                        color_continuous_scale="algae",
                        range_color=[0, max(df_map["total_deaths"][df_map["total_deaths"].notna()])],
                        labels={'total_deaths': 'Number of deaths'},
                        animation_frame="date",
                        title="Cumulative number of Covid related deaths"
                        ))


fig_map.update_layout( geo_scope="africa", geo_resolution=50,  title_x=0.5,
                      title=dict(font=dict(size=25)))

save_or_display_html(fig_map, "map_total_deaths")
