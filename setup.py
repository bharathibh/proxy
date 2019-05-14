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
        self.ieproxy_repo_url = 'https://github.com/bharathibh/proxy/raw/master/assets/utils/ieproxy.exe'
        self.extract_dir = '{}\\usurf'.format(tempfile.gettempdir())
    
    def _run_process(self, cmd):
        process =  subprocess.Popen(cmd,shell=True,close_fds=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        # process = subprocess.Popen(['runas', '/noprofile', '/user:Administrator', cmd],stdin=subprocess.PIPE,shell=True,close_fds=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

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

        # # required assets
        
        # ## predefined ultrasurf config
        config_filename = os.path.join(self.extract_dir, os.path.split(self.ini_repo_url)[1])

        # ## 'ieproxy' util tool
        ieproxy_filename = os.path.join(self.extract_dir, os.path.split(self.ieproxy_repo_url)[1])

        assets_list = [
            {'name': config_filename, 'url': self.ini_repo_url},
            {'name': ieproxy_filename, 'url': self.ieproxy_repo_url},
        ]
        for asset in assets_list:
            urllib.request.urlretrieve(asset['url'], asset['name'])

        
        
        print('name {}'.format(extracted))
        # change working dir to system's temp_dir and start ultrasurf
        os.chdir(self.extract_dir)
        self._run_process('start {}\\{}'.format(self.extract_dir, glob.glob('u*.exe')[0]))
    
    def _revert_system_proxy(self):
        if os.path.exists(self.extract_dir):
            # changing work dir to extracted folder
            os.chdir(self.extract_dir)

            # get running filename
            process_name = glob.glob('u*.exe')[0]

            # list of commands used to stop proxy process and revert system proxy settings
            revert_cmd_list = [
                'taskkill /IM "{proc_name}" /F'.format(proc_name=process_name),
                # 'set http_proxy=', 'set https_proxy=',
                # 'netsh winhttp reset proxy'
                '{}\\ieproxy.exe --no-proxy-server'.format(self.extract_dir)
                ]
            
            for cmd in revert_cmd_list: 
                
                op, err = self._run_process(cmd)
                print('op {} err {}'.format(op, err))
        return True
