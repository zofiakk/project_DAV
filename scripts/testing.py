"""Testing

Script which creates the animated plot displaying
the ratio of positive and negative tests in neighboring
countries during the pandemic
"""
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from utils import save_or_display_html

# Read the data and choose a subset
data = pd.read_csv(
    "../data/covid19za_provincial_timeline_testing_positivityrate.csv")
data["YYYYMMDD"] = pd.to_datetime(data["YYYYMMDD"], format='%Y%m%d')
data = data.melt(id_vars=["YYYYMMDD"],
                 value_name="Positive", var_name="Province")
data["Negative"] = 1 - data["Positive"]
data = data.melt(id_vars=["YYYYMMDD", "Province"])
data["date"] = data["YYYYMMDD"].dt.date.astype("str")


# Create the animation
fig = go.Figure()

fig = px.bar(data,
             x="Province",
             y="value",
             color="variable",
             animation_frame="date",
             color_discrete_sequence=["#238c0e", "#8f1f0e"])

# Change the yaxis range
fig.update_yaxes(range=[0, 1])

# Change the plot layout
fig.update_layout(title={
    'text': "Positive vs Negative Covid tests",
    'x': 0.5,
    'y': 0.95,
    'xanchor': 'center',
    'yanchor': 'top',
    "font": {"size": 25}},
    legend_title_text='Case type',
    yaxis_title="Positive vs Negative ratio",
    font=dict(size=15),
    sliders=[{
        "active": 0,
        "y": -0.02,
        "yanchor": "top",
        "xanchor": "left",
        "currentvalue": {
            "font": {"size": 20},
            "prefix": "Date:",
            "visible": True,
            "xanchor": "right"
        }}],
    updatemenus=[{"buttons": [
        {"args": [None, {"frame": {"duration": 500,
                                   "redraw": False},
                         "fromcurrent": True,
                         "transition": {"duration": 300,
                                        "easing": "quadratic-in-out"}}],
         "label": "Play",
         "method": "animate"},
        {"args": [[None], {"frame": {"duration": 0,
                                     "redraw": False},
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


save_or_display_html(fig, "ZA_testing")
