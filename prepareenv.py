import subprocess
import sys


def install():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'marvel']),
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'certifi']),
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pymongo']),
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyyaml']),
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'dnspython']),


install()
