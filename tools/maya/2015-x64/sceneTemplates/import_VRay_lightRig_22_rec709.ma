//Maya ASCII 2012 scene
//Name: import_VRay_lightRig_22_rec709.ma
//Last modified: Wed, Mar 06, 2013 03:56:21 PM
//Codeset: 1252
requires maya "2012";
requires "vrayformaya" "2.20.01";
requires "Mayatomr" "2012.0m - 3.9.1.48 ";
requires "ikSpringSolver" "1.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2012";
fileInfo "version" "2012 x64";
fileInfo "cutIdentifier" "201201172029-821146";
fileInfo "osv" "Microsoft Windows 7 Business Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -s -n "persp";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 3427.0066575330638 2704.1919091408831 -3687.1030174488433 ;
	setAttr ".r" -type "double3" -22.538352729600334 -220.99999999998437 0 ;
createNode camera -s -n "perspShape" -p "persp";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999986;
	setAttr ".ncp" 7.5;
	setAttr ".fcp" 75000;
	setAttr ".coi" 4858.3413225935092;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".lls" 35;
createNode transform -s -n "top";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 67507.500000000015 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 7.5;
	setAttr ".fcp" 75000;
	setAttr ".coi" 3754.4452004999998;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".lls" 35;
	setAttr ".o" yes;
createNode transform -s -n "front";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 67507.500000000015 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 7.5;
	setAttr ".fcp" 75000;
	setAttr ".coi" 3754.4452004999998;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".lls" 35;
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 67507.500000000015 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 7.5;
	setAttr ".fcp" 75000;
	setAttr ".coi" 3754.4452004999998;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".lls" 35;
	setAttr ".o" yes;
createNode transform -n "VRay_lightRig_21_rec709:turntable";
	addAttr -ci true -sn "turntableVersion" -ln "turntableVersion" -dv 22 -at "long";
	setAttr ".s" -type "double3" 2.1 2.1 2.1 ;
	setAttr -cb on ".turntableVersion";
createNode transform -n "VRay_lightRig_21_rec709:renderCam" -p "VRay_lightRig_21_rec709:turntable";
	setAttr -l on ".tx";
	setAttr ".r" -type "double3" 0 0 -5.172681101354183e-014 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode camera -n "VRay_lightRig_21_rec709:renderCamShape" -p "VRay_lightRig_21_rec709:renderCam";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".ovr" 1.3;
	setAttr ".fl" 80;
	setAttr ".coi" 170.00979776401209;
	setAttr ".imn" -type "string" "persp1";
	setAttr ".den" -type "string" "persp1_depth";
	setAttr ".man" -type "string" "persp1_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".lls" 75;
	setAttr ".dr" yes;
createNode transform -n "VRay_lightRig_21_rec709:envLight" -p "VRay_lightRig_21_rec709:turntable";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightDomeShape -n "VRay_lightRig_21_rec709:envLightShape" -p "VRay_lightRig_21_rec709:envLight";
	setAttr -k off ".v";
	setAttr ".inv" yes;
	setAttr ".afd" no;
	setAttr ".afs" no;
	setAttr ".udt" yes;
	setAttr ".dsp" yes;
createNode transform -n "VRay_lightRig_21_rec709:subsurface_light" -p "VRay_lightRig_21_rec709:turntable";
	setAttr ".t" -type "double3" 8.3464220600214162e-014 108.65358899279769 -454.69311383947917 ;
	setAttr ".r" -type "double3" 0 180 0 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightRectShape -n "VRay_lightRig_21_rec709:subsurface_lightShape" 
		-p "VRay_lightRig_21_rec709:subsurface_light";
	setAttr -k off ".v";
	setAttr ".usi" 150;
	setAttr ".vsi" 150;
	setAttr ".intens" 10;
	setAttr ".inv" yes;
	setAttr ".nd" yes;
	setAttr ".subs" 32;
createNode transform -n "VRay_lightRig_21_rec709:mainLights" -p "VRay_lightRig_21_rec709:turntable";
createNode transform -n "VRay_lightRig_21_rec709:fill_light" -p "VRay_lightRig_21_rec709:mainLights";
	setAttr ".t" -type "double3" -329.96888952032515 84.64227423633109 461.97907687617032 ;
	setAttr ".r" -type "double3" 0 -35.725638341079367 0 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightRectShape -n "VRay_lightRig_21_rec709:fill_lightShape" -p "VRay_lightRig_21_rec709:fill_light";
	setAttr -k off ".v";
	setAttr ".usi" 150;
	setAttr ".vsi" 150;
	setAttr ".shad" no;
	setAttr ".intens" 0.22499999403953552;
	setAttr ".inv" yes;
	setAttr ".nd" yes;
	setAttr ".subs" 32;
createNode transform -n "VRay_lightRig_21_rec709:rim_light" -p "VRay_lightRig_21_rec709:mainLights";
	setAttr ".t" -type "double3" -407.21026015744849 259.64907546586147 -284.84781761513131 ;
	setAttr ".r" -type "double3" 160.15072043969218 -50.442999999999969 179.814 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" -5.5511151231257827e-016 2.2204460492503131e-016 0 ;
	setAttr ".rpt" -type "double3" 8.1749110470471417e-016 -1.21638357868772e-018 -4.8973915897283329e-016 ;
createNode VRayLightRectShape -n "VRay_lightRig_21_rec709:rim_lightShape" -p "VRay_lightRig_21_rec709:rim_light";
	setAttr -k off ".v";
	setAttr ".usi" 150;
	setAttr ".vsi" 150;
	setAttr ".intens" 1.7999999523162842;
	setAttr ".inv" yes;
	setAttr ".nd" yes;
	setAttr ".subs" 32;
createNode transform -n "VRay_lightRig_21_rec709:key_light" -p "VRay_lightRig_21_rec709:mainLights";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 346.12412473650301 275.09711022860404 388.25236847112842 ;
	setAttr ".r" -type "double3" -18.600000000000168 42.070189989848693 0 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightRectShape -n "VRay_lightRig_21_rec709:key_lightShape" -p "VRay_lightRig_21_rec709:key_light";
	setAttr -k off ".v";
	setAttr ".on" no;
	setAttr ".usi" 75;
	setAttr ".vsi" 75;
	setAttr ".intens" 0.93999999761581421;
	setAttr ".inv" yes;
	setAttr ".nd" yes;
	setAttr ".subs" 32;
createNode transform -n "VRay_lightRig_21_rec709:iblD_keyLight" -p "VRay_lightRig_21_rec709:mainLights";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightDomeShape -n "VRay_lightRig_21_rec709:iblD_keyLightShape" -p "VRay_lightRig_21_rec709:iblD_keyLight";
	setAttr -k off ".v";
	setAttr ".gre" 100;
	setAttr ".intens" 17;
	setAttr ".inv" yes;
	setAttr ".udt" yes;
	setAttr ".tres" 1024;
	setAttr ".dsp" yes;
	setAttr ".subs" 32;
	setAttr ".vptsrgb" no;
	setAttr ".vpg" 2.2000000476837158;
createNode transform -n "VRay_lightRig_21_rec709:ibls" -p "VRay_lightRig_21_rec709:turntable";
	setAttr ".s" -type "double3" 0.47619047619047616 0.47619047619047616 0.47619047619047616 ;
createNode transform -n "VRay_lightRig_21_rec709:iblA" -p "VRay_lightRig_21_rec709:ibls";
	setAttr ".v" no;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightDomeShape -n "VRay_lightRig_21_rec709:iblAShape" -p "VRay_lightRig_21_rec709:iblA";
	setAttr -k off ".v";
	setAttr ".intens" 45;
	setAttr ".inv" yes;
	setAttr ".udt" yes;
	setAttr ".tres" 1024;
	setAttr ".dsp" yes;
	setAttr ".subs" 32;
	setAttr ".lsc" 50;
	setAttr ".vptsrgb" no;
	setAttr ".vpg" 2.2000000476837158;
