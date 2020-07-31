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
"""
This function retrieves the data from the NOAA website. It then cleans the data and puts it into two
pandas data frames.

One data frame is called storm_basics. This includes the storm code and the name of the storm.

The second data frame is called storm_details. This includes the storm code, the status of the storm, 
the date and time of that measurement, latitude of that measurement, longitude of that measurement, 
if that measurement was made for landfall (0 for no, 1 for yes), and finally the number measurement that was
for the storm (0th index refers to first measurement).  
"""
# def retrieve() -> tuple:
def retrieve():
    raw_data = rq.get("https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2019-052520.txt", stream=True)

    storm_code = list()
    storm_name = list()

    storm_code_details = list()
    storm_type = list()
    date_time = list()
    storm_lat = list()
    storm_lon = list()
    land = list()
    indexes = list()

    index = 0

    # Takes the input from raw_data line by line and puts it into the correct data frames
    for line in raw_data.iter_lines():
        if line:
            line_str = line.decode("utf-8")
            if line_str[0] == "A":
                storm_name.append(line_str[9:28].strip())
                storm_code.append(line_str[0:8].strip())
                index = 0
            else:
                storm_code_details.append(storm_code[-1])

                storm_type.append(line_str[19:21].strip())

                date = line_str[0:8]
                time = line_str[10:14]
                date_time.append(dt.datetime.strptime(f"{date} {time}", "%Y%m%d %H%M"))

                storm_lat.append(line_str[23:28].strip())

                storm_lon.append(line_str[30:36].strip())

                land_str = line_str[16].strip()
                if land_str != "L":
                    land.append(0)
                else:
                    land.append(1)

                indexes.appened(index)
                index += 1

    # hurricane_basics = pd.DataFrame(data={"storm_code": storm_code, "storm_name": storm_name})
    # return raw_data


if __name__ == "__main__":
    retrieve()
