"""Provinces population size

Function which creates stationary bar plot showing
population density in different South African provinces
"""

import pandas as pd
import plotly.graph_objs as go
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import save_stationary_plotly

# REad data and choose a subset
pop = pd.read_csv("../data/provinces_population_2020.csv")
pop = pop[['ADM1_NAME', 'T_TL']]
pop = pop[~pop.isnull().any(axis=1)]
pop = pop.astype({'T_TL': 'int'})
sizes = pd.read_csv("../data/provinces_sizes.csv", sep=";", thousands=',')
sizes = sizes[["ADM1_EN", "AREA_SQKM"]]
sizes = sizes.astype({'AREA_SQKM': 'float'})
provinces = sizes.ADM1_EN.to_list()
pop["density"] = pop.T_TL/sizes.AREA_SQKM

# Create a plot
fig = go.Figure()
text = round(pop.density, 4).to_list()
text = [str(i*1000) + "/km²" for i in text]
fig.add_traces(go.Bar(x=provinces,
                      y=round(pop.density, 5),
                      text=text,
                      visible=True,
                      marker_color=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A',
                                    '#19D3F3', '#B6E880', '#FF6692', '#FF97FF']))

# Modify text above bars
fig.update_traces(textfont_size=12, textangle=0,
                  textposition="outside",
                  cliponaxis=False
                  )
fig.update_yaxes(tickformat=",.1e")

# Modify plot layout
fig.update_layout(
    title={
        'text': "Population density in South African provinces",
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},
    font=dict(size=15),
    xaxis_title="Provinces",
    xaxis=dict(categoryorder='total descending',
                tickfont=dict(family='Helvetica',
                              size=15,
                              color='black')),
    yaxis_title="Population density",
    yaxis=dict(
        tickfont=dict(family='Helvetica',
                      size=15,
                      color='black'))
)

# Change plot margins
fig.update_layout(
    autosize=True,
    margin={'l': 0, 'r': 0, 'b': 0, 't': 50},
    plot_bgcolor='rgba(0,0,0,0)'
)

fig.update_yaxes(showline=True, linecolor='black', gridcolor='lightgrey')
fig.update_xaxes(showline=True, linecolor='black', showgrid=False)


save_stationary_plotly(fig, "provinces_density")
