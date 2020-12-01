# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 13:27:18 2020

@author: ll_stsekeid
"""
import argparse
import os,inspect
import pandas as pd
import h5py



## Input argument parser
parser = argparse.ArgumentParser(
    description='CRO MXEval Test Release v1.0'
    #epilog="End of test programm."
)



parser.add_argument("iRequestType",
                    help="Select number 1 to process MXEval functionalities! (1)",
                    type=int)

args = parser.parse_args()




#Input Vehicle parameter
def openVehicleData(sFilePath,sFileName,sLat,sLon):
    """
    Return a pandas DataFrame with vehicle GPS data. 
    
    The function parses different files (.mat, .csv) by the file path.
    
    @type   sFileName:  string
    @param  sFileName:  file path
    @rtype  dfvehicle:  pandas DataFrame
    @return dfvehicle:  the input vehicle GPS data
    """
    ### Get pandas DataFrame
    dfvehicle = pd.DataFrame()
    if sFileName[-3:] == 'mat':
        f = h5py.File(sFilePath+sFileName,'r')
        lat = f.get(sLat)
        lon = f.get(sLon)
        lat = list(lat)
        lon = list(lon)
        dfvehicle[sLat] = lat[0]
        dfvehicle[sLon] = lon[0]
    elif sFileName[-3:] == 'csv' or sFileName[-3:] == 'txt' :
        dfvehicle = pd.read_csv(sFilePath+sFileName,sep=',', encoding='cp1252')
    return dfvehicle




def main():
    # current directory path
    sCurrentDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    # current parent directory path
    sParentDir = os.path.dirname(sCurrentDir)
    print('Current directory: ',sCurrentDir)
    parser.print_help()
    print('Hello World!')
    arg = input()
    print(arg)
    df = openVehicleData('C:\\Users\\ll_stsekeid\\Desktop\\Pyinstaller\\','data.mat','INS_Lat_Abs_POI2','INS_Long_Abs_POI2')
    print(df.head())



if __name__ == "__main__":
    main()