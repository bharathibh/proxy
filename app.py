import os
import PySimpleGUIWx as sg

menu_def = ['UNUSED', ['My', 'Simple', '---', 'Menu', 'Exit']]

tray = sg.SystemTray(menu=menu_def, filename=os.path.join(os.getcwd(), '/assets/icons/on.png'))

tray.ShowMessage('Starting', 'Now Starting the application')

while True:
    event = tray.Read()
    if event == 'Exit':
        break
    elif event == 'Menu':       # add your checks here
        pass
    tray.ShowMessage('Event', '{}'.format(event))