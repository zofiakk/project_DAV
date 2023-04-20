import pandas as pd
import plotly.graph_objs as go
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import save_stationary_plotly, save_or_display_html

pop = pd.read_csv("../data/provinces_population_2020.csv")
pop = pop[['ADM1_NAME', 'T_TL']]
pop = pop[~pop.isnull().any(axis=1)]
pop = pop.astype({'T_TL':'int'})
sizes = pd.read_csv("../data/provinces_sizes.csv", sep=";", thousands=',')
sizes = sizes[["ADM1_EN", "AREA_SQKM"]]
sizes = sizes.astype({'AREA_SQKM':'float'})
provinces = sizes.ADM1_EN.to_list()
pop["density"] = pop.T_TL/sizes.AREA_SQKM

fig = go.Figure()

fig.add_traces(go.Bar(x=provinces,
                    y=round(pop.density,5),
                    hovertemplate= "Population per sqrt km: %{y}<br><extra></extra>",
                    visible=True,
                    marker_color=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#B6E880', '#FF6692', '#FF97FF']))
fig.update_layout(
    title={
        'text': "Population density in South African provinces",
        'x':0.5,
        'y':0.92,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},
    font=dict(size=18),
    xaxis_title="Provinces",
    xaxis = dict(categoryorder = 'total descending',
            tickfont=dict(family='Helvetica',
                            size=18,
                            color='black')),
    yaxis_title="Population density",
    yaxis = dict(
        tickfont=dict(family='Helvetica',
                      size=18,
                      color='black'))
    )