createNode transform -n "VRay_lightRig_21_rec709:iblB" -p "VRay_lightRig_21_rec709:ibls";
	setAttr ".v" no;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightDomeShape -n "VRay_lightRig_21_rec709:iblBShape" -p "VRay_lightRig_21_rec709:iblB";
	setAttr -k off ".v";
	setAttr ".gre" 100;
	setAttr ".intens" 80;
	setAttr ".inv" yes;
	setAttr ".udt" yes;
	setAttr ".tres" 1024;
	setAttr ".dsp" yes;
	setAttr ".subs" 32;
	setAttr ".lsc" 50;
	setAttr ".vptsrgb" no;
	setAttr ".vpg" 2.2000000476837158;
createNode transform -n "VRay_lightRig_21_rec709:iblC" -p "VRay_lightRig_21_rec709:ibls";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightDomeShape -n "VRay_lightRig_21_rec709:iblCShape" -p "VRay_lightRig_21_rec709:iblC";
	setAttr -k off ".v";
	setAttr ".gre" 100;
	setAttr ".intens" 100;
	setAttr ".inv" yes;
	setAttr ".udt" yes;
	setAttr ".tres" 1024;
	setAttr ".dsp" yes;
	setAttr ".subs" 32;
	setAttr ".lsc" 50;
	setAttr ".vptsrgb" no;
	setAttr ".vpg" 2.2000000476837158;
createNode transform -n "VRay_lightRig_21_rec709:iblE" -p "VRay_lightRig_21_rec709:ibls";
	setAttr ".v" no;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightDomeShape -n "VRay_lightRig_21_rec709:iblEShape" -p "VRay_lightRig_21_rec709:iblE";
	setAttr -k off ".v";
	setAttr ".gre" 100;
	setAttr ".intens" 70;
	setAttr ".inv" yes;
	setAttr ".udt" yes;
	setAttr ".tres" 1024;
	setAttr ".dsp" yes;
	setAttr ".subs" 32;
	setAttr ".lsc" 50;
	setAttr ".vptsrgb" no;
	setAttr ".vpg" 2.2000000476837158;
createNode transform -n "VRay_lightRig_21_rec709:iblF" -p "VRay_lightRig_21_rec709:ibls";
	setAttr ".v" no;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightDomeShape -n "VRay_lightRig_21_rec709:iblFShape" -p "VRay_lightRig_21_rec709:iblF";
	setAttr -k off ".v";
	setAttr ".intens" 27;
	setAttr ".inv" yes;
	setAttr ".udt" yes;
	setAttr ".tres" 1024;
	setAttr ".dsp" yes;
	setAttr ".subs" 16;
	setAttr ".lsc" 50;
	setAttr ".vptsrgb" no;
	setAttr ".vpg" 2.2000000476837158;
createNode transform -n "VRay_lightRig_21_rec709:iblG" -p "VRay_lightRig_21_rec709:ibls";
	setAttr ".v" no;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightDomeShape -n "VRay_lightRig_21_rec709:iblGShape" -p "VRay_lightRig_21_rec709:iblG";
	setAttr -k off ".v";
	setAttr ".intens" 18;
	setAttr ".inv" yes;
	setAttr ".udt" yes;
	setAttr ".tres" 1024;
	setAttr ".dsp" yes;
	setAttr ".subs" 16;
	setAttr ".lsc" 50;
	setAttr ".vptsrgb" no;
	setAttr ".vpg" 2.2000000476837158;
createNode transform -n "VRay_lightRig_21_rec709:iblH" -p "VRay_lightRig_21_rec709:ibls";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightDomeShape -n "VRay_lightRig_21_rec709:iblHShape" -p "VRay_lightRig_21_rec709:iblH";
	setAttr -k off ".v";
	setAttr ".intens" 135;
	setAttr ".inv" yes;
	setAttr ".udt" yes;
	setAttr ".tres" 1024;
	setAttr ".dsp" yes;
	setAttr ".subs" 16;
	setAttr ".lsc" 50;
	setAttr ".vptsrgb" no;
	setAttr ".vpg" 2.2000000476837158;
createNode transform -n "VRay_lightRig_21_rec709:iblI" -p "VRay_lightRig_21_rec709:ibls";
	setAttr ".v" no;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightDomeShape -n "VRay_lightRig_21_rec709:iblIShape" -p "VRay_lightRig_21_rec709:iblI";
	setAttr -k off ".v";
	setAttr ".intens" 60;
	setAttr ".inv" yes;
	setAttr ".udt" yes;
	setAttr ".tres" 1024;
	setAttr ".dsp" yes;
	setAttr ".subs" 16;
	setAttr ".lsc" 50;
	setAttr ".vptsrgb" no;
	setAttr ".vpg" 2.2000000476837158;
createNode transform -n "VRay_lightRig_21_rec709:iblJ" -p "VRay_lightRig_21_rec709:ibls";
	setAttr ".v" no;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightDomeShape -n "VRay_lightRig_21_rec709:iblJShape" -p "VRay_lightRig_21_rec709:iblJ";
	setAttr -k off ".v";
	setAttr ".intens" 50;
	setAttr ".inv" yes;
	setAttr ".udt" yes;
	setAttr ".tres" 1024;
	setAttr ".dsp" yes;
	setAttr ".subs" 16;
	setAttr ".lsc" 50;
	setAttr ".vptsrgb" no;
	setAttr ".vpg" 2.2000000476837158;
createNode transform -n "VRay_lightRig_21_rec709:iblK" -p "VRay_lightRig_21_rec709:ibls";
	setAttr ".v" no;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightDomeShape -n "VRay_lightRig_21_rec709:iblKShape" -p "VRay_lightRig_21_rec709:iblK";
	setAttr -k off ".v";
	setAttr ".intens" 80;
	setAttr ".inv" yes;
	setAttr ".udt" yes;
	setAttr ".tres" 1024;
	setAttr ".dsp" yes;
	setAttr ".subs" 16;
	setAttr ".lsc" 50;
	setAttr ".vptsrgb" no;
	setAttr ".vpg" 2.2000000476837158;
createNode transform -n "VRay_lightRig_21_rec709:iblL" -p "VRay_lightRig_21_rec709:ibls";
	setAttr ".v" no;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightDomeShape -n "VRay_lightRig_21_rec709:iblLShape" -p "VRay_lightRig_21_rec709:iblL";
	setAttr -k off ".v";
	setAttr ".intens" 60;
	setAttr ".inv" yes;
	setAttr ".udt" yes;
	setAttr ".tres" 1024;
	setAttr ".dsp" yes;
	setAttr ".subs" 16;
	setAttr ".lsc" 50;
	setAttr ".vptsrgb" no;
	setAttr ".vpg" 2.2000000476837158;
createNode transform -n "VRay_lightRig_21_rec709:beautyFill" -p "VRay_lightRig_21_rec709:ibls";
	setAttr ".t" -type "double3" -478.45488980447146 122.73129764268008 669.869661470447 ;
	setAttr ".r" -type "double3" 0 -35.725638341079367 0 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightRectShape -n "VRay_lightRig_21_rec709:beautyFillShape" -p "VRay_lightRig_21_rec709:beautyFill";
	setAttr -k off ".v";
	setAttr ".lc" -type "float3" 0.89300001 0.98038334 1 ;
	setAttr ".usi" 150;
	setAttr ".vsi" 150;
	setAttr ".shad" no;
	setAttr ".intens" 0.10000000149011612;
	setAttr ".inv" yes;
	setAttr ".nd" yes;
	setAttr ".subs" 32;
createNode transform -n "VRay_lightRig_21_rec709:beautyRim" -p "VRay_lightRig_21_rec709:ibls";
	setAttr ".t" -type "double3" -588.55900113175142 373.15564395653684 -416.34483446441334 ;
	setAttr ".r" -type "double3" 158.60504860892857 -51.272087835833617 -179.60155578997185 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode VRayLightRectShape -n "VRay_lightRig_21_rec709:beautyRimShape" -p "VRay_lightRig_21_rec709:beautyRim";
	setAttr -k off ".v";
	setAttr ".lc" -type "float3" 0.91600001 0.96079999 1 ;
	setAttr ".usi" 220;
	setAttr ".vsi" 220;
	setAttr ".intens" 1.8999999761581421;
	setAttr ".inv" yes;
	setAttr ".nd" yes;
	setAttr ".subs" 16;
createNode lightLinker -s -n "lightLinker1";
	setAttr -s 5 ".lnk";
	setAttr -s 4 ".slnk";
