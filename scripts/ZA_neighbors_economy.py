import plotly.graph_objs as go
import pandas as pd
from utils import save_or_display_html, get_economy_data

data = get_economy_data()
print(data)
neighbours = ["South Africa", "Namibia", "Botswana", "Zimbabwe", "Eswatini", "Lesotho"]

data_grr = data[data["Subject Descriptor"] =="Gross domestic product, current prices"]
data_grr = data_grr[data_grr["Units"] == "U.S. dollars"]
pd.set_option("display.max_columns", None)

print(data[data["Subject Descriptor"] =='Volume of exports of goods'])
fig = go.Figure()
fig.add_trace(go.Bar(x=data_grr["Country"],
                     y=data_grr["change"],
                     name="GDP", visible=True))
fig.add_trace(go.Bar(x=data[data["Subject Descriptor"] =='Volume of exports of goods']["Country"],
                     y=data[data["Subject Descriptor"] =='Volume of exports of goods']["change"],
                     name="Exports of goods", visible=True))
fig.add_trace(go.Bar(x=data[data["Subject Descriptor"] =='Volume of Imports of goods']["Country"],
                     y=data[data["Subject Descriptor"] =='Volume of Imports of goods']["change"],
                     name="Import of goods", visible=True))

save_or_display_html(fig, "economy")