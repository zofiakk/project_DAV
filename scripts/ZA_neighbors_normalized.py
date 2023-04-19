import pandas as pd
from utils import get_some_countries, save_or_display_html, get_country_averages
import plotly.graph_objects as go
from datetime import datetime

neighbours = ["South Africa", "Namibia", "Botswana", "Zimbabwe", "Eswatini", "Lesotho"]

data = pd.read_csv("../data/new_covid_za.csv")

data = get_some_countries(data, neighbours)
data = data.fillna(method="ffill")

dates = data.date.to_list()

fig = go.Figure()

datasets = ["total_cases","total_deaths", "total_tests", "total_vaccinations" ]

for index, dataset in enumerate(datasets):
    if index == 0:
        if dataset == "total_deaths":
            fig.add_traces(go.Bar(x=neighbours,
                            y=round(data[data.date == dates[-1]][dataset]/data[data.date == dates[-1]]["population"],5),
                            marker_color=['#FFA15A', '#AB63FA', '#636EFA', '#19D3F3', '#EF553B', '#00CC96'],
                            hovertemplate= "Number divided by population: %{y}<br><extra></extra>",
                                visible=True))
        else:
            fig.add_traces(go.Bar(x=neighbours,
                                y=round(data[data.date == dates[-1]][dataset]/data[data.date == dates[-1]]["population"],3),
                                marker_color=['#FFA15A', '#AB63FA', '#636EFA', '#19D3F3', '#EF553B', '#00CC96'],
                                hovertemplate= "Number divided by population: %{y}<br><extra></extra>",
                                    visible=True))
    else:
        if dataset == "total_deaths":
            fig.add_traces(go.Bar(x=neighbours,
                                y=round(data[data.date == dates[-1]][dataset]/data[data.date == dates[-1]]["population"], 5),
                                marker_color=['#FFA15A', '#AB63FA', '#636EFA', '#19D3F3', '#EF553B', '#00CC96'],
                                hovertemplate= "Number divided by population: %{y}<br><extra></extra>",
                                    visible=False))
        else:
            fig.add_traces(go.Bar(x=neighbours,
                            y=round(data[data.date == dates[-1]][dataset]/data[data.date == dates[-1]]["population"], 3),
                             marker_color=['#FFA15A', '#AB63FA', '#636EFA', '#19D3F3', '#EF553B', '#00CC96'],
                            hovertemplate= "Number divided by population: %{y}<br><extra></extra>",
                                visible=False))


updatemenus = list([
    dict(active=0,
         yanchor="top",
         x=0.0,
         xanchor="left",
         y=1.13,
         buttons=list([
            dict(label='Total cases by population',
                 method='update',
                 args=[{'visible' : [True, False, False, False]},
                       {'title': 'Normalized total number of cases',
                        'yaxis': {'title': 'Total number of cases/population'}}
                    ]),
            dict(label='Daily new deaths',
                 method='update',
                 args=[{'visible' : [False, True, False, False]},
                       {'title': 'Normalized total number of deaths',
                        'yaxis': {'title': 'Total number of deaths/population'}}]),
            dict(label='Daily new tests',
                 method='update',
                 args=[{'visible' : [False, False, True, False]},
                       {'title': 'Normalized total number of tests',
                        'yaxis': {'title': 'Total number of tests/population'}}]),
            dict(label='Daily new vaccinations',
                 method='update',
                 args=[{'visible' : [False,  False, False,  True]},
                       {'title': 'Normalized total number of vaccinations',
                        'yaxis': {'title': 'Total number of vaccinations/population'}}]),
            ]),
        )
    ])

fig.update_layout(
    updatemenus = updatemenus,
    font=dict(size=15),
    title={
        'text': "Neighbors comparison normalized by populations",
        'x': 0.5,
        'y': 0.92,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},
    xaxis_title="Countries",
    xaxis = dict(
        tickfont=dict(family='Helvetica',
                      size=20,
                      color='black')),
    yaxis_title="Total number of cases/population",
    yaxis = dict(
        tickfont=dict(family='Helvetica',
                      size=20,
                      color='black'))
    )


save_or_display_html(fig, "ZA_neighbors_normalized")
