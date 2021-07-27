import os
import subprocess
import sys

a = subprocess.Popen([sys.executable, 'API.py'])
code = a.wait()
print (code)


