"""ZA neighbors masks

Script which creates interactive line plot showing
the predicted percentage of population which uses
the masks during the pandemic
"""
import plotly.graph_objs as go
from utils import save_or_display_html, get_masks_data

# Get the data
data = get_masks_data()

neighbours = ["South Africa", "Namibia",
              "Botswana", "Zimbabwe", "Eswatini", "Lesotho"]

fig = go.Figure()

# Add scatter for each country
for country, data_for_country in data.groupby("location_name"):
    if country in neighbours:
        fig.add_scatter(x=data_for_country.date,
                        y=data_for_country.mask_use_mean * 100,
                        name=country, mode='lines',
                        hovertemplate="Date: %{x}<br>" +
                        "Masks usage percentage: %{y}%<br>" +
                        "<extra></extra>",
                        line=dict(width=2))

# Add the worldwide data
data_global = data[data["location_name"] == "Global"]
fig.add_scatter(x=data_global.date,
                y=data_global.mask_use_mean * 100,
                name="Global", mode='lines',
                hovertemplate="Date: %{x}<br>" +
                "Masks usage percentage: %{y}%<br>" +
                "<extra></extra>",
                line=dict(width=2))

# Modify the xaxis ticks
dates = data[data["location_name"] == "South Africa"].date.to_list()
chosen = dates[0::60]
fig.update_layout(xaxis=dict(
    tickmode="array",
    tickvals=chosen,
    ticktext=chosen,
    tickangle=45,
))

# Modify the plot layout
fig.update_layout(
    font=dict(size=15),
    xaxis_title="Date",
    yaxis_title="Percentage of population [%]",
    legend_title_text='Country',
    title={
        'text': "Estimated mask usage",
        'x': 0.5,
        'y': 0.92,
        'xanchor': 'center',
        'yanchor': 'top',
        "font": {"size": 25}},)

save_or_display_html(fig, "masks")
