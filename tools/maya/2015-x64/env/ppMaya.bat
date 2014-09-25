set "MODE=pub"
set "PP_MAYA=2014"
set "MAYA_INSTALL_PATH=C:/Program Files/Autodesk/Maya%PP_MAYA%/"

REM /////////////////
REM SERVER FILE PATHS
REM /////////////////

set "PP_JOB_SERVERS=M:\;P:\;N:\"
set "PP_RESOURCE=\\moon\pipeline\%MODE%"
REM OLD VERSION SPECIFIC MAYA set "MAYA_PPTOOLS=%PP_RESOURCE%\maya\%PP_MAYA%x64"
set "MAYA_PPTOOLS=%PP_RESOURCE%\maya\common"
set "MAYA_PPTOOLS_VERSIONED=%PP_RESOURCE%\maya\%PP_MAYA%x64"
set "MAYA_PPTOOLS_COMMON=%PP_RESOURCE%\maya\common"


REM //////////////
REM VRAY CONFIG
REM /////////////

set "PP_VRAY=vray23002"

REM AUTH FILE BELOW LETS US AUTOMATICALLY SET COPPER AS VRAY SERVER
set "VRAY_AUTH_CLIENT_FILE_PATH=%PP_RESOURCE%\bin\win32\vray\%PP_VRAY%\license"
REM set "VRAY_PLUGINS_x64=%PP_RESOURCE%\bin\win32vray\%PP_VRAY%\maya_vray\vrayplugins"
set "VRAY_FOR_MAYA%PP_MAYA%_MAIN_x64=%PP_RESOURCE%\bin\win32\vray\%PP_VRAY%\maya_vray"
set "VRAY_FOR_MAYA%PP_MAYA%_PLUGINS_x64=%PP_RESOURCE%\bin\win32\vray\%PP_VRAY%\maya_vray\vrayplugins"
set "VRAY_TOOLS_MAYA%PP_MAYA%_x64=%PP_RESOURCE%\bin\win32\vray\%PP_VRAY%\vray\bin"

REM // COPY vray dlls locally to maya install path (needed to properly load vray off of network)
if exist "C:\Program Files\Autodesk\Maya2014\bin\maya.exe" (
    if not exist "C:\Program Files\Autodesk\Maya%PP_MAYA%\bin\vray.dll" copy "\\moon\pipeline\dev\bin\win32\vray\vray23002\maya_root\bin\vray.dll" "C:\Program Files\Autodesk\Maya%PP_MAYA%\bin\vray.dll"
	if not exist "C:\Program Files\Autodesk\Maya%PP_MAYA%\bin\svml_dispmd.dll" copy "\\moon\pipeline\dev\bin\win32\vray\vray23002\maya_root\bin\svml_dispmd.dll" "C:\Program Files\Autodesk\Maya%PP_MAYA%\bin\svml_dispmd.dll"
	if not exist "C:\Program Files\Autodesk\Maya%PP_MAYA%\bin\libmmd.dll" copy "\\moon\pipeline\dev\bin\win32\vray\vray23002\maya_root\bin\libmmd.dll" "C:\Program Files\Autodesk\Maya%PP_MAYA%\bin\libmmd.dll"
	if not exist "C:\Program Files\Autodesk\Maya%PP_MAYA%\bin\dte_wrapper.dll" copy "\\moon\pipeline\dev\bin\win32\vray\vray23002\maya_root\bin\dte_wrapper.dll" "C:\Program Files\Autodesk\Maya%PP_MAYA%\bin\dte_wrapper.dll"
)


REM //////////////
REM ARNOLD CONFIG
REM /////////////

set "PP_ARNOLD=0.25.3"
set "ARNOLD_LICENSE_HOST=192.168.2.174"
set "MTOA_EXTENSIONS_PATH=%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\extensions"
set "ARNOLD_PLUGIN_PATH=%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\shaders"
REM DEFINED ABOVE ALREADY set "MAYA_MODULE_PATH=%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy"
set "MAYA_RENDER_DESC_PATH=%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy"




REM //////////////
REM MAYA CONFIG
REM /////////////

set "RLM_LICENSE=2765@192.168.2.174"

//set "MAYA_SCRIPT_PATH=%PP_RESOURCE%\maya\common\scripts;%MAYA_PPTOOLS%\scripts\production;%PP_RESOURCE%\bin\win32\vray\%PP_VRAY%\maya_vray\scripts;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\scripts;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\scripts"
set "MAYA_SCRIPT_PATH=%PP_RESOURCE%\maya\common\scripts;%MAYA_PPTOOLS%\scripts\production;%PP_RESOURCE%\bin\win32\vray\%PP_VRAY%\maya_vray\scripts;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\scripts;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\scripts;%PP_RESOURCE%\bin\win32\realflow\maya2012\scripts\others"
//set "MAYA_PLUG_IN_PATH=%MAYA_PPTOOLS%\plugins;%PP_RESOURCE%\bin\win32\vray\%PP_VRAY%\maya_vray\plug-ins;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\plug-ins"
set "MAYA_PLUG_IN_PATH=%MAYA_PPTOOLS%\plugins;%PP_RESOURCE%\bin\win32\vray\%PP_VRAY%\maya_vray\plug-ins;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\plug-ins;%PP_RESOURCE%\bin\win32\realflow\maya2012\bin\plug-ins"
set "XBMLANGPATH=%PP_RESOURCE%\bin\win32\vray\%PP_VRAY%\maya_vray\icons;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\icons;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\icons"

set "MAYA_SHELF_PATH=%MAYA_PPTOOLS%\shelves"
set "MAYA_MODULE_PATH=%MAYA_PPTOOLS%\modules;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\modules"
set "MAYA_PRESET_PATH=%MAYA_PPTOOLS%\presets;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\presets"
set "PYTHONPATH=%PP_RESOURCE%\lib\python;%MAYA_PPTOOLS%\scripts\production;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\scripts"


set "exocortex_LICENSE=5053@sparkle-1"

set "PATH=%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\lib;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\bin;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\bin\;%PP_RESOURCE%\bin\win32\vray\%PP_VRAY%\vray\bin;%PATH%";

REM !!!! SET USERNAMES THAT ARE ALLOWED TO USE SHAVE HAIRCUT !!!!!
FOR %%A IN (ari jason mirelle raphe jeong phuwit hayden adam) DO IF %%A==%USERNAME% set "MAYA_PLUG_IN_PATH=%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\plug-ins;%MAYA_PLUG_IN_PATH%"

REM copying adobe camera raw preference file to user's appdata directory
REM copy "\\moon\pipeline\dev\config\Default_766173B5EFB0DD03.xmp" "%APPDATA%\Adobe\CameraRaw\Defaults\Default_766173B5EFB0DD03.xmp"

start \REALTIME "Maya" "C:\Program Files\Autodesk\Maya%PP_MAYA%\bin\maya.exe" -noAutoloadPlugins
