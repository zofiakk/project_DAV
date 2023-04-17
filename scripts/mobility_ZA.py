import pandas as pd
import plotly.graph_objects as go
from utils import save_or_display_html

mobility_ZA = pd.read_csv("../data/mobility/ZA_moblility.csv")
mobility_ZA = mobility_ZA.loc[mobility_ZA.sub_region_1.isnull(), :]

colors = (['indianred']*2+['lightsalmon']*5)*12*12 + ['indianred']

fig = go.Figure()

fig.add_traces(go.Bar(
    x=mobility_ZA.date,
    y=mobility_ZA.retail_and_recreation_percent_change_from_baseline,
    hovertemplate= "Date: %{x}<br>" + \
                    "% change in mobility: %{y}<br>" + \
                    "<extra></extra>",
    marker_color=colors 
))

fig.add_traces(go.Bar(
    x=mobility_ZA.date,
    y=mobility_ZA.grocery_and_pharmacy_percent_change_from_baseline,
    hovertemplate= "Date: %{x}<br>" + \
                    "% change in mobility: %{y}<br>" + \
                    "<extra></extra>",
    visible = False,
    marker_color=colors 
))

fig.add_traces(go.Bar(
    x=mobility_ZA.date,
    y=mobility_ZA.parks_percent_change_from_baseline,
    hovertemplate= "Date: %{x}<br>" + \
                    "% change in mobility: %{y}<br>" + \
                    "<extra></extra>",
    visible = False,
    marker_color=colors 
))


fig.add_traces(go.Bar(
    x=mobility_ZA.date,
    y=mobility_ZA.transit_stations_percent_change_from_baseline,
    hovertemplate= "Date: %{x}<br>" + \
                    "% change in mobility: %{y}<br>" + \
                    "<extra></extra>",
    visible = False,
    marker_color=colors 
))

fig.add_traces(go.Bar(
    x=mobility_ZA.date,
    y=mobility_ZA.workplaces_percent_change_from_baseline,
    hovertemplate= "Date: %{x}<br>" + \
                    "% change in mobility: %{y}<br>" + \
                    "<extra></extra>",
    visible = False,
    marker_color=colors 
))

fig.add_traces(go.Bar(
    x=mobility_ZA.date,
    y=mobility_ZA.residential_percent_change_from_baseline,
    hovertemplate= "Date: %{x}<br>" + \
                    "% change in mobility: %{y}<br>" + \
                    "<extra></extra>",
    visible = False,
    marker_color=colors 
))

updatemenus = list([
    dict(active=1,
         yanchor="top",
         xanchor="left",
         x=0.0,
         y=1.15,
         buttons=list([
            dict(label='Retail & Recreation',
                 method='update',
                 args=[{'visible': [True, False, False, False, False, False]},
                       {'title': 'Retail & Recreation Mobility Change From Baseline'}]),
            dict(label='Grocery & Pharmacy',
                 method='update',
                 args=[{'visible': [False, True, False, False, False, False]},
                       {'title': 'Grocery & Pharmacy Mobility Change From Baseline'}]),
             dict(label='Parks',
                 method='update',
                 args=[{'visible': [False, False, True, False, False, False]},
                       {'title': 'Parks Mobility Change From Baseline'}]),
             dict(label='Transit Stations',
                 method='update',
                 args=[{'visible': [False, False, False, True, False, False]},
                       {'title': 'Transit Stations Mobility Change From Baseline'}]),
             dict(label='Workplaces',
                 method='update',
                 args=[{'visible': [False, False, False, False, True, False]},
                       {'title': 'Workplaces Mobility Change From Baseline'}]),
             dict(label='Residential',
                 method='update',
                 args=[{'visible': [False, False, False, False, False, True]},
                       {'title': 'Residential Mobility Change From Baseline'}]),
            ]),
        )
    ])

fig.update_layout(
    updatemenus = updatemenus,
    font=dict(size=18),
    xaxis_title="Dates",
    yaxis_title="Percentage of change",
    title={
        'text': "Mobility report",
        'x':0.5,
        'y':0.95,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}})

dates = mobility_ZA.date.to_list()
#dates.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%d"))
chosen = dates[0::60]
fig.update_layout(xaxis=dict(
        tickmode="array",
        tickvals=chosen,
        ticktext=chosen,
        tickangle=45,
    ))

save_or_display_html(fig, "mobility")

