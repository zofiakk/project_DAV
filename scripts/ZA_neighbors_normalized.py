"""ZA neighbors normalized

Function which creates interactive bar plot showing
the pandemic data in each of the neighboring countries
normalized by its population
"""
import pandas as pd
from utils import get_some_countries, save_or_display_html
import plotly.graph_objects as go

neighbours = ["South Africa", "Namibia",
              "Botswana", "Zimbabwe", "Eswatini", "Lesotho"]

# Read the data
data = pd.read_csv("../data/new_covid_za.csv")

data = get_some_countries(data, neighbours)
data = data.fillna(method="ffill")

dates = data.date.to_list()


fig = go.Figure()

datasets = ["total_cases", "total_deaths", "total_tests", "total_vaccinations"]
# For each indicator create the bar plot
for index, dataset in enumerate(datasets):
    if index == 0:
        if dataset == "total_deaths":
            fig.add_traces(go.Bar(
                x=neighbours,
                y=round(data[data.date == dates[-1]][dataset] /
                        data[data.date == dates[-1]]["population"], 5),
                marker_color=['#FFA15A', '#AB63FA', '#636EFA', '#19D3F3',
                              '#EF553B', '#00CC96'],
                hovertemplate="Total deaths-population ratio: %{y}<br><extra></extra>",
                visible=True))
        elif dataset == "total_tests":
            fig.add_traces(go.Bar(
                x=neighbours,
                y=round(data[data.date == dates[-1]][dataset] /
                        data[data.date == dates[-1]]["population"], 3),
                marker_color=['#FFA15A', '#AB63FA', '#636EFA', '#19D3F3',
                              '#EF553B', '#00CC96'],
                hovertemplate="Total tests-population ratio: %{y}<br><extra></extra>",
                visible=True))
        elif dataset == "total_cases":
            fig.add_traces(go.Bar(
                x=neighbours,
                y=round(data[data.date == dates[-1]][dataset] /
                        data[data.date == dates[-1]]["population"], 3),
                marker_color=['#FFA15A', '#AB63FA', '#636EFA', '#19D3F3',
                              '#EF553B', '#00CC96'],
                hovertemplate="Total cases-population ratio: %{y}<br><extra></extra>",
                visible=True))
        else:
            fig.add_traces(go.Bar(
                x=neighbours,
                y=round(data[data.date == dates[-1]][dataset] /
                        data[data.date == dates[-1]]["population"], 3),
                marker_color=['#FFA15A', '#AB63FA', '#636EFA',
                              '#19D3F3', '#EF553B', '#00CC96'],
                hovertemplate="Total vaccinations-population ratio: %{y}<br><extra></extra>",
                visible=True))
    else:
        if dataset == "total_deaths":
            fig.add_traces(go.Bar(
                x=neighbours,
                y=round(data[data.date == dates[-1]][dataset] /
                        data[data.date == dates[-1]]["population"], 5),
                marker_color=[
                    '#FFA15A', '#AB63FA', '#636EFA', '#19D3F3', '#EF553B', '#00CC96'],
                hovertemplate="Total deaths-population ratio: %{y}<br><extra></extra>",
                visible=False))
        elif dataset == "total_tests":
            fig.add_traces(go.Bar(
                x=neighbours,
                y=round(data[data.date == dates[-1]][dataset] /
                        data[data.date == dates[-1]]["population"], 3),
                marker_color=[
                    '#FFA15A', '#AB63FA', '#636EFA', '#19D3F3', '#EF553B', '#00CC96'],
                hovertemplate="Total tests-population ratio: %{y}<br><extra></extra>",
                visible=False))
        elif dataset == "total_cases":
            fig.add_traces(go.Bar(
                x=neighbours,
                y=round(data[data.date == dates[-1]][dataset] /
                        data[data.date == dates[-1]]["population"], 3),
                marker_color=[
                    '#FFA15A', '#AB63FA', '#636EFA', '#19D3F3', '#EF553B', '#00CC96'],
                hovertemplate="Total cases-population ratio: %{y}<br><extra></extra>",
                visible=False))
        else:
            fig.add_traces(go.Bar(
                x=neighbours,
                y=round(data[data.date == dates[-1]][dataset] /
                        data[data.date == dates[-1]]["population"], 3),
                marker_color=[
                    '#FFA15A', '#AB63FA', '#636EFA', '#19D3F3', '#EF553B', '#00CC96'],
                hovertemplate="Total vaccinations-population ratio: %{y}<br><extra></extra>",
                visible=False))


# Add the dropdown menu
updatemenus = list([
    dict(active=0,
         yanchor="top",
         x=0.0,
         xanchor="left",
         y=1.13,
         buttons=list([
             dict(label='Total cases by population',
                  method='update',
                  args=[{'visible': [True, False, False, False]},
                        {'title': 'Normalized total number of cases',
                        'yaxis': {'title': 'Total cases-population ratio'}}
                        ]),
             dict(label='Total deaths by population',
                  method='update',
                  args=[{'visible': [False, True, False, False]},
                        {'title': 'Normalized total number of deaths',
                        'yaxis': {'title': 'Total deaths-population ratio'}}]),
             dict(label='Total tests by population',
                  method='update',
                  args=[{'visible': [False, False, True, False]},
                        {'title': 'Normalized total number of tests',
                        'yaxis': {'title': 'Total tests-population ratio'}}]),
             dict(label='Total vaccinations by population',
                  method='update',
                  args=[{'visible': [False,  False, False,  True]},
                        {'title': 'Normalized total number of vaccinations',
                        'yaxis': {'title': 'Total vaccinations-population ratio'}}]),
         ]),)
])

# Modify the layout
fig.update_layout(
    updatemenus=updatemenus,
    font=dict(size=15),
    title={
        'text': 'Normalized total number of cases',
        'x': 0.5,
        'y': 0.92,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},
    xaxis_title="Countries",
    xaxis=dict(
        tickfont=dict(family='Helvetica',
                      size=20,
                      color='black')),
    yaxis_title="Total cases-population ratio",
    yaxis=dict(
        tickfont=dict(family='Helvetica',
                      size=20,
                      color='black'))
)

save_or_display_html(fig, "ZA_neighbors_normalized")
