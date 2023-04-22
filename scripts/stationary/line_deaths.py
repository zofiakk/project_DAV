"""Line deaths

Function which creates stationary line plot showing
number of deaths and vaccinations on two separate yaxes
"""
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import get_country_averages, get_some_countries, save_stationary_plotly


# Load data, choose a subset and get the averages
data = pd.read_csv("../data/new_covid_za.csv")
data = get_some_countries(data, ["South Africa"]).fillna(method="ffill")
data = get_country_averages(
    data, ["new_deaths_per_million", "new_vaccinations_smoothed_per_million"])


# Create two subplots with separate yaxes
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=data['date'],
               y=data["new_deaths_per_million30"],
               name="New deaths",
               line=dict(color='black')),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=data['date'],
               y=data["new_vaccinations_smoothed_per_million30"],
               name="New vaccinations",
               line=dict(color='green')),
    secondary_y=True)

# Modify plot layout
fig.update_layout(height=600, width=1000,
                  plot_bgcolor='rgba(0,0,0,0)',
                  autosize=True,
                  margin={'l': 0, 'r': 0, 'b': 50, 't': 50},
                  title={'text': "New deaths vs new vaccinations",
                         'y': 0.95, 'x': 0.5,
                         'xanchor': 'center', 'yanchor': 'top'},
                  titlefont=dict(size=30),
                  xaxis=dict(tickfont={"size": 15},
                             title='Date'),
                  legend=dict(font=dict(size=20),
                              orientation="h",
                              y=-0.25, x=0.5, xanchor='center',
                              yanchor='bottom'
                              ),
                  font=dict(size=18),)

# Add axis titles
fig.update_yaxes(dict(tickfont={"size": 15},
                      title='Average new cases per million'),
                 secondary_y=False,
                 color='black',
                 gridcolor="lightgrey",
                 showline=True,)
fig.update_yaxes(dict(tickfont={"size": 15},
                      title='Average new vaccinations per million'),
                 secondary_y=True, color='green',
                 gridcolor="lightgrey",
                 showline=True)

fig.update_xaxes(showline=True, linecolor="lightgrey",
                 showgrid=True, gridcolor='lightgrey')


save_stationary_plotly(fig, "line_death")
