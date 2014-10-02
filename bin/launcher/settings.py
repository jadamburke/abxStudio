__author__ = 'adamb'

import os, sys
#this identifies the root of the launcher
LAUNCHER = os.path.dirname(os.path.realpath(__file__))
BIN = os.path.dirname(LAUNCHER)
ROOT = os.path.dirname(BIN)
CONFIG = os.path.join(ROOT,'config')

os.environ['PP_ROOT'] = ROOT
os.environ['PP_CONFIG'] = CONFIG


os.environ['PATH'] += ';\\\\pp-fs-nyc\\pipeline\\nyc\\lib\\python\\pyqt4\\4.8.4'
os.environ['PYTHONPATH'] += ';\\\\pp-fs-nyc\\pipeline\\nyc\\lib\\python\\pyqt4\\4.8.4'
sys.path.append('\\\\pp-fs-nyc\\pipeline\\nyc\\lib\\python\\pyqt4\\4.8.4')

print os.environ['PYTHONPATH']
print sys.path
import yaml



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

RES = os.path.join(LAUNCHER, 'res')

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

UTILITIES = {
    'email': {
        'show': True,
        'versions':{
            '1':{
                'modes':{
                    'ui':{
                        'linux': '/',
                        'mac': '/',
                        'win32': 'chrome.exe https://owa.passion-email.com/owa'
                    }
                },
                'path':{
                    'linux': '/',
                    'mac': '/',
                    'win32': 'C:/Program Files (x86)/Google/Chrome/Application'
                }
            }
        }
    },
    'qube' : {
        'show': True,
        'versions':{
            '6.5.0':{
                'modes':{
                    'ui':{
                        'linux': '/',
                        'mac': '/',
                        'win32': 'qube.exe'
                    }
                },
                'path':{
                    'linux': '/',
                    'mac': '/',
                    'win32': 'C:/Program Files (x86)/pfx/qube/bin'
                }
            }
        }
    },
    'chrome': {
        'show': True,
        'versions':{
            '37':{
                'modes':{
                    'ui':{
                        'linux': '/',
                        'mac': '/',
                        'win32': 'chrome.exe'
                    }
                },
                'path':{
                    'linux': '/',
                    'mac': '/',
                    'win32': 'C:/Program Files (x86)/Google/Chrome/Application'
                }
            }
        }
    },
    'shotgun': {
        'show': True,
        'versions':{
            '1':{
                'modes':{
                    'ui':{
                        'linux': '/',
                        'mac': '/',
                        'win32': 'chrome.exe http://passion-pictures.shotgunstudio.com'
                    }
                },
                'path':{
                    'linux': '/',
                    'mac': '/',
                    'win32': 'C:/Program Files (x86)/Google/Chrome/Application'
                }
            }
        }
    }
}
