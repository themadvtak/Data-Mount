''' This program takes in a userInterface object
    It will continue the gui and give mounting options on Win10
    Will return boolean if user wants to restart program
'''

import platform
import os
import PySimpleGUI as sg

class ImageMount:
    def __init__(self, interface, directory):
        self.title = interface.title
        self.theme = interface.theme
        self.window = interface.window
        self.images = interface.images
        self.directory = directory
        self.decision = self.mount()
        
    def mount(self):
        layout = []
        
        #Setting UI
        layout.append([sg.Text('The images you need are:', key='text')])
        layout.append([sg.Listbox( values=self.images, size=(120, 10), select_mode=None, key='data' )])
        layout.append([sg.Button('Mount All', size=(120,1),pad=(5,20), key='mntButton')])
        layout.append([sg.Text('Thank you for using the AllData Image Mounter', pad=(5,100), font=("Helvetica", 27))])
        layout.append([sg.Button('Restart', size=(20,1),pad=((425,5),(50,3)),key='restart'),sg.Button('Exit', size=(20,1),pad=(5,(50,3)),key='exit')] )

        sg.theme(self.theme)	# Maintain theme
        window = sg.Window(self.title, layout, location=self.window.CurrentLocation(), size=self.window.size)
        
        #if OS not windows 10
        if platform.system()+platform.release() != "Windows10":
            window.finalize()
            window.element('mntButton').update(visible=False)
        
        #Close old window
        event, values = window.read()
        self.window.close()
        
        #determine which button was pressed
        while True:
            if event == 'mntButton':
                for i in self.images:
                    image = os.path.join(self.directory,i)
                    errorCode = os.system("PowerShell Mount-DiskImage "+""""'"""+image+"""'" """)
                    if errorCode:
                        sg.popup_error("Error mounting", image, "\nCheck path and try again")
            elif event == 'restart':
                '''print("Restarting")'''
                window.close()
                return True
            else:
                '''print ("Closing")'''
                window.close()
                return False
            event, values = window.read()