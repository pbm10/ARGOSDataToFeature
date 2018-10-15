##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2018
## Author: John.Fay@duke.edu (for ENV859)
##---------------------------------------------------------------------

# Import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
inputFile = 'V:/ARGOSTracking/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = "V:/ARGOSTracking/ARGOSTracking/Scratch/ARGOStrack.shp"

#Open the ARGOS Data file for reading
inputFileObj = open(inputFile,'r')

#Get the first line so we can loop
lineString = inputFileObj.readline()
while lineString:
    #Get code to run only if the line contains "Date :"
    if "Date :" in lineString:

        #Split the line string into a list
        lineList = lineString.split()

        #Get attributes from first line
        tagID = lineList[0]

        #Get the next line
        line2String = inputFileObj.readline()
        line2Data = line2String.split()

        #Get attributes from second line
        obsLat = line2Data[2]
        obsLon = line2Data[5]
        print(tagID,obsLat,obsLon)
        break
    
    #Get the next line
    lineString = inputFileObj.readline()

#Close the file object
inputFileObj.close()