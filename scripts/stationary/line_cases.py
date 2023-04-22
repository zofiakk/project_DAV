"""Line cases

Function which creates stationary line plot showing
number of cases and vaccinations on two separate yaxes
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import get_country_averages, get_some_countries, save_stationary_plotly
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Load data, choose a subset and get the averages
data = pd.read_csv("../data/new_covid_za.csv")
data = get_some_countries(data, ["South Africa"]).fillna(method="ffill")
data = get_country_averages(
    data, ["new_cases_per_million", "new_vaccinations_smoothed_per_million"])


# Create two subplots with separate yaxes
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=data['date'], y=data["new_cases_per_million30"],
               name="New deaths", line=dict(color='blue')),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=data['date'], y=data["new_vaccinations_smoothed_per_million30"],
               name="New vaccinations", line=dict(color='green')),
    secondary_y=True,
)

# Modify plot layout
fig.update_layout(hovermode="x", height=600, width=1000,
                  template='plotly_white', paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  title={'text': "New cases vs new vaccinations",
                           'y': 0.9, 'x': 0.5, 'xanchor': 'center',
                           'yanchor': 'top'},
                  titlefont=dict(size=25),
                  xaxis=dict(tickfont={"size": 15},
                             titlefont={"color": "#673ab7"},
                             title='<b>Date</b>'),
                  legend=dict(font=dict(size=15)),
                  legend_title_text='Legend')

# Add axis titles
fig.update_yaxes(dict(tickfont={"size": 15},
                      titlefont={"color": "#673ab7"},
                      title='<b>Average new cases per million</b>'),
                 secondary_y=False,
                 color='blue')
fig.update_yaxes(dict(tickfont={"size": 15},
                      titlefont={"color": "#673ab7"},
                      title='<b>Average new vaccinations per million</b>'),
                 secondary_y=True,
                 color='green')


save_stationary_plotly(fig, "line_cases")
