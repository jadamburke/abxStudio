set "PP_JOB_SERVERS=%HOMEDRIVE%%HOMEPATH%\Documents\maya\projects"
set "PP_RESOURCE=%HOMEDRIVE%%HOMEPATH%\Documents\maya\pp"
set "MAYA_PPTOOLS=%PP_RESOURCE%\maya\2012-x64"

set "MAYA_SCRIPT_PATH=%PP_RESOURCE%\maya\2012-x64\scripts\production;%PP_RESOURCE%\vray\vray22001\maya_vray\scripts"
set "MAYA_PLUG_IN_PATH=%PP_RESOURCE%\maya\2012-x64\plugins;%PP_RESOURCE%\vray\vray22001\maya_vray\plug-ins"
set "XBMLANGPATH=%PP_RESOURCE%\vray\vray22001\maya_vray\icons"

set "MAYA_SHELF_PATH=%PP_RESOURCE%\maya\2012-x64\shelves"
set "MAYA_MODULE_PATH=%PP_RESOURCE%\maya\2012-x64\modules"
set "MAYA_PRESET_PATH=%PP_RESOURCE%\maya\2012-x64\presets"
set "PYTHONPATH=%PP_RESOURCE%\python"

start "Maya" "C:\Program Files\Autodesk\Maya2012\bin\maya.exe"