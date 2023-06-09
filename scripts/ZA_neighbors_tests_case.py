"""ZA neighbors tests case

Function which creates interactive line plot showing
average number of tests per confirmed case in
neighboring countries
"""
import plotly.graph_objs as go
import pandas as pd
from utils import save_or_display_html, get_country_averages

# Read the data, choose its subset and calculate the averages
data = pd.read_csv(
    "../data/number-of-covid-19-tests-per-confirmed-case-bar-chart.csv")
neighbours = ["South Africa", "Namibia",
              "Botswana", "Zimbabwe", "Eswatini", "Lesotho"]
data = data[data.Entity.isin(neighbours)]
data = data.fillna(method="ffill")
data = get_country_averages(data, ["cumulative_tests_per_case"])

fig = go.Figure()
# Add scatter for each country
for country, data_for_country in data.groupby("Entity"):
    fig.add_scatter(x=data_for_country.Day,
                    y=data_for_country.cumulative_tests_per_case30,
                    name=country, mode='lines+markers',
                    hovertemplate="Date: %{x}<br>" +
                    "Tests: %{y}<br>" +
                    "<extra></extra>",
                    line=dict(width=2),
                    marker=dict(size=5, maxdisplayed=80),)

# Modify teh xaxis ticks
dates = data[data["Entity"] == "South Africa"].Day.to_list()
chosen = dates[0::60]
fig.update_layout(xaxis=dict(
    tickmode="array",
    tickvals=chosen,
    ticktext=chosen,
    tickangle=45,
))

# Modify the layout
fig.update_layout(
    font=dict(size=15),
    xaxis_title="Date",
    yaxis_title="Average number of tests per case",
    legend_title_text='Country',
    title={
        'text': "Average number of tests per confirmed case",
        'x': 0.5,
        'y': 0.92,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},)

save_or_display_html(fig, "tests_per_case")
