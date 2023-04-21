"""ZA survey

Function which creates interactive bar plot showing
the survey results obtained in South Africa
"""

import pandas as pd
from utils import save_or_display_html
import plotly.graph_objects as go

# Read the data
data = pd.read_csv("../data/geopoll-coronavirus-round2-data_weighted_2020-04-30_final.csv",
                   sep=";",
                   encoding='latin-1')

# Categories on which the results will be separated and their colors
genders = ['Female', 'Male', 'Other']
ages = ['15-25', '26-35', '36+']
colors = {
    "Ages": {
        '15-25': "#FADD75",
        '26-35': "#F28F1D",
        '36+': "#F6C619",
    },
    "Genders": {
        "Female": "#2B6045",
        "Male": "#5EB88A",
        "Other": "#9ED4B9",
    }
}

# Biggest Concerns- data
index = list(set(data["Concerns"].to_list()))
y_data_ages = []
y_data_genders = []
for concern in index:
    data_concern = data[data["Concerns"] == concern]
    y = []
    y_gender = []
    for age in ages:
        y.append(
            round(
                data_concern[data_concern["Age Group"] == age].shape[0]/data.shape[0]*100, 2))
    for gender in genders:
        y_gender.append(
            round(
                data_concern[data_concern["Gender"] == gender].shape[0]/data.shape[0]*100, 2))
    y_data_ages.append(y)
    y_data_genders.append(y_gender)

df = pd.concat(
    [pd.DataFrame(
        y_data_ages,
        index=index,
        columns=ages),
     pd.DataFrame(
        y_data_genders,
        index=index,
        columns=genders)],
    axis=1,
    keys=["Ages", "Genders"]
)

# Create the figure and change its layout
fig = go.Figure(
    layout=go.Layout(
        barmode="relative",
        yaxis2=go.layout.YAxis(
            visible=False,
            matches="y",
            overlaying="y",
            anchor="x",
        ),
        font=dict(size=18),
        legend_x=1.01,
        legend_y=1.01,
        xaxis_title="Response",
        yaxis_title="Percentage of responders",
        title={
            'text': "What concerns you the most about Coronavirus?",
            'x': 0.5,
            'y': 0.92,
            'xanchor': 'center',
            'yanchor': 'top',
            "font": {"size": 20}},
    )
)


# Biggest concerns- add bars
for i, t in enumerate(colors):
    for j, col in enumerate(df[t].columns):
        if (df[t][col] == 0).all():
            continue
        fig.add_bar(
            x=df.index,
            y=df[t][col],
            yaxis=f"y{i + 1}",
            offsetgroup=str(i),
            width=2/5,
            offset=(i - 1) * 2/5,
            legendgroup=t,
            legendgrouptitle_text=t,
            name=col,
            marker_color=colors[t][col],
            marker_line=dict(width=1, color="#333"),
            hovertemplate="Response:%{x}<br>%{y}%<extra></extra>"
        )

# Risk Awareness- data
index = list(set(data["RiskAwareness"].to_list()))
y_data_ages = []
y_data_genders = []
for risk in index:
    data_concern = data[data["RiskAwareness"] == risk]
    y = []
    y_gender = []
    for age in ages:
        y.append(round(
            data_concern[data_concern["Age Group"] == age].shape[0]/data.shape[0]*100, 2))
    for gender in genders:
        y_gender.append(round(
            data_concern[data_concern["Gender"] == gender].shape[0]/data.shape[0]*100, 2))
    y_data_ages.append(y)
    y_data_genders.append(y_gender)

df = pd.concat(
    [pd.DataFrame(
        y_data_ages,
        index=index,
        columns=ages),
     pd.DataFrame(
        y_data_genders,
        index=index,
        columns=genders)],
    axis=1,
    keys=["Ages", "Genders"]
)

# Risk Awareness- add bars
for i, t in enumerate(colors):
    for j, col in enumerate(df[t].columns):
        if (df[t][col] == 0).all():
            continue
        fig.add_bar(
            x=df.index,
            y=df[t][col],
            yaxis=f"y{i + 1}",
            offsetgroup=str(i),
            width=2/5,
            offset=(i - 1) * 2/5,
            legendgroup=t,
            legendgrouptitle_text=t,
            name=col,
            marker_color=colors[t][col],
            marker_line=dict(width=1, color="#333"),
            hovertemplate="Response:%{x}<br>%{y}%<extra></extra>",
            visible=False
        )

