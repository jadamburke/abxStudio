set "MODE=pub"
set "PP_JOB_SERVERS=M:\;P:\jobs;N:\"
set "PP_RESOURCE=\\moon\pipeline\%MODE%"
set "MAYA_PPTOOLS=%PP_RESOURCE%\maya\2012-x64"
set "MAYA_PPTOOLS_COMMON=%PP_RESOURCE%\maya\common"


set "MAYA_SCRIPT_PATH=%PP_RESOURCE%\maya\common\scripts;%MAYA_PPTOOLS%\scripts\production;%PP_RESOURCE%\bin\win32\vray\vray22001\maya_vray\scripts;%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012\scripts"
set "MAYA_PLUG_IN_PATH=%MAYA_PPTOOLS%\plugins;%PP_RESOURCE%\bin\win32\vray\vray22001\maya_vray\plug-ins;%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012\plug-ins"
set "XBMLANGPATH=%PP_RESOURCE%\bin\win32\vray\vray22001\maya_vray\icons;%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012\icons"

set "MAYA_SHELF_PATH=%MAYA_PPTOOLS%\shelves"
set "MAYA_MODULE_PATH=%MAYA_PPTOOLS%\modules;%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012"
set "MAYA_PRESET_PATH=%MAYA_PPTOOLS%\presets"
set "PYTHONPATH=%PP_RESOURCE%\lib\python;%MAYA_PPTOOLS%\scripts\production;%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012\scripts"

REM set "ARNOLD_LICENSE_HOST=192.168.2.174"
set "ARNOLD_LICENSE_HOST=192.168.2.53"
set "MTOA_EXTENSIONS_PATH=%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012\extensions"
set "ARNOLD_PLUGIN_PATH=%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012\shaders"
REM DEFINED ABOVE ALREADY set "MAYA_MODULE_PATH=%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012"
set "MAYA_RENDER_DESC_PATH=%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012;\\moon\pipeline\bin\win32\vray\vray22001\maya_root\bin\rendererDesc"

set "PATH=%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012\bin\;%PATH%";




REM start "Maya" "C:\Program Files\Autodesk\Maya2012\bin\Render.exe" %*
REM C:\"Program Files"\Autodesk\Maya2012\bin\Render.exe %*