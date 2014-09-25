set "MODE=pub"
set "PP_JOB_SERVERS=M:\;P:\jobs;N:\"
set "PP_RESOURCE=\\moon\pipeline\%MODE%"
REM set "PP_RESOURCE=\\monkey\resources\pipeline\%MODE%"
set "MAYA_PPTOOLS=%PP_RESOURCE%\maya\2014-x64"
set "MAYA_PPTOOLS_COMMON=%PP_RESOURCE%\maya\common"
set "PP_ARNOLD=0.21.0x";

REM //////////////
REM VRAY CONFIG
REM /////////////

REM COPIES THE VRAY.DLL TO BE IN SAME PATH AS maya.exe
IF NOT EXIST "C:\Program Files\Autodesk\Maya2014\bin\vray.dll" COPY "\\moon\pipeline\pub\bin\win32\vray\vray23002\maya_root\bin\vray.dll" "C:\Program Files\Autodesk\Maya2014\bin\vray.dll"
IF NOT EXIST "C:\Program Files\Autodesk\Maya2014\bin\dte_wrapper.dll" COPY "\\moon\pipeline\pub\bin\win32\vray\vray23002\maya_root\bin\dte_wrapper.dll" "C:\Program Files\Autodesk\Maya2014\bin\dte_wrapper.dll"
IF NOT EXIST "C:\Program Files\Autodesk\Maya2014\bin\libmmd.dll" COPY "\\moon\pipeline\pub\bin\win32\vray\vray23002\maya_root\bin\libmmd.dll" "C:\Program Files\Autodesk\Maya2014\bin\libmmd.dll"
IF NOT EXIST "C:\Program Files\Autodesk\Maya2014\bin\svml_dispmd.dll" COPY "\\moon\pipeline\pub\bin\win32\vray\vray23002\maya_root\bin\svml_dispmd.dll" "C:\Program Files\Autodesk\Maya2014\bin\svml_dispmd.dll"

REM COPIES THE VRAY RENDERDESC.XML TO RenderDesc FOLDER
IF NOT EXIST "C:\Program Files\Autodesk\Maya2014\bin\rendererDesc\vrayRenderer.xml" COPY "\\moon\pipeline\dev\bin\win32\vray\vray23002\maya_root\bin\rendererDesc\vrayRenderer.xml" "C:\Program Files\Autodesk\Maya2014\bin\rendererDesc\vrayRenderer.xml"


set "VRAY_AUTH_CLIENT_FILE_PATH=%PP_RESOURCE%\bin\win32\vray\vray23002\license"
set "VRAY_FOR_MAYA2014_MAIN_x64=%PP_RESOURCE%\bin\win32\vray\vray23002\maya_vray"
set "VRAY_FOR_MAYA2014_PLUGINS_x64=%PP_RESOURCE%\bin\win32\vray\vray23002\maya_vray\vrayplugins"
set "VRAY_PLUGINS_x64=%PP_RESOURCE%\bin\win32vray\vray23002\maya_vray\vrayplugins"
set "VRAY_TOOLS_MAYA2014_x64=%PP_RESOURCE%\bin\win32\vray\vray23002\vray\bin"


set "MAYA_SCRIPT_PATH=%PP_RESOURCE%\maya\common\scripts;%MAYA_PPTOOLS%\scripts\production;%PP_RESOURCE%\bin\win32\vray\vray23002\maya_vray\scripts;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\2012\scripts;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2014\scripts"
set "MAYA_PLUG_IN_PATH=%MAYA_PPTOOLS%\plugins;%PP_RESOURCE%\bin\win32\vray\vray23002\maya_vray\plug-ins;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\2012\plug-ins"
set "XBMLANGPATH=%PP_RESOURCE%\bin\win32\vray\vray23002\maya_vray\icons;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\2012\icons;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2014\icons"

set "MAYA_SHELF_PATH=%MAYA_PPTOOLS%\shelves"
set "MAYA_MODULE_PATH=%MAYA_PPTOOLS%\modules;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\2012;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\modules"
set "MAYA_PRESET_PATH=%MAYA_PPTOOLS%\presets;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\presets"
set "PYTHONPATH=%PP_RESOURCE%\lib\python;%MAYA_PPTOOLS%\scripts\production;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\2012\scripts"

set "ARNOLD_LICENSE_HOST=192.168.2.53"
set "MTOA_EXTENSIONS_PATH=%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\2012\extensions"
set "ARNOLD_PLUGIN_PATH=%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\2012\shaders"
REM DEFINED ABOVE ALREADY set "MAYA_MODULE_PATH=%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\2012"
set "MAYA_RENDER_DESC_PATH=%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\2012"

set "RLM_LICENSE=2765@192.168.2.174"

set "PATH=%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\lib;%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\bin;%PP_RESOURCE%\bin\win32\arnold\%PP_ARNOLD%\mtoadeploy\2012\bin\;%PATH%";

REM !!!! SET USERNAMES THAT ARE ALLOWED TO USE SHAVE HAIRCUT !!!!!
REM need all farm machines to load shave. 
REM ! CUT HERE ! FOR %%A IN (ari jason doug mirelle adam) DO IF %%A==%USERNAME% set "MAYA_PLUG_IN_PATH=%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\plug-ins;%MAYA_PLUG_IN_PATH%"
set "MAYA_PLUG_IN_PATH=%PP_RESOURCE%\bin\win32\shaveHaircut\maya2012\plug-ins;%MAYA_PLUG_IN_PATH%"


REM start "Maya" "C:\Program Files\Autodesk\Maya2014\bin\Render.exe" %*
C:\"Program Files"\Autodesk\Maya2014\bin\Render.exe %*