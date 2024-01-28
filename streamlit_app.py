import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import folium
import geopandas as gpd
import requests
import io

# Create a map centered on the UK
uk_map = folium.Map(location=[54.7023545, -3.2765753], zoom_start=6)

# Display the map
uk_map

# Create a map centered on Cornwall and Devon
cornwall_devon_map = folium.Map(location=[50.5, -4.5], zoom_start=9)

# Display the map
cornwall_devon_map

# Replace 'file_path.gpkg' with the actual file path of your geopackage
file_path = 'pdbayes/streamlit-example/codepo_gb.gpkg'

# Load the geopackage into a GeoPandas dataframe
gdf = gpd.read_file(file_path)