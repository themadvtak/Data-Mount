''' This program will take 2 arguments: Location of iso's and starting letter of mounting
    It will then present a easy command line interface to identify which iso's are needed
    Once iso's are identified, it will mount said iso's to be used by AllData (Windows 10 Only)'''

#STD Libraries
import sys
import os

#Other files
from DataParser import DataParse
import Interface
import PathGenerator
import ImageMounter

#Global Config Vars
inputFile = "AllData.10.53_2013Q3_Full_Set_DVD_Contain.txt"
image = "image.gif"
        
def main():
    #set initial flags
    retry = True
    dataFile = inputFile
    splashImage = image
    
    #account for running off .exe
    try:
        '''print (sys._MEIPASS)'''
        dataFile = sys._MEIPASS + "\\" + inputFile
        splashImage = sys._MEIPASS + "\\" + image
    except AttributeError:
        '''print ("Not running .exe")'''
        pass

    #Parse text file
    filedata = DataParse(dataFile)  #create DataParse object and call loadData
    
    while retry:
        #First Object: Send nothing. Gets Path. Return UI Window and Path
        interface = PathGenerator.PathObject(splashImage)
        #Second Object: Sends UI, gets make and year, returns ISOs array, and window
        images = Interface.userInterface(filedata.data, interface)
        #Then get the option to mount.
        mount = ImageMounter.ImageMount(images, interface.directory)
        retry = mount.decision

if __name__ == '__main__':
    main()
