__author__ = 'adamb'

import os,sys

import urllib2
from subprocess import Popen, PIPE, STDOUT

import yaml

# this serves as the brain of the project system. You can ask it about a file
# and it will be able to know what it is 

# it can read the global studio config and initialize a setup or it can read a custom config on a 
# per project level, or any custom config to alter or override it



def list_servers():
	for share in STUDIO['servers']:
		print (share+": "+STUDIO['servers'][share]['root_path'])

def list_jobs(share):
	try:
		path = STUDIO['servers'][share]['root_path']
		return [name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))]
	except:
		print (share+" is not a valid share name as per config")


# given a file path determine shot info about it
#  0:Server 1:Job 2:ShotFolder 3:Seq 4:Shot 5:dept 6:subDept 7:take 8:version 9:ext
#def get_info_from_path(path):
	# get info


#this identifies the root of the launcher
CORE = os.path.dirname(os.path.realpath(__file__))
LAUNCHER = os.path.dirname(CORE)
BIN = os.path.dirname(LAUNCHER)
ROOT = os.path.dirname(BIN)
CONFIG = os.path.join(ROOT,'config')

f = open(CONFIG+"/studio.yml")
# use safe_load instead load
STUDIO = yaml.safe_load(f)
f.close()
print "Loaded studio Config Successfully"

os.environ['ST_JOB_SERVERS'] = STUDIO['servers']['jobs']['root_path']

list_servers()