createNode displayLayerManager -n "layerManager";
createNode displayLayer -n "defaultLayer";
createNode renderLayerManager -n "renderLayerManager";
createNode renderLayer -n "defaultRenderLayer";
	setAttr ".g" yes;
createNode displayLayerManager -n "layerManager1";
createNode displayLayer -n "defaultLayer1";
createNode renderLayerManager -n "renderLayerManager1";
createNode renderLayer -n "defaultRenderLayer1";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"top\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n"
		+ "                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n"
		+ "                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 0\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n"
		+ "            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n"
		+ "            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n"
		+ "            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 0\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"side\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n"
		+ "                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n"
		+ "                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n"
		+ "                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -shadows 0\n            $editorName;\n"
		+ "modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n"
		+ "                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n"
		+ "                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n"
		+ "                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n"
		+ "            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n"
		+ "            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 1\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n"
		+ "                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n"
		+ "                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 1\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n"
		+ "            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n"
		+ "            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            outlinerEditor -e \n"
		+ "                -docTag \"isolOutln_fromSeln\" \n                -showShapes 0\n                -showAttributes 0\n                -showConnected 0\n                -showAnimCurvesOnly 0\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 1\n                -showAssets 1\n                -showContainedOnly 1\n                -showPublishedAsConnected 0\n                -showContainerContents 1\n                -ignoreDagHierarchy 0\n                -expandConnections 0\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 0\n                -highlightActive 1\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"defaultSetFilter\" \n                -showSetMembers 1\n"
		+ "                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n"
		+ "            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n"
		+ "            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"graphEditor\" -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n"
		+ "                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n"
		+ "                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n"
		+ "                -smoothness \"fine\" \n                -resultSamples 1.25\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n"
		+ "                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n"
		+ "                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1.25\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n"
		+ "                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dopeSheetPanel\" -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n"
		+ "                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n"
		+ "                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n"
		+ "                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n"
		+ "                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"clipEditorPanel\" -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n"
		+ "                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"sequenceEditorPanel\" -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -image \"C:/Documents and Settings/bwilliams/My Documents/maya/projects/Tests/images/Cubes_01_large.tif\" \n"
		+ "                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range -1 -1 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n"
		+ "                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -image \"C:/Documents and Settings/bwilliams/My Documents/maya/projects/Tests/images/Cubes_01_large.tif\" \n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range -1 -1 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"visorPanel\" -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"createNodePanel\" -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Texture Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"polyTexturePlacementPanel\" -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"renderWindowPanel\" -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"blendShapePanel\" (localizedPanelLabel(\"Blend Shape\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tblendShapePanel -unParent -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tblendShapePanel -edit -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynRelEdPanel\" -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"relationshipPanel\" -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"referenceEditorPanel\" -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"componentEditorPanel\" -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynPaintScriptedPanelType\" -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"Stereo\" -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels `;\nstring $editorName = ($panelName+\"Editor\");\n"
		+ "            stereoCameraView -e \n                -editorChanged \"updateModelPanelBar\" \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n"
		+ "                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n"
		+ "                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                $editorName;\nstereoCameraView -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "string $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -editorChanged \"updateModelPanelBar\" \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n"
		+ "                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n"
		+ "                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                $editorName;\nstereoCameraView -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n"
		+ "        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-defaultImage \"\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"vertical2\\\" -ps 1 50 100 -ps 2 50 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Hypershade\")) \n\t\t\t\t\t\"scriptedPanel\"\n\t\t\t\t\t\"$panelName = `scriptedPanel -unParent  -type \\\"hyperShadePanel\\\" -l (localizedPanelLabel(\\\"Hypershade\\\")) -mbv $menusOkayInPanels `\"\n\t\t\t\t\t\"scriptedPanel -edit -l (localizedPanelLabel(\\\"Hypershade\\\")) -mbv $menusOkayInPanels  $panelName\"\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 375 -size 900 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"1 -1.000000 0.000000 -0.000000 0.000000 1.000000 0.000000\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 10 -ast 1 -aet 10 ";
	setAttr ".st" 6;
createNode mentalrayItemsList -s -n "mentalrayItemsList";
	setAttr -s 19 ".opt";
createNode mentalrayGlobals -s -n "mentalrayGlobals";
	addAttr -ci true -h true -sn "sunAndSkyShader" -ln "sunAndSkyShader" -at "message";
	setAttr ".rvb" 3;
	setAttr ".ivb" no;
createNode mentalrayOptions -s -n "miDefaultOptions";
	addAttr -ci true -m -sn "stringOptions" -ln "stringOptions" -at "compound" -nc 
		3;
	addAttr -ci true -sn "name" -ln "name" -dt "string" -p "stringOptions";
	addAttr -ci true -sn "value" -ln "value" -dt "string" -p "stringOptions";
	addAttr -ci true -sn "type" -ln "type" -dt "string" -p "stringOptions";
	setAttr ".minsp" 0;
	setAttr ".maxsp" 2;
	setAttr ".maxr" 2;
	setAttr ".fgr" 50;
	setAttr ".fgpd" 0.10000000149011612;
	setAttr -s 28 ".stringOptions";
	setAttr ".stringOptions[0].name" -type "string" "rast motion factor";
	setAttr ".stringOptions[0].value" -type "string" "1.0";
	setAttr ".stringOptions[0].type" -type "string" "scalar";
	setAttr ".stringOptions[1].name" -type "string" "rast transparency depth";
	setAttr ".stringOptions[1].value" -type "string" "8";
	setAttr ".stringOptions[1].type" -type "string" "integer";
	setAttr ".stringOptions[2].name" -type "string" "rast useopacity";
	setAttr ".stringOptions[2].value" -type "string" "true";
	setAttr ".stringOptions[2].type" -type "string" "boolean";
	setAttr ".stringOptions[3].name" -type "string" "importon";
	setAttr ".stringOptions[3].value" -type "string" "false";
	setAttr ".stringOptions[3].type" -type "string" "boolean";
	setAttr ".stringOptions[4].name" -type "string" "importon density";
	setAttr ".stringOptions[4].value" -type "string" "1.0";
	setAttr ".stringOptions[4].type" -type "string" "scalar";
	setAttr ".stringOptions[5].name" -type "string" "importon merge";
	setAttr ".stringOptions[5].value" -type "string" "0.0";
	setAttr ".stringOptions[5].type" -type "string" "scalar";
	setAttr ".stringOptions[6].name" -type "string" "importon trace depth";
	setAttr ".stringOptions[6].value" -type "string" "0";
	setAttr ".stringOptions[6].type" -type "string" "integer";
	setAttr ".stringOptions[7].name" -type "string" "importon traverse";
	setAttr ".stringOptions[7].value" -type "string" "true";
	setAttr ".stringOptions[7].type" -type "string" "boolean";
	setAttr ".stringOptions[8].name" -type "string" "shadowmap pixel samples";
	setAttr ".stringOptions[8].value" -type "string" "3";
	setAttr ".stringOptions[8].type" -type "string" "integer";
	setAttr ".stringOptions[9].name" -type "string" "ambient occlusion";
	setAttr ".stringOptions[9].value" -type "string" "false";
	setAttr ".stringOptions[9].type" -type "string" "boolean";
	setAttr ".stringOptions[10].name" -type "string" "ambient occlusion rays";
	setAttr ".stringOptions[10].value" -type "string" "256";
	setAttr ".stringOptions[10].type" -type "string" "integer";
	setAttr ".stringOptions[11].name" -type "string" "ambient occlusion cache";
	setAttr ".stringOptions[11].value" -type "string" "false";
	setAttr ".stringOptions[11].type" -type "string" "boolean";
	setAttr ".stringOptions[12].name" -type "string" "ambient occlusion cache density";
	setAttr ".stringOptions[12].value" -type "string" "1.0";
	setAttr ".stringOptions[12].type" -type "string" "scalar";
	setAttr ".stringOptions[13].name" -type "string" "ambient occlusion cache points";
	setAttr ".stringOptions[13].value" -type "string" "64";
	setAttr ".stringOptions[13].type" -type "string" "integer";
	setAttr ".stringOptions[14].name" -type "string" "irradiance particles";
	setAttr ".stringOptions[14].value" -type "string" "false";
	setAttr ".stringOptions[14].type" -type "string" "boolean";
	setAttr ".stringOptions[15].name" -type "string" "irradiance particles rays";
	setAttr ".stringOptions[15].value" -type "string" "256";
	setAttr ".stringOptions[15].type" -type "string" "integer";
	setAttr ".stringOptions[16].name" -type "string" "irradiance particles interpolate";
	setAttr ".stringOptions[16].value" -type "string" "1";
	setAttr ".stringOptions[16].type" -type "string" "integer";
	setAttr ".stringOptions[17].name" -type "string" "irradiance particles interppoints";
	setAttr ".stringOptions[17].value" -type "string" "64";
	setAttr ".stringOptions[17].type" -type "string" "integer";
	setAttr ".stringOptions[18].name" -type "string" "irradiance particles indirect passes";
	setAttr ".stringOptions[18].value" -type "string" "0";
	setAttr ".stringOptions[18].type" -type "string" "integer";
	setAttr ".stringOptions[19].name" -type "string" "irradiance particles scale";
	setAttr ".stringOptions[19].value" -type "string" "1.0";
	setAttr ".stringOptions[19].type" -type "string" "scalar";
	setAttr ".stringOptions[20].name" -type "string" "irradiance particles env";
	setAttr ".stringOptions[20].value" -type "string" "true";
	setAttr ".stringOptions[20].type" -type "string" "boolean";
	setAttr ".stringOptions[21].name" -type "string" "irradiance particles env rays";
	setAttr ".stringOptions[21].value" -type "string" "256";
	setAttr ".stringOptions[21].type" -type "string" "integer";
	setAttr ".stringOptions[22].name" -type "string" "irradiance particles env scale";
	setAttr ".stringOptions[22].value" -type "string" "1";
	setAttr ".stringOptions[22].type" -type "string" "integer";
	setAttr ".stringOptions[23].name" -type "string" "irradiance particles rebuild";
	setAttr ".stringOptions[23].value" -type "string" "true";
	setAttr ".stringOptions[23].type" -type "string" "boolean";
	setAttr ".stringOptions[24].name" -type "string" "irradiance particles file";
	setAttr ".stringOptions[24].value" -type "string" "";
	setAttr ".stringOptions[24].type" -type "string" "string";
	setAttr ".stringOptions[25].name" -type "string" "geom displace motion factor";
	setAttr ".stringOptions[25].value" -type "string" "1.0";
	setAttr ".stringOptions[25].type" -type "string" "scalar";
	setAttr ".stringOptions[26].name" -type "string" "contrast all buffers";
	setAttr ".stringOptions[26].value" -type "string" "true";
	setAttr ".stringOptions[26].type" -type "string" "boolean";
	setAttr ".stringOptions[27].name" -type "string" "finalgather normal tolerance";
	setAttr ".stringOptions[27].value" -type "string" "25.842";
	setAttr ".stringOptions[27].type" -type "string" "scalar";
