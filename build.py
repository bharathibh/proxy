import shutil
import subprocess

build_cmds = [
    'pip install -r requirements.txt',
    'pyinstaller --noconsole -n cloud setup.py',
    'cp -r assets/ dist/cloud/',

]

for cmd in build_cmds:
    process =  subprocess.Popen(cmd,shell=True,close_fds=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout_value, stderr_value = process.communicate()
    print('> {}:\n'.format(cmd))
    if stdout_value is not None:
        print('Success!\n')
    elif stderr_value is not None:
        print('Error:\n{}').format(stderr_value.decode())

shutil.make_archive('cloud', 'zip', 'dist/cloud')
