# pyinstaller
The test.py is the test script.
With the anaconda prompt and pyinstaller 4.0 the test.py script will be processed to test.exe.
Python version is 3.8.6 and windows Version is 10.0.18363.1198.

## 1. Hello World!
The test.py scirpt has only a print('Hello World').  
console: pyinstaller --onefile --console test.py  
test.exe -> 10.5 MB  
open with cmd:   
C:\Users\ll_stsekeid\Desktop\Pyinstaller>test.exe   
Hello World!  

## 2. User Input!
The test.py scirpt has user input as input(arg).  
console: pyinstaller --onefile --console test.py  
test.exe -> 10.8 MB  
open cmd:  
C:\Users\ll_stsekeid\Desktop\Pyinstaller>test.exe  
Hello World!  
My name is Basti  
My name is Basti  

## 3. argparse!
The test.py scirpt has argparse argument.  
console: pyinstaller --onefile --console test.py  
test.exe -> 10.8 MB  
open cmd:  
C:\Users\ll_stsekeid\Desktop\Pyinstaller>test.exe 1
usage: test.exe [-h] iRequestType

CRO MXEval Test Release v1.0

positional arguments:
  iRequestType  Select number 1 to process MXEval
                functionalities! (1)

optional arguments:
  -h, --help    show this help message and exit
Hello World!
My name is Basti
My name is Basti

## 4. import os,sys 
The test.py scirpt has os,sys imported.  
console: pyinstaller --onefile --console test.py  
test.exe -> 10.8 MB  
open cmd:   
C:\Users\ll_stsekeid\Desktop\Pyinstaller>test.exe 1  
Current directory:  C:\Users\ll_stsekeid\Desktop\Pyinstaller  
usage: test.exe [-h] iRequestType  
  
CRO MXEval Test Release v1.0  
  
positional arguments:  
  iRequestType  Select number 1 to process MXEval  
                functionalities! (1)  
  
optional arguments:  
  -h, --help    show this help message and exit  
Hello World!  
My name is Basti1  
My name is Basti1  

## 5. import pandas, h5py (input vehicle data)
### first try
The test.py scirpt has pandas, h5py imported.   
console: pyinstaller --onefile --console test.py   
test.exe -> 382.5 MB   
open cmd:   
C:\Users\ll_stsekeid\Desktop\Pyinstaller>test.exe 1  
nothing happens! 

### second try
The test.py scirpt has pandas, h5py imported.  
Modified test.spec with hiddenimports=['h5py']  
console: pyinstaller --onefile --top-level=DEBUG test.spec
test.exe -> 382.5 MB
C:\Users\ll_stsekeid\Desktop\Pyinstaller>test.exe 1  
nothing happens! 

### third try
The test.py scirpt has pandas, h5py imported.  
Modified test.spec  
from PyInstaller.utils.hooks import collect_submodules  

hidden_imports = collect_submodules('h5py')  

a = Analysis(['test.py'],  
            binaries=None,  
            datas=[],  
            hiddenimports=hidden_imports,  
			
console: pyinstaller --onefile --top-level=DEBUG test.spec  
test.exe -> 382.6 MB  
C:\Users\ll_stsekeid\Desktop\Pyinstaller>test.exe 1  
nothing happens! 

