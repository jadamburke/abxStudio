set "MODE=pub"
set "PP_JOB_SERVERS=M:\;P:\jobs;N:\"
set "PP_RESOURCE=\\moon\pipeline\%MODE%"
set "MAYA_PPTOOLS=%PP_RESOURCE%\maya\2012-x64"
set "MAYA_PPTOOLS_COMMON=%PP_RESOURCE%\maya\common"

REM //////////////
REM VRAY CONFIG
REM /////////////
set "VRAY_AUTH_CLIENT_FILE_PATH=%PP_RESOURCE%\bin\win32\vray\vray22001\license"
set "VRAY_FOR_MAYA2012_MAIN_x64=%PP_RESOURCE%\bin\win32\vray\vray22001\maya_vray"
set "VRAY_FOR_MAYA2012_PLUGINS_x64=%PP_RESOURCE%\bin\win32\vray\vray22001\maya_vray\vrayplugins"
set "VRAY_PLUGINS_x64=%PP_RESOURCE%\bin\win32vray\vray22001\maya_vray\vrayplugins"
set "VRAY_TOOLS_MAYA2012_x64=%PP_RESOURCE%\bin\win32\vray\vray22001\vray\bin"


set "MAYA_SCRIPT_PATH=%PP_RESOURCE%\maya\common\scripts;%MAYA_PPTOOLS%\scripts\production;%PP_RESOURCE%\bin\win32\vray\vray22001\maya_vray\scripts;%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012\scripts;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\scripts"
set "MAYA_PLUG_IN_PATH=%MAYA_PPTOOLS%\plugins;%PP_RESOURCE%\bin\win32\vray\vray22001\maya_vray\plug-ins;%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012\plug-ins"
set "XBMLANGPATH=%PP_RESOURCE%\bin\win32\vray\vray22001\maya_vray\icons;%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012\icons;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\icons"

set "MAYA_SHELF_PATH=%MAYA_PPTOOLS%\shelves"
set "MAYA_MODULE_PATH=%MAYA_PPTOOLS%\modules;%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\modules"
set "MAYA_PRESET_PATH=%MAYA_PPTOOLS%\presets;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\presets"
set "PYTHONPATH=%PP_RESOURCE%\lib\python;%MAYA_PPTOOLS%\scripts\production;%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012\scripts"

set "ARNOLD_LICENSE_HOST=192.168.2.174"
set "MTOA_EXTENSIONS_PATH=%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012\extensions"
set "ARNOLD_PLUGIN_PATH=%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012\shaders"
REM DEFINED ABOVE ALREADY set "MAYA_MODULE_PATH=%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012"
set "MAYA_RENDER_DESC_PATH=%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012"

REM set "RLM_LICENSE=2765@192.168.2.174"

set "PATH=%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\lib;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\bin;%PP_RESOURCE%\bin\win32\arnold\0.17.1\mtoadeploy\2012\bin\;%PATH%";

REM !!!! SET USERNAMES THAT ARE ALLOWED TO USE SHAVE HAIRCUT !!!!!
REM FOR %%A IN (ari jason mirelle raphe jeong phuwit) DO IF %%A==%USERNAME% set "MAYA_PLUG_IN_PATH=%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\plug-ins;%MAYA_PLUG_IN_PATH%"

REM copying adobe camera raw preference file to user's appdata directory
copy "\\moon\pipeline\dev\config\Default_766173B5EFB0DD03.xmp" "%APPDATA%\Adobe\CameraRaw\Defaults\Default_766173B5EFB0DD03.xmp"

start "Maya" "C:\Program Files\Autodesk\Maya2012\bin\maya.exe"
