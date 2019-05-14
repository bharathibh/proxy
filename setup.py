import os
import glob
import requests
import subprocess
import tempfile
import urllib
import zipfile

class Proxy(object):
    def __init__(self):
        super(Proxy, self).__init__()
        self.zip_direct_url = 'https://ultrasurf.us/download/u.zip'
        self.zip_repo_url = 'https://github.com/bharathibh/proxy/raw/master/u.zip'
        self.ini_repo_url = 'https://raw.githubusercontent.com/bharathibh/proxy/master/u.ini'
        self.extract_dir = '{}\\usurf'.format(tempfile.gettempdir())
    
    def _run_process(self, cmd):
        process =  subprocess.Popen(cmd,shell=True,close_fds=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout_value, stderr_value = process.communicate()
        return stdout_value,stderr_value
    def _extract_zip(self, input_zip):
        with zipfile.ZipFile(input_zip) as zip_obj:
            file_names = zip_obj.namelist()
            for file_name in file_names:
                if file_name.endswith('.exe'):
                    zip_obj.extract(file_name, self.extract_dir)
                    return zip_obj.filename
        # with zipfile.ZipFile(input_zip, 'r') as zip_obj:
        #     zip_obj.extractall(self.extract_dir)
        return False

    def _run(self):
        response_zip = requests.get(self.zip_direct_url)
        # Write it to temp file
        zip_file = tempfile.NamedTemporaryFile()
        zip_file.write(response_zip.content)
        extracted = self._extract_zip(zip_file)
        config_filename = os.path.join(self.extract_dir, os.path.split(self.ini_repo_url)[1])
        
        # download preloaded config
        urllib.request.urlretrieve(self.ini_repo_url, config_filename)
        
        o, e = self._run_process('whoami')
        print('name {}'.format(extracted))
        # change working dir to system's temp_dir and start ultrasurf
        os.chdir(self.extract_dir)
        self._run_process('start {}\\{}'.format(self.extract_dir, glob.glob('*.exe')[0]))
    
    def _revert_system_proxy(self):

        # changing work dir to extracted folder
        os.chdir(self.extract_dir)

        # get running filename
        process_name = glob.glob('*.exe')[0]

        # list of commands used to stop proxy process and revert system proxy settings
        revert_cmd_list = [
            'taskkill /IM "{proc_name}" /F'.format(proc_name=process_name),
            # 'set http_proxy=', 'set https_proxy=',
            'netsh winhttp reset proxy'
            ]
        
        for cmd in revert_cmd_list:    
            self._run_process(cmd)
        return True
        
            
        
        

        # self._run_process('start {}\\')
        # print(self._run_process('dir {}'.format(tempfile.gettempdir())))
        
        # print(self._run_process('dir {}'.format(zip_file.name)))
