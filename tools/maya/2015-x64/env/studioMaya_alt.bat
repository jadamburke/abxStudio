set "MODE=pub"
set "STUDIO=Studio"
set "PP_JOB_SERVERS=\\diskstation\jobs\"
set "PP_RESOURCE=\\diskstation\res\studio\%MODE%"
set "MAYA_PPTOOLS=%PP_RESOURCE%\maya\2012-x64"
set "MAYA_PPTOOLS_COMMON=%PP_RESOURCE%\maya\common"
REM set "PP_ARNOLD=0.21.0x";
set "PP_ARNOLD=0.25.3";

REM //////////////
REM VRAY CONFIG
REM /////////////
set "VRAY_AUTH_CLIENT_FILE_PATH=%PP_RESOURCE%\bin\win32\vray\vray22001\license"
set "VRAY_FOR_MAYA2012_MAIN_x64=%PP_RESOURCE%\bin\win32\vray\vray22001\maya_vray"
set "VRAY_FOR_MAYA2012_PLUGINS_x64=%PP_RESOURCE%\bin\win32\vray\vray22001\maya_vray\vrayplugins"
set "VRAY_PLUGINS_x64=%PP_RESOURCE%\bin\win32vray\vray22001\maya_vray\vrayplugins"
set "VRAY_TOOLS_MAYA2012_x64=%PP_RESOURCE%\bin\win32\vray\vray22001\vray\bin"


set "MAYA_SCRIPT_PATH=%PP_RESOURCE%\maya\common\scripts;%MAYA_PPTOOLS%\scripts\production;%PP_RESOURCE%\bin\win32\vray\vray22001\maya_vray\scripts;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\scripts;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\scripts"
set "MAYA_PLUG_IN_PATH=%MAYA_PPTOOLS%\plugins;%PP_RESOURCE%\bin\win32\vray\vray22001\maya_vray\plug-ins;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\plug-ins"
set "XBMLANGPATH=%PP_RESOURCE%\bin\win32\vray\vray22001\maya_vray\icons;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\icons;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\icons"

set "MAYA_SHELF_PATH=%MAYA_PPTOOLS%\shelves"
set "MAYA_MODULE_PATH=%MAYA_PPTOOLS%\modules;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\modules"
set "MAYA_PRESET_PATH=%MAYA_PPTOOLS%\presets;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\presets"
set "PYTHONPATH=%PP_RESOURCE%\lib\python;%MAYA_PPTOOLS%\scripts\production;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\scripts"

set "ARNOLD_LICENSE_HOST=127.0.0.1"
set "ARNOLD_LICENSE_PORT=5053"
set "MTOA_EXTENSIONS_PATH=%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\extensions"
set "ARNOLD_PLUGIN_PATH=%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\shaders"
REM DEFINED ABOVE ALREADY set "MAYA_MODULE_PATH=%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy"
set "MAYA_RENDER_DESC_PATH=%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy"

set "RLM_LICENSE=2765@127.0.0.1"

set "PATH=%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\lib;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\bin;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\bin;%PATH%";

REM ZYNC CONFIG
set "PYTHONPATH=%PYTHONPATH%;C:/Users/adam/AppData/Local/zync/zync-maya;"
set "XBMLANGPATH=%XBMLANGPATH%;C:/Users/adam/AppData/Local/zync/zync-maya;"


REM !!!! SET USERNAMES THAT ARE ALLOWED TO USE SHAVE HAIRCUT !!!!!
FOR %%A IN (ari jason mirelle raphe jeong phuwit hayden adam tingting) DO IF %%A==%USERNAME% set "MAYA_PLUG_IN_PATH=%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\plug-ins;%MAYA_PLUG_IN_PATH%"

REM copying adobe camera raw preference file to user's appdata directory
copy "\\moon\pipeline\dev\config\Default_766173B5EFB0DD03.xmp" "%APPDATA%\Adobe\CameraRaw\Defaults\Default_766173B5EFB0DD03.xmp"

start "Maya" "C:\Program Files\Autodesk\Maya2012\bin\maya.exe" -noAutoloadPlugins