createNode mentalrayFramebuffer -s -n "miDefaultFramebuffer";
createNode ikSpringSolver -s -n "ikSpringSolver";
createNode mentalrayOptions -s -n "miContourPreset";
createNode mentalrayOptions -s -n "Draft";
	setAttr ".maxr" 2;
createNode mentalrayOptions -s -n "DraftMotionBlur";
	setAttr ".maxr" 2;
	setAttr ".mb" 1;
	setAttr ".tconr" 1;
	setAttr ".tcong" 1;
	setAttr ".tconb" 1;
	setAttr ".tcona" 1;
createNode mentalrayOptions -s -n "DraftRapidMotion";
	setAttr ".scan" 3;
	setAttr ".rapc" 1;
	setAttr ".raps" 0.25;
	setAttr ".maxr" 2;
	setAttr ".mb" 1;
	setAttr ".tconr" 1;
	setAttr ".tcong" 1;
	setAttr ".tconb" 1;
	setAttr ".tcona" 1;
createNode mentalrayOptions -s -n "Preview";
	setAttr ".minsp" -1;
	setAttr ".maxsp" 1;
	setAttr ".fil" 1;
	setAttr ".rflr" 2;
	setAttr ".rfrr" 2;
	setAttr ".maxr" 4;
createNode mentalrayOptions -s -n "PreviewMotionblur";
	setAttr ".minsp" -1;
	setAttr ".maxsp" 1;
	setAttr ".fil" 1;
	setAttr ".rflr" 2;
	setAttr ".rfrr" 2;
	setAttr ".maxr" 4;
	setAttr ".mb" 1;
	setAttr ".tconr" 0.5;
	setAttr ".tcong" 0.5;
	setAttr ".tconb" 0.5;
	setAttr ".tcona" 0.5;
createNode mentalrayOptions -s -n "PreviewRapidMotion";
	setAttr ".minsp" -1;
	setAttr ".maxsp" 1;
	setAttr ".fil" 1;
	setAttr ".scan" 3;
	setAttr ".rapc" 3;
	setAttr ".rflr" 2;
	setAttr ".rfrr" 2;
	setAttr ".maxr" 4;
	setAttr ".mb" 1;
	setAttr ".tconr" 0.5;
	setAttr ".tcong" 0.5;
	setAttr ".tconb" 0.5;
	setAttr ".tcona" 0.5;
createNode mentalrayOptions -s -n "PreviewCaustics";
	setAttr ".minsp" -1;
	setAttr ".maxsp" 1;
	setAttr ".fil" 1;
	setAttr ".rflr" 2;
	setAttr ".rfrr" 2;
	setAttr ".maxr" 4;
	setAttr ".ca" yes;
	setAttr ".cc" 1;
	setAttr ".cr" 1;
createNode mentalrayOptions -s -n "PreviewGlobalIllum";
	setAttr ".minsp" -1;
	setAttr ".maxsp" 1;
	setAttr ".fil" 1;
	setAttr ".rflr" 2;
	setAttr ".rfrr" 2;
	setAttr ".maxr" 4;
	setAttr ".gi" yes;
	setAttr ".gc" 1;
	setAttr ".gr" 1;
createNode mentalrayOptions -s -n "PreviewFinalGather";
	setAttr ".minsp" -1;
	setAttr ".maxsp" 1;
	setAttr ".fil" 1;
	setAttr ".rflr" 2;
	setAttr ".rfrr" 2;
	setAttr ".maxr" 4;
	setAttr ".fg" yes;
createNode mentalrayOptions -s -n "Production";
	setAttr ".minsp" 0;
	setAttr ".maxsp" 2;
	setAttr ".fil" 2;
	setAttr ".rflr" 10;
	setAttr ".rfrr" 10;
	setAttr ".maxr" 20;
createNode mentalrayOptions -s -n "ProductionMotionblur";
	setAttr ".minsp" 0;
	setAttr ".maxsp" 2;
	setAttr ".fil" 2;
	setAttr ".rflr" 10;
	setAttr ".rfrr" 10;
	setAttr ".maxr" 20;
	setAttr ".mb" 2;
createNode mentalrayOptions -s -n "ProductionRapidMotion";
	setAttr ".minsp" 0;
	setAttr ".maxsp" 2;
	setAttr ".fil" 2;
	setAttr ".scan" 3;
	setAttr ".rapc" 8;
	setAttr ".raps" 2;
	setAttr ".rflr" 10;
	setAttr ".rfrr" 10;
	setAttr ".maxr" 20;
	setAttr ".mb" 2;
createNode mentalrayOptions -s -n "ProductionFineTrace";
	setAttr ".conr" 0.019999999552965164;
	setAttr ".cong" 0.019999999552965164;
	setAttr ".conb" 0.019999999552965164;
	setAttr ".minsp" 1;
	setAttr ".maxsp" 2;
	setAttr ".fil" 1;
	setAttr ".filw" 0.75;
	setAttr ".filh" 0.75;
	setAttr ".jit" yes;
	setAttr ".scan" 0;
createNode mentalrayOptions -s -n "ProductionRapidFur";
	setAttr ".conr" 0.039999999105930328;
	setAttr ".cong" 0.029999999329447746;
	setAttr ".conb" 0.070000000298023224;
	setAttr ".minsp" 0;
	setAttr ".maxsp" 2;
	setAttr ".fil" 1;
	setAttr ".filw" 1.1449999809265137;
	setAttr ".filh" 1.1449999809265137;
	setAttr ".jit" yes;
	setAttr ".scan" 3;
	setAttr ".rapc" 3;
	setAttr ".raps" 0.25;
	setAttr ".ray" no;
	setAttr ".shmth" 3;
	setAttr ".shmap" 3;
	setAttr ".mbsm" no;
	setAttr ".bism" 0.019999999552965164;