# HealthBehavior- data
index = list(set(data["HealthBehavior"].to_list()))
y_data_ages = []
y_data_genders = []
for risk in index:
    data_concern = data[data["HealthBehavior"] == risk]
    y = []
    y_gender = []
    for age in ages:
        y.append(round(
            data_concern[data_concern["Age Group"] == age].shape[0]/data.shape[0]*100, 2))
    for gender in genders:
        y_gender.append(round(
            data_concern[data_concern["Gender"] == gender].shape[0]/data.shape[0]*100, 2))
    y_data_ages.append(y)
    y_data_genders.append(y_gender)

df = pd.concat(
    [pd.DataFrame(
        y_data_ages,
        index=index,
        columns=ages),
     pd.DataFrame(
        y_data_genders,
        index=index,
        columns=genders)],
    axis=1,
    keys=["Ages", "Genders"]
)

# HealthBehavior- add bars
for i, t in enumerate(colors):
    for j, col in enumerate(df[t].columns):
        if (df[t][col] == 0).all():
            continue
        fig.add_bar(
            x=df.index,
            y=df[t][col],
            yaxis=f"y{i + 1}",
            offsetgroup=str(i),
            width=2/5,
            offset=(i - 1) * 2/5,
            legendgroup=t,
            legendgrouptitle_text=t,
            name=col,
            marker_color=colors[t][col],
            marker_line=dict(width=1, color="#333"),
            hovertemplate="Response:%{x}<br>%{y}%<extra></extra>",
            visible=False
        )

# GovernmentTrust- data
index = list(set(data["GovernmentTrust"].to_list()))
y_data_ages = []
y_data_genders = []
for risk in index:
    data_concern = data[data["GovernmentTrust"] == risk]
    y = []
    y_gender = []
    for age in ages:
        y.append(round(
            data_concern[data_concern["Age Group"] == age].shape[0]/data.shape[0]*100, 2))
    for gender in genders:
        y_gender.append(round(
            data_concern[data_concern["Gender"] == gender].shape[0]/data.shape[0]*100, 2))
    y_data_ages.append(y)
    y_data_genders.append(y_gender)

df = pd.concat(
    [pd.DataFrame(
        y_data_ages,
        index=index,
        columns=ages),
     pd.DataFrame(
        y_data_genders,
        index=index,
        columns=genders)],
    axis=1,
    keys=["Ages", "Genders"]
)

# GovernmentTrust- add bars
for i, t in enumerate(colors):
    for j, col in enumerate(df[t].columns):
        if (df[t][col] == 0).all():
            continue
        fig.add_bar(
            x=df.index,
            y=df[t][col],
            yaxis=f"y{i + 1}",
            offsetgroup=str(i),
            width=2/5,
            offset=(i - 1) * 2/5,
            legendgroup=t,
            legendgrouptitle_text=t,
            name=col,
            marker_color=colors[t][col],
            marker_line=dict(width=1, color="#333"),
            hovertemplate="Response:%{x}<br>%{y}%<extra></extra>",
            visible=False
        )

# SocialMedia- data
index = list(set(data["SocialMedia"].to_list()))
y_data_ages = []
y_data_genders = []
for risk in index:
    data_concern = data[data["SocialMedia"] == risk]
    y = []
    y_gender = []
    for age in ages:
        y.append(round(
            data_concern[data_concern["Age Group"] == age].shape[0]/data.shape[0]*100, 2))
    for gender in genders:
        y_gender.append(round(
            data_concern[data_concern["Gender"] == gender].shape[0]/data.shape[0]*100, 2))
    y_data_ages.append(y)
    y_data_genders.append(y_gender)

df = pd.concat(
    [pd.DataFrame(
        y_data_ages,
        index=index,
        columns=ages),
     pd.DataFrame(
        y_data_genders,
        index=index,
        columns=genders)],
    axis=1,
    keys=["Ages", "Genders"])

# SocialMedia- add bars
for i, t in enumerate(colors):
    for j, col in enumerate(df[t].columns):
        if (df[t][col] == 0).all():
            continue
        fig.add_bar(
            x=df.index,
            y=df[t][col],
            yaxis=f"y{i + 1}",
            offsetgroup=str(i),
            width=2/5,
            offset=(i - 1) * 2/5,
            legendgroup=t,
            legendgrouptitle_text=t,
            name=col,
            marker_color=colors[t][col],
            marker_line=dict(width=1, color="#333"),
            hovertemplate="Response:%{x}<br>%{y}%<extra></extra>",
            visible=False
        )

