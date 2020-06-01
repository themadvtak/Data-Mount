''' This program takes Zero Arguments.
    It will create a GUI and handle user interactions
    Will return GUI window and path
'''

import PySimpleGUI as sg

class PathObject:
    def __init__(self, image):
        self.image = image
        self.window = self.loadWindow()
        
    def loadWindow(self):
        layout = []
        defaultDir = "Enter Directory"
        title = "All Data Image Mounter"
        sg.theme('Dark Blue 3')	# Add a touch of color
        
        layout.append([sg.Text('Welcome To AllData Mount!', pad=(150,20), font=("Helvetica", 25))])
        layout.append([sg.Image(self.image, pad=(100,(20,50)))])
        layout.append([sg.Text('Please enter directory containing disc images:', font=("Helvetica", 12))])
        layout.append([sg.InputText(defaultDir, size=(97,1), key='text' ),sg.FolderBrowse(pad=(15,3))])
        layout.append([sg.Button('Next', size=(20,1), pad=((600,5),(150,3)))] ) 
        
        # Create the Window
        window = sg.Window(title, layout, size=(800,600))
        
        # Get user input
        event, values = window.read()
        while values['text'] == defaultDir:
            sg.popup_error('Please select a directory and try again')
            event, values = window.read()
            
        '''print('You entered ', values['text'])'''
        self.directory = values['text']
        self.title = title
        self.theme = sg.theme()
        
        return window