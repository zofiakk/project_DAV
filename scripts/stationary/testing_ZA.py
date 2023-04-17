import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import get_country_averages


data = pd.read_csv("../data/covid19za_timeline_testing.csv")
data = data[["date", "cumulative_tests","cumulative_tests_private",
             ]]
data = pd.melt(data, "date")
print(data)

sns.lineplot(data=data, x=data["date"], y='value', hue='variable')

plt.show()