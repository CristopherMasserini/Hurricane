"""
Author: Cristopher Masserini
Date Created: 07/29/2020

This project is designed to be a detailed dashboard of the history of Hurricane$
The data is provided by NOAA HURDAT2 (https://www.nhc.noaa.gov/data/hurdat/hurd$
which has data from 1851 to 2019.

This file is for the importing of the data from the NOAA site provided. The dat$
with an odd structure (no titles and a row for the name of the storm before the$
cleaning of the data to put it in the proper format for a dashboard and visuali$
"""

# ---- Imports ----
import requests as rq
import pandas as pd


# ---- Scrapping ----
# Retrieves and returns the data from the NOAA website in its raw text form.
def retrieve():
    raw_data = rq.get("https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2019-0$

    for line in raw_data.iter_lines():
        if line:
            print(raw_data.text)

    # return raw_data


if __name__ == "__main__":
    retrieve()
    # print(test)
    # pass