createNode mentalrayOptions -s -n "ProductionRapidHair";
	setAttr ".conr" 0.039999999105930328;
	setAttr ".cong" 0.029999999329447746;
	setAttr ".conb" 0.070000000298023224;
	setAttr ".minsp" 0;
	setAttr ".maxsp" 2;
	setAttr ".fil" 1;
	setAttr ".filw" 1.1449999809265137;
	setAttr ".filh" 1.1449999809265137;
	setAttr ".jit" yes;
	setAttr ".scan" 3;
	setAttr ".rapc" 6;
	setAttr ".ray" no;
	setAttr ".shmth" 3;
	setAttr ".shmap" 3;
	setAttr ".mbsm" no;
	setAttr ".bism" 0.019999999552965164;
createNode mentalrayOptions -s -n "PreviewImrRayTracyOff";
	setAttr ".splck" no;
	setAttr ".minsp" 0;
	setAttr ".fil" 1;
	setAttr ".ray" no;
createNode mentalrayOptions -s -n "PreviewImrRayTracyOn";
	setAttr ".splck" no;
	setAttr ".minsp" 0;
	setAttr ".fil" 1;
	setAttr ".rfrr" 2;
	setAttr ".maxr" 3;
	setAttr ".shrd" 1;
createNode VRaySettingsNode -s -n "vraySettings";
	setAttr ".gi" yes;
	setAttr ".se" 3;
	setAttr ".rdist" 1500;
	setAttr ".cfile" -type "string" "";
	setAttr ".casf" -type "string" "";
	setAttr ".st" 2;
	setAttr ".aaft" 6;
	setAttr ".fnm" -type "string" "";
	setAttr ".as" no;
	setAttr ".asf" -type "string" "";
	setAttr ".imcp" 3;
	setAttr ".imaxr" -1;
	setAttr ".icts" 0.4;
	setAttr ".ints" 0.2;
	setAttr ".ifile" -type "string" "";
	setAttr ".iscf" no;
	setAttr ".impass" no;
	setAttr ".ias" no;
	setAttr ".iasf" -type "string" "";
	setAttr ".ofn" -type "string" "";
	setAttr ".pmfile" -type "string" "";
	setAttr ".pmasf" -type "string" "";
	setAttr ".cmbm" 1.95;
	setAttr ".cmsm" yes;
	setAttr ".cmao" yes;
	setAttr ".cmlw" yes;
	setAttr ".cg" 1.9500000476837158;
	setAttr ".vrscfile" -type "string" "";
	setAttr ".mtah" yes;
	setAttr ".mpp" -type "string" "";
	setAttr ".ddms" 2;
	setAttr ".srdml" 13000;
	setAttr ".srgx" 32;
	setAttr ".srgy" 32;
	setAttr ".smsgl" 4;
	setAttr ".goldhl" 0;
	setAttr ".gomld" yes;
	setAttr ".wi" 576;
	setAttr ".he" 324;
	setAttr ".aspr" 1.7769999504089355;
	setAttr ".fnprx" -type "string" "raphe/raphe5";
	setAttr ".defd" -type "string" "";
	setAttr ".exrc" 3;
	setAttr ".exratr" -type "string" "";
	setAttr ".pngc" 8;
	setAttr ".tiffbpp" 8;
	setAttr ".animbo" yes;
	setAttr ".imgfs" -type "string" "exr (multichannel)";
	setAttr ".bkc" -type "string" "map1";
	setAttr ".vfbOn" yes;
	setAttr ".vfbSA" -type "Int32Array" 168 665 6 667 344 707 626
		 1297 325 322 325 50193 1 0 0 0 0 0 597
		 1 1 1 0 0 0 0 1 0 5 0 1065353216
		 1 1 2 1065353216 1065353216 1065353216 1065353216 1 0 5 0 0
		 0 0 1 0 5 0 1065353216 1 137531 65536 1 1313131313
		 65536 944879383 0 -525502228 1065353216 1621981420 1034147594 1053609164 1065353216 5 0 0
		 -2147483648 -2147483648 1022540247 1043327232 0 2 1041243735 1052266988 -1117864682 -1113753528 1029618963 1033730119
		 0 2 1052614959 1058567764 -1107847700 -1111808496 1039635948 1035675152 0 2 1059698673 1062445166
		 -1107264264 -1113311112 1040219384 1034172536 1 2 1065353216 1065353216 -1108663288 -1113959216 0 0
		 0 2 1 2 -1 0 0 0 1869111636 24941 0 0
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 16777215 0 70
		 1 32 53 1632775510 1868963961 1632444530 622879097 2036429430 1936876918 544108393 1701978236 1919247470
		 1835627552 1915035749 1701080677 1835627634 5989 544165376 1835103347 1634934896 543450486 1713401449 560295017 0
		 1 1 0 0 0 0 ;
	setAttr ".sRGBOn" yes;
	setAttr ".resf" yes;
	setAttr ".reea" no;
	setAttr ".mSceneName" -type "string" "//moon/pipeline/dev/maya/2012-x64/sceneTemplates/import_VRay_lightRig_22_rec709.ma";
	setAttr ".shFileName" -type "string" "";
	setAttr ".shrFileName" -type "string" "";
createNode file -n "VRay_lightRig_21_rec709:skyTexture";
	addAttr -ci true -sn "vrayFileGammaEnable" -ln "vrayFileGammaEnable" -dv 1 -at "long";
	addAttr -ci true -sn "vrayFileColorSpace" -ln "vrayFileColorSpace" -dv 1 -at "long";
	addAttr -ci true -sn "vrayFileGammaValue" -ln "vrayFileGammaValue" -dv 2.2000000476837158 
		-min 0.0010000000474974513 -max 100 -smx 3 -at "float";
	setAttr ".bnm" -type "string" "VRayShaders";
	setAttr ".ftn" -type "string" "M:/backlot/images/environment/LDR/00073_full_neutral.png";
createNode VRayPlaceEnvTex -n "VRay_lightRig_21_rec709:VRayPlaceEnvTex1";
	setAttr ".bnm" -type "string" "VRayShaders";
	setAttr ".mt" 2;
createNode setRange -n "VRay_lightRig_21_rec709:placeSkyTexture";
	setAttr ".bnm" -type "string" "VRayShaders";
	setAttr ".m" -type "float3" 1 1 0 ;
	setAttr ".om" -type "float3" 1 1 0 ;
createNode animCurveTA -n "VRay_lightRig_21_rec709:turntable2_rotateY";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 0 20 360 21 360 40 720 41 720 42 18.947;
	setAttr -s 6 ".kit[4:5]"  18 18;
	setAttr -s 6 ".kot[4:5]"  18 18;
createNode animCurveTA -n "VRay_lightRig_21_rec709:mainLights1_rotateY";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  20 0 40 0;
createNode animCurveTU -n "VRay_lightRig_21_rec709:subsurface_light1_visibility";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  40 0 41 1 42 0;
createNode animCurveTU -n "VRay_lightRig_21_rec709:mainLights1_visibility";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  40 1 41 0;
createNode VRayPlaceEnvTex -n "VRay_lightRig_21_rec709:VRayPlaceEnvTex2";
	setAttr ".mt" 2;
createNode animCurveTU -n "VRay_lightRig_21_rec709:envLight_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  40 1 41 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode objectSet -n "VRay_lightRig_21_rec709:deleteSet";
	setAttr ".ihi" 0;
	setAttr -s 53 ".dnsm";
createNode animCurveTL -n "VRay_lightRig_21_rec709:renderCam_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  20 530 21 230 41 530;
	setAttr -s 3 ".kot[0:2]"  5 5 18;
createNode animCurveTL -n "VRay_lightRig_21_rec709:renderCam_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1 55 21 90 41 55;
	setAttr -s 3 ".kot[0:2]"  5 5 18;
createNode file -n "VRay_lightRig_21_rec709:iblAFile";
	setAttr ".ftn" -type "string" "M:/Skylanders2013_PP10102/3D/Skylanders2013_maya//sourceimages/S3_010_angle01_sun_unwrapped_flipped_1024.hdr";
