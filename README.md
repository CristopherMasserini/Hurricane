# Hurricane
A detailed dashboard of the history of severe storms in the Atlantic Basin. The data is provided by NOAA HURDAT2 (https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2019-052520.txt) which has data from 1851 to 2019.

# Files
## data_import
This file is for the importing of the data from the NOAA site provided. The data is in comma-separated format
with an odd structure (no titles and a row for the name of the storm before the important data). This requires
cleaning of the data to put it in the proper format for a dashboard and visualizations.

## storm_visualizations
This file is for creating the visualization of the storm data processed in the data_processing.py file.
These visualizations are designed to be used either with the dashboard of independently.

The file uses the plotly library for the geo-plotting. This may require additional installation.
