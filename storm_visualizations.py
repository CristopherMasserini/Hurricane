"""
Author: Cristopher Masserini
Date Created: 07/31/2020

This project is designed to be a detailed dashboard of the history of severe storms in the Atlantic Basin.
The data is provided by NOAA HURDAT2 (https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2019-052520.txt)
which has data from 1851 to 2019.

This file is for creating the visualization of the storm data processed in the data_processing.py file.
These visualizations are designed to be used either with the dashboard of independently.

The file uses the plotly library for the geo-plotting. This may require additional installation.
"""

# ---- Imports ----
import data_import as di
import pandas as pd
import plotly as ply


# ---- Functionality ----
def world_plot(df: pd.DataFrame):
    data = dict(
        type='choropleth',
        locations=df['CountryCode'],
        z=df['Store Count'],
        text=df['Brand'],
        colorbar={'title': 'Starbucks Stores - World Wide'},
    )
    layout = dict(
        title='Stores Count',
        geo=dict(
            showframe=False,
            projection={'type': 'natural earth'}
        )
    )

    choromap = ply.go.Figure(data=[data], layout=layout)
    ply.iplot(choromap)


if __name__ == "__main__":
    basics, details = di.retrieve()
