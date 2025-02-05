# HDF4 Processor  

## Overview  
**HDF4 Processor** is a Python tool designed for extracting, processing, and visualising satellite data stored in HDF4 format. It supports geospatial metadata parsing, dataset extraction, and mapping using Cartopy.  

## Features  
- Parses metadata from HDF4 XML files.  
- Reads dataset contents from HDF4 files.  
- Visualises geospatial data on a map.  
- Modular structure for easy maintenance and extension.  

## Installation  
Ensure you have Python installed, then install the required dependencies:  
```sh
pip install -r requirements.txt
```

## Usage
Edit the file paths (metadata and dataset) in `config.py`.
Run the main script:
```sh
python main.py
```
The script will parse metadata, extract the dataset, and generate a visualisation.

## Visualisation example
RCCM category count dataset plot for files in `/sample_data`:

![RCCM category count dataset plot](/sample_data/plot_example.png)