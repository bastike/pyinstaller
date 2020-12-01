# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 13:27:18 2020

@author: ll_stsekeid
"""
import argparse
import os,inspect




## Input argument parser
parser = argparse.ArgumentParser(
    description='CRO MXEval Test Release v1.0'
    #epilog="End of test programm."
)



parser.add_argument("iRequestType",
                    help="Select number 1 to process MXEval functionalities! (1)",
                    type=int)

args = parser.parse_args()




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



if __name__ == "__main__":
    main()