# MediaConsumption- data
index = list(set(data["MediaConsumption"].to_list()))
y_data_ages = []
y_data_genders = []
for risk in index:
    data_concern = data[data["MediaConsumption"] == risk]
    y = []
    y_gender = []
    for age in ages:
        y.append(round(
            data_concern[data_concern["Age Group"] == age].shape[0]/data.shape[0]*100, 2))
    for gender in genders:
        y_gender.append(round(
            data_concern[data_concern["Gender"] == gender].shape[0]/data.shape[0]*100, 2))
    y_data_ages.append(y)
    y_data_genders.append(y_gender)

df = pd.concat(
    [pd.DataFrame(
        y_data_ages,
        index=index,
        columns=ages),
     pd.DataFrame(
        y_data_genders,
        index=index,
        columns=genders)],
    axis=1,
    keys=["Ages", "Genders"]
)

# MediaConsumption- add bars
for i, t in enumerate(colors):
    for j, col in enumerate(df[t].columns):
        if (df[t][col] == 0).all():
            continue
        fig.add_bar(
            x=df.index,
            y=df[t][col],
            yaxis=f"y{i + 1}",
            offsetgroup=str(i),
            width=2/5,
            offset=(i - 1) * 2/5,
            legendgroup=t,
            legendgrouptitle_text=t,
            name=col,
            marker_color=colors[t][col],
            marker_line=dict(width=1, color="#333"),
            hovertemplate="Response:%{x}<br>%{y}%<extra></extra>",
            visible=False
        )

# Create the dropdown menu
updatemenus = list([
    dict(active=0,
         yanchor="top",
         x=0.0,
         xanchor="left",
         y=1.15,
         buttons=list([
             dict(label='Biggest concerns',
                  method='update',
                  args=[{'visible': [True, True, True, True, True,
                                     False, False, False, False, False,
                                     False, False, False, False, False,
                                     False, False, False, False, False,
                                     False, False, False, False, False,
                                     False, False, False, False, False, ]},
                        {'title': 'What concerns you the most about Coronavirus?'}
                        ]),
             dict(label='Risk Awareness',
                  method='update',
                  args=[{'visible': [False, False, False, False, False,
                                     True, True, True, True, True,
                                     False, False, False, False, False,
                                     False, False, False, False, False,
                                     False, False, False, False, False, ]},
                        {'title': 'Do you believe that you or your family are at risk?'}]),
             dict(label='Healthcare',
                  method='update',
                  args=[{'visible': [False, False, False, False, False,
                                     False, False, False, False, False,
                                     True, True, True, True, True,
                                     False, False, False, False, False,
                                     False, False, False, False, False,
                                     False, False, False, False, False, ]},
                        {'title': 'What would you do if you showed mild symptoms?'}]),
             dict(label='Government',
                  method='update',
                  args=[{'visible': [False, False, False, False, False,
                                     False, False, False, False, False,
                                     False, False, False, False, False,
                                     True, True, True, True, True,
                                     False, False, False, False, False,
                                     False, False, False, False, False, ]},
                        {'title':
                         'On the scale of 1-5, where 1=Strongly disagree & 5=Strongly agree<br>rate your agreement with <br>"My government has done enough to stop the spread of the virus"'}]),
             dict(label='Social media',
                  method='update',
                  args=[{'visible': [False, False, False, False, False,
                                     False, False, False, False, False,
                                     False, False, False, False, False,
                                     False, False, False, False, False,
                                     True, True, True, True, True,
                                     False, False, False, False, False, ]},
                        {'title': 'Where are you getting information on social media?'}]),
             dict(label='Media consumption',
                  method='update',
                  args=[{'visible': [False, False, False, False, False,
                                     False, False, False, False, False,
                                     False, False, False, False, False,
                                     False, False, False, False, False,
                                     False, False, False, False, False,
                                     True, True, True, True, True, ]},
                        {'title': 'How has your media consumption changed in the past week?'}]),
         ]),
         )
])
fig.update_layout(updatemenus=updatemenus)

save_or_display_html(fig, "ZA_survey")
