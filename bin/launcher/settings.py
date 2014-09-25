__author__ = 'adamb'

import os, sys
os.environ['PATH'] += ';\\\\pp-fs-nyc\\pipeline\\nyc\\lib\\python\\pyqt4\\4.8.4'
os.environ['PYTHONPATH'] += ';\\\\pp-fs-nyc\\pipeline\\nyc\\lib\\python\\pyqt4\\4.8.4'
sys.path.append('\\\\pp-fs-nyc\\pipeline\\nyc\\lib\\python\\pyqt4\\4.8.4')

print os.environ['PYTHONPATH']
print sys.path
import yaml

#this specifies the root of the launcher
ROOT = os.path.dirname(os.path.realpath(__file__))
CONFIG = os.path.join(ROOT,'..','..','config')
MODE = "pub"
SITE = "ny"
SERVER = "pp-fs-nyc"
SHARES = {
    'prod' : 'production',
    'sys' : 'pipeline',
    'user' : 'personal',
    'lib' : 'lib',
    'job' : 'jobs'
}
DRIVE_MAP = {
    'prod' : 'P:',
    'sys' : 'T:',
    'user' : 'W:',
    'lib' : 'R:',
    'job' : 'Z:'
}

RES = os.path.join(ROOT, 'res')

#load the apps dictionary
f = open(CONFIG+"/app.yml")
# use safe_load instead load
APPS = yaml.safe_load(f)
f.close()

#load the modules dictionary
f = open(CONFIG+"/modules.yml")
# use safe_load instead load
MODULES = yaml.safe_load(f)
f.close()

#load the workgroups dictionary
f = open(CONFIG+"/workgroups.yml")
# use safe_load instead load
WORKGRP = yaml.safe_load(f)
f.close()