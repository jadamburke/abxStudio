rem @echo off 
set "MODE=pub"
set "PP_MAYA=2015"
set "MAYA_INSTALL_PATH=C:/Program Files/Autodesk/Maya%PP_MAYA%/"

REM set "ADSKFLEX_LICENSE_FILE=27000@ppny-dc01"

set "PP_MAYA_DIR=C:/Program Files/Autodesk/Maya%PP_MAYA%"
set "MTOA_VERSION=1.1.0.4"
set "MAYA_RENDER_DESC_PATH=%MAYA_RENDER_DESC_PATH%;R:\studio\nyc\bin\arnold\maya\%MTOA_VERSION%\win\2015"
set "MAYA_PLUG_IN_PATH=%MAYA_PLUG_IN_PATH%;R:\studio\nyc\bin\arnold\maya\%MTOA_VERSION%\win\2015\plug-ins"
set "MAYA_SCRIPT_PATH=%MAYA_SCRIPT_PATH%;R:\studio\nyc\bin\arnold\maya\%MTOA_VERSION%\win\2015\scripts"
REM set "MTOA_EXTENSIONS_PATH=R:\studio\nyc\bin\arnold\maya\%MTOA_VERSION%\2015\win\extensions"
set "MAYA_MODULE_PATH=%MAYA_MODULE_PATH%;R:\studio\nyc\bin\alembic\ExocortexCrateSuite1.1.145\Windows\Maya2015;R:\studio\nyc\bin\arnold\maya\%MTOA_VERSION%\win\2015"
REM set "ARNOLD_PLUGIN_PATH=R:\studio\nyc\bin\arnold\maya\%MTOA_VERSION%\win\2015\shaders"
set "EXOCORTEX_LICENSE=5063@ppny-lic"
REM set "solidangle_LICENSE=localhost"

set "MAYA_SCRIPT_PATH=%MAYA_SCRIPT_PATH%;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/cafm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/xmaya;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/brushes;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/dialogs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/fxmodules;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/tabs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/util;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/widgets;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts;"
set "MAYA_PLUG_IN_RESOURCE_PATH=C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/resources;%MAYA_PLUG_IN_RESOURCE_PATH%"
set "PYTHON_PATH=%PYTHON_PATH%;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/cafm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/xmaya;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/brushes;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/dialogs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/fxmodules;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/tabs;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/util;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts/xgenm/ui/widgets;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/scripts"
set "PATH=C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/bin;%PATH%"
set "MAYA_PLUG_IN_PATH=%MAYA_PLUG_IN_PATH%;C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/plug-ins;"

REM LOAD XGEN
set "XGEN_LOCATION=C:/Program Files/Autodesk/Maya2015/plug-ins/xgen/"
set "XGEN_ROOT=//pp-fs-nyc/production/J0166_PPNY_ChildHunger/xgen"

REM LOAD MENTAL RAY
set "MAYA_MODULE_PATH=%MAYA_MODULE_PATH%;R:\studio\nyc\bin\mentalray\maya\2015\modules"

REM LOAD REALFLOW BIN LOADER
set "MAYA_MODULE_PATH=%MAYA_MODULE_PATH%;R:\studio\nyc\bin\maya\realflow\win\14.8.012\Maya2015"

REM LOAD REALFLOW RENDER TOOLKIT
set "MAYA_MODULE_PATH=%MAYA_MODULE_PATH%;R:\studio\nyc\bin\maya\rfrk\win\2014\Maya2015"
set "PATH=%PATH%;R:\studio\nyc\bin\maya\rfrk\win\2014\RFRK 2014 For Maya"
set "PATH=%PATH%;R:\studio\nyc\bin\maya\rfrk\win\2014\Maya2015\bin"

REM Do batch render
echo "%PP_MAYA_DIR%/bin/render.exe" %*
"%PP_MAYA_DIR%/bin/render.exe" %*