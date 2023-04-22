"""ZA neighbors

Script which creates stationary line plot showing
number of cases in neighboring countries
"""

from datetime import datetime
import plotly.graph_objects as go
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import get_some_countries, save_stationary_plotly, get_country_averages
import pandas as pd



neighbours = ["South Africa", "Namibia",
              "Botswana", "Zimbabwe", "Eswatini", "Lesotho"]

# read the data, choose a subset and count the averages
data = pd.read_csv("../data/new_covid_za.csv")
data = get_some_countries(data, neighbours)
data = data.fillna(method="ffill")
data = get_country_averages(data, ["new_cases_per_million"])

# Create the plot
fig = go.Figure()
for country, data_for_country in data.groupby("location"):
    fig.add_scatter(
        x=data_for_country.date,
        y=data_for_country.new_cases_per_million30,
        name=country,
        mode='lines+markers',
        line=dict(width=2),
        marker=dict(size=5, maxdisplayed=70),
        visible=True)

# Change legend placement (inside)
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="right",
    x=0.99
))

# Modify xaxis ticks
dates = data.date.to_list()
dates.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%d"))
chosen = dates[0::410]
fig.update_layout(xaxis=dict(
    tickmode="array",
    tickvals=chosen,
    ticktext=chosen,
    tickangle=45,
))

# Modify plot layout
fig.update_layout(
    font=dict(size=15),
    legend_title_text='Country',
    title={
        'text': "Daily new cases per million",
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},
    xaxis_title="Date",
    yaxis_title="Average number of cases per million",
)

# Change plot margins
fig.update_layout(
    autosize=True,
    margin={'l': 0, 'r': 0, 'b': 0, 't': 50},
    plot_bgcolor='rgba(0,0,0,0)'
)

fig.update_yaxes(showline=True, linecolor='black', gridcolor='lightgrey')
fig.update_xaxes(showline=True, linecolor='black', showgrid=False)

save_stationary_plotly(fig, "ZA_neighbors")
