setx /M MAYA_RENDER_DESC_PATH "\\monkey\resources\vray\vray22001\maya_root\bin\rendererDesc"
setx /M VRAY_FOR_MAYA2012_MAIN_x64 "\\monkey\resources\vray\vray22001\maya_vray"
setx /M VRAY_FOR_MAYA2012_PLUGINS_x64 "\\monkey\resources\vray\vray22001\maya_vray\vrayplugins"
setx /M VRAY_TOOLS_MAYA2012_x64 "\\monkey\resources\vray\vray22001\vray\bin"
setx /M VRAY_AUTH_CLIENT_FILE_PATH "\\monkey\resources\vray\vray22001\license"

setx /M PATH "%PATH%;\\monkey\resources\vray\vray22001\vray\bin\;\\monkey\resources\vray\vray22001\maya_vray\bin\;\\monkey\resources\vray\vray22001\maya_root\bin\"
setx /M VRAY_PLUGINS_x64 "\\monkey\resources\vray\vray22001\maya_vray\vrayplugins"

REM copies the maya/bin DLL files to the users install of maya because vray refuses to look at PATH variable. Possible bug???
copy "\\monkey\resources\vray\vray22001\maya_root\bin\dte_wrapper.dll" "C:\Program Files\Autodesk\Maya2012\bin\dte_wrapper.dll"
copy "\\monkey\resources\vray\vray22001\maya_root\bin\libmmd.dll" "C:\Program Files\Autodesk\Maya2012\bin\libmmd.dll"
copy "\\monkey\resources\vray\vray22001\maya_root\bin\svml_dispmd.dll" "C:\Program Files\Autodesk\Maya2012\bin\svml_dispmd.dll"
copy "\\monkey\resources\vray\vray22001\maya_root\bin\vray.dll" "C:\Program Files\Autodesk\Maya2012\bin\vray.dll"
copy "\\monkey\resources\vray\vray22001\maya_root\bin\rendererDesc\vrayRenderer.xml" "C:\Program Files\Autodesk\Maya2012\bin\rendererDesc\vrayRenderer.xml"



REM hardcodes certain vray environment variables so that mayabatch.exe can find the vray plugin automatically
setx /M MAYA_SCRIPT_PATH "\\monkey\resources\vray\vray22001\maya_vray\scripts"
setx /M MAYA_PLUG_IN_PATH "\\monkey\resources\vray\vray22001\maya_vray\plug-ins"
setx /M XBMLANGPATH "\\monkey\resources\vray\vray22001\maya_vray\icons"