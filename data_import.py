"""
Author: Cristopher Masserini
Date Created: 07/29/2020

This project is designed to be a detailed dashboard of the history of Hurricanes in the Atlantic Basin.
The data is provided by NOAA HURDAT2 (https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2019-052520.txt)
which has data from 1851 to 2019.

This file is for the importing of the data from the NOAA site provided. The data is in comma-seperated format
with an odd structure (no titles and a row for the name of the storm before the important data). This requires
cleaning of the data to put it in the proper format for a dashboard and visualizations.
"""

# ---- Imports ----
import requests as rq
import pandas as pd
import datetime as dt


# ---- Scrapping ----
# Retrieves and returns the data from the NOAA website in its raw text form.
def retrieve():
    raw_data = rq.get("https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2019-052520.txt", stream=True)

    hurricane_code = ""
    hurricane_name = ""
    date_time = ""

    # Takes the input from raw_data line by line and puts it into the correct dataframes
    for line in raw_data.iter_lines():
        if line:
            line_str = line.decode("utf-8")
            if line_str[0] == "A":
                hurricane_name = line_str[9:28].strip()
            else:
                date = line_str[0:8]
                time = line_str[10:14]
                date_time = dt.datetime.strptime(f"{date} {time}", "%Y%m%d %H%M")

        print(hurricane_name)
        print(date_time)

    # return raw_data


if __name__ == "__main__":
    retrieve()
