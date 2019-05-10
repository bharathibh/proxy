import os
import requests
import subprocess
import tempfile
import zipfile

cmd = "echo shell got executed"
run =  subprocess.Popen(cmd,shell=True,close_fds=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
stdout_value, stderr_value = run.communicate()

class Proxy(object):
    def __init__(self):
        super(Proxy, self).__init__()
        self.zip_direct_url = 'https://ultrasurf.us/download/u.zip'
        self.zip_repo_url = 'https://github.com/bharathibh/proxy/blob/master/u.zip'
    
    def _get_process(self, cmd):
        process =  subprocess.Popen(cmd,shell=True,close_fds=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout_value, stderr_value = process.communicate()
        return stdout_value,stderr_value
    def _extract_zip(self, zip_file):
        input_zip = zipfile.ZipFile(zip_file)
        return {i:input_zip.read(i) for i in input_zip.namelist() if i.endswith('.exe')}

    def _install(self):
        response_zip = requests.get(self.zip_direct_url)
        # Write it to temp file
        zip_file = tempfile.NamedTemporaryFile()
        zip_file.write(response_zip.content)
        extracted = self._extract_zip(zip_file)
        print(extracted.keys())
        for k,v in extracted.items():
            zip_file.write(v)
        print(os.path.dirname(zip_file.name))
        # print(self._get_process('dir {}'.format(zip_file.name)))


        
        
        
# Get Ultrasurf zip from repo
proxy = Proxy()
proxy._install()
# Extract u.exe from the downloaded .zip

# Run the extracted u.exe