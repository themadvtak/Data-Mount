''' This program takes 2 arguments = FileData and PathObject.
    It will create a GUI and handle user interactions
    Will return userInterface object
'''

import PySimpleGUI as sg
from time import sleep

class userInterface:
    def __init__(self, fileData, interface):
        self.file = fileData
        self.window = interface.window
        self.title = interface.title
        self.theme = interface.theme
        self.images = self.loadDemo()
        
    def loadDemo(self):
        layout = []
        temp = []
        
        for i in self.file: #Iteretate through self to get Makes
            temp.append(i)
        temp.sort()
        
        sg.theme(self.theme)	# Maintain theme
        layout.append([sg.Text('Please Select Make(s):', key='text')])
        layout.append([sg.Listbox( values=temp, size=(120, 30), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, default_values=temp[0], key='box' )])
        layout.append([sg.Button('Next', size=(20,1), pad=((600,5),(15,3)))] ) 
        
        # Create the Window
        window = sg.Window(self.title, layout, location=self.window.CurrentLocation(), size=self.window.size)
        event, values = window.read()
        
        self.window.close()
        self.window = window
        
    #   if event in (None, 'Cancel'):	# if user closes window or clicks cancel
    #      break
        '''print('You entered ', values['box'])'''
        
        
        #Get year data based on user input
        temp = [] #Clear temp
        for i in values['box']:
            for j in (self.file[i]):
                temp.append(j[0])
        makes = values['box']
        #Now we will refresh text and listbox with Year data
        temp.sort()
        temp = list(dict.fromkeys(temp)) #Remove Duplicates
        window['text'].Update('Please Select Year(s):')
        window.Element('box').Update(values=temp, set_to_index=0)
        event, values = window.read()
        '''print('You entered ', values['box'])'''
        
        #We have what we need, getting images
        images = self.getImages(makes,values['box'])
        images = list(dict.fromkeys(images)) #Remove Duplicates
        '''print('Images Outputted ', images)'''
            
        return images
            
    def getImages(self, make, year):
    #Takes in 2 lists, will return relevant image names
        imageNames = []
    
        for i in make:
            for j in year:
                for k in self.file[i]:
                    if k[0] == j:
                        #print(k[1])
                        imageNames.append(k[1])
    
        return imageNames
        
    