createNode place2dTexture -n "VRay_lightRig_21_rec709:place2dTexture1";
createNode VRayPlaceEnvTex -n "VRay_lightRig_21_rec709:VRayPlaceEnvTex3";
	setAttr ".mt" 2;
	setAttr ".hr" -200;
createNode file -n "VRay_lightRig_21_rec709:iblBFile";
	setAttr ".ftn" -type "string" "M:/Skylanders2013_PP10102/3D/Skylanders2013_maya//sourceimages/S3_120_unwrapped_flipped_1024.hdr";
createNode place2dTexture -n "VRay_lightRig_21_rec709:place2dTexture2";
createNode VRayPlaceEnvTex -n "VRay_lightRig_21_rec709:VRayPlaceEnvTex4";
	setAttr ".mt" 2;
	setAttr ".hr" 240;
createNode file -n "VRay_lightRig_21_rec709:iblCFile";
	setAttr ".cg" -type "float3" 1 0.9091 0.79799998 ;
	setAttr ".ftn" -type "string" "M:/Skylanders2013_PP10102/3D/Skylanders2013_maya//sourceimages/S3_400_unwrapped_flipped_1024_tt1.hdr";
createNode place2dTexture -n "VRay_lightRig_21_rec709:place2dTexture3";
createNode VRayPlaceEnvTex -n "VRay_lightRig_21_rec709:VRayPlaceEnvTex5";
	setAttr ".mt" 2;
	setAttr ".hr" 39.732440948486328;
createNode file -n "VRay_lightRig_21_rec709:iblDFile";
	setAttr ".ftn" -type "string" "M:/Skylanders2013_PP10102/3D/Skylanders2013_maya//sourceimages/S3_210_centerRoom_unwrapped_flipped_1024_tt4.hdr";
createNode place2dTexture -n "VRay_lightRig_21_rec709:place2dTexture4";
createNode VRayPlaceEnvTex -n "VRay_lightRig_21_rec709:VRayPlaceEnvTex6";
	setAttr ".mt" 2;
createNode file -n "VRay_lightRig_21_rec709:iblEFile";
	setAttr ".ftn" -type "string" "M:/Skylanders2013_PP10102/3D/Skylanders2013_maya//sourceimages/S3_860_unwrapped_flipped_1024.hdr";
createNode place2dTexture -n "VRay_lightRig_21_rec709:place2dTexture5";
createNode VRayPlaceEnvTex -n "VRay_lightRig_21_rec709:VRayPlaceEnvTex7";
	setAttr ".mt" 2;
	setAttr ".hr" 250.43478393554687;
createNode file -n "VRay_lightRig_21_rec709:iblFFile";
	setAttr ".ftn" -type "string" "M:/STORY2012_PP10088/SOURCE/SHOOT/December2012/S3_180_STILL/IBL/hdr/unwrapped_flipped_1024.hdr";
createNode place2dTexture -n "VRay_lightRig_21_rec709:place2dTexture6";
createNode VRayPlaceEnvTex -n "VRay_lightRig_21_rec709:VRayPlaceEnvTex8";
	setAttr ".mt" 2;
	setAttr ".hr" 297.39129638671875;
createNode file -n "VRay_lightRig_21_rec709:iblGFile";
	setAttr ".ftn" -type "string" "M:/STORY2012_PP10088/SOURCE/SHOOT/December2012/S3_180_STILL/IBL/hdr/unwrapped_flipped_1024.hdr";
createNode place2dTexture -n "VRay_lightRig_21_rec709:place2dTexture7";
createNode VRayPlaceEnvTex -n "VRay_lightRig_21_rec709:VRayPlaceEnvTex9";
	setAttr ".mt" 2;
	setAttr ".hr" 301.00335693359375;
createNode animCurveTU -n "VRay_lightRig_21_rec709:iblH_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  42 0 43 1 44 0;
	setAttr -s 3 ".kot[0:2]"  5 5 5;
createNode file -n "VRay_lightRig_21_rec709:iblHFile";
	setAttr ".cg" -type "float3" 0.91600001 0.97619998 1 ;
	setAttr ".ftn" -type "string" "M:/STORY2012_PP10088/SOURCE/SHOOT/December2012/S3_010_MOCO/IBL/hdr2/angle03_far_unwrapped_flipped_1024.hdr";
createNode place2dTexture -n "VRay_lightRig_21_rec709:place2dTexture8";
createNode VRayPlaceEnvTex -n "VRay_lightRig_21_rec709:VRayPlaceEnvTex10";
	setAttr ".mt" 2;
	setAttr ".hr" 130;
	setAttr ".vr" 8;
createNode file -n "VRay_lightRig_21_rec709:iblIFile";
	setAttr ".ftn" -type "string" "M:/STORY2012_PP10088/SOURCE/SHOOT/December2012/S3_280_MOCO/IBL/hdr/unwrapped_flipped_1024.hdr";
createNode place2dTexture -n "VRay_lightRig_21_rec709:place2dTexture9";
createNode VRayPlaceEnvTex -n "VRay_lightRig_21_rec709:VRayPlaceEnvTex11";
	setAttr ".mt" 2;
	setAttr ".hr" 226.35450744628906;
createNode file -n "VRay_lightRig_21_rec709:iblJFile";
	setAttr ".ftn" -type "string" "M:/STORY2012_PP10088/SOURCE/SHOOT/December2012/S3_830_STILL/IBL/hdr/unwrapped_flipped_1024.hdr";
createNode place2dTexture -n "VRay_lightRig_21_rec709:place2dTexture10";
createNode VRayPlaceEnvTex -n "VRay_lightRig_21_rec709:VRayPlaceEnvTex12";
	setAttr ".mt" 2;
	setAttr ".hr" 296.18728637695312;
createNode file -n "VRay_lightRig_21_rec709:iblKFile";
	setAttr ".ftn" -type "string" "M:/STORY2012_PP10088/SOURCE/SHOOT/December2012/S3_410_STILL/IBL/hdr/unwrapped_flipped_1024.hdr";
createNode place2dTexture -n "VRay_lightRig_21_rec709:place2dTexture11";
createNode VRayPlaceEnvTex -n "VRay_lightRig_21_rec709:VRayPlaceEnvTex13";
	setAttr ".mt" 2;
	setAttr ".hr" 349.16387939453125;
createNode file -n "VRay_lightRig_21_rec709:iblLFile";
	setAttr ".ftn" -type "string" "M:/STORY2012_PP10088/SOURCE/SHOOT/December2012/S3_460_MOCO/IBL/hdr/unwrapped_flipped_1024.hdr";
createNode place2dTexture -n "VRay_lightRig_21_rec709:place2dTexture12";
createNode VRayPlaceEnvTex -n "VRay_lightRig_21_rec709:VRayPlaceEnvTex14";
	setAttr ".mt" 2;
	setAttr ".hr" 163.74581909179687;
createNode animCurveTU -n "VRay_lightRig_21_rec709:iblC_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  41 0 42 1 43 0;
	setAttr -s 3 ".kot[0:2]"  5 5 5;
createNode animCurveTU -n "VRay_lightRig_21_rec709:beautyRim_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  42 0 43 1 44 0;
	setAttr -s 3 ".kot[0:2]"  5 5 5;
createNode animCurveTU -n "VRay_lightRig_21_rec709:beautyFill_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  42 0 43 1 44 0;
	setAttr -s 3 ".kot[0:2]"  5 5 5;
createNode animCurveTU -n "VRay_lightRig_21_rec709:iblRot";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr -s 6 ".ktv[0:5]"  1 203.47825622558594 20 -156.52200317382812
		 21 -156.52200317382812 40 -516.52197265625 41 203.478 42 184.531005859375;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr ".unw" 1;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
	setAttr -cb on ".mimt";
	setAttr -cb on ".miop";
	setAttr -k on ".mico";
	setAttr -cb on ".mise";
	setAttr -cb on ".mism";
	setAttr -cb on ".mice";
	setAttr -av -cb on ".micc";
	setAttr -k on ".micr";
	setAttr -k on ".micg";
	setAttr -k on ".micb";
	setAttr -cb on ".mica";
	setAttr -cb on ".micw";
	setAttr -cb on ".mirw";
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
	setAttr -cb on ".mimt";
	setAttr -cb on ".miop";
	setAttr -k on ".mico";
	setAttr -cb on ".mise";
	setAttr -cb on ".mism";
	setAttr -cb on ".mice";
	setAttr -av -cb on ".micc";
	setAttr -k on ".micr";
	setAttr -k on ".micg";
	setAttr -k on ".micb";
	setAttr -cb on ".mica";
	setAttr -cb on ".micw";
	setAttr -cb on ".mirw";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".s";
