import pandas as pd
import sys


def get_smaller_data(data:pd.DataFrame, every_nth:int=7):
    # Get only one date per week
    dates = sorted(list(set(data["date"].to_list())))[::every_nth]
    df_map = data[data["date"].isin(dates)]
    return df_map

def get_some_countries(data:pd.DataFrame, names:list):
    new_data = data[data["location"].isin(names)]
    return new_data

def get_provincial_averages(data:pd.DataFrame, provinces:list):
    for province in provinces:
        data[province+"7"] = data[province].rolling(7).mean().round()
        data[province+"30"] = data[province].rolling(30).mean().round()
    return data


def get_country_averages(data:pd.DataFrame, column_names:list):
    for column in column_names:
        data[column+"7"] = data[column].rolling(7).mean().round(2)
        data[column+"30"] = data[column].rolling(30).mean().round(2)
    return data


def save_or_display_html(fig, name:str):
    args = sys.argv
    if len(args) > 1:
        print(name)
        if args[1] == "1":
            path = "../images/"
            fig.write_html(f"{path}{name}.html")
            print(f"The plot was saved to {path}{name}.html")
        else:
            fig.show()
    else:
        fig.show()

def get_masks_data():
    data_2020 = pd.read_csv("../data/data_download_file_reference_2020_new.csv")
    data_2021 = pd.read_csv("../data/data_download_file_reference_2021_new.csv")
    data_2022 = pd.read_csv("../data/data_download_file_reference_2022_new.csv")

    data_2020 = data_2020[["location_name", "date", "mask_use_mean"]]
    data_2021 = data_2021[["location_name", "date", "mask_use_mean"]]
    data_2022 = data_2022[["location_name", "date", "mask_use_mean"]]
    data = pd.concat([data_2020, data_2021, data_2022], axis=0)
    data = data.sort_values(by=["location_name", "date"])
    data = data.reset_index()
    return data

def get_economy_data():
    data = pd.read_csv("../data/WEO_data.csv", sep=";")
    data = data[["Country", "Subject Descriptor", "Units", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]]
    data = data[data["Subject Descriptor"].isin(["Gross domestic product, current prices",
                                                  "Volume of exports of goods",
                                                  "Volume of Imports of goods",
                                                  "Inflation, average consumer prices",
                                                  "General government gross debt"])]
    print(data)
    data["change"] = data.apply(lambda row: 100 - (float(row["2021"].replace(",", "")) / float(row["2018"].replace(",", "")) * 100), axis=1)
    return data