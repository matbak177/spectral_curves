import arcpy
import os

folder=r'C:\Users\mati\Desktop\park\2020-05-14' #change path
arcpy.CheckOutExtension("Spatial")
mxd=arcpy.mapping.MapDocument("CURRENT")

in_raster=r'D:\T34UFE_20200514T094029.tif'

#it's working on "current map"
for lyr in arcpy.mapping.ListLayers(mxd):
	name=lyr.name+r'_p'
	
	#create random points
	arcpy.CreateRandomPoints_management(folder,name,lyr.name,"",3)

	#create extract multivalues to point	
	arcpy.sa.ExtractMultiValuesToPoints(lyr.name+"_p",in_raster,"NONE")

