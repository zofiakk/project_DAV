import pandas as pd
from utils import get_some_countries, save_or_display_html, get_country_averages
import plotly.graph_objects as go
from datetime import datetime

neighbours = ["South Africa", "Namibia", "Botswana", "Zimbabwe", "Eswatini", "Lesotho"]

data = pd.read_csv("../data/new_covid_za.csv")

data = get_some_countries(data, neighbours)
#!!!!!- fillna
data = data.fillna(method="ffill")

data = get_country_averages(data, ["new_cases_per_million", "new_deaths_per_million",
                                   "new_tests_per_thousand", "new_vaccinations"])

fig = go.Figure()
for country, data_for_country in data.groupby("location"):
    fig.add_scatter(
        x=data_for_country.date,
        y=data_for_country.new_cases_per_million7,
        name=country,
        mode='lines+markers',
        hovertemplate= "Date: %{x}<br>" + "Number of observed: %{y}<br>" + "<extra></extra>",
        line=dict(width=2),
        marker=dict(size=5, maxdisplayed=70),
        visible=True)

updatemenus = list([
    dict(active=0,
         yanchor="top",
         x=0.0,
         xanchor="left",
         y=1.13,
         buttons=list([
            dict(label='Daily new cases',
                 method='update',
                 args=[{'y': [data_for_country.new_cases_per_million7 for _, data_for_country in data.groupby("location")]},
                       {'title': 'Daily new cases per million',
                        'yaxis': {'title': 'Average number of cases per million'}}
                    ]),
            dict(label='Daily new deaths',
                 method='update',
                 args=[{'y': [data_for_country.new_deaths_per_million7 for _, data_for_country in data.groupby("location")]},
                       {'title': 'Daily new deaths per million',
                        'yaxis': {'title': 'Average number of deaths per million'}}]),
            dict(label='Daily new tests',
                 method='update',
                 args=[{'y': [data_for_country.new_tests_per_thousand7 for _, data_for_country in data.groupby("location")]},
                       {'title': 'Daily new tests per thousand',
                        'yaxis': {'title': 'Average number of tests per thousand'}}]),
            dict(label='Daily new vaccinations',
                 method='update',
                 args=[{'y': [data_for_country.new_vaccinations7 for _, data_for_country in data.groupby("location")]},
                       {'title': 'Daily new vaccinations',
                        'yaxis': {'title': 'Average number of vaccinations'}}]),
            ]),
        )
    ])

dates = data.date.to_list()
dates.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%d"))
chosen = dates[0::410]
fig.update_layout(xaxis=dict(
        tickmode="array",
        tickvals=chosen,
        ticktext=chosen,
        tickangle=45,
    ))

fig.update_layout(
    updatemenus = updatemenus,
    font=dict(size=15),
    legend_title_text='Country',
    title={
        'text': "Daily new cases per million",
        'x': 0.5,
        'y': 0.92,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},
    xaxis_title="Date",
    yaxis_title="Average number of cases per million",
    )


save_or_display_html(fig, "ZA_neighbors")
