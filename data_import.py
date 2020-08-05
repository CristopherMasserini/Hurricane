"""
Author: Cristopher Masserini
Date Created: 07/29/2020

This project is designed to be a detailed dashboard of the history of severe storms in the Atlantic Basin.
The data is provided by NOAA HURDAT2 (https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2019-052520.txt)
which has data from 1851 to 2019.

This file is for the importing of the data from the NOAA site provided. The data is in comma-separated format
with an odd structure (no titles and a row for the name of the storm before the important data). This requires
cleaning of the data to put it in the proper format for a dashboard and visualizations.
"""

# ---- Imports ----
import requests as rq
import pandas as pd
import datetime as dt

# ---- Scrapping ----
"""
retrieve()

This function retrieves the data from the NOAA website. It then cleans the data and puts it into two
pandas data frames.

One data frame is called storm_basics. This includes the storm code and the name of the storm.

The second data frame is called storm_details. This includes the storm code, the status of the storm, 
the date and time of that measurement, latitude of that measurement, longitude of that measurement, 
if that measurement was made for landfall (0 for no, 1 for yes), and finally the best_track_index 
is the best track entry for that storm (1st index refers to first measurement).  

Returns a tuple of the two data frames
"""


def retrieve() -> tuple:
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

    index = 1

    # Takes the input from raw_data line by line and puts it into the correct data frames
    for line in raw_data.iter_lines():
        if line:
            line_str = line.decode("utf-8")
            if line_str[0] == "A":
                # Code of the storm
                storm_code.append(line_str[0:8].strip())

                # Name of the storm
                storm_name.append(line_str[9:28].strip())

                # Resetting the index
                index = 1
            else:
                # Code of the storm
                storm_code_details.append(storm_code[-1])

                # Storm type at that best track entry
                storm_type.append(line_str[19:21].strip())

                # Date and time of the best track entry
                date = line_str[0:8]
                time = line_str[10:14]
                date_time.append(dt.datetime.strptime(f"{date} {time}", "%Y%m%d %H%M"))

                # Latitude of the storm of the best track entry
                storm_lat.append(float(line_str[23:27].strip()))

                # Longitude of the storm of the best track entry
                storm_lon.append(-float(line_str[30:35].strip()))

                # If the storm made landfall at the best track entry
                land_str = line_str[16].strip()
                if land_str != "L":
                    land.append(0)
                else:
                    land.append(1)

                # Counting the index of the best track entry for the storm
                indexes.append(index)
                index += 1

    # Creating the data frames
    hurricane_basics = pd.DataFrame(data={"storm_code": storm_code, "storm_name": storm_name})
    hurricane_details = pd.DataFrame(data={"storm_code": storm_code_details, "storm_type": storm_type,
                                           "data_time": date_time, "storm_lat": storm_lat,
                                           "storm_lon": storm_lon, "land": land, "best_track_index": indexes})

    # Returning the data frames
    return hurricane_basics, hurricane_details


"""
field_filter()

Adds the ability to easily filter the data frames
df is the data frame to filter, field is the field to be filtered on, 
and value is the value the field should have

Returns the filtered data frame
"""


def field_filter(df: pd.DataFrame, field: str, value: str) -> pd.DataFrame:
    return df[df[field] == value]


if __name__ == "__main__":
    basics, details = retrieve()

    storm_creation = field_filter(details, "best_track_index", 1)
    storm_landfall = field_filter(details, "land", 1)

    basics.to_csv("storm_basics.csv", index=False)
    details.to_csv("storm_details.csv", index=False)
    storm_creation.to_csv("storm_creation.csv", index=False)
    storm_landfall.to_csv("storm_landfall.csv", index=False)

