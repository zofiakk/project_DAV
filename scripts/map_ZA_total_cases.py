import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from utils import get_smaller_data, save_or_display_html

df_map_all = pd.read_csv("../data/new_covid_za.csv")

# Get only one date per week
df_map = get_smaller_data(df_map_all, 7)

# Create the animation
fig_map = go.Figure(px.choropleth(df_map,
                        locations='iso_code', color='total_cases',
                        hover_name='location',
                        color_continuous_scale="algae",
                        range_color=[0, max(df_map["total_cases"][df_map["total_cases"].notna()])],
                        labels={'total_cases': 'Number of cases'},
                        animation_frame="date",
                        title="Cumulative number of cases"
                        ))

# Change the layout
fig_map.update_layout(geo_scope="africa", geo_resolution=50,  title_x=0.5,
                      title=dict(font=dict(size=25)),
                      font=dict(size=15),
                      sliders= [{
                        "active": 0,
                        "y":-0.02,
                        "yanchor": "top",
                        "xanchor": "left",
                        "currentvalue": {
                            "font": {"size": 20},
                            "prefix": "Date:",
                            "visible": True,
                            "xanchor": "right"
                        }}],
                updatemenus=[{"buttons": [
                  {"args": [None, {"frame": {"duration": 500, "redraw": False},
                                   "fromcurrent": True,
                                   "transition": {"duration": 300,
                                                  "easing": "quadratic-in-out"}}],
                   "label": "Play",
                   "method": "animate"},
                  { "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate"}],
                              "direction": "left",
                              "pad": {"r": 10, "t": 87},
                              "showactive": False,
                              "type": "buttons",
                              "x": 0.1,
                              "xanchor": "right",
                              "y": 0,
                              "yanchor": "top"}])



save_or_display_html(fig_map, "map_total_cases")
