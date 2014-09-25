#!/bin/bash -x
MAYA_VERSION=2014
MAYA_INSTALL_PATH="/Applications/Autodesk/maya2014" # default should be "/Applications/Autodesk/maya${MAYA_VERSION}/"
if ( ! test -d "${MAYA_INSTALL_PATH}/Maya.app" ) ; then
    echo "ERROR: This script does not appear to be located in the Maya application bundle!"
fi


echo "Welcome to the Autodesk Maya ${MAYA_VERSION} shell"
PATH="${MAYA_INSTALL_PATH}/Maya.app/Contents/bin":/usr/aw/COM/bin:/usr/aw/COM/etc:${PATH}
export PATH

MAYA_LOCATION="${MAYA_INSTALL_PATH}/Maya.app/Contents"
export MAYA_LOCATION

DYLD_LIBRARY_PATH="${MAYA_LOCATION}/MacOS":${DYLD_LIBRARY_PATH}
export DYLD_LIBRARY_PATH


MODE="pub"
export MODE

PP_RESOURCE="/Volumes/res/studio/${MODE}"
export PP_RESOURCE

PP_JOB_SERVERS="/Volumes/jobs/"
export PP_JOB_SERVERS

MAYA_PPTOOLS="${PP_RESOURCE}/maya/common"
export MAYA_PPTOOLS

MAYA_PPTOOLS_VERSIONED="${PP_RESOURCE}/maya/2014-x64"
export MAYA_PPTOOLS_VERSIONED

MAYA_PPTOOLS_COMMON="${PP_RESOURCE}/maya/common"
export MAYA_PPTOOLS_COMMON

PP_MAYA="2014"
export PP_MAYA

STUDIO="Studio"
export PP_MAYA

PP_ARNOLD="0.25.3"
export PP_ARNOLD




MAYA_SCRIPT_PATH="${MAYA_PPTOOLS}/scripts/production"
export MAYA_SCRIPT_PATH

MAYA_PLUG_IN_PATH="${MAYA_PPTOOLS_VERSIONED}/plugins"
export MAYA_PLUG_IN_PATH

XBMLANGPATH="${PP_RESOURCE}/vray/vray22001/maya_vray/icons"
export XBMLANGPATH

MAYA_SHELF_PATH="${MAYA_PPTOOLS}/shelves"
export MAYA_SHELF_PATH

MAYA_MODULE_PATH="${MAYA_PPTOOLS}/shelves"
export MAYA_MODULE_PATH

MAYA_PRESET_PATH="${MAYA_PPTOOLS}/presets"
export MAYA_PRESET_PATH

PYTHONPATH="${PP_RESOURCE}/python"
export PYTHONPATH
