import os
import subprocess

cmd = ['python', 'subpro.py']
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, env=os.environ)
process.wait()
# for line in process.stdout:
#     print(line)
#     print('\n')
