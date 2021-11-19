import subprocess
import sys


def install():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'marvel']),
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'certifi']),
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pymongo']),


install()
