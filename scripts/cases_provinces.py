import plotly.graph_objects as go
import pandas as pd
from utils import get_provincial_averages, save_or_display_html
import itertools


provinces = ["EC", "FS", "GP", "KZN", "LP", "MP", "NC", "NW", "WC"]


data_deaths = get_provincial_averages(pd.read_csv(
    "../data/covid19za_provincial_cumulative_timeline_deaths.csv").fillna(method="ffill"),
    provinces)
data_confirmed = get_provincial_averages(pd.read_csv(
    "../data/covid19za_provincial_cumulative_timeline_confirmed.csv").fillna(method="ffill"),
    provinces)
data_recoveries = get_provincial_averages(pd.read_csv(
    "../data/covid19za_provincial_cumulative_timeline_recoveries.csv").fillna(method="ffill"),
    provinces)
data_vaccination = get_provincial_averages(pd.read_csv(
    "../data/covid19za_provincial_cumulative_timeline_vaccination.csv").fillna(method="ffill"),
    provinces)

data_vaccination.date = pd.to_datetime(
    data_vaccination['date'], format='%Y-%m-%d').dt.strftime('%d-%m-%Y')

datasets = [data_deaths, data_confirmed, data_recoveries, data_vaccination]

fig = go.Figure()

provinces = ["EC", "FS", "GP", "KZN", "LP", "MP", "NC", "NW", "WC"]
provinces_codes = {
    'Western Cape': 'WC',
    'Northern Cape': 'NC',
    'Eastern Cape': 'EC',
    'Gauteng': 'GP',
    'KwaZulu-Natal': 'KZN',
    'Mpumalanga': 'MP',
    'Free State': 'FS',
    'Limpopo': 'LP',
    'North West': 'NW',
}

provinces_codes = {v: k for k, v in provinces_codes.items()}

for index, dataset in enumerate(datasets):
    dates = dataset["date"]
    if index != 0:
        for province in provinces:
            fig.add_trace(go.Scatter(
                x=dates, y=dataset[province+"7"],
                name=provinces_codes[province],
                marker_color=fig.layout['template']['layout']['colorway'],
                visible=False,
                hovertemplate="Date: %{x}<br>" +
                "Number of cases: %{y}<br>" +
                "<extra></extra>",))
    else:
        for province in provinces:
            fig.add_traces(go.Scatter(
                x=dates, y=dataset[province+"7"],
                name=provinces_codes[province],
                marker_color=fig.layout['template']['layout']['colorway'],
                hovertemplate="Date: %{x}<br>" +
                "Number of cases: %{y}<br>" +
                "<extra></extra>",),)

updatemenus = [
    dict(name="Data Type",
         yanchor="top",
         x=0.0,
         xanchor="left",
         y=1.13,
         buttons=list([
             dict(label="Deaths",
                  method='update',
                  args=[{"visible":
                         list(itertools.chain.from_iterable([[True] * 9, [False] * 27]))},
                        {'title': 'Covid-19 deaths',
                         'yaxis': {'title': 'Average number of deaths'},
                         "xaxis": dict(
                             tickmode="array",
                             tickvals=data_deaths.date.to_list()[::60],
                             ticktext=data_deaths.date.to_list()[::60],
                             tickangle=45,
                         )}]),
             dict(label="Confirmed",
                  method='update',
                  args=[{"visible":
                         list(itertools.chain.from_iterable([[False] * 9,
                                                             [True] * 9,
                                                             [False] * 18]))},
                        {'title': 'Covid-19 confirmed cases',
                        'yaxis': {'title': 'Average number of confirmed cases'},
                         "xaxis": dict(
                            tickmode="array",
                            tickvals=data_confirmed.date.to_list()[::60],
                            ticktext=data_confirmed.date.to_list()[::60],
                            tickangle=45,
                        )}]),
             dict(label="Recoveries",
                  method='update',
                  args=[{"visible":
                         list(itertools.chain.from_iterable([[False] * 18,
                                                             [True] * 9,
                                                             [False] * 9]))},
                        {'title': 'Covid-19 recoveries',
                         'yaxis': {'title': 'Average number of recoveries'},
                         "xaxis": dict(
                             tickmode="array",
                             tickvals=data_recoveries.date.to_list()[::60],
                             ticktext=data_recoveries.date.to_list()[::60],
                             tickangle=45,
                         )}]),
             dict(label="Vaccinations",
                  method='update',
                  args=[{"visible":
                         list(itertools.chain.from_iterable([[False] * 27, [True] * 9]))},
                        {'title': 'Covid-19 vaccinations',
                         'yaxis': {'title': 'Average number of vaccinations'},
                         "xaxis": dict(
                             tickmode="array",
                             tickvals=data_vaccination.date.to_list()[::60],
                             ticktext=data_vaccination.date.to_list()[::60],
                             tickangle=45,
                         )}]),
         ]),
         )
]

fig.update_layout(
    title={
        'text': "Covid-19 cases in South African provinces",
        'x': 0.5,
        'y': 0.92,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},
    xaxis_title="Date",
    yaxis_title="Average number of cases",
    legend_title="Provinces",
    font=dict(size=16),
    font_color="black",
    updatemenus=updatemenus
)

fig.update_layout(xaxis=dict(
    tickmode="array",
    tickvals=data_deaths["date"].to_list()[::60],
    ticktext=data_deaths["date"].to_list()[::60],
    tickangle=45,
))

save_or_display_html(fig, "provinces_cases")
