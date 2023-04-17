import pandas as pd
import calendar

data = pd.read_csv("../data/data_download_file_reference_2020.csv",sep=",")
print(data.shape)
neighbours = ["South Africa", "Namibia", "Botswana", "Zimbabwe", "Eswatini", "Global", "Lesotho"]
data = data[data["location_name"].isin(neighbours)]
print(data.shape)

data.to_csv("../data/data_download_file_reference_2020_new.csv")