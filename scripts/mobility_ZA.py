"""Mobility ZA

Script which creates interactive bar plot showing
changes in mobility in South Africa during the Covid pandemic
"""

import pandas as pd
import plotly.graph_objects as go
from utils import save_or_display_html

# Read the data and choose the columns pertaining the whole country
mobility_ZA = pd.read_csv("../data/ZA_moblility.csv")
mobility_ZA = mobility_ZA.loc[mobility_ZA.sub_region_1.isnull(), :]

# Create the colors list- weekends and weekdays in different colors
colors = (['red']*2+['orange']*5)*12*12 + ['red']

# Create the plot
fig = go.Figure()

# Add separate traces
fig.add_traces(go.Bar(
    x=mobility_ZA.date,
    y=mobility_ZA.retail_and_recreation_percent_change_from_baseline,
    hovertemplate="Date: %{x}<br>" +
    "% change in mobility: %{y}<br>" +
    "<extra></extra>",
    marker_color=colors
))

fig.add_traces(go.Bar(
    x=mobility_ZA.date,
    y=mobility_ZA.grocery_and_pharmacy_percent_change_from_baseline,
    hovertemplate="Date: %{x}<br>" +
    "% change in mobility: %{y}<br>" +
    "<extra></extra>",
    visible=False,
    marker_color=colors
))

fig.add_traces(go.Bar(
    x=mobility_ZA.date,
    y=mobility_ZA.parks_percent_change_from_baseline,
    hovertemplate="Date: %{x}<br>" +
    "% change in mobility: %{y}<br>" +
    "<extra></extra>",
    visible=False,
    marker_color=colors
))


fig.add_traces(go.Bar(
    x=mobility_ZA.date,
    y=mobility_ZA.transit_stations_percent_change_from_baseline,
    hovertemplate="Date: %{x}<br>" +
    "% change in mobility: %{y}<br>" +
    "<extra></extra>",
    visible=False,
    marker_color=colors
))

fig.add_traces(go.Bar(
    x=mobility_ZA.date,
    y=mobility_ZA.workplaces_percent_change_from_baseline,
    hovertemplate="Date: %{x}<br>" +
    "% change in mobility: %{y}<br>" +
    "<extra></extra>",
    visible=False,
    marker_color=colors
))

fig.add_traces(go.Bar(
    x=mobility_ZA.date,
    y=mobility_ZA.residential_percent_change_from_baseline,
    hovertemplate="Date: %{x}<br>" +
    "% change in mobility: %{y}<br>" +
    "<extra></extra>",
    visible=False,
    marker_color=colors
))

# Create the drop down menu
updatemenus = list([
    dict(active=0,
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

# Update the plot layout
fig.update_layout(
    updatemenus=updatemenus,
    font=dict(size=18),
    xaxis_title="Dates",
    yaxis_title="Percentage of change",
    title={
        'text': "Retail & Recreation Mobility Change From Baseline",
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}})

# Modify the xaxis ticksF
dates = mobility_ZA.date.to_list()
chosen = dates[0::60]
fig.update_layout(xaxis=dict(
    tickmode="array",
    tickvals=chosen,
    ticktext=chosen,
    tickangle=45,
))

save_or_display_html(fig, "mobility")
