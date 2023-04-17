import pandas as pd
import plotly.graph_objects as go
from utils import get_some_countries, get_country_averages, save_or_display_html


data = pd.read_csv("../data/new_covid_za.csv")

data = get_some_countries(data, ["South Africa"]).fillna(method="ffill")
data = get_country_averages(data,
                            ["new_cases", "new_deaths", "new_tests",
                             "new_vaccinations", "total_cases", "total_deaths",
                             "total_tests", "total_vaccinations"])
fig = go.Figure()

dates = data.date.to_list()
# Daily cases
fig.add_scatter(x=data.date,
                y=data.new_cases7,
                name="Cases",
                mode='lines+markers',
                line=dict(width=2, color = "#1f77b4"),
                marker=dict(size=5, maxdisplayed=90),
                hovertemplate= "Cases: %{y}<br><extra></extra>")

# Daily deaths
fig.add_scatter(x=data.date,
                y=data.new_deaths7,
                name="Deaths",
                mode='lines',
                line=dict(width=2, dash="dash", color = '#d62728'),
                hovertemplate= "Deaths: %{y}<br><extra></extra>")

# Daily tests
fig.add_scatter(x=data.date,
                y=data.new_tests7,
                name="Tests",
                mode='lines',
                line=dict(width=2, color = '#2ca02c'),
                hovertemplate= "Tests: %{y}<br><extra></extra>")

# Daily vaccinations
fig.add_scatter(x=data.date,
                y=data.new_vaccinations7,
                name="Vaccinations",
                mode='lines',
                line=dict(width=2, dash="dot", color = '#9467bd'),
                hovertemplate= "Vaccinations: %{y}<br><extra></extra>")

# Total cases
fig.add_scatter(x=data.date,
                y=data.total_cases7,
                name="Total cases",
                mode='lines+markers',
                line=dict(width=2, color = '#1f77b4'),
                marker=dict(size=5, maxdisplayed=90),
                hovertemplate= "Total cases: %{y}<br><extra></extra>",
                visible=False)

# Total deaths
fig.add_scatter(x=data.date,
                y=data.total_deaths7,
                name="Total deaths",
                mode='lines',
                line=dict(width=2, dash="dash", color = '#d62728'),
                hovertemplate= "Total deaths: %{y}<br><extra></extra>",
                visible=False)

# Total tests
fig.add_scatter(x=data.date,
                y=data["total_tests7"],
                name="Total tests",
                mode='lines',
                line=dict(width=2, color = "#2ca02c"),
                hovertemplate="Total tests: %{y}<br><extra></extra>",
                visible = False)

# Total vaccinations
fig.add_scatter(x=data.date,
                y=data["total_vaccinations7"],
                name="Total vaccinations",
                mode='lines',
                line=dict(width=2, dash="dot", color = '#9467bd'),
                hovertemplate= "Total vaccinations: %{y}<br><extra></extra>",
                visible = False)

updatemenus = list([
    dict(direction="right",
         type = "buttons",
         showactive=True,
         active=1,
         yanchor="top",
         xanchor="left",
         x=0.0,
         y=1.15,
         buttons=list([
            dict(label='Log Scale',
                 method='update',
                 args=[{'visible': [True]*4 + [False]*4},
                       {'yaxis': {'type': 'log'}}]),
            dict(label='Linear Scale',
                 method='update',
                 args=[{'visible':[True]*4 + [False]*4},
                       {'yaxis': {'type': 'linear'}}])
            ]),
        ),
    dict(direction="right",
         type = "buttons",
         showactive=True,
         active=1,
         yanchor="top",
         xanchor="left",
         x=0.0,
         y=1.3,
         buttons=list([
            dict(label='Total',
                 method='update',
                 args=[{'visible': [False]*4 + [True]*4},
                       {'title': 'Covid-19 total cases',
                        'yaxis': {'title': 'Average number of total cases'}}]),
            dict(label='Daily',
                 method='update',
                 args=[{'visible': [True]*4 + [False]*4},
                       {'title': 'Covid-19 daily cases',
                        'yaxis': {'title': 'Average number of daily cases'}}])
            ]),
        )
    
    ])


fig.update_layout(legend_title_text='Case type',
                  hovermode="x",
                  updatemenus=updatemenus,
                  font=dict(size=15),
                  xaxis_title="Date",
                  yaxis_title="Average number of cases",)

fig.update_layout(
    title={
        'text': "Covid-19 cases",
        'x':0.5,
        'y':0.92,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},
    xaxis=dict(
        tickmode="array",
        tickvals=dates[0::90],
        ticktext=dates[0::90],
        tickformat='%Y-%m-%d',
        tickangle=45,
    ),
    font=dict(size=18),)

save_or_display_html(fig, "ZA_covid")