select -ne :defaultTextureList1;
	setAttr -s 13 ".tx";
select -ne :lightList1;
	setAttr -s 19 ".l";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 27 ".u";
select -ne :defaultRenderingList1;
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultRenderGlobals;
	addAttr -ci true -sn "renderPreset" -ln "renderPreset" -dt "string";
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".macc";
	setAttr -k on ".macd";
	setAttr -k on ".macq";
	setAttr -k on ".mcfr";
	setAttr -cb on ".ifg";
	setAttr -k on ".clip";
	setAttr -k on ".edm";
	setAttr -k on ".edl";
	setAttr -cb on ".ren" -type "string" "vray";
	setAttr -av -k on ".esr";
	setAttr -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf";
	setAttr -cb on ".imfkey";
	setAttr -k on ".gama";
	setAttr -cb on ".an" yes;
	setAttr -cb on ".ar";
	setAttr -k on ".fs" 101;
	setAttr -k on ".ef" 301;
	setAttr -av -k on ".bfs";
	setAttr -cb on ".me";
	setAttr -cb on ".se";
	setAttr -k on ".be";
	setAttr -cb on ".ep";
	setAttr -k on ".fec";
	setAttr -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -cb on ".oft" -type "string" "";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -cb on ".pff" yes;
	setAttr -cb on ".peie";
	setAttr -cb on ".ifp";
	setAttr ".rv" -type "string" "";
	setAttr -k on ".comp";
	setAttr -k on ".cth";
	setAttr -k on ".soll";
	setAttr -k on ".rd";
	setAttr -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -k on ".shs";
	setAttr -k on ".lpr";
	setAttr -cb on ".gv";
	setAttr -cb on ".sv";
	setAttr -k on ".mm";
	setAttr -k on ".npu";
	setAttr -k on ".itf";
	setAttr -k on ".shp";
	setAttr -cb on ".isp";
	setAttr -k on ".uf";
	setAttr -k on ".oi";
	setAttr -k on ".rut";
	setAttr -k on ".mb";
	setAttr -av -k on ".mbf";
	setAttr -k on ".afp";
	setAttr -k on ".pfb";
	setAttr -k on ".pram" -type "string" "currentTime -e `currentTime -q`;";
	setAttr -k on ".poam" -type "string" "";
	setAttr -k on ".prlm" -type "string" "";
	setAttr -k on ".polm" -type "string" "";
	setAttr -cb on ".prm" -type "string" "";
	setAttr -cb on ".pom" -type "string" "";
	setAttr -cb on ".pfrm";
	setAttr -cb on ".pfom";
	setAttr -av -k on ".bll";
	setAttr -k on ".bls";
	setAttr -av -k on ".smv";
	setAttr -k on ".ubc";
	setAttr -k on ".mbc";
	setAttr -cb on ".mbt";
	setAttr -k on ".udbx";
	setAttr -k on ".smc";
	setAttr -k on ".kmv";
	setAttr -cb on ".isl";
	setAttr -cb on ".ism";
	setAttr -cb on ".imb";
	setAttr -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -k on ".tlwd";
	setAttr -k on ".tlht";
	setAttr -k on ".jfc";
	setAttr -cb on ".rsb";
	setAttr -k on ".ope";
	setAttr -k on ".oppf";
	setAttr -cb on ".hbl" -type "string" "VRayShaders";
	setAttr ".renderPreset" -type "string" "LO";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av ".w" 576;
	setAttr -av ".h" 324;
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al" yes;
	setAttr -av ".dar" 1.7769999504089355;
	setAttr -av -k on ".ldar";
	setAttr -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -k on ".isu";
	setAttr -k on ".pdu";
select -ne :defaultLightSet;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -s 19 ".dsm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr ".ro" yes;
select -ne :defaultObjectSet;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr ".ro" yes;
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -cb on ".hwcc";
	setAttr -cb on ".hwdp";
	setAttr -cb on ".hwql";
	setAttr -k on ".hwfr";
select -ne :defaultHardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av -k on ".rp";
	setAttr -k on ".cai";
	setAttr -k on ".coi";
	setAttr -cb on ".bc";
	setAttr -av -k on ".bcb";
	setAttr -av -k on ".bcg";
	setAttr -av -k on ".bcr";
	setAttr -k on ".ei";
	setAttr -k on ".ex";
	setAttr -av -k on ".es";
	setAttr -av -k on ".ef";
	setAttr -av -k on ".bf";
	setAttr -k on ".fii";
	setAttr -av -k on ".sf";
	setAttr -k on ".gr";
	setAttr -k on ".li";
	setAttr -k on ".ls";
	setAttr -k on ".mb";
	setAttr -k on ".ti";
	setAttr -k on ".txt";
	setAttr -k on ".mpr";
	setAttr -k on ".wzd";
	setAttr ".fn" -type "string" "im";
	setAttr -k on ".if";
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
	setAttr -k on ".as";
	setAttr -k on ".ds";
	setAttr -k on ".lm";
	setAttr -k on ".fir";
	setAttr -k on ".aap";
	setAttr -k on ".gh";
	setAttr -cb on ".sd";
connectAttr "VRay_lightRig_21_rec709:turntable2_rotateY.o" "VRay_lightRig_21_rec709:turntable.ry"
		;
connectAttr "VRay_lightRig_21_rec709:renderCam_translateZ.o" "VRay_lightRig_21_rec709:renderCam.tz"
		;
connectAttr "VRay_lightRig_21_rec709:renderCam_translateY.o" "VRay_lightRig_21_rec709:renderCam.ty"
		;
connectAttr "VRay_lightRig_21_rec709:envLight_visibility.o" "VRay_lightRig_21_rec709:envLight.v"
		;
connectAttr "VRay_lightRig_21_rec709:skyTexture.oc" "VRay_lightRig_21_rec709:envLightShape.dt"
		;
connectAttr "VRay_lightRig_21_rec709:subsurface_light1_visibility.o" "VRay_lightRig_21_rec709:subsurface_light.v"
		;
connectAttr "VRay_lightRig_21_rec709:mainLights1_rotateY.o" "VRay_lightRig_21_rec709:mainLights.ry"
		;
connectAttr "VRay_lightRig_21_rec709:mainLights1_visibility.o" "VRay_lightRig_21_rec709:mainLights.v"
		;
connectAttr "VRay_lightRig_21_rec709:iblDFile.oc" "VRay_lightRig_21_rec709:iblD_keyLightShape.dt"
		;
connectAttr "VRay_lightRig_21_rec709:iblAFile.oc" "VRay_lightRig_21_rec709:iblAShape.dt"
		;
connectAttr "VRay_lightRig_21_rec709:iblBFile.oc" "VRay_lightRig_21_rec709:iblBShape.dt"
		;
connectAttr "VRay_lightRig_21_rec709:iblC_visibility.o" "VRay_lightRig_21_rec709:iblC.v"
		;
connectAttr "VRay_lightRig_21_rec709:iblCFile.oc" "VRay_lightRig_21_rec709:iblCShape.dt"
		;
connectAttr "VRay_lightRig_21_rec709:iblEFile.oc" "VRay_lightRig_21_rec709:iblEShape.dt"
		;
connectAttr "VRay_lightRig_21_rec709:iblFFile.oc" "VRay_lightRig_21_rec709:iblFShape.dt"
		;
connectAttr "VRay_lightRig_21_rec709:iblGFile.oc" "VRay_lightRig_21_rec709:iblGShape.dt"
		;
connectAttr "VRay_lightRig_21_rec709:iblH_visibility.o" "VRay_lightRig_21_rec709:iblH.v"
		;
connectAttr "VRay_lightRig_21_rec709:iblHFile.oc" "VRay_lightRig_21_rec709:iblHShape.dt"
		;
connectAttr "VRay_lightRig_21_rec709:iblIFile.oc" "VRay_lightRig_21_rec709:iblIShape.dt"
		;
connectAttr "VRay_lightRig_21_rec709:iblJFile.oc" "VRay_lightRig_21_rec709:iblJShape.dt"
		;
