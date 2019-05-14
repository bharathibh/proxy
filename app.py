import os
import PySimpleGUIWx as sg

from setup import Proxy

class ProxyConnection(object):
    def __init__(self):
        super(ProxyConnection, self).__init__()

        self.CONNECT = 'Connect'
        self.DISCONNECT = 'Disconnect'
        self.EXIT = 'Exit'
        
        # tray icon details
        self.icon_dir = os.path.join(os.getcwd()+'/assets/icons')
        self.on_icon = os.path.join(self.icon_dir+'/on.png')
        self.off_icon = os.path.join(self.icon_dir+'/off.png')
        # ##

        # system tray items
        self.context_items = [self.CONNECT, self.DISCONNECT, '---', self.EXIT]
        self.menu_def = ['UNUSED', self.context_items]
        self.tray = sg.SystemTray(menu=self.menu_def, filename=os.path.join(os.getcwd()+ '/assets/icons/on.png'))
        # ##
        
        # proxy details
        self.proxy = Proxy()
        # ##
    
    def _connect(self):
        try:
            self.tray.ShowMessage('Starting', 'Intialising..')
            self.proxy._run()
        except Exception as ex:
            self.tray.ShowMessage('Error', '{}'.format(ex))
    def _disconnect(self):
        try:
            self.tray.ShowMessage('Reverting', 'Please Wait')
            self.proxy._revert_system_proxy()
            self.tray.ShowMessage('Disconnected', 'All settings reverted')
        except Exception as ex:
            self.tray.ShowMessage('Error', '{}'.format(ex))
    def _start(self):
        print('started..')
        self._connect()
        while True:
            event = self.tray.Read()
            if event == self.EXIT:
                break
            elif event == self.CONNECT:
                self._connect()
            elif event == self.DISCONNECT:
                self._disconnect()

if __name__ == "__main__":
    proxy_conn = ProxyConnection()
    proxy_conn._start()