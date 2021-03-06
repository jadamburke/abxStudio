__author__ = 'adamb'

import os, sys
#this identifies the root of the launcher
LAUNCHER = os.path.dirname(os.path.realpath(__file__))
BIN = os.path.dirname(LAUNCHER)
ROOT = os.path.dirname(BIN)
CONFIG = os.path.join(ROOT,'config')

os.environ['ST_ROOT'] = ROOT.replace('\\','/')
os.environ['ST_CONFIG'] = CONFIG.replace('\\','/')

# import the proper version of PYQT
# need to look at a better way of sourcing pyqt / pyside
pyQTPath = os.path.join(ROOT,'lib','python','pyqt4','4.10.3')
os.environ['PATH'] += (';'+pyQTPath)
print ('setting pyQTPath to '+pyQTPath)
try:
    os.environ['PYTHONPATH'] += (';'+pyQTPath)
except:
    os.environ['PYTHONPATH'] = (pyQTPath)
sys.path.append(pyQTPath)

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
#RES = 'E:\\temp\\res'
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
                        'win32': 'chrome.exe http://mail.passion-pictures.com'
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
    },
    'internal': {
        'show': True,
        'versions':{
            '1':{
                'modes':{
                    'ui':{
                        'linux': '/',
                        'mac': '/',
                        'win32': 'firefox.exe http://internal/'
                    }
                },
                'path':{
                    'linux': '/',
                    'mac': '/',
                    'win32': 'C:/Program Files (x86)/Mozilla Firefox'
                }
            }
        }
    }
}