connectAttr "VRay_lightRig_21_rec709:iblKFile.oc" "VRay_lightRig_21_rec709:iblKShape.dt"
		;
connectAttr "VRay_lightRig_21_rec709:iblLFile.oc" "VRay_lightRig_21_rec709:iblLShape.dt"
		;
connectAttr "VRay_lightRig_21_rec709:beautyFill_visibility.o" "VRay_lightRig_21_rec709:beautyFill.v"
		;
connectAttr "VRay_lightRig_21_rec709:beautyRim_visibility.o" "VRay_lightRig_21_rec709:beautyRim.v"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":defaultObjectSet.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr ":mentalrayGlobals.msg" ":mentalrayItemsList.glb";
connectAttr ":miContourPreset.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":Draft.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":DraftMotionBlur.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":DraftRapidMotion.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":Preview.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":PreviewMotionblur.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":PreviewRapidMotion.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":PreviewCaustics.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":PreviewGlobalIllum.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":PreviewFinalGather.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":Production.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":ProductionMotionblur.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":ProductionRapidMotion.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":ProductionFineTrace.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":ProductionRapidFur.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":ProductionRapidHair.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":PreviewImrRayTracyOff.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":PreviewImrRayTracyOn.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":miDefaultOptions.msg" ":mentalrayItemsList.opt" -na;
connectAttr ":miDefaultFramebuffer.msg" ":mentalrayItemsList.fb" -na;
connectAttr ":miDefaultOptions.msg" ":mentalrayGlobals.opt";
connectAttr ":miDefaultFramebuffer.msg" ":mentalrayGlobals.fb";
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex2.ouv" "VRay_lightRig_21_rec709:skyTexture.uv"
		;
connectAttr "VRay_lightRig_21_rec709:placeSkyTexture.ox" "VRay_lightRig_21_rec709:skyTexture.u"
		;
connectAttr "VRay_lightRig_21_rec709:placeSkyTexture.oy" "VRay_lightRig_21_rec709:skyTexture.v"
		;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex1.ou" "VRay_lightRig_21_rec709:placeSkyTexture.vx"
		;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex1.ov" "VRay_lightRig_21_rec709:placeSkyTexture.vy"
		;
connectAttr "VRay_lightRig_21_rec709:turntable.iog" "VRay_lightRig_21_rec709:deleteSet.dsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:skyTexture.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:placeSkyTexture.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex2.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex1.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr ":initialShadingGroup.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm" 
		-na;
connectAttr ":initialParticleSE.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm" -na
		;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex3.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex4.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex5.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex6.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex7.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:mainLights1_rotateY.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:turntable2_rotateY.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:renderCam_translateY.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:renderCam_translateZ.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:envLight_visibility.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:iblC_visibility.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:mainLights1_visibility.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:subsurface_light1_visibility.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:iblAFile.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:iblBFile.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:iblCFile.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:iblDFile.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:iblEFile.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex10.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex11.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex12.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex13.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex14.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex8.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex9.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:iblH_visibility.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:iblFFile.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:iblGFile.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:iblHFile.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:iblIFile.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:iblJFile.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:iblKFile.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:iblLFile.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture1.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture10.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture11.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture12.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture2.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture3.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture4.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture5.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture6.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture7.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture8.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture9.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:beautyFill_visibility.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:beautyRim_visibility.msg" "VRay_lightRig_21_rec709:deleteSet.dnsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex3.ouv" "VRay_lightRig_21_rec709:iblAFile.uv"
		;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex4.ouv" "VRay_lightRig_21_rec709:iblBFile.uv"
		;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex5.ouv" "VRay_lightRig_21_rec709:iblCFile.uv"
		;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex6.ouv" "VRay_lightRig_21_rec709:iblDFile.uv"
		;
connectAttr "VRay_lightRig_21_rec709:iblRot.o" "VRay_lightRig_21_rec709:VRayPlaceEnvTex6.hr"
		;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex7.ouv" "VRay_lightRig_21_rec709:iblEFile.uv"
		;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex8.ouv" "VRay_lightRig_21_rec709:iblFFile.uv"
		;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex9.ouv" "VRay_lightRig_21_rec709:iblGFile.uv"
		;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex10.ouv" "VRay_lightRig_21_rec709:iblHFile.uv"
		;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex11.ouv" "VRay_lightRig_21_rec709:iblIFile.uv"
		;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex12.ouv" "VRay_lightRig_21_rec709:iblJFile.uv"
		;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex13.ouv" "VRay_lightRig_21_rec709:iblKFile.uv"
		;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex14.ouv" "VRay_lightRig_21_rec709:iblLFile.uv"
		;
connectAttr "VRay_lightRig_21_rec709:skyTexture.msg" ":defaultTextureList1.tx" -na
		;
connectAttr "VRay_lightRig_21_rec709:iblAFile.msg" ":defaultTextureList1.tx" -na
		;
connectAttr "VRay_lightRig_21_rec709:iblBFile.msg" ":defaultTextureList1.tx" -na
		;
connectAttr "VRay_lightRig_21_rec709:iblCFile.msg" ":defaultTextureList1.tx" -na
		;
connectAttr "VRay_lightRig_21_rec709:iblDFile.msg" ":defaultTextureList1.tx" -na
		;
connectAttr "VRay_lightRig_21_rec709:iblEFile.msg" ":defaultTextureList1.tx" -na
		;
connectAttr "VRay_lightRig_21_rec709:iblFFile.msg" ":defaultTextureList1.tx" -na
		;
connectAttr "VRay_lightRig_21_rec709:iblGFile.msg" ":defaultTextureList1.tx" -na
		;
connectAttr "VRay_lightRig_21_rec709:iblHFile.msg" ":defaultTextureList1.tx" -na
		;
connectAttr "VRay_lightRig_21_rec709:iblIFile.msg" ":defaultTextureList1.tx" -na
		;
connectAttr "VRay_lightRig_21_rec709:iblJFile.msg" ":defaultTextureList1.tx" -na
		;
connectAttr "VRay_lightRig_21_rec709:iblKFile.msg" ":defaultTextureList1.tx" -na
		;
connectAttr "VRay_lightRig_21_rec709:iblLFile.msg" ":defaultTextureList1.tx" -na
		;
connectAttr "VRay_lightRig_21_rec709:fill_lightShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:rim_lightShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:key_lightShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:envLightShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:subsurface_lightShape.ltd" ":lightList1.l" 
		-na;
connectAttr "VRay_lightRig_21_rec709:iblAShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:iblBShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:iblCShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:iblD_keyLightShape.ltd" ":lightList1.l" -na
		;
connectAttr "VRay_lightRig_21_rec709:iblEShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:iblFShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:iblGShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:iblHShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:iblIShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:iblJShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:iblKShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:iblLShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:beautyRimShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:beautyFillShape.ltd" ":lightList1.l" -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex1.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:placeSkyTexture.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex2.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture1.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex3.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture2.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex4.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture3.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex5.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture4.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex6.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture5.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex7.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture6.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex8.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture7.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex9.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture8.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex10.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture9.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex11.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture10.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex12.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture11.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex13.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:place2dTexture12.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "VRay_lightRig_21_rec709:VRayPlaceEnvTex14.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr ":perspShape.msg" ":defaultRenderGlobals.sc";
connectAttr "VRay_lightRig_21_rec709:fill_light.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:rim_light.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:key_light.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:envLight.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:subsurface_light.iog" ":defaultLightSet.dsm"
		 -na;
connectAttr "VRay_lightRig_21_rec709:iblA.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:iblB.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:iblC.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:iblD_keyLight.iog" ":defaultLightSet.dsm" -na
		;
connectAttr "VRay_lightRig_21_rec709:iblE.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:iblF.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:iblG.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:iblH.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:iblI.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:iblJ.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:iblK.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:iblL.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:beautyRim.iog" ":defaultLightSet.dsm" -na;
connectAttr "VRay_lightRig_21_rec709:beautyFill.iog" ":defaultLightSet.dsm" -na;
// End of import_VRay_lightRig_22_rec709.ma
