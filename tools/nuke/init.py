## init.py
## loaded by nuke before menu.py

import sys


def createLockFile():
	
	filename = nuke.root().knob("name").getValue()
	if not filename:
		return ''
		
	lockFilePath = filename.replace( '.nk', '.lock')
	open( lockFilePath, "w").close()
	return lockFilePath

def deleteLockFile(filename=None):
	
	if not filename:
		filename = nuke.root().knob("name").getValue()
		
	if not filename:
		return 'no file found'
		
	lockFilePath = filename.replace( '.nk', '.lock')
	if os.path.exists( lockFilePath):
		os.remove( lockFilePath)
		return lockFilePath
	else:
		return ''



def onScriptLoad():
	createLockFile()

def onScriptSave():
	createLockFile()

def onScriptClose():
	deleteLockFile()

def onCreateNode():
	return

nuke.addOnScriptLoad(onScriptLoad)
nuke.addOnScriptSave(onScriptSave)
nuke.addOnUserCreate(onCreateNode)
nuke.addOnScriptClose(onScriptClose)

nuke.pluginAddPath('./plugins')
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./icons')
nuke.pluginAddPath('./scripts')

#create write directory
def createWriteDir():
  import nuke, os, errno
  file = nuke.filename(nuke.thisNode())
  dir = os.path.dirname( file )
  osdir = nuke.callbacks.filenameFilter( dir )
  # cope with the directory existing already by ignoring that exception
  try:
    os.makedirs( osdir )
  except OSError, e:
    if e.errno != errno.EEXIST:
      raise
nuke.addBeforeRender(createWriteDir)

print 'STUDIO INIT.PY WAS RUN'