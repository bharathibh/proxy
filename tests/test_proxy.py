import unittest

import os
import glob
import tempfile
from setup import ProxyConnection

class TestProxy(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestProxy, self).__init__(*args, **kwargs)
        self.proxy_conn = ProxyConnection()    
        self.extract_dir = '{}\\usurf'.format(tempfile.gettempdir())
        self.file_patterns = ['u*.exe', 'u.ini', 'ieproxy.exe']
        self.proxy_conn.proxy._revert_system_proxy()
        self.proxy_conn._start()
        self.proxy_conn.proxy._revert_system_proxy()
    
    def test_proxy_dir(self):
        self.assertTrue(os.path.exists(self.extract_dir), 'Extracting folder not exists')
        print('Passed! Extracting folder exists')
    
    def test_assets(self):
        os.chdir(self.extract_dir)
        file_list = [f for p in self.file_patterns for f in glob.glob(p)]
        self.assertEqual(len(self.file_patterns), len(file_list), 'Required files not found')
        print('Passed! Required files are exists')

if __name__ == "__main__":
    unittest.main()

        