import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import get_country_averages

"""Może lepiej dwie- lb testów i pozytywne
covid19za_provincial_timeline_testing.csv
"""
data = pd.read_csv("../data/covid19za_provincial_timeline_testing_positivityrate.csv")
data["YYYYMMDD"] = pd.to_datetime(data["YYYYMMDD"], format='%Y%m%d')

data = get_country_averages(data, ["Total"])
data = data.melt(id_vars=["YYYYMMDD"], value_name="Positive", var_name="Province")
data["date"] = data["YYYYMMDD"].dt.date.astype("str")

data_total = data[data.Province == "Total7"]

print(data)

sns.lineplot(data=data_total, x="date", y="Positive", hue="Province")
plt.show()
#sns.show()
