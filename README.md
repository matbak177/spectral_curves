# spectral_curves

## Summary
The script creates line graphs for the twelve bands of Sentinel 2 for objects(deciduous forest,coniferous forest,grass,building,stagnant water,flowing water) over a given time period.
The tool allows you to assess in which period and with the use of which bands the greatest difference in pixel value is

## How it's working
Download rasters in a place specified by you, at a specified time. Create polygons for different objects. Turn on the script for ArcMap and then the script for visualization

## Setup
Download all files and put them in a folder. Change the path in the script and run

## Data Source
* raster (Sentinel-2) - https://finder.creodias.eu/ 

## Technologies
* Python 2.7/3.8 - library: pandas,numpy,matplotlib,simpledbf,arcpy,os
* ArcMap 10.6
