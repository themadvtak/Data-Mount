''' This program takes 1 argument = DataFile. It will parse file and present data in 2d Array
    DataParse['Make'] = [Year][Image]
    Duplicate Images are stored as seperate values
'''

import re
import linecache
from collections import defaultdict

class DataParse:
    def __init__(self, inputFile):
        self.file = inputFile
        self.index = self.generateIndex()
        self.data = self.loadData()
        
    def generateIndex(self):
        #Function will find sections in text file and get image and index
        f = open(self.file, "r")
        indexOutput = []
        number = 0
    
        for line in f:
            number += 1
            if (".iso" not in line) and (".isz" not in line): #Find start indeces of iso contents 
                continue
            else:
                #print (line, number)
                image = re.findall('\(([^)]+)', line)[0]
                indexOutput.append([image, number])
    
        f.close()
        return indexOutput
            
    def loadData(self):
        #Function will read the input data and sort it in Dictlist
        #Dictlist['make'] = [Year, Disc]
        
        index = self.index
        data = defaultdict(list)

        for i in index: #i = [imageName, lineWhereFound]
            try: 
                next = index[index.index(i)+1] #Get ranges
                #print (i[1], next[1])
            except IndexError:
                continue
                
            for j in range(i[1]+1,next[1]-1): #Get makes and build Dictlist. i[0] has image name
                section = linecache.getline(self.file, j) # Get each line in range i-i+1
                section = ' '.join( section.split() ) #remove special characters
                
                try: 
                    int(section[-2]) #Simple expression to remove extra lines
                    make = section.rsplit(' ',1)[0] #Split lines
                    year = section.rsplit(' ',1)[1]
                    
                    if ( "-" in year ): #Found range
                        starty = year.split('-')[0]
                        endy = year.split('-')[1]
                        if int(starty) < 100: #Different year format
                            starty = "19" + starty
                            endy = "19" + endy
                        
                        for k in range( int(starty),int(endy)+1 ): #decrementing and incrementing to get 2 edge years
                            data[make].append([str(k),i[0]]) #For every year in the range
                    elif int(year) < 100: #Different year format
                        year = "19" + year
                        data[make].append([year,i[0]])
                    else:
                        data[make].append([year,i[0]])
                        
                except: 
                    continue
                    
        return data