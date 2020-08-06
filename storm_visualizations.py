"""
Author: Cristopher Masserini
Date Created: 07/31/2020

This project is designed to be a detailed dashboard of the history of severe storms in the Atlantic Basin.
The data is provided by NOAA HURDAT2 (https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2019-052520.txt)
which has data from 1851 to 2019.

This file is for creating the visualization of the storm data processed in the data_processing.py file.
These visualizations are designed to be used either with the dashboard of independently.

This uses geopandas and descartes which may need additional installation.
"""

# ---- Imports ----
import data_import as di
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import descartes
from shapely.geometry import Point, Polygon



# ---- Functionality ----
"""
Creates a plot of the world showing the longitude and latitude  of the storms in the data frame provided.
"""


def world_plot(df: pd.DataFrame):
    # First we set the Coordinate Reference System (https://geopandas.org/projections.html)
    crs = {'init', 'EPSG:4326'}

    # Next, we put the longitude and latitude into points so geopandas can understand it
    lon_lat = [Point(point) for point in zip(df['storm_lon'], df['storm_lat'])]


if __name__ == "__main__":
    _, details = di.retrieve()
    storm_landfall = di.field_filter(details, "land", 1)

    world = gpd.read_file(
        gpd.datasets.get_path('naturalearth_lowres')
    )

    # First we set the Coordinate Reference System (https://geopandas.org/projections.html)
    crs = {'init': 'epsg:4326'}

    # Next, we put the longitude and latitude into points so geopandas can understand it
    lon_lat = [Point(point) for point in zip(storm_landfall['storm_lon'], storm_landfall['storm_lat'])]

    df = gpd.GeoDataFrame(storm_landfall, crs=crs, geometry=lon_lat)

    fig, ax = plt.subplots(figsize=(15, 15))
    world.plot(ax=ax, alpha=0.8)

    storm_landfall[storm_landfall["storm_type"] == "HU"].plot(ax=ax, markersize=10, color="red", marker="x", label="Landfall")
    storm_landfall[storm_landfall["storm_type"] != "HU"].plot(ax=ax, markersize=10, color="red", marker="x", label="Landfall")

    plt.show()

    print(world)

    # world_plot(storm_landfall)
