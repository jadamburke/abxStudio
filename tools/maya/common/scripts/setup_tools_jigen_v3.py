#    RIG AND SETUP AUTO By Guillaume BRUNET - JIGEN
#
#    Author : Guillaume BRUNET
#    Date : 12-2013
#    Version : 3.0
#
#    How to :
#
#    Copy this script in a shelf button
#    and copy the folder "GB_SETUP" in :
#    Win : {Drive}:\Documents and Settings\{username}\My Documents\maya\{version}\prefs\icons
#    Mac : /Users/{username}/Library/Preferences/Autodesk/maya/{version}/prefs/icons
#    Linux : ~{username}/maya/{version}/prefs/icons
#
#    OR
#
#    Copy "shelf_GB_Plugins.mel" in :
#    Win : {Drive}:\Documents and Settings\{username}\My Documents\maya\{version}\prefs\shelves
#    Mac : /Users/{username}/Library/Preferences/Autodesk/maya/{version}/prefs/shelves
#    Linux : ~{username}/maya/{version}/prefs/shelves
#    and copy the folder "GB_SETUP" in :
#    Win : {Drive}:\Documents and Settings\{username}\My Documents\maya\{version}\prefs\icons
#    Mac : /Users/{username}/Library/Preferences/Autodesk/maya/{version}/prefs/icons
#    Linux : ~{username}/maya/{version}/prefs/icons


# import des commandes maya
import maya.cmds as cmds
from maya.OpenMaya import MVector
import math
import maya.mel as mel

# suppresion de la fenetre SetupByGui si elle existe
if (cmds.window("SetupByGui", ex=True)):
    cmds.deleteUI("SetupByGui")

# creation de la fenetre SetupByGui
cmds.window("SetupByGui", t="SETUP TOOLS - Guillaume BRUNET - JIGEN", w=413, h=800, s=False)

cmds.columnLayout("Principal")
cmds.rowLayout(nc=2)
cmds.separator(w=100, st="none")
cmds.separator(h=25, w=213, st="in")
cmds.setParent("..")

cmds.text(fn="boldLabelFont", w=413, l="  SETUP TOOLS - JIGEN")

cmds.rowLayout(nc=2)
cmds.separator(w=100, st="none")
cmds.separator(h=25, w=213, st="in")
cmds.setParent("..")

cmds.rowLayout(nc=5)
cmds.separator(w=43, st="none")
cmds.text(al="left", w=57, l="Character :")
cmds.textField("addPersoName", w=208, ec="win.addPersoVerif()", aie=True)
cmds.separator(w=3, st="none")
cmds.button(l="Add",w=57, c="win.addPersoVerif()")
cmds.setParent("..")

cmds.rowLayout(nc=2)
cmds.separator(w=103, st="none")
cmds.textScrollList("persoListe", h=72, w=207, sc="win.persoSelected()")
cmds.setParent("..")

cmds.separator(h=5, st="none")

cmds.rowLayout(nc=2)
cmds.separator(w=103, st="none")
cmds.button("delPerso", l="Delete", w=207, c="persoSel.supprPerso()", en=False)
cmds.setParent("..")

cmds.separator(h=9)

cmds.tabLayout("AutoRig", h=623, w=413)

cmds.columnLayout("AutoRig")

cmds.separator(h=9)
cmds.rowLayout(nc=5)
cmds.separator(w=93, st="none")
cmds.text(w=50, al="left", l="Spine :")
cmds.radioCollection("spineRadioCollection")
cmds.radioButton("FKSpine", w=60, l="FK", en=False, cc="persoSel.changeSpine()")
cmds.radioButton("IKSpine", w=60, sl=True, en=False, l="IK", cc="persoSel.changeSpine()")
cmds.radioButton("RibbonSpine", l="Ribbon", en=False, cc="persoSel.changeSpine()")
cmds.setParent("..")

cmds.rowLayout(nc=2)
cmds.separator(w=100, st="none")
cmds.separator(h=25, w=213, st="in")
cmds.setParent("..")

cmds.rowLayout(nc=3)
cmds.separator(w=47, st="none")
cmds.button("posJointsBtn", w=150, c="persoSel.posJoints()", en=False, l="Joints positioning")
cmds.button("creaJointsBtn", w=150, c="persoSel.creaJoints()", en=False, l="Create joints")
cmds.setParent("..")

cmds.rowLayout(nc=2)
cmds.separator(w=100, st="none")
cmds.separator(h=25, w=213, st="in")
cmds.setParent("..")

cmds.rowLayout(nc=3)
cmds.separator(w=47, st="none")
cmds.button(w=150, c="LRA(True)", l="Show LRA")
cmds.button(w=150, c="LRA(False)", l="Hide LRA")
cmds.setParent("..")

cmds.separator(h=15, st="none")
cmds.rowLayout(nc=2)
cmds.separator(w=103, st="none")
cmds.button(w=199, c="OJ()", l="Align  LRA")
cmds.setParent("..")

cmds.separator(h=15, st="none")
cmds.rowLayout(nc=2)
cmds.separator(w=120, st="none")
cmds.checkBox("hierarchyLRA", onc="win.hiLRA(True)", ofc="win.hiLRA(False)", l="Influence children chain joints")
cmds.setParent("..")
                
cmds.separator(h=15, st="none")
cmds.rowLayout(nc=2)
cmds.separator(w=103, st="none")
cmds.button(w=199, c="JOX(90)", l="Rotate LRA (90)")
cmds.setParent("..")

cmds.separator(h=15, st="none")
cmds.rowLayout(nc=3)
cmds.separator(w=47, st="none")
cmds.button(w=150, c="JOX(0)", l="Rotate LRA (degrees) :")
cmds.floatField("R_JOXvaleur", min=-180, max=180, v=45, w=150, h=25, pre=2)
cmds.setParent("..")

cmds.rowLayout(nc=2)
cmds.separator(w=100, st="none")
cmds.separator(h=25, w=213, st="in")
cmds.setParent("..")

cmds.rowLayout(nc=5)
cmds.separator(w=45, st="none")
cmds.text(w=60, al="right", l="Leg :          ")
cmds.checkBox("FKLeg", cc="persoSel.changeLeg('FK')", en=False, w=90, l=" FK")
cmds.checkBox("IKLeg", cc="persoSel.changeLeg('IK')", en=False, w=90, v=True, l=" IK")
cmds.checkBox("RibbonLeg", cc="persoSel.changeLeg('Ribbon')", en=False, w=90, l=" Ribbon")
cmds.setParent("..")

cmds.separator(h=15, st="none")
cmds.rowLayout(nc=5)
cmds.separator(w=45, st="none")
cmds.text(w=60, al="right", l="Arm :          ")
cmds.checkBox("FKArm", cc="persoSel.changeArm('FK')", en=False, v=True, w=90, l=" FK")
cmds.checkBox("IKArm", cc="persoSel.changeArm('IK')", en=False, w=90, l=" IK")
cmds.checkBox("RibbonArm",cc="persoSel.changeArm('Ribbon')", en=False, w=90, l=" Ribbon")
cmds.setParent("..")

cmds.separator(h=15, st="none")
cmds.rowLayout(nc=5)
cmds.separator(w=43, st="none")
cmds.text(w=62, al="left", l="Hand :")
cmds.checkBox("CTRLHand", cc="persoSel.changeHand('ctrl')", en=False, v=True, w=90, l=" Hand Ctrl")
cmds.checkBox("FKHand", cc="persoSel.changeHand('FK')", en=False, w=90, l=" Fingers FK")
cmds.checkBox("ULTIMHand", cc="persoSel.changeHand('ultim')", en=False, w=90, l=" Ultimate")
cmds.setParent("..")

cmds.separator(h=15, st="none")
cmds.rowLayout(nc=4)
cmds.separator(w=120, st="none")
cmds.text(w=70, al="right", l="Head :          ")
cmds.radioCollection("headRadioCollection")
cmds.radioButton("FKHead", w=60, sl=True, l="FK", en=False, cc="persoSel.changeHead()")
cmds.radioButton("IKHead", l="IK", en=False, cc="persoSel.changeHead()")
cmds.setParent("..")

cmds.separator(h=10, st="none")
cmds.rowLayout(nc=2)
cmds.separator(w=103, st="none")
cmds.button("autoRigBtn", w=199, c="persoSel.autoRig()", en=False, l="AutoRig")
cmds.setParent("..")

cmds.rowLayout(nc=2)
cmds.separator(w=100, st="none")
cmds.separator(h=25, w=213, st="in")
cmds.setParent("..")

cmds.rowLayout(nc=2)
cmds.separator(w=50, st="none")
cmds.text(w=313, al="center", l="Select first your GEO, then, click on \"Bind Skin\".\n(\"Bind to :\" must be on \"Selected joints\")")
cmds.setParent("..")

cmds.separator(h=15, st="none")
cmds.rowLayout(nc=2)
cmds.separator(w=103, st="none")
cmds.button("bindSkinBtn", w=199, c="persoSel.bindSkin()", en=False, l="Bind Skin")
cmds.setParent("..")

cmds.setParent("..")

cmds.formLayout("Selection")

cmds.iconTextButton("bg", st="iconOnly", i1="GB_SETUP/BG.png", en=False)

cmds.iconTextButton("L_W", c="sel.select(\"L_W\")", st="iconOnly", i1="GB_SETUP/btn.png", l="L_Wrist")
cmds.iconTextButton("R_W", c="sel.select(\"R_W\")", st="iconOnly", i1="GB_SETUP/btn.png", l="R_Wrist")
cmds.iconTextButton("L_E", c="sel.select(\"L_E\")", st="iconOnly", i1="GB_SETUP/btn.png", l="L_Elbow")
cmds.iconTextButton("R_E", c="sel.select(\"R_E\")", st="iconOnly", i1="GB_SETUP/btn.png", l="R_Elbow")
cmds.iconTextButton("L_S", c="sel.select(\"L_S\")", st="iconOnly", i1="GB_SETUP/btn.png", l="L_Shoulder")
cmds.iconTextButton("R_S", c="sel.select(\"R_S\")", st="iconOnly", i1="GB_SETUP/btn.png", l="R_Shoulder")
cmds.iconTextButton("L_C", c="sel.select(\"L_C\")", st="iconOnly", i1="GB_SETUP/btn.png", l="L_Clavicle")
cmds.iconTextButton("R_C", c="sel.select(\"R_C\")", st="iconOnly", i1="GB_SETUP/btn.png", l="R_Clavicle")
cmds.iconTextButton("C_N", c="sel.select(\"C_N\")", st="iconOnly", i1="GB_SETUP/btn.png", l="C_Neck")
cmds.iconTextButton("C_C", c="sel.select(\"C_C\")", st="iconOnly", i1="GB_SETUP/btn.png", l="C_Chest")
cmds.iconTextButton("C_MS", c="sel.select(\"C_MS\")", st="iconOnly", i1="GB_SETUP/btn.png", l="C_MidSpine")
cmds.iconTextButton("C_LS", c="sel.select(\"C_LS\")", st="iconOnly", i1="GB_SETUP/btn.png", l="C_LowSpine")
cmds.iconTextButton("C_P", c="sel.select(\"C_P\")", st="iconOnly", i1="GB_SETUP/btn.png", l="C_Pelvis")
cmds.iconTextButton("L_L", c="sel.select(\"L_L\")", st="iconOnly", i1="GB_SETUP/btn.png", l="L_Leg")
cmds.iconTextButton("R_L", c="sel.select(\"R_L\")", st="iconOnly", i1="GB_SETUP/btn.png", l="R_Leg")
cmds.iconTextButton("L_K", c="sel.select(\"L_K\")", st="iconOnly", i1="GB_SETUP/btn.png", l="L_Knee")
cmds.iconTextButton("R_K", c="sel.select(\"R_K\")", st="iconOnly", i1="GB_SETUP/btn.png", l="R_Knee")
cmds.iconTextButton("L_A", c="sel.select(\"L_A\")", st="iconOnly", i1="GB_SETUP/btn.png", l="L_Ankle")
cmds.iconTextButton("R_A", c="sel.select(\"R_A\")", st="iconOnly", i1="GB_SETUP/btn.png", l="R_Ankle")
cmds.iconTextButton("L_B", c="sel.select(\"L_B\")", st="iconOnly", i1="GB_SETUP/btn.png", l="L_Ball")
cmds.iconTextButton("R_B", c="sel.select(\"R_B\")", st="iconOnly", i1="GB_SETUP/btn.png", l="R_Ball")
cmds.iconTextButton("C_H", c="sel.select(\"C_H\")", st="iconOnly", i1="GB_SETUP/btn.png", l="C_Head")

cmds.text("L_A_T", w=80, l="L Arm")
cmds.button("L_A_IK", c="sel.snapArmIK(\"L\")", l="Snap IK to FK", w=80)
cmds.button("L_A_FK", c="sel.snapArmFK(\"L\")", l="Snap FK to IK", w=80)
cmds.button("S_L_A", c="sel.switchArm(\"L\")", l="Switch", w=80)
cmds.text("R_A_T", w=80, l="R Arm")
cmds.button("R_A_IK", c="sel.snapArmIK(\"R\")", l="Snap IK to FK", w=80)
cmds.button("R_A_FK", c="sel.snapArmFK(\"R\")", l="Snap FK to IK", w=80)
cmds.button("S_R_A", c="sel.switchArm(\"R\")", l="Switch", w=80)
cmds.text("L_L_T", w=80, l="L Leg")
cmds.button("L_L_IK", c="sel.snapLegIK(\"L\")", l="Snap IK to FK", w=80)
cmds.button("L_L_FK", c="sel.snapLegFK(\"L\")", l="Snap FK to IK", w=80)
cmds.button("S_L_L", c="sel.switchLeg(\"L\")", l="Switch", w=80)
cmds.text("R_L_T", w=80, l="R Leg")
cmds.button("R_L_IK", c="sel.snapLegIK(\"R\")", l="Snap IK to FK", w=80)
cmds.button("R_L_FK", c="sel.snapLegFK(\"R\")", l="Snap FK to IK", w=80)
cmds.button("S_R_L", c="sel.switchLeg(\"R\")", l="Switch", w=80)
cmds.button("RaZ_A", c="sel.RaZ(\"A\")", l="RaZ All", w=80)
cmds.button("RaZ_S", c="sel.RaZ(\"S\")", l="RaZ Selected", w=80)

cmds.setParent("..")

cmds.setParent("..")

cmds.setParent("..")

cmds.formLayout("Selection", e=True, af=[("L_W", "top", 265), ("L_W", "left", 357)])
cmds.formLayout("Selection", e=True, af=[("R_W", "top", 265), ("R_W", "left", 19)])
cmds.formLayout("Selection", e=True, af=[("L_E", "top", 190), ("L_E", "left", 312)])
cmds.formLayout("Selection", e=True, af=[("R_E", "top", 190), ("R_E", "left", 67)])
cmds.formLayout("Selection", e=True, af=[("L_S", "top", 110), ("L_S", "left", 260)])
cmds.formLayout("Selection", e=True, af=[("R_S", "top", 110), ("R_S", "left", 120)])
cmds.formLayout("Selection", e=True, af=[("L_C", "top", 115), ("L_C", "left", 210)])
cmds.formLayout("Selection", e=True, af=[("R_C", "top", 115), ("R_C", "left", 170)])
cmds.formLayout("Selection", e=True, af=[("C_N", "top", 90), ("C_N", "left", 190)])
cmds.formLayout("Selection", e=True, af=[("C_C", "top", 130), ("C_C", "left", 190)])
cmds.formLayout("Selection", e=True, af=[("C_MS", "top", 180), ("C_MS", "left", 190)])
cmds.formLayout("Selection", e=True, af=[("C_LS", "top", 245), ("C_LS", "left", 190)])
cmds.formLayout("Selection", e=True, af=[("C_P", "top", 285), ("C_P", "left", 190)])
cmds.formLayout("Selection", e=True, af=[("L_L", "top", 270), ("L_L", "left", 225)])
cmds.formLayout("Selection", e=True, af=[("R_L", "top", 270), ("R_L", "left", 155)])
cmds.formLayout("Selection", e=True, af=[("L_K", "top", 415), ("L_K", "left", 210)])
cmds.formLayout("Selection", e=True, af=[("R_K", "top", 415), ("R_K", "left", 170)])
cmds.formLayout("Selection", e=True, af=[("L_A", "top", 555), ("L_A", "left", 205)])
cmds.formLayout("Selection", e=True, af=[("R_A", "top", 555), ("R_A", "left", 175)])
cmds.formLayout("Selection", e=True, af=[("L_B", "top", 570), ("L_B", "left", 215)])
cmds.formLayout("Selection", e=True, af=[("R_B", "top", 570), ("R_B", "left", 165)])
cmds.formLayout("Selection", e=True, af=[("C_H", "top", 0), ("C_H", "left", 190)])
cmds.formLayout("Selection", e=True, af=[("L_A_T", "top", 5), ("L_A_T", "right", 5)])
cmds.formLayout("Selection", e=True, af=[("L_A_IK", "top", 22), ("L_A_IK", "right", 5)])
cmds.formLayout("Selection", e=True, af=[("L_A_FK", "top", 49), ("L_A_FK", "right", 5)])
cmds.formLayout("Selection", e=True, af=[("S_L_A", "top", 76), ("S_L_A", "right", 5)])
cmds.formLayout("Selection", e=True, af=[("R_A_T", "top", 5), ("R_A_T", "left", 5)])
cmds.formLayout("Selection", e=True, af=[("R_A_IK", "top", 22), ("R_A_IK", "left", 5)])
cmds.formLayout("Selection", e=True, af=[("R_A_FK", "top", 49), ("R_A_FK", "left", 5)])
cmds.formLayout("Selection", e=True, af=[("S_R_A", "top", 76), ("S_R_A", "left", 5)])
cmds.formLayout("Selection", e=True, af=[("L_L_T", "bottom", 86), ("L_L_T", "right", 5)])
cmds.formLayout("Selection", e=True, af=[("L_L_IK", "bottom", 59), ("L_L_IK", "right", 5)])
cmds.formLayout("Selection", e=True, af=[("L_L_FK", "bottom", 32), ("L_L_FK", "right", 5)])
cmds.formLayout("Selection", e=True, af=[("S_L_L", "bottom", 5), ("S_L_L", "right", 5)])
cmds.formLayout("Selection", e=True, af=[("R_L_T", "bottom", 86), ("R_L_T", "left", 5)])
cmds.formLayout("Selection", e=True, af=[("R_L_IK", "bottom", 59), ("R_L_IK", "left", 5)])
cmds.formLayout("Selection", e=True, af=[("R_L_FK", "bottom", 32), ("R_L_FK", "left", 5)])
cmds.formLayout("Selection", e=True, af=[("S_R_L", "bottom", 5), ("S_R_L", "left", 5)])
cmds.formLayout("Selection", e=True, af=[("RaZ_A", "bottom", 200), ("RaZ_A", "left", 35)])
cmds.formLayout("Selection", e=True, af=[("RaZ_S", "bottom", 200), ("RaZ_S", "right", 35)])

cmds.formLayout("Selection", e=True, af=[("bg", "top", 0), ("bg", "left", 0), ("bg", "bottom", 0), ("bg", "right", 0)])
 
cmds.showWindow("SetupByGui")

# scriptJob
jobSelExist = False
jobUndoRedoExist = False
jobs = cmds.scriptJob(lj=True)
for job in jobs:
    if job.find("changeSelec()") != -1:
        jobSelExist = True
    if job.find("majPerso(True)") != -1:
        jobUndoRedoExist = True

if not jobSelExist:
    cmds.scriptJob(e=["SelectionChanged","changeSelec()"], per=True)
if not jobUndoRedoExist:
    cmds.scriptJob(e=["Undo", "majPerso(True)"], per=True)
    cmds.scriptJob(e=["Redo", "majPerso(True)"], per=True)

persoSel = ""
undoAction = False

# def majPerso
def majPerso(UndoV):
    #variable
    global persoSel
    global undoAction
    if persoSel != "":
        undoAction = UndoV
        ctrlsPerso = ["%s_C_Ultimate_ctrl"%persoSel.nom, "%s_L_ElbowIK_ctrl"%persoSel.nom, "%s_R_ElbowIK_ctrl"%persoSel.nom, "%s_L_ArmIK_ctrl"%persoSel.nom, "%s_R_ArmIK_ctrl"%persoSel.nom, "%s_L_ShoulderFK_ctrl"%persoSel.nom, "%s_R_ShoulderFK_ctrl"%persoSel.nom, "%s_L_ElbowFK_ctrl"%persoSel.nom, "%s_R_ElbowFK_ctrl"%persoSel.nom, "%s_L_WristFK_ctrl"%persoSel.nom, "%s_R_WristFK_ctrl"%persoSel.nom, "%s_L_KneeIK_ctrl"%persoSel.nom, "%s_R_KneeIK_ctrl"%persoSel.nom, "%s_L_Foot_ctrl"%persoSel.nom, "%s_R_Foot_ctrl"%persoSel.nom, "%s_C_COG_ctrl"%persoSel.nom, "%s_C_SpineMidFK_ctrl"%persoSel.nom, "%s_C_SpineUpFK_ctrl"%persoSel.nom, "%s_C_Pelvis_ctrl"%persoSel.nom, "%s_L_LegFK_ctrl"%persoSel.nom, "%s_L_KneeFK_ctrl"%persoSel.nom, "%s_L_AnkleFK_ctrl"%persoSel.nom, "%s_L_BallFK_ctrl"%persoSel.nom, "%s_R_LegFK_ctrl"%persoSel.nom, "%s_R_KneeFK_ctrl"%persoSel.nom, "%s_R_AnkleFK_ctrl"%persoSel.nom, "%s_R_BallFK_ctrl"%persoSel.nom, "%s_C_Neck_ctrl"%persoSel.nom, "%s_C_Head_ctrl"%persoSel.nom, "%s_C_Eyes_ctrl"%persoSel.nom, "%s_L_Eye_ctrl"%persoSel.nom, "%s_R_Eye_ctrl"%persoSel.nom, "%s_C_Neck_ctrl_constraint"%persoSel.nom, "%s_L_Hand_ctrl"%persoSel.nom, "%s_R_Hand_ctrl"%persoSel.nom, "%s_L_LegSwitch_ctrl"%persoSel.nom, "%s_R_LegSwitch_ctrl"%persoSel.nom, "%s_L_Ultim_Hand_ctrl"%persoSel.nom, "%s_R_Ultim_Hand_ctrl"%persoSel.nom, "%s_L_Thumb01_FK_ctrl"%persoSel.nom, "%s_L_Thumb02_FK_ctrl"%persoSel.nom, "%s_L_Thumb03_FK_ctrl"%persoSel.nom, "%s_L_Index01_FK_ctrl"%persoSel.nom, "%s_L_Index02_FK_ctrl"%persoSel.nom, "%s_L_Index03_FK_ctrl"%persoSel.nom, "%s_L_Middle01_FK_ctrl"%persoSel.nom, "%s_L_Middle02_FK_ctrl"%persoSel.nom, "%s_L_Middle03_FK_ctrl"%persoSel.nom, "%s_L_Ring01_FK_ctrl"%persoSel.nom, "%s_L_Ring02_FK_ctrl"%persoSel.nom, "%s_L_Ring03_FK_ctrl"%persoSel.nom, "%s_L_Pinky01_FK_ctrl"%persoSel.nom, "%s_L_Pinky02_FK_ctrl"%persoSel.nom, "%s_L_Pinky03_FK_ctrl"%persoSel.nom, "%s_R_Thumb01_FK_ctrl"%persoSel.nom, "%s_R_Thumb02_FK_ctrl"%persoSel.nom, "%s_R_Thumb03_FK_ctrl"%persoSel.nom, "%s_R_Index01_FK_ctrl"%persoSel.nom, "%s_R_Index02_FK_ctrl"%persoSel.nom, "%s_R_Index03_FK_ctrl"%persoSel.nom, "%s_R_Middle01_FK_ctrl"%persoSel.nom, "%s_R_Middle02_FK_ctrl"%persoSel.nom, "%s_R_Middle03_FK_ctrl"%persoSel.nom, "%s_R_Ring01_FK_ctrl"%persoSel.nom, "%s_R_Ring02_FK_ctrl"%persoSel.nom, "%s_R_Ring03_FK_ctrl"%persoSel.nom, "%s_R_Pinky01_FK_ctrl"%persoSel.nom, "%s_R_Pinky02_FK_ctrl"%persoSel.nom, "%s_R_Pinky03_FK_ctrl"%persoSel.nom]
        ctrls = 0
        ctrlOK = True
        tempoJntsPerso = ["%s_C_Root_jnt"%persoSel.nom, "%s_C_Spine01_jnt"%persoSel.nom, "%s_C_Spine02_jnt"%persoSel.nom, "%s_C_Spine03_jnt"%persoSel.nom, "%s_C_Spine04_jnt"%persoSel.nom, "%s_C_Spine05_jnt"%persoSel.nom, "%s_C_Spine06_jnt"%persoSel.nom, "%s_C_Spine07_jnt"%persoSel.nom, "%s_C_Spine08_jnt"%persoSel.nom, "%s_C_Pelvis_jnt"%persoSel.nom, "%s_L_Clavicle_jnt"%persoSel.nom, "%s_L_Shoulder_jnt"%persoSel.nom, "%s_L_Elbow_jnt"%persoSel.nom, "%s_L_ForeArm_jnt"%persoSel.nom, "%s_L_Wrist_jnt"%persoSel.nom, "%s_R_Clavicle_jnt"%persoSel.nom, "%s_R_Shoulder_jnt"%persoSel.nom, "%s_R_Elbow_jnt"%persoSel.nom, "%s_R_ForeArm_jnt"%persoSel.nom, "%s_R_Wrist_jnt"%persoSel.nom, "%s_L_Leg_jnt"%persoSel.nom, "%s_L_Knee_jnt"%persoSel.nom, "%s_L_Ankle_jnt"%persoSel.nom, "%s_L_Ball_jnt"%persoSel.nom, "%s_L_Toe_jnt"%persoSel.nom, "%s_R_Leg_jnt"%persoSel.nom, "%s_R_Knee_jnt"%persoSel.nom, "%s_R_Ankle_jnt"%persoSel.nom, "%s_R_Ball_jnt"%persoSel.nom, "%s_R_Toe_jnt"%persoSel.nom, "%s_L_Thumb01_jnt"%persoSel.nom, "%s_L_Thumb02_jnt"%persoSel.nom, "%s_L_Thumb03_jnt"%persoSel.nom, "%s_L_Thumb04_jnt"%persoSel.nom, "%s_L_Index01_jnt"%persoSel.nom, "%s_L_Index02_jnt"%persoSel.nom, "%s_L_Index03_jnt"%persoSel.nom, "%s_L_Index04_jnt"%persoSel.nom, "%s_L_Middle01_jnt"%persoSel.nom, "%s_L_Middle02_jnt"%persoSel.nom, "%s_L_Middle03_jnt"%persoSel.nom, "%s_L_Middle04_jnt"%persoSel.nom, "%s_L_Ring01_jnt"%persoSel.nom, "%s_L_Ring02_jnt"%persoSel.nom, "%s_L_Ring03_jnt"%persoSel.nom, "%s_L_Ring04_jnt"%persoSel.nom, "%s_L_Pinky01_jnt"%persoSel.nom, "%s_L_Pinky02_jnt"%persoSel.nom, "%s_L_Pinky03_jnt"%persoSel.nom, "%s_L_Pinky04_jnt"%persoSel.nom, "%s_R_Thumb01_jnt"%persoSel.nom, "%s_R_Thumb02_jnt"%persoSel.nom, "%s_R_Thumb03_jnt"%persoSel.nom, "%s_R_Thumb04_jnt"%persoSel.nom, "%s_R_Index01_jnt"%persoSel.nom, "%s_R_Index02_jnt"%persoSel.nom, "%s_R_Index03_jnt"%persoSel.nom, "%s_R_Index04_jnt"%persoSel.nom, "%s_R_Middle01_jnt"%persoSel.nom, "%s_R_Middle02_jnt"%persoSel.nom, "%s_R_Middle03_jnt"%persoSel.nom, "%s_R_Middle04_jnt"%persoSel.nom, "%s_R_Ring01_jnt"%persoSel.nom, "%s_R_Ring02_jnt"%persoSel.nom, "%s_R_Ring03_jnt"%persoSel.nom, "%s_R_Ring04_jnt"%persoSel.nom, "%s_R_Pinky01_jnt"%persoSel.nom, "%s_R_Pinky02_jnt"%persoSel.nom, "%s_R_Pinky03_jnt"%persoSel.nom, "%s_R_Pinky04_jnt"%persoSel.nom, "%s_C_Neck_jnt"%persoSel.nom, "%s_C_Head_jnt"%persoSel.nom, "%s_C_HeadEnd_jnt"%persoSel.nom, "%s_C_Jaw_jnt"%persoSel.nom, "%s_C_JawEnd_jnt"%persoSel.nom, "%s_L_Eye_jnt"%persoSel.nom, "%s_R_Eye_jnt"%persoSel.nom]
        tempoJnts = 0
        tempoJntOK = True
        sphsPerso = ["%s_Scale_ctrl"%persoSel.nom, "%s_C_Pelvis_sph"%persoSel.nom, "%s_C_Root_sph"%persoSel.nom, "%s_C_Spine01_sph"%persoSel.nom, "%s_C_Spine02_sph"%persoSel.nom, "%s_C_Spine03_sph"%persoSel.nom, "%s_C_Spine04_sph"%persoSel.nom, "%s_C_Spine05_sph"%persoSel.nom, "%s_C_Spine06_sph"%persoSel.nom, "%s_C_Spine07_sph"%persoSel.nom, "%s_C_Spine08_sph"%persoSel.nom, "%s_C_Neck_sph"%persoSel.nom, "%s_C_Head_sph"%persoSel.nom, "%s_C_HeadEnd_sph"%persoSel.nom, "%s_C_Jaw_sph"%persoSel.nom, "%s_C_JawEnd_sph"%persoSel.nom, "%s_L_Leg_sph"%persoSel.nom, "%s_R_Leg_sph"%persoSel.nom, "%s_L_Knee_sph"%persoSel.nom, "%s_R_Knee_sph"%persoSel.nom, "%s_L_Ankle_sph"%persoSel.nom, "%s_R_Ankle_sph"%persoSel.nom, "%s_L_Ball_sph"%persoSel.nom, "%s_R_Ball_sph"%persoSel.nom, "%s_L_Toe_sph"%persoSel.nom, "%s_R_Toe_sph"%persoSel.nom, "%s_L_Clavicle_sph"%persoSel.nom, "%s_R_Clavicle_sph"%persoSel.nom, "%s_L_Shoulder_sph"%persoSel.nom, "%s_R_Shoulder_sph"%persoSel.nom, "%s_L_Elbow_sph"%persoSel.nom, "%s_R_Elbow_sph"%persoSel.nom, "%s_L_ForeArm_sph"%persoSel.nom, "%s_R_ForeArm_sph"%persoSel.nom, "%s_L_Wrist_sph"%persoSel.nom, "%s_L_Thumb01_sph"%persoSel.nom, "%s_L_Thumb02_sph"%persoSel.nom, "%s_L_Thumb03_sph"%persoSel.nom, "%s_L_Thumb04_sph"%persoSel.nom, "%s_L_Index01_sph"%persoSel.nom, "%s_L_Index02_sph"%persoSel.nom, "%s_L_Index03_sph"%persoSel.nom, "%s_L_Index04_sph"%persoSel.nom, "%s_L_Middle01_sph"%persoSel.nom, "%s_L_Middle02_sph"%persoSel.nom, "%s_L_Middle03_sph"%persoSel.nom, "%s_L_Middle04_sph"%persoSel.nom, "%s_L_Ring01_sph"%persoSel.nom, "%s_L_Ring02_sph"%persoSel.nom, "%s_L_Ring03_sph"%persoSel.nom, "%s_L_Ring04_sph"%persoSel.nom, "%s_L_Pinky01_sph"%persoSel.nom, "%s_L_Pinky02_sph"%persoSel.nom, "%s_L_Pinky03_sph"%persoSel.nom, "%s_L_Pinky04_sph"%persoSel.nom, "%s_R_Wrist_sph"%persoSel.nom, "%s_R_Thumb01_sph"%persoSel.nom, "%s_R_Thumb02_sph"%persoSel.nom, "%s_R_Thumb03_sph"%persoSel.nom, "%s_R_Thumb04_sph"%persoSel.nom, "%s_R_Index01_sph"%persoSel.nom, "%s_R_Index02_sph"%persoSel.nom, "%s_R_Index03_sph"%persoSel.nom, "%s_R_Index04_sph"%persoSel.nom, "%s_R_Middle01_sph"%persoSel.nom, "%s_R_Middle02_sph"%persoSel.nom, "%s_R_Middle03_sph"%persoSel.nom, "%s_R_Middle04_sph"%persoSel.nom, "%s_R_Ring01_sph"%persoSel.nom, "%s_R_Ring02_sph"%persoSel.nom, "%s_R_Ring03_sph"%persoSel.nom, "%s_R_Ring04_sph"%persoSel.nom, "%s_R_Pinky01_sph"%persoSel.nom, "%s_R_Pinky02_sph"%persoSel.nom, "%s_R_Pinky03_sph"%persoSel.nom, "%s_R_Pinky04_sph"%persoSel.nom, "%s_L_Eye_sph"%persoSel.nom, "%s_R_Eye_sph"%persoSel.nom, "%s_Wrist_ctrl"%persoSel.nom]
        sphs = 0
        sphOK = True
        tempo_head = "Rien"
        tempo_spine = "Rien"
        if persoSel != "":
            for ctrl in ctrlsPerso:
                if cmds.objExists(ctrl):
                    ctrls += 1
            if ctrls < 10:
                ctrlOK = False
            if not ctrlOK:
                for tempoJnt in tempoJntsPerso:
                    if cmds.objExists(tempoJnt):
                        tempoJnts += 1
                if tempoJnts < 10:
                    tempoJntOK = False
            if not tempoJntOK:
                for sph in sphsPerso:
                    if cmds.objExists(sph):
                        sphs += 1
                if sphs < 10:
                    sphOK = False
            # majWin
            if ctrlOK:
                persoSel.jp = True
                persoSel.cj = True
                persoSel.ar = True
            elif tempoJntOK:
                persoSel.jp = True
                persoSel.cj = True
                persoSel.ar = False
            elif sphOK:
                persoSel.jp = True
                persoSel.cj = False
                persoSel.ar = False
            else:
                persoSel.jp = False
                persoSel.cj = False
                persoSel.ar = False
            if cmds.objExists("%s_L_ElbowIK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_ElbowIK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_ArmIK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_ArmIK_ctrl"%persoSel.nom):
                tempo_armIK = True
            else:
                tempo_armIK = False
            if cmds.objExists("%s_L_ShoulderFK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_ShoulderFK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_ElbowFK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_ElbowFK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_WristFK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_WristFK_ctrl"%persoSel.nom):
                tempo_armFK = True
            else:
                tempo_armFK = False
            if cmds.objExists("%s_L_UpperArm_Ribbn01_jnt"%persoSel.nom) and cmds.objExists("%s_L_UpperArm_Ribbn02_jnt"%persoSel.nom) and cmds.objExists("%s_L_UpperArm_Ribbn03_jnt"%persoSel.nom) and cmds.objExists("%s_L_UpperArm_Ribbn04_jnt"%persoSel.nom) and cmds.objExists("%s_L_UpperArm_Ribbn05_jnt"%persoSel.nom) and cmds.objExists("%s_R_LowerArm_Ribbn01_jnt"%persoSel.nom) and cmds.objExists("%s_R_LowerArm_Ribbn02_jnt"%persoSel.nom) and cmds.objExists("%s_R_LowerArm_Ribbn03_jnt"%persoSel.nom) and cmds.objExists("%s_R_LowerArm_Ribbn04_jnt"%persoSel.nom) and cmds.objExists("%s_R_LowerArm_Ribbn05_jnt"%persoSel.nom):
                tempo_armRibbon = True
            else:
                tempo_armRibbon = False
            if tempo_armIK or tempo_armFK or tempo_armRibbon:
                persoSel.armFK = tempo_armFK
                persoSel.armIK = tempo_armIK
                persoSel.armRibbon = tempo_armRibbon
            if cmds.objExists("%s_L_KneeIK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_KneeIK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_Foot_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Foot_ctrl"%persoSel.nom):
                tempo_legIK = True
            else:
                tempo_legIK = False
            if cmds.objExists("%s_L_LegFK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_KneeFK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_AnkleFK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_BallFK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_LegFK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_KneeFK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_AnkleFK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_BallFK_ctrl"%persoSel.nom):
                tempo_legFK = True
            else:
                tempo_legFK = False
            if cmds.objExists("%s_L_UpperLeg_Ribbn01_jnt"%persoSel.nom) and cmds.objExists("%s_L_UpperLeg_Ribbn02_jnt"%persoSel.nom) and cmds.objExists("%s_L_UpperLeg_Ribbn03_jnt"%persoSel.nom) and cmds.objExists("%s_L_UpperLeg_Ribbn04_jnt"%persoSel.nom) and cmds.objExists("%s_L_UpperLeg_Ribbn05_jnt"%persoSel.nom) and cmds.objExists("%s_R_LowerLeg_Ribbn01_jnt"%persoSel.nom) and cmds.objExists("%s_R_LowerLeg_Ribbn02_jnt"%persoSel.nom) and cmds.objExists("%s_R_LowerLeg_Ribbn03_jnt"%persoSel.nom) and cmds.objExists("%s_R_LowerLeg_Ribbn04_jnt"%persoSel.nom) and cmds.objExists("%s_R_LowerLeg_Ribbn05_jnt"%persoSel.nom):
                tempo_legRibbon = True
            else:
                tempo_legRibbon = False
            if tempo_legIK or tempo_legFK or tempo_legRibbon:
                persoSel.legFK = tempo_legFK
                persoSel.legIK = tempo_legIK
                persoSel.legRibbon = tempo_legRibbon
            if cmds.objExists("%s_L_Hand_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Hand_ctrl"%persoSel.nom):
                tempo_handCtrl = True
            else:
                tempo_handCtrl = False
            if cmds.objExists("%s_L_Thumb01_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_Thumb02_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_Thumb03_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_Index01_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_Index02_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_Index03_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_Middle01_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_Middle02_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_Middle03_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_Ring01_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_Ring02_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_Ring03_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_Pinky01_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_Pinky02_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_L_Pinky03_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Thumb01_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Thumb02_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Thumb03_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Index01_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Index02_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Index03_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Middle01_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Middle02_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Middle03_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Ring01_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Ring02_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Ring03_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Pinky01_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Pinky02_FK_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Pinky03_FK_ctrl"%persoSel.nom):
                tempo_handFK = True
            else:
                tempo_handFK = False
            if cmds.objExists("%s_L_Ultim_Hand_ctrl"%persoSel.nom) and cmds.objExists("%s_R_Ultim_Hand_ctrl"%persoSel.nom):
                tempo_handUltimate = True
            else:
                tempo_handUltimate = False
            if tempo_handCtrl or tempo_handFK or tempo_handUltimate:
                persoSel.handCtrl = tempo_handCtrl
                persoSel.handUltimate = tempo_handUltimate
                persoSel.handFK = tempo_handFK
            if cmds.objExists("%s_C_Neck_ctrl"%persoSel.nom):
                tempo_head = "FK"
            elif cmds.objExists("%s_C_Neck_ctrl"%persoSel.nom):
                tempo_head = "IK"
            if tempo_head != "Rien":
                persoSel.head = tempo_head
            if cmds.objExists("%s_C_Spine01_jnt"%persoSel.nom) and cmds.objExists("%s_C_Spine02_jnt"%persoSel.nom) and cmds.objExists("%s_C_Spine03_jnt"%persoSel.nom) and cmds.objExists("%s_C_Spine04_jnt"%persoSel.nom) and cmds.objExists("%s_C_Spine05_jnt"%persoSel.nom) and cmds.objExists("%s_C_Spine06_jnt"%persoSel.nom) and cmds.objExists("%s_C_Spine07_jnt"%persoSel.nom) and cmds.objExists("%s_C_Spine08_jnt"%persoSel.nom):
                tempo_spine = "IK"
            elif cmds.objExists("%s_C_Spine_Ribbn01_jnt"%persoSel.nom) and cmds.objExists("%s_C_Spine_Ribbn02_jnt"%persoSel.nom) and cmds.objExists("%s_C_Spine_Ribbn03_jnt"%persoSel.nom) and cmds.objExists("%s_C_Spine_Ribbn04_jnt"%persoSel.nom) and cmds.objExists("%s_C_Spine_Ribbn05_jnt"%persoSel.nom):
                tempo_spine = "Ribbon"
            elif cmds.objExists("%s_C_Chest_jnt"%persoSel.nom) and cmds.objExists("%s_C_Middle_jnt"%persoSel.nom):
                tempo_spine = "FK"
            if tempo_spine != "Rien":
                persoSel.spine = tempo_spine
            win.majWin()
# end def majPerso

# def changeSelec
def changeSelec():
    # variables    
    global undoAction
    global persoSel
    objs = []
    objs = cmds.ls(sl=True)
    persoExist = False
    if not undoAction:
        if len(objs) == 1:
            obj = objs[0]
            if obj.find("_C_Ultimate_ctrl") != -1:
                nomPerso = obj[:obj.find("_")]
                for i in range(0, len(win.nomPerso)):
                    if win.nomPerso[i] == nomPerso:
                        cmds.textScrollList("persoListe", e=True, sii=(i+1))
                        win.persoSelected()
                        persoExist = True
                if not persoExist:
                    cmds.textField("addPersoName", e=True, tx=nomPerso)
                    win.addPersoVerif()
    else:
        undoAction = False
        while cmds.undoInfo(q=True, un=True).find("changeSelec()") != -1:
            cmds.undo()
        undoAction = False
    # changement btn autoSelect
    if persoSel != "":
        sel = []
        sel = cmds.ls(sl=True)
        ctrls = [("%s_C_Head_ctrl"%persoSel.nom), ("%s_C_SpineUpFK_ctrl"%persoSel.nom), ("%s_C_SpineMidFK_ctrl"%persoSel.nom), ("%s_C_COG_ctrl"%persoSel.nom), ("%s_L_LegFK_ctrl"%persoSel.nom), ("%s_R_LegFK_ctrl"%persoSel.nom), ("%s_L_KneeFK_ctrl"%persoSel.nom), ("%s_R_KneeFK_ctrl"%persoSel.nom), ("%s_L_AnkleFK_ctrl"%persoSel.nom), ("%s_R_AnkleFK_ctrl"%persoSel.nom), ("%s_L_BallFK_ctrl"%persoSel.nom), ("%s_R_BallFK_ctrl"%persoSel.nom), ("%s_L_Foot_ctrl"%persoSel.nom), ("%s_R_Foot_ctrl"%persoSel.nom), ("%s_L_KneeIK_ctrl"%persoSel.nom), ("%s_R_KneeIK_ctrl"%persoSel.nom), ("%s_L_Clavicle_ctrl"%persoSel.nom), ("%s_R_Clavicle_ctrl"%persoSel.nom), ("%s_L_ElbowIK_ctrl"%persoSel.nom), ("%s_R_ElbowIK_ctrl"%persoSel.nom), ("%s_L_ArmIK_ctrl"%persoSel.nom), ("%s_R_ArmIK_ctrl"%persoSel.nom), ("%s_L_ShoulderFK_ctrl"%persoSel.nom), ("%s_R_ShoulderFK_ctrl"%persoSel.nom), ("%s_L_ElbowFK_ctrl"%persoSel.nom), ("%s_R_ElbowFK_ctrl"%persoSel.nom), ("%s_L_WristFK_ctrl"%persoSel.nom), ("%s_R_WristFK_ctrl"%persoSel.nom), ("%s_C_Pelvis_ctrl"%persoSel.nom), ("%s_C_Neck_ctrl"%persoSel.nom), ("%s_C_Chest_ctrl"%persoSel.nom), ("%s_C_Middle_ctrl"%persoSel.nom), ("%s_C_Root_ctrl"%persoSel.nom), ("%s_C_Spine_ctrl"%persoSel.nom)]
        btns = ["C_H", "C_C", "C_MS", "C_LS", "L_L", "R_L", "L_K", "R_K", "L_A", "R_A", "L_B", "R_B", "L_B", "R_B", "L_K", "R_K", "L_C", "R_C", "L_E", "R_E", "L_W", "R_W", "L_S", "R_S","L_E", "R_E", "L_W", "R_W", "C_P", "C_N", "C_C", "C_MS", "C_LS", "C_MS"]
        for i in range(0, len(btns)):
            cmds.iconTextButton(btns[i], e=True, i1="GB_SETUP/btn.png")
        if len(sel) > 0:
            for obj in sel:
                for i in range(0, len(ctrls)):
                    if obj == ctrls[i]:
                        cmds.iconTextButton(btns[i], e=True, i1="GB_SETUP/btnPressed.png")

# end def changeSelec

# def colorize
def colorize(cote, objs):
    for obj in objs:
        if cote == "R":
            cmds.setAttr("%s.overrideEnabled"%obj, 1)
            cmds.setAttr("%s.overrideColor"%obj, 6)
        elif cote == "L":
            cmds.setAttr("%s.overrideEnabled"%obj, 1)
            cmds.setAttr("%s.overrideColor"%obj, 13)
        else:
            cmds.setAttr("%s.overrideEnabled"%obj, 1)
            cmds.setAttr("%s.overrideColor"%obj, 17)
# end def colorize

# def lockAndHide
def lockAndHide(objs, l, h, attrs):
    for obj in objs:
        for attr in attrs:
            if l:
                cmds.setAttr("%s.%s"%(obj, attr), l=True)
            if h:
                cmds.setAttr("%s.%s"%(obj, attr), k=False, cb=False)
#end def lockAndHide

# def lastChild
def lastChild(obj):
    a = cmds.listRelatives(obj, c=True)
    b = ""
    if a != None:
        while isinstance(a, list):
            b = a[0]
            a = cmds.listRelatives(a[0], c=True)
        return b
    else:
        return obj
# end def lastChild

# def topParent
def topParent(obj):
    a = cmds.listRelatives(obj, p=True)
    b = ""
    if a != None:
        while isinstance(a, list):
            b = a[0]
            a = cmds.listRelatives(a[0], p=True)
        return b
    else:
        return obj
# end def topParent

# def LRA
def LRA(on):
    if on:
        on = 1
    else:
        on = 0
    selection = [""]
    selection = cmds.ls(sl=True)
    if len(selection) > 0:
        cmds.select(topParent(selection[0]))
        cmds.select(hi=True)
        selectedObj = cmds.ls(sl=True)
        for obj in selectedObj:
            if obj.find("_jnt") != -1:
                cmds.setAttr(("%s.displayLocalAxis"%obj), on)
        cmds.select(selection)
# end def LRA

# def resym
def resym():
    sel = [""]
    sel = cmds.ls(sl=True)
    if len(sel) > 0:
        infos = sel[0].split("_")
        perso = infos[0]
        cote = infos[1]
        delCote = "R"
        if cote == "R":
            delCote = "L"
        if cote != "C":
            cmds.delete(("%s_%s_Clavicle_jnt"%(perso, delCote)), ("%s_%s_Leg_jnt"%(perso, delCote)), ("%s_%s_Thumb01_jnt"%(perso, delCote)), ("%s_%s_Index01_jnt"%(perso, delCote)), ("%s_%s_Middle01_jnt"%(perso, delCote)), ("%s_%s_Ring01_jnt"%(perso, delCote)), ("%s_%s_Pinky01_jnt"%(perso, delCote)))
            cmds.mirrorJoint(("%s_%s_Clavicle_jnt"%(perso, cote)), myz=True, mb=True, sr=(("_%s_"%cote), ("_%s_"%delCote)))
            cmds.mirrorJoint(("%s_%s_Leg_jnt"%(perso, cote)), myz=True, mb=True, sr=(("_%s_"%cote), ("_%s_"%delCote)))
            cmds.mirrorJoint(("%s_%s_Thumb01_jnt"%(perso, cote)), myz=True, mb=True, sr=(("_%s_"%cote), ("_%s_"%delCote)))
            cmds.mirrorJoint(("%s_%s_Index01_jnt"%(perso, cote)), myz=True, mb=True, sr=(("_%s_"%cote), ("_%s_"%delCote)))
            cmds.mirrorJoint(("%s_%s_Middle01_jnt"%(perso, cote)), myz=True, mb=True, sr=(("_%s_"%cote), ("_%s_"%delCote)))
            cmds.mirrorJoint(("%s_%s_Ring01_jnt"%(perso, cote)), myz=True, mb=True, sr=(("_%s_"%cote), ("_%s_"%delCote)))
            cmds.mirrorJoint(("%s_%s_Pinky01_jnt"%(perso, cote)), myz=True, mb=True, sr=(("_%s_"%cote), ("_%s_"%delCote)))
        cmds.select(sel[0])
# end def resym

# def RA0
def RA0():
    selectedObj = [""]
    selectedObj = cmds.ls(sl=True)
    if len(selectedObj) > 0:
        if win.hiLRAon:
            cmds.select(hi=True)
            selObj = [""]
            selObj = cmds.ls(sl=True)
            parent = [""]
            parent = cmds.listRelatives(selObj[0], p=True)
            cmds.parent(w=True)
            if len(selObj) > 1:
                for i in range(1, len(selObj)):
                    cmds.setAttr(("%s.rotateAxis"%selObj[i-1]), 0, 0, 0, type="double3")
                    cmds.parent(selObj[i], selObj[i-1])
                cmds.setAttr(("%s.rotateAxis"%selObj[i]), 0, 0, 0, type="double3")
            else:
                cmds.setAttr(("%s.rotateAxis"%selObj[0]), 0, 0, 0, type="double3")
            if len(parent) > 0:
                cmds.parent(selObj[0], parent[0])
        else:
            selObj = cmds.ls(sl=True)
            parent = [""]
            parent = cmds.listRelatives(selObj[0], p=True)
            enfant = [""]
            enfant = cmds.listRelatives(selObj[0], c=True)
            cmds.parent(selObj[0], w=True)
            if len(enfant) > 0:
                cmds.parent(enfant[0], w=True)
            cmds.setAttr(("%s.rotateAxis"%selObj[0]), 0, 0, 0, type="double3")
            if len(parent) > 0:
                cmds.parent(selObj[0], parent[0])
            if len(enfant) > 0:
                cmds.parent(enfant[0], selObj[0])
        cmds.select(selectedObj[0])
        resym()
# end def RA0

# def JOX
def JOX(rotate):
    if rotate == 0:
        rot = cmds.floatField("R_JOXvaleur", q=True, v=True)
    else:
        rot = rotate
    selectedObj = [""]
    selectedObj = cmds.ls(sl=True)
    if len(selectedObj) > 0:
        if win.hiLRAon:
            cmds.select(hi=True)
        selObj = cmds.ls(sl=True)
        for obj in selObj:
            newJO = cmds.getAttr("%s.jointOrientX"%obj) - float(rot)
            cmds.setAttr(("%s.jointOrientX"%obj), newJO)
            newRA = cmds.getAttr("%s.rotateAxisX"%obj) + float(rot)
            cmds.setAttr(("%s.rotateAxisX"%obj), newRA)
        parent = selObj[0]
        newJO = cmds.getAttr("%s.jointOrientX"%parent) % 360
        sansVirgule = int(cmds.getAttr("%s.jointOrientX"%parent))
        virgule = cmds.getAttr("%s.jointOrientX"%parent) - sansVirgule
        cmds.setAttr(("%s.jointOrientX"%parent), newJO + virgule)
        cmds.select(selectedObj[0])
        RA0()
# end def JOX

# def OJ
def OJ():
    sel = [""]
    sel = cmds.ls(sl=True)
    if len(sel) > 0:
        cmds.select(topParent(sel[0]), hi=True)
        selectedObj = cmds.ls(sl=True)
        cmds.parent(w=True)
        for obj in selectedObj:
            cmds.setAttr(("%s.rotate"%obj), 0, 0, 0, type="double3")
        for i in range(1, len(selectedObj)):
            cmds.parent(selectedObj[i], selectedObj[i-1])
            cmds.joint(selectedObj[i-1], e=True, zso=True, oj="xyz", sao="xdown")
        cmds.setAttr(("%s.jointOrient"%(lastChild(selectedObj[0]))), 0, 0, 0, type="double3")
        for i in range((len(selectedObj)-1), 1, -1):
            tJO = cmds.getAttr("%s.jointOrientX"%selectedObj[i-1])
            for j in range((i-1), len(selectedObj)):
                newJO = cmds.getAttr("%s.jointOrientX"%selectedObj[j]) - float(tJO)
                cmds.setAttr(("%s.jointOrientX"%selectedObj[j]), newJO)
                newRA = cmds.getAttr("%s.rotateAxisX"%selectedObj[j]) + float(tJO)
                cmds.setAttr(("%s.rotateAxisX"%selectedObj[j]), newRA)
        cmds.select(selectedObj[0], hi=True)
        cmds.parent(w=True)
        for i in range(1, len(selectedObj)):
            cmds.setAttr(("%s.rotateAxis"%selectedObj[i-1]), 0, 0, 0, type="double3")
            cmds.parent((selectedObj[i]), (selectedObj[i-1]))
        cmds.setAttr(("%s.rotate"%selectedObj[i]), 0, 0, 0, type="double3")
        cmds.select(sel[0])
        resym()
# end def OJ

# class autoRig
class autoRig:
    # def legIK
    def legIK(self, perso, cotes):
        for cote in cotes:
            # variables
            leg = "%s_%s_Leg"%(perso, cote)
            knee = "%s_%s_Knee"%(perso, cote)
            ankle = "%s_%s_Ankle"%(perso, cote)
            ball = "%s_%s_Ball"%(perso, cote)
            toe = "%s_%s_Toe"%(perso, cote)
            legJnts = [leg, knee, ankle, ball, toe]
            cmds.duplicate(("%s_jnt"%leg), n=("%sIK_jnt"%leg))
            for i in range(0,4):
                child = cmds.listRelatives(("%sIK_jnt"%legJnts[i]), f=True, c=True)
                cmds.rename(child[0], ("%sIK_jnt"%legJnts[i+1]))
            scale = cmds.xform(("%s_Scale_ctrl"%perso), q=True, r=True, s=True)
            # ctrl
            cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=scale[0], s=8, n=("%s_%s_Foot_ctrl"%(perso, cote)))
            cmds.delete(cmds.pointConstraint(("%sIK_jnt"%ankle), ("%s_%s_Foot_ctrl"%(perso, cote)), n=("%s_%s_Foot_contrainte"%(perso, cote))))
            cmds.move(0, ("%s_%s_Foot_ctrl.cv[0:7]"%(perso, cote)), y=True, a=True, wd=True)
            cmds.scale(1.5, ("%s_%s_Foot_ctrl.cv[0:7]"%(perso, cote)), x=True, r=True, os=True)
            cmds.move((2.3 * scale[0]), ("%s_%s_Foot_ctrl.cv[4:6]"%(perso, cote)), z=True, r=True, os=True, wd=True)
            if cote == "L":
                cmds.move((-.2 * scale[0]), ("%s_%s_Foot_ctrl.cv[6]"%(perso, cote)), x=True, r=True, os=True, wd=True)
            else:
                cmds.move((.2 * scale[0]), ("%s_%s_Foot_ctrl.cv[4]"%(perso, cote)), x=True, r=True, os=True, wd=True)
            cmds.move((.7 * scale[0]), ("%s_%s_Foot_ctrl.cv[5]"%(perso, cote)), z=True, r=True, os=True, wd=True)
            cmds.move((1.5 * scale[0]), ("%s_%s_Foot_ctrl.cv[3]"%(perso, cote)), ("%s_%s_Foot_ctrl.cv[7]"%(perso, cote)), z=True, r=True, os=True, wd=True)
            if cote == "L":
                cmds.move((.4 * scale[0]), ("%s_%s_Foot_ctrl.cv[3]"%(perso, cote)), ("%s_%s_Foot_ctrl.cv[7]"%(perso, cote)), x=True, r=True, os=True, wd=True)
            else:
                cmds.move((-.4 * scale[0]), ("%s_%s_Foot_ctrl.cv[3]"%(perso, cote)), ("%s_%s_Foot_ctrl.cv[7]"%(perso, cote)), x=True, r=True, os=True, wd=True)
            cmds.scale(.4, ("%s_%s_Foot_ctrl.cv[3]"%(perso, cote)), ("%s_%s_Foot_ctrl.cv[7]"%(perso, cote)), r=True, os=True)
            cmds.move((.7 * scale[0]), ("%s_%s_Foot_ctrl.cv[0]"%(perso, cote)), ("%s_%s_Foot_ctrl.cv[2]"%(perso, cote)), z=True, r=True, os=True, wd=True)
            ctrl = "%s_%s_Foot_ctrl"%(perso, cote)
            cmds.makeIdentity(ctrl, a=True, t=True, r=True, s=True, n=False)
            cmds.delete(ctrl, ch=True)
            # ball ikhl
            cmds.hide(cmds.ikHandle(sj=("%sIK_jnt"%ankle), ee=("%sIK_jnt"%ball), s="sticky", sol="ikSCsolver", n=("%s_ikhl"%ball)))
            # toe ikhl
            cmds.hide(cmds.ikHandle(sj=("%sIK_jnt"%ball), ee=("%sIK_jnt"%toe), s="sticky", sol="ikSCsolver", n=("%s_ikhl"%toe)))
            # add attributes
            cmds.addAttr(ctrl, k=True, h=False, ln="Foot", at="enum", en="-----:")
            cmds.addAttr(ctrl, k=True, h=False, ln="Foot_Step", at="double", min=0, max=20, dv=0)
            cmds.addAttr(ctrl, k=True, h=False, ln="Toe_Pivot", at="double", min=-10, max=10, dv=0)
            cmds.addAttr(ctrl, k=True, h=False, ln="Toe_Roll", at="double", min=-10, max=10, dv=0)
            # reverse foot
            translate = cmds.xform(("%s_ikhl"%ball), q=True, a=True, t=True)
            cmds.group(em=True, name=("%s_%s_IK_Heel_grp"%(perso, cote)))
            cmds.xform(piv=(translate[0], translate[1], translate[2]))
            cmds.hide(cmds.ikHandle(sj=("%sIK_jnt"%leg), ee=("%sIK_jnt"%ankle), s="sticky", sol="ikRPsolver", n=("%s_ikhl"%ankle)))
            cmds.parent(("%s_ikhl"%ankle), ("%s_%s_IK_Heel_grp"%(perso, cote)))
            cmds.group(em=True, name=("%sIK_grp"%ball))
            cmds.xform(piv=(translate[0], translate[1], translate[2]))
            cmds.parent(("%s_ikhl"%ball), ("%sIK_grp"%ball))
            cmds.parent(("%s_ikhl"%toe), ("%sIK_grp"%ball))
            translate = cmds.xform(("%s_ikhl"%toe), q=True, a=True, t=True)
            cmds.group(em=True, name=("%sIK_grp"%toe))
            cmds.xform(piv=(translate[0], translate[1], translate[2]))
            cmds.parent(("%sIK_grp"%ball), ("%sIK_grp"%toe))
            cmds.parent(("%s_%s_IK_Heel_grp"%(perso, cote)), ("%sIK_grp"%toe))
            translate = cmds.xform(("%s_ikhl"%ankle), q=True, a=True, t=True)
            cmds.group(em=True, name=("%sIK_grp"%ankle))
            cmds.xform(piv=(translate[0], translate[1], translate[2]))
            cmds.parent(("%sIK_grp"%toe), ("%sIK_grp"%ankle))
            cmds.parent(("%sIK_grp"%ankle), ctrl)
            # driven keys
            cmds.setDrivenKeyframe(("%s_%s_IK_Heel_grp.rx"%(perso, cote)), cd=("%s.Foot_Step"%ctrl))
            cmds.setDrivenKeyframe(("%s_%s_IK_Heel_grp.rx"%(perso, cote)), cd=("%s.Foot_Step"%ctrl), dv=10, dn=True, v=40)
            cmds.setDrivenKeyframe(("%sIK_grp.rx"%toe), cd=("%s.Foot_Step"%ctrl), dv=10, dn=True, v=0)
            cmds.setDrivenKeyframe(("%s_%s_IK_Heel_grp.rx"%(perso, cote)), cd=("%s.Foot_Step"%ctrl), dv=20, dn=True, v=0)
            cmds.setDrivenKeyframe(("%sIK_grp.rx"%toe), cd=("%s.Foot_Step"%ctrl), dv=20, dn=True, v=40)
            cmds.setDrivenKeyframe(("%sIK_grp.ry"%toe), cd=("%s.Toe_Pivot"%ctrl), itt="linear", ott="linear")
            cmds.setDrivenKeyframe(("%sIK_grp.ry"%toe), cd=("%s.Toe_Pivot"%ctrl), dv=-10, dn=True, v=25, itt="linear", ott="linear")
            cmds.setDrivenKeyframe(("%sIK_grp.ry"%toe), cd=("%s.Toe_Pivot"%ctrl), dv=10, dn=True, v=-25, itt="linear", ott="linear")
            cmds.setDrivenKeyframe(("%sIK_grp.rx"%ball), cd=("%s.Toe_Roll"%ctrl), itt="linear", ott="linear")
            cmds.setDrivenKeyframe(("%sIK_grp.rx"%ball), cd=("%s.Toe_Roll"%ctrl), dv=-10, dn=True, v=45, itt="linear", ott="linear")
            cmds.setDrivenKeyframe(("%sIK_grp.rx"%ball), cd=("%s.Toe_Roll"%ctrl), dv=10, dn=True, v=-45, itt="linear", ott="linear")
            # pole vector
            cmds.curve(d=True, p=[(0, 1.5, 1.5), (0, 1.5, -1.5), (0, -1.5, -1.5), (0, -1.5, 1.5), (0, 1.5, 1.5)], n=("%sIK_ctrl"%knee))
            cmds.scale(scale[0], scale[0], scale[0], ("%sIK_ctrl"%knee), r=True, os=True)
            legPos = cmds.xform(("%sIK_jnt"%leg), q=True, ws=True, rp=True)
            kneePos = cmds.xform(("%sIK_jnt"%knee), q=True, ws=True, rp=True)
            anklePos = cmds.xform(("%sIK_jnt"%ankle), q=True, ws=True, rp=True)
            legVector = MVector(legPos[0], legPos[1], legPos[2])
            kneeVector = MVector(kneePos[0], kneePos[1], kneePos[2])
            ankleVector = MVector(anklePos[0], anklePos[1], anklePos[2])
            midPoint = (legVector + ankleVector) / 2
            pvDist = kneeVector - midPoint
            pvPos = pvDist * 3 + midPoint
            cmds.move(pvPos.x, pvPos.y, pvPos.z, ("%sIK_ctrl"%knee), a=True, ws=True)
            cmds.rotate(0, 90,45, ("%sIK_ctrl"%knee), a=True, os=True)
            cmds.scale(.3, .3, .3, ("%sIK_ctrl"%knee), r=True, os=True)
            cmds.makeIdentity(("%sIK_ctrl"%knee), a=True, t=True, r=True, s=True, n=False)
            cmds.delete(("%sIK_ctrl"%knee), ch=True)
            cmds.poleVectorConstraint(("%sIK_ctrl"%knee), ("%s_ikhl"%ankle), n=("%s_pv"%knee))
            colorize(cote, [ctrl, ("%sIK_ctrl"%knee)])
            # clean scene
            lockAndHide([("%sIK_ctrl"%knee)], True, True, ["rx", "ry", "rz", "sx", "sy", "sz"])
            lockAndHide([("%s_%s_Foot_ctrl"%(perso, cote))], True, True, ["sx", "sy", "sz"])
    # end def legIK

    # def legFK
    def legFK(self, perso, cotes):
        for cote in cotes:
            # variables
            leg = "%s_%s_Leg"%(perso, cote)
            knee = "%s_%s_Knee"%(perso, cote)
            ankle = "%s_%s_Ankle"%(perso, cote)
            ball = "%s_%s_Ball"%(perso, cote)
            toe = "%s_%s_Toe"%(perso, cote)
            legJnts = [leg, knee, ankle, ball, toe]
            cmds.duplicate(("%s_jnt"%leg), n=("%sFK_jnt"%leg))
            for i in range(0,4):
                child = cmds.listRelatives(("%sFK_jnt"%legJnts[i]), f=True, c=True)
                cmds.rename(child[0], ("%sFK_jnt"%legJnts[i+1]))
            scale = cmds.xform(("%s_Scale_ctrl"%perso), q=True, r=True, s=True)
            # ctrl
            FKctrls = [leg, knee, ankle, ball]
            for FKctrl in FKctrls:
                cmds.circle(c=(0, 0, 0), nr=(1, 0, 0), r=(scale[0] * 1.2), s=8, n=("%sFK_ctrl"%FKctrl))
                cmds.group(n=("%sFK_grp"%FKctrl))
                cmds.delete(cmds.parentConstraint(("%sFK_jnt"%FKctrl), ("%sFK_grp"%FKctrl), n=("%sFK_contrainte"%FKctrl)))
                colorize(cote, ["%sFK_ctrl"%FKctrl])
                cmds.delete("%sFK_ctrl"%FKctrl, ch=True)
            cmds.parent(("%sFK_grp"%knee), ("%sFK_ctrl"%leg))
            cmds.parent(("%sFK_grp"%ankle), ("%sFK_ctrl"%knee))
            cmds.parent(("%sFK_grp"%ball), ("%sFK_ctrl"%ankle))
            cmds.orientConstraint(("%sFK_ctrl"%leg), ("%sFK_jnt"%leg), n=("%sFK_contrainte"%leg))
            cmds.orientConstraint(("%sFK_ctrl"%knee), ("%sFK_jnt"%knee), n=("%sFK_contrainte"%knee))
            cmds.orientConstraint(("%sFK_ctrl"%ankle), ("%sFK_jnt"%ankle), n=("%sFK_contrainte"%ankle))
            cmds.orientConstraint(("%sFK_ctrl"%ball), ("%sFK_jnt"%ball), n=("%sFK_contrainte"%ball))
            # clean scene
            cmds.transformLimits(("%sFK_ctrl"%ball), ry=(-45, 45), ery=(True, True))
            lockAndHide([("%sFK_ctrl"%leg), ("%sFK_ctrl"%ankle)], True, True, ["tx", "ty", "tz", "sx", "sy", "sz"])
            lockAndHide([("%sFK_ctrl"%knee), ("%sFK_ctrl"%ball)], True, True, ["tx", "ty", "tz", "sx", "sy", "sz", "rx", "rz"])
    # end def LegFK

    # def legRibbon
    def legRibbon(self, perso, cotes):
        for cote in cotes:
            # variables
            knee = "%s_%s_Knee"%(perso, cote)
            leg = "%s_%s_Leg"%(perso, cote)
            ankle = "%s_%s_Ankle"%(perso, cote)
            type = ""
            scale = cmds.xform(("%s_Scale_ctrl"%perso), q=True, r=True, s=True)
            # mise en position
            nomRibbn = ["UpperLeg", "LowerLeg"]
            for name in nomRibbn:
                if persoSel.legIK and persoSel.legFK:
                    if name == "UpperLeg":
                        cmds.pointConstraint("%s_jnt"%(leg), "%s_%s_%s_RibbnPos_hi_loc"%(perso, cote, name), n="%s_%s_%s_RibbnPos_hi_loc_point_contrainte"%(perso, cote, name))
                        cmds.orientConstraint("%s_jnt"%(leg), "%s_%s_%s_RibbnPos_hi_loc"%(perso, cote, name), o=(90, 0, 0), n="%s_%s_%s_RibbnPos_hi_loc_orient_contrainte"%(perso, cote, name))
                        cmds.delete(cmds.pointConstraint("%s_jnt"%(knee), "%s_%s_%s_RibbnPos_low_loc"%(perso, cote, name)))
                        cmds.delete(cmds.orientConstraint("%s_jnt"%(knee), "%s_%s_%s_RibbnPos_low_loc"%(perso, cote, name), o=(90, 0, 0)))
                    else:
                        cmds.delete(cmds.pointConstraint("%s_jnt"%(knee), "%s_%s_%s_RibbnPos_hi_loc"%(perso, cote, name)))
                        cmds.delete(cmds.orientConstraint("%s_jnt"%(knee), "%s_%s_%s_RibbnPos_hi_loc"%(perso, cote, name), o=(90, 0, 0)))
                        cmds.pointConstraint("%s_jnt"%(ankle), "%s_%s_%s_RibbnPos_low_loc"%(perso, cote, name), n="%s_%s_%s_RibbnPos_low_loc_point_contrainte"%(perso, cote, name))
                        cmds.orientConstraint("%s_jnt"%(ankle), "%s_%s_%s_RibbnPos_low_loc"%(perso, cote, name), o=(90, 0, 0), n="%s_%s_%s_RibbnPos_low_loc_orient_contrainte"%(perso, cote, name))
                else:
                    if persoSel.legIK:
                        type = "IK"
                    else:
                        type = "FK"
                    if name == "UpperLeg":
                        cmds.pointConstraint("%s%s_jnt"%(leg, type), "%s_%s_%s_RibbnPos_hi_loc"%(perso, cote, name), n="%s_%s_%s_RibbnPos_hi_loc_point_contrainte"%(perso, cote, name))
                        cmds.orientConstraint("%s%s_jnt"%(leg, type), "%s_%s_%s_RibbnPos_hi_loc"%(perso, cote, name), o=(90, 0, 0), n="%s_%s_%s_RibbnPos_hi_loc_orient_contrainte"%(perso, cote, name))
                        cmds.delete(cmds.pointConstraint("%s%s_jnt"%(knee, type), "%s_%s_%s_RibbnPos_low_loc"%(perso, cote, name)))
                        cmds.delete(cmds.orientConstraint("%s%s_jnt"%(knee, type), "%s_%s_%s_RibbnPos_low_loc"%(perso, cote, name), o=(90, 0, 0)))
                    else:
                        cmds.delete(cmds.pointConstraint("%s%s_jnt"%(knee, type), "%s_%s_%s_RibbnPos_hi_loc"%(perso, cote, name)))
                        cmds.delete(cmds.orientConstraint("%s%s_jnt"%(knee, type), "%s_%s_%s_RibbnPos_hi_loc"%(perso, cote, name), o=(90, 0, 0)))
                        cmds.pointConstraint("%s%s_jnt"%(ankle, type), "%s_%s_%s_RibbnPos_low_loc"%(perso, cote, name), n="%s_%s_%s_RibbnPos_low_loc_point_contrainte"%(perso, cote, name))
                        cmds.orientConstraint("%s%s_jnt"%(ankle, type), "%s_%s_%s_RibbnPos_low_loc"%(perso, cote, name), o=(90, 0, 0), n="%s_%s_%s_RibbnPos_low_loc_orient_contrainte"%(perso, cote, name))
            # ctrls
            cmds.circle(c=(0, 0, 0), nr=(1, 0, 0), r=(scale[0] * 1), s=8, n=("%sRibbn_ctrl"%knee))
            cmds.scale(.36, .36, .36, ("%sRibbn_ctrlShape.cv[1]"%knee), ("%sRibbn_ctrlShape.cv[3]"%knee), ("%sRibbn_ctrlShape.cv[5]"%knee), ("%sRibbn_ctrlShape.cv[7]"%knee), r=True)
            cmds.group(("%sRibbn_ctrl"%knee), n=("%sRibbn_grp"%knee))
            cmds.pointConstraint(("%s%s_jnt"%(knee,type)), ("%sRibbn_grp"%knee), n=("%sRibbn_ctrl_point_contrainte"%knee))
            cmds.orientConstraint(("%s%s_jnt"%(knee,type)), ("%sRibbn_grp"%knee), n=("%sRibbn_ctrl_orient_contrainte"%knee))
            cmds.parent("%s_%s_UpperLeg_RibbnPos_low_loc"%(perso, cote), ("%sRibbn_ctrl"%knee))
            cmds.parent("%s_%s_LowerLeg_RibbnPos_hi_loc"%(perso, cote), ("%sRibbn_ctrl"%knee))
            colorize(cote, ["%sRibbn_ctrl"%knee])
            # twist upperLeg
            signe = -1
            if cote == "R":
                signe = 1
            for i in range(1,6):
                cmds.group("%s_%s_UpperLeg_Ribbn0%i_jnt"%(perso, cote, i), n="%s_%s_UpperLeg_Ribbn0%i_grp"%(perso, cote, i))
                rX = cmds.getAttr("%s_%s_UpperLeg_Ribbn0%i_jnt.rotateX"%(perso, cote, i))
                rY = cmds.getAttr("%s_%s_UpperLeg_Ribbn0%i_jnt.rotateY"%(perso, cote, i))
                rZ = cmds.getAttr("%s_%s_UpperLeg_Ribbn0%i_jnt.rotateZ"%(perso, cote, i))
                cmds.setAttr("%s_%s_UpperLeg_Ribbn0%i_jnt.jointOrientX"%(perso, cote, i), rX)
                cmds.setAttr("%s_%s_UpperLeg_Ribbn0%i_jnt.jointOrientY"%(perso, cote, i), rY)
                cmds.setAttr("%s_%s_UpperLeg_Ribbn0%i_jnt.jointOrientZ"%(perso, cote, i), rZ)
                cmds.setAttr("%s_%s_UpperLeg_Ribbn0%i_jnt.rotateX"%(perso, cote, i), 0)
                cmds.setAttr("%s_%s_UpperLeg_Ribbn0%i_jnt.rotateY"%(perso, cote, i), 0)
                cmds.setAttr("%s_%s_UpperLeg_Ribbn0%i_jnt.rotateZ"%(perso, cote, i), 0)
                cmds.shadingNode("multiplyDivide", n=("%s_%s_UpLegTwist0%i_MD"%(perso, cote, i)), au=True)
                cmds.connectAttr(("%s%s_jnt.rotateX"%(leg, type)), ("%s_%s_UpLegTwist0%i_MD.input1X"%(perso, cote, i)), f=True)
                cmds.connectAttr(("%s_%s_UpLegTwist0%i_MD.outputX"%(perso, cote, i)), ("%s_%s_UpperLeg_Ribbn0%i_grp.rotateY"%(perso, cote, i)), f=True)
                cmds.setAttr(("%s_%s_UpLegTwist0%i_MD.input2X"%(perso, cote, i)), (signe * (-1 + (i-1) * .25)))
            # ctrls middle
            for name in nomRibbn:
                ribbn = "%s_%s_%s_Ribbn"%(perso, cote, name)
                cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=(scale[0] * 1), s=8, n=("%s_ctrl"%ribbn))
                cmds.scale(.36, .36, .36, ("%s_ctrlShape.cv[1]"%ribbn), ("%s_ctrlShape.cv[3]"%ribbn), ("%s_ctrlShape.cv[5]"%ribbn), ("%s_ctrlShape.cv[7]"%ribbn), r=True)
                cmds.group("%s_ctrl"%ribbn, n=("%s_grp"%ribbn))
                cmds.delete(cmds.parentConstraint("%sDriver_mid_jnt"%ribbn, "%s_grp"%ribbn))
                cmds.parent("%s_grp"%ribbn, "%sAim_mid_loc"%ribbn)
                cmds.pointConstraint("%s_ctrl"%ribbn, "%sDriver_mid_jnt"%ribbn, n=("%s_point_contrainte"%ribbn))
                cmds.orientConstraint("%s_ctrl"%ribbn, "%sDriver_mid_jnt"%ribbn, n=("%s_orient_contrainte"%ribbn))
                colorize(cote, ["%s_ctrl"%ribbn])
    # end def legRibbon

    # def switchLeg
    def switchLeg(self, perso, cotes):
        for cote in cotes:
            # variables
            leg = "%s_%s_Leg"%(perso, cote)
            knee = "%s_%s_Knee"%(perso, cote)
            ankle = "%s_%s_Ankle"%(perso, cote)
            ball = "%s_%s_Ball"%(perso, cote)
            toe = "%s_%s_Toe"%(perso, cote)
            legJnts = [leg, knee, ankle, ball, toe]
            scale = cmds.xform(("%s_Scale_ctrl"%perso), q=True, r=True, s=True)
            # ctrl
            cmds.circle(c=(0, 0, 0), nr=(0, 0, 1), sw=360, r=(scale[0] * 1.5), s=16, n=("%sSwitch_ctrl"%leg))
            cmds.scale(.52, .52, .52, ("%sSwitch_ctrl.cv[1]"%leg), ("%sSwitch_ctrl.cv[3]"%leg), ("%sSwitch_ctrl.cv[5]"%leg), ("%sSwitch_ctrl.cv[7]"%leg), ("%sSwitch_ctrl.cv[9]"%leg), ("%sSwitch_ctrl.cv[11]"%leg), ("%sSwitch_ctrl.cv[13]"%leg), ("%sSwitch_ctrl.cv[15]"%leg), r=True, p=(0, 0, 0))
            cmds.scale(.6, .6, .6, ("%sSwitch_ctrl"%leg), r=True, os=True)
            cmds.delete(cmds.parentConstraint(("%s_jnt"%ankle), ("%sSwitch_ctrl"%leg), sr=["x", "y", "z"], n=("%sSwitch_ctrl_contrainte"%leg)))
            cmds.move(0, 0, (scale[0] * -2), ("%sSwitch_ctrl"%leg), r=True, os=True, wd=True)
            cmds.makeIdentity(("%sSwitch_ctrl"%leg), a=True, t=True, r=True, s=True, n=False)
            cmds.delete(("%sSwitch_ctrl"%leg), ch=True)
            colorize(cote, ["%sSwitch_ctrl"%leg])
            cmds.parentConstraint(("%s_jnt"%ankle), ("%sSwitch_ctrl"%leg), mo=True, n=("%sSwitch_contrainte"%leg))
            # add attributs
            cmds.addAttr(("%sSwitch_ctrl"%leg), ln="IKFK_Switch", at="double", min=0, max=10, dv=0)
            cmds.setAttr(("%sSwitch_ctrl.IKFK_Switch"%leg), e=True, k=True)
            # contraintes et driven keys
            for jnt in legJnts:
                cmds.parentConstraint(("%sFK_jnt"%jnt), ("%s_jnt"%jnt), n=("%s_contrainte"%jnt))
                cmds.parentConstraint(("%sIK_jnt"%jnt), ("%s_jnt"%jnt), n=("%s_contrainte"%jnt))
                cmds.setDrivenKeyframe(("%s_contrainte.%sFK_jntW0"%(jnt, jnt)), cd=("%sSwitch_ctrl.IKFK_Switch"%leg), dv=0, dn=True, v=0)
                cmds.setDrivenKeyframe(("%s_contrainte.%sIK_jntW1"%(jnt, jnt)), cd=("%sSwitch_ctrl.IKFK_Switch"%leg), dv=0, dn=True, v=1)
                cmds.setDrivenKeyframe(("%s_contrainte.%sFK_jntW0"%(jnt, jnt)), cd=("%sSwitch_ctrl.IKFK_Switch"%leg), dv=10, dn=True, v=1)
                cmds.setDrivenKeyframe(("%s_contrainte.%sIK_jntW1"%(jnt, jnt)), cd=("%sSwitch_ctrl.IKFK_Switch"%leg), dv=10, dn=True, v=0)
                if jnt != toe:
                    cmds.setDrivenKeyframe(("%sFK_ctrl.visibility"%jnt), cd=("%sSwitch_ctrl.IKFK_Switch"%leg), dv=0, dn=True, v=0)
                    cmds.setDrivenKeyframe(("%sFK_ctrl.visibility"%jnt), cd=("%sSwitch_ctrl.IKFK_Switch"%leg), dv=4, dn=True, v=1)
                    lockAndHide([("%sFK_ctrl"%jnt)], False, True, ["v"])

            cmds.setDrivenKeyframe(("%s_%s_Foot_ctrl.visibility"%(perso, cote)), cd=("%sSwitch_ctrl.IKFK_Switch"%leg), dv=6, dn=True, v=1)
            cmds.setDrivenKeyframe(("%s_%s_Foot_ctrl.visibility"%(perso, cote)), cd=("%sSwitch_ctrl.IKFK_Switch"%leg), dv=10, dn=True, v=0)
            cmds.setDrivenKeyframe(("%sIK_ctrl.visibility"%knee), cd=("%sSwitch_ctrl.IKFK_Switch"%leg), dv=6, dn=True, v=1)
            cmds.setDrivenKeyframe(("%sIK_ctrl.visibility"%knee), cd=("%sSwitch_ctrl.IKFK_Switch"%leg), dv=10, dn=True, v=0)
            # clean scene
            lockAndHide(["%sSwitch_ctrl"%leg], True, True, ["tx", "ty", "tz", "rx", "ry", "rz", "sx", "sy", "sz", "v"])
            lockAndHide([("%sIK_ctrl"%knee), ("%s_%s_Foot_ctrl"%(perso, cote))], False, True, ["v"])
            cmds.hide(("%sIK_jnt"%leg), ("%sFK_jnt"%leg))
    # end def switchLeg

    # def armIK
    def armIK(self, perso, cotes):
        for cote in cotes:
            # variables
            shoulder = "%s_%s_Shoulder"%(perso, cote)
            elbow = "%s_%s_Elbow"%(perso, cote)
            foreArm = "%s_%s_ForeArm"%(perso, cote)
            wrist = "%s_%s_Wrist"%(perso, cote)
            clavicle = "%s_%s_Clavicle"%(perso, cote)
            armJnts = [shoulder, elbow, foreArm, wrist, clavicle]
            cmds.duplicate(("%s_jnt"%shoulder), n=("%sIK_jnt"%shoulder))
            for i in range(0, 3):
                child = cmds.listRelatives(("%sIK_jnt"%armJnts[i]), f=True, c=True)
                cmds.rename(child[0], ("%sIK_jnt"%armJnts[i+1]))
            scale = cmds.xform(("%s_Scale_ctrl"%perso), q=True, r=True, s=True)
            # IK
            cmds.hide(cmds.ikHandle(sj=("%sIK_jnt"%shoulder), ee=("%sIK_jnt"%foreArm), s="sticky", sol="ikRPsolver", n=("%s_ikhl"%foreArm)))
            # ctrl
            # arm
            cmds.circle(c=(0, 0, 0), nr=(1, 0, 0), r=scale[0], s=8, n=("%s_%s_ArmIK_ctrl"%(perso, cote)))
            cmds.group(n=("%s_%s_ArmIK_grp"%(perso, cote)))
            cmds.delete(cmds.parentConstraint(("%sIK_jnt"%wrist), ("%s_%s_ArmIK_grp"%(perso, cote)), n=("%s_%s_ArmIK_contrainte"%(perso, cote))))
            # Ik modification
            cmds.setAttr('ikSystem.globalSolve', 0)
            cmds.parent(("%sIK_jnt"%wrist), w=True)
            tr = cmds.xform(("%sIK_jnt"%wrist), q=True, t=True)
            cmds.move(tr[0], tr[1], tr[2], ("%s_ikhl.scalePivot"%foreArm), ("%s_ikhl.rotatePivot"%foreArm))
            cmds.parent(("%sIK_jnt"%wrist), ("%sIK_jnt"%foreArm))
            effectorAll = cmds.connectionInfo(("%s_ikhl.endEffector"%foreArm), sfd=True)
            effector = effectorAll[:effectorAll.find(".")]
            cmds.move(tr[0], tr[1], tr[2], ("%s.scalePivot"%effector), ("%s.rotatePivot"%effector))
            cmds.setAttr('ikSystem.globalSolve', 1)
            # parentage
            cmds.parent(("%s_ikhl"%foreArm), ("%s_%s_ArmIK_ctrl"%(perso, cote)))
            cmds.orientConstraint(("%s_%s_ArmIK_ctrl"%(perso, cote)), ("%sIK_jnt"%wrist), mo=True, n=("%sIK_contrainte"%foreArm))
            # pole vector
            cmds.curve(d=True, p=[(0, 1.5, 1.5), (0, 1.5, -1.5), (0, -1.5, -1.5), (0, -1.5, 1.5), (0, 1.5, 1.5)], n=("%sIK_ctrl"%elbow))
            cmds.scale(scale[0], scale[0], scale[0], ("%sIK_ctrl"%elbow), r=True, os=True)
            shoulderPos = cmds.xform(("%sIK_jnt"%shoulder), q=True, ws=True, rp=True)
            elbowPos = cmds.xform(("%sIK_jnt"%elbow), q=True, ws=True, rp=True)
            wristPos = cmds.xform(("%sIK_jnt"%wrist), q=True, ws=True, rp=True)
            shoulderVector = MVector(shoulderPos[0], shoulderPos[1], shoulderPos[2])
            elbowVector = MVector(elbowPos[0], elbowPos[1], elbowPos[2])
            wristVector = MVector(wristPos[0], wristPos[1], wristPos[2])
            midPoint = (shoulderVector + wristVector) / 2
            pvDist = elbowVector - midPoint
            pvPos = pvDist * 3 + midPoint
            cmds.move(pvPos.x, pvPos.y, pvPos.z, ("%sIK_ctrl"%elbow), a=True, ws=True)
            cmds.rotate(0, 90, 45, ("%sIK_ctrl"%elbow), a=True, os=True)
            cmds.scale(.3, .3, .3, ("%sIK_ctrl"%elbow), r=True, os=True)
            cmds.makeIdentity(("%sIK_ctrl"%elbow), a=True, t=True, r=True, s=True, n=False)
            cmds.delete(("%sIK_ctrl"%elbow), ch=True)
            cmds.poleVectorConstraint(("%sIK_ctrl"%elbow), ("%s_ikhl"%foreArm), n=("%s_pv"%elbow))
            # auto rotation foreArm
            cmds.shadingNode("multiplyDivide", n=("%sIK_Up_MD"%foreArm), au=True)
            cmds.connectAttr(("%s_%s_ArmIK_ctrl.rotateX"%(perso, cote)), ("%sIK_Up_MD.input1X"%foreArm), f=True)
            cmds.connectAttr(("%sIK_Up_MD.outputX"%foreArm), ("%sIK_jnt.rotateX"%foreArm), f=True)
            cmds.setAttr("%sIK_Up_MD.input2X"%foreArm, .5)
            colorize(cote, [("%s_%s_ArmIK_ctrl"%(perso, cote)), ("%sIK_ctrl"%elbow)])
            # clean scene
            lockAndHide([("%sIK_ctrl"%elbow)], True, True, ["rx", "ry", "rz", "sx", "sy", "sz"])
            lockAndHide([("%s_%s_ArmIK_ctrl"%(perso, cote))], True, True, ["sx", "sy", "sz"])
    # end def armIK

    # def armFK
    def armFK(self, perso, cotes):
        for cote in cotes:
            shoulder = "%s_%s_Shoulder"%(perso, cote)
            elbow = "%s_%s_Elbow"%(perso, cote)
            foreArm = "%s_%s_ForeArm"%(perso, cote)
            wrist = "%s_%s_Wrist"%(perso, cote)
            clavicle = "%s_%s_Clavicle"%(perso, cote)
            armJnts = [shoulder, elbow, foreArm, wrist, clavicle]
            cmds.duplicate(("%s_jnt"%shoulder), n=("%sFK_jnt"%shoulder))
            for i in range(0, 3):
                child = cmds.listRelatives(("%sFK_jnt"%armJnts[i]), f=True, c=True)
                cmds.rename(child[0], ("%sFK_jnt"%armJnts[i+1]))
            scale = cmds.xform(("%s_Scale_ctrl"%perso), q=True, r=True, s=True)
            # ctrl
            FKctrls = [shoulder, elbow, wrist]
            for FKctrl in FKctrls:
                cmds.circle(c=(0, 0, 0), nr=(1, 0, 0), r=(scale[0] * 1.2), s=8, n=("%sFK_ctrl"%FKctrl))
                cmds.group(n=("%sFK_grp"%FKctrl))
                cmds.delete(cmds.parentConstraint(("%sFK_jnt"%FKctrl), ("%sFK_grp"%FKctrl), n=("%sFK_contrainte"%FKctrl)))
                colorize(cote, ["%sFK_ctrl"%FKctrl])
                cmds.delete("%sFK_ctrl"%FKctrl, ch=True)
            cmds.parent(("%sFK_grp"%elbow), ("%sFK_ctrl"%shoulder))
            cmds.parent(("%sFK_grp"%wrist), ("%sFK_ctrl"%elbow))
            cmds.orientConstraint(("%sFK_ctrl"%shoulder), ("%sFK_jnt"%shoulder), n=("%sFK_contrainte"%shoulder))
            cmds.orientConstraint(("%sFK_ctrl"%elbow), ("%sFK_jnt"%elbow), n=("%sFK_contrainte"%elbow))
            cmds.orientConstraint(("%sFK_ctrl"%wrist), ("%sFK_jnt"%wrist), n=("%sFK_contrainte"%wrist))
            # auto rotation foreArm
            cmds.shadingNode("multiplyDivide", n=("%sFK_Up_MD"%foreArm), au=True)
            cmds.connectAttr(("%s_%s_WristFK_ctrl.rotateX"%(perso, cote)), ("%sFK_Up_MD.input1X"%foreArm), f=True)
            cmds.connectAttr(("%sFK_Up_MD.outputX"%foreArm), ("%sFK_jnt.rotateX"%foreArm), f=True)
            cmds.setAttr("%sFK_Up_MD.input2X"%foreArm, .5)
            colorize(cote, [("%s_%s_WristFK_ctrl"%(perso, cote)), ("%sFK_ctrl"%elbow)])
            # clean scene
            lockAndHide([("%sFK_ctrl"%shoulder), ("%sFK_ctrl"%wrist)], True, True, ["tx", "ty", "tz", "sx", "sy", "sz"])
            lockAndHide([("%sFK_ctrl"%elbow)], True, True, ["tx", "ty", "tz", "sx", "sy", "sz", "rx", "rz"])
    # end def armFK

    # def armRibbon
    def armRibbon(self, perso, cotes):
        for cote in cotes:
            # variables
            elbow = "%s_%s_Elbow"%(perso, cote)
            shoulder = "%s_%s_Shoulder"%(perso, cote)
            type = ""
            scale = cmds.xform(("%s_Scale_ctrl"%perso), q=True, r=True, s=True)
            # mise en position
            nomRibbn = ["UpperArm", "LowerArm"]
            for name in nomRibbn:
                if persoSel.armIK and persoSel.armFK:
                    if name == "UpperArm":
                        cmds.parentConstraint("%s_%s_Shoulder_jnt"%(perso, cote), "%s_%s_%s_RibbnPos_hi_loc"%(perso, cote, name), n="%s_%s_%s_RibbnPos_hi_loc_contrainte"%(perso, cote, name))
                        cmds.delete(cmds.parentConstraint("%s_%s_Elbow_jnt"%(perso, cote), "%s_%s_%s_RibbnPos_low_loc"%(perso, cote, name)))
                    else:
                        cmds.delete(cmds.parentConstraint("%s_%s_Elbow_jnt"%(perso, cote), "%s_%s_%s_RibbnPos_hi_loc"%(perso, cote, name)))
                        cmds.parentConstraint("%s_%s_Wrist_jnt"%(perso, cote), "%s_%s_%s_RibbnPos_low_loc"%(perso, cote, name), n="%s_%s_%s_RibbnPos_low_loc_contrainte"%(perso, cote, name))
                elif persoSel.armIK:
                    type = "IK"
                    if name == "UpperArm":
                        cmds.parentConstraint("%s_%s_ShoulderIK_jnt"%(perso, cote), "%s_%s_%s_RibbnPos_hi_loc"%(perso, cote, name), n="%s_%s_%s_RibbnPos_hi_loc_contrainte"%(perso, cote, name))
                        cmds.delete(cmds.parentConstraint("%s_%s_ElbowIK_jnt"%(perso, cote), "%s_%s_%s_RibbnPos_low_loc"%(perso, cote, name)))
                    else:
                        cmds.delete(cmds.parentConstraint("%s_%s_ElbowIK_jnt"%(perso, cote), "%s_%s_%s_RibbnPos_hi_loc"%(perso, cote, name)))
                        cmds.parentConstraint("%s_%s_WristIK_jnt"%(perso, cote), "%s_%s_%s_RibbnPos_low_loc"%(perso, cote, name), n="%s_%s_%s_RibbnPos_low_loc_contrainte"%(perso, cote, name))
                elif persoSel.armFK:
                    type = "FK"
                    if name == "UpperArm":
                        cmds.parentConstraint("%s_%s_ShoulderFK_jnt"%(perso, cote), "%s_%s_%s_RibbnPos_hi_loc"%(perso, cote, name), n="%s_%s_%s_RibbnPos_hi_loc_contrainte"%(perso, cote, name))
                        cmds.delete(cmds.parentConstraint("%s_%s_ElbowFK_jnt"%(perso, cote), "%s_%s_%s_RibbnPos_low_loc"%(perso, cote, name)))
                    else:
                        cmds.delete(cmds.parentConstraint("%s_%s_ElbowFK_jnt"%(perso, cote), "%s_%s_%s_RibbnPos_hi_loc"%(perso, cote, name)))
                        cmds.parentConstraint("%s_%s_WristFK_jnt"%(perso, cote), "%s_%s_%s_RibbnPos_low_loc"%(perso, cote, name), n="%s_%s_%s_RibbnPos_low_loc_contrainte"%(perso, cote, name))
            # ctrls
            cmds.circle(c=(0, 0, 0), nr=(1, 0, 0), r=(scale[0] * 1), s=8, n=("%sRibbn_ctrl"%elbow))
            cmds.scale(.36, .36, .36, ("%sRibbn_ctrlShape.cv[1]"%elbow), ("%sRibbn_ctrlShape.cv[3]"%elbow), ("%sRibbn_ctrlShape.cv[5]"%elbow), ("%sRibbn_ctrlShape.cv[7]"%elbow), r=True)
            cmds.group(("%sRibbn_ctrl"%elbow), n=("%sRibbn_grp"%elbow))
            cmds.pointConstraint(("%s%s_jnt"%(elbow,type)), ("%sRibbn_grp"%elbow), n=("%sRibbn_ctrl_point_contrainte"%elbow))
            cmds.orientConstraint(("%s%s_jnt"%(elbow,type)), ("%sRibbn_grp"%elbow), n=("%sRibbn_ctrl_orient_contrainte"%elbow))
            cmds.parent("%s_%s_UpperArm_RibbnPos_low_loc"%(perso, cote), ("%sRibbn_ctrl"%elbow))
            cmds.parent("%s_%s_LowerArm_RibbnPos_hi_loc"%(perso, cote), ("%sRibbn_ctrl"%elbow))
            colorize(cote, ["%sRibbn_ctrl"%elbow])
            # twist upperArm
            signe = 1
            if cote == "R":
                signe = -1
            for i in range(1,6):
                cmds.group("%s_%s_UpperArm_Ribbn0%i_jnt"%(perso, cote, i), n="%s_%s_UpperArm_Ribbn0%i_grp"%(perso, cote, i))
                rX = cmds.getAttr("%s_%s_UpperArm_Ribbn0%i_jnt.rotateX"%(perso, cote, i))
                rY = cmds.getAttr("%s_%s_UpperArm_Ribbn0%i_jnt.rotateY"%(perso, cote, i))
                rZ = cmds.getAttr("%s_%s_UpperArm_Ribbn0%i_jnt.rotateZ"%(perso, cote, i))
                cmds.setAttr("%s_%s_UpperArm_Ribbn0%i_jnt.jointOrientX"%(perso, cote, i), rX)
                cmds.setAttr("%s_%s_UpperArm_Ribbn0%i_jnt.jointOrientY"%(perso, cote, i), rY)
                cmds.setAttr("%s_%s_UpperArm_Ribbn0%i_jnt.jointOrientZ"%(perso, cote, i), rZ)
                cmds.setAttr("%s_%s_UpperArm_Ribbn0%i_jnt.rotateX"%(perso, cote, i), 0)
                cmds.setAttr("%s_%s_UpperArm_Ribbn0%i_jnt.rotateY"%(perso, cote, i), 0)
                cmds.setAttr("%s_%s_UpperArm_Ribbn0%i_jnt.rotateZ"%(perso, cote, i), 0)
                cmds.shadingNode("multiplyDivide", n=("%s_%s_UpArmTwist0%i_MD"%(perso, cote, i)), au=True)
                cmds.connectAttr(("%s%s_jnt.rotateX"%(shoulder, type)), ("%s_%s_UpArmTwist0%i_MD.input1X"%(perso, cote, i)), f=True)
                cmds.connectAttr(("%s_%s_UpArmTwist0%i_MD.outputX"%(perso, cote, i)), ("%s_%s_UpperArm_Ribbn0%i_grp.rotateX"%(perso, cote, i)), f=True)
                cmds.setAttr(("%s_%s_UpArmTwist0%i_MD.input2X"%(perso, cote, i)), (signe * (-1 + (i-1) * .25)))
            # ctrls middle
            for name in nomRibbn:
                ribbn = "%s_%s_%s_Ribbn"%(perso, cote, name)
                cmds.circle(c=(0, 0, 0), nr=(1, 0, 0), r=(scale[0] * 1), s=8, n=("%s_ctrl"%ribbn))
                cmds.scale(.36, .36, .36, ("%s_ctrlShape.cv[1]"%ribbn), ("%s_ctrlShape.cv[3]"%ribbn), ("%s_ctrlShape.cv[5]"%ribbn), ("%s_ctrlShape.cv[7]"%ribbn), r=True)
                cmds.group("%s_ctrl"%ribbn, n=("%s_grp"%ribbn))
                cmds.delete(cmds.parentConstraint("%sDriver_mid_jnt"%ribbn, "%s_grp"%ribbn))
                cmds.parent("%s_grp"%ribbn, "%sAim_mid_loc"%ribbn)
                cmds.pointConstraint("%s_ctrl"%ribbn, "%sDriver_mid_jnt"%ribbn, n=("%s_point_contrainte"%ribbn))
                cmds.orientConstraint("%s_ctrl"%ribbn, "%sDriver_mid_jnt"%ribbn, n=("%s_orient_contrainte"%ribbn))
                colorize(cote, ["%s_ctrl"%ribbn])
    # end def armRibbon

# def switchArm
    def switchArm(self, perso, cotes):
        for cote in cotes:
            # variables
            shoulder = "%s_%s_Shoulder"%(perso, cote)
            elbow = "%s_%s_Elbow"%(perso, cote)
            foreArm = "%s_%s_ForeArm"%(perso, cote)
            wrist = "%s_%s_Wrist"%(perso, cote)
            clavicle = "%s_%s_Clavicle"%(perso, cote)
            armJnts = [shoulder, elbow, foreArm, wrist]
            # attributs
            cmds.setAttr(("%s_%s_Hand_ctrl.visibility"%(perso, cote)), 1)
            cmds.setAttr(("%s_%s_Hand_ctrl.IKFK_Switch"%(perso, cote)), k=True)
            # parentage
            for jnt in armJnts:
                cmds.parentConstraint(("%sFK_jnt"%jnt), ("%s_jnt"%jnt), n=("%s_contrainte"%jnt))
                cmds.parentConstraint(("%sIK_jnt"%jnt), ("%s_jnt"%jnt), n=("%s_contrainte"%jnt))
                cmds.setDrivenKeyframe(("%s_contrainte.%sFK_jntW0"%(jnt, jnt)), cd=("%s_%s_Hand_ctrl.IKFK_Switch"%(perso, cote)), dv=0, dn=True, v=0)
                cmds.setDrivenKeyframe(("%s_contrainte.%sIK_jntW1"%(jnt, jnt)), cd=("%s_%s_Hand_ctrl.IKFK_Switch"%(perso, cote)), dv=0, dn=True, v=1)
                cmds.setDrivenKeyframe(("%s_contrainte.%sFK_jntW0"%(jnt, jnt)), cd=("%s_%s_Hand_ctrl.IKFK_Switch"%(perso, cote)), dv=10, dn=True, v=1)
                cmds.setDrivenKeyframe(("%s_contrainte.%sIK_jntW1"%(jnt, jnt)), cd=("%s_%s_Hand_ctrl.IKFK_Switch"%(perso, cote)), dv=10, dn=True, v=0)
                if jnt != foreArm:
                    cmds.setDrivenKeyframe(("%sFK_ctrl.visibility"%jnt), cd=("%s_%s_Hand_ctrl.IKFK_Switch"%(perso, cote)), dv=0, dn=True, v=0)
                    cmds.setDrivenKeyframe(("%sFK_ctrl.visibility"%jnt), cd=("%s_%s_Hand_ctrl.IKFK_Switch"%(perso, cote)), dv=4, dn=True, v=1)
            cmds.setDrivenKeyframe(("%s_%s_ArmIK_ctrl.visibility"%(perso, cote)), cd=("%s_%s_Hand_ctrl.IKFK_Switch"%(perso, cote)), dv=6, dn=True, v=1)
            cmds.setDrivenKeyframe(("%s_%s_ArmIK_ctrl.visibility"%(perso, cote)), cd=("%s_%s_Hand_ctrl.IKFK_Switch"%(perso, cote)), dv=10, dn=True, v=0)
            cmds.setDrivenKeyframe(("%sIK_ctrl.visibility"%elbow), cd=("%s_%s_Hand_ctrl.IKFK_Switch"%(perso, cote)), dv=6, dn=True, v=1)
            cmds.setDrivenKeyframe(("%sIK_ctrl.visibility"%elbow), cd=("%s_%s_Hand_ctrl.IKFK_Switch"%(perso, cote)), dv=10, dn=True, v=0)
            # clean scene
            lockAndHide([("%s_%s_ArmIK_ctrl"%(perso, cote)), ("%sIK_ctrl"%elbow), ("%sFK_ctrl"%shoulder), ("%sFK_ctrl"%elbow), ("%sFK_ctrl"%wrist)], False, True, ["v"])
            cmds.hide(("%sIK_jnt"%shoulder), ("%sFK_jnt"%shoulder))
    # end def switchArm

    # def fingersAndClavicle
    def fingersAndClavicle(self, perso, cotes, ctrl, ultim, fk, FKarm):
        for cote in cotes:
            # variables
            thumb = "%s_%s_Thumb"%(perso, cote)
            index = "%s_%s_Index"%(perso, cote)
            middle = "%s_%s_Middle"%(perso, cote)
            ring = "%s_%s_Ring"%(perso, cote)
            pinky = "%s_%s_Pinky"%(perso, cote)
            fingers = [thumb, index, middle, ring, pinky]
            wrist = "%s_%s_Wrist"%(perso, cote)
            clavicle = "%s_%s_Clavicle"%(perso, cote)
            fingersName = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
            scale = cmds.xform(("%s_Scale_ctrl"%perso), q=True, r=True, s=True)
            # ctrl
            hCtrl = ("%s_%s_Hand_ctrl"%(perso, cote))
            cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), sw=360, r=(scale[0] * 1.5), s=16, n=hCtrl)
            cmds.scale(.52, .52, .52, ("%s.cv[1]"%hCtrl), ("%s.cv[3]"%hCtrl), ("%s.cv[5]"%hCtrl), ("%s.cv[7]"%hCtrl), ("%s.cv[9]"%hCtrl), ("%s.cv[11]"%hCtrl), ("%s.cv[13]"%hCtrl), ("%s.cv[15]"%hCtrl), r=True, p=(0, 0, 0))
            cmds.scale(.4, .4, .4, hCtrl, r=True, os=True)
            cmds.delete(cmds.parentConstraint(("%s_jnt"%wrist), hCtrl, n=("%s_contrainte"%hCtrl)))
            if cote == "L":
                cmds.move((.5 * scale[0]), scale[0], 0, hCtrl, r=True, os=True, wd=True)
            else:
                cmds.move(-(.5 * scale[0]), -scale[0], 0, hCtrl, r=True, os=True, wd=True)
            cmds.makeIdentity(hCtrl, a=True, t=True, r=True, s=True, n=False)
            cmds.delete(hCtrl, ch=True)
            cmds.addAttr(hCtrl, ln="IKFK_Switch", at="double", min=0, max=10, dv=0)
            cmds.setAttr(("%s.IKFK_Switch"%hCtrl), e=True, k=False)
            cmds.setAttr(("%s.visibility"%hCtrl), 0)
            colorize(cote, [hCtrl])
            # ctrl
            if ctrl:
                cmds.setAttr(("%s.visibility"%hCtrl), 1)
                for finger in fingersName:
                    # attributs
                    cmds.addAttr(hCtrl, ln=finger, at="enum", en="-----:")
                    cmds.setAttr("%s.%s"%(hCtrl, finger), e=True, cb=True)
                    cmds.addAttr(hCtrl, ln="%s_Pivot"%finger, at="double", min=-10, max=10, dv=0, k=True, h=False)
                    cmds.addAttr(hCtrl, ln="%s_Twist"%finger, at="double", min=-10, max=10, dv=0, k=True, h=False)
                    for i in range(1, 4):
                        cmds.addAttr(hCtrl, ln="%s_0%s"%(finger, i), at="double", min=-10, max=10, dv=0, k=True, h=False)
            # utlim
            if ultim:
                uCtrl = ("%s_%s_Ultim_Hand_ctrl"%(perso, cote))
                cmds.circle(c=(0, 0, 0), nr=(1, 0, 0), r=1, s=8, n=uCtrl)
                cmds.group(n="%s_%s_Ultim_Hand_grp"%(perso, cote))
                cmds.move(0, 2, 0, ("%s_%s_Ultim_Hand_grp"%(perso, cote)), a=True, ws=True)
                # attributs
                cmds.addAttr(uCtrl, ln="Finger_Influence", at="enum", en="-----:")
                cmds.setAttr("%s.Finger_Influence"%uCtrl, e=True, cb=True)
                for i in range(0, 5):
                    cmds.group(n=("%s_ctrl_intermediaire_grp"%fingers[i]), em=True)
                    cmds.move(0, 0, (2 - i), ("%s_ctrl_intermediaire_grp"%fingers[i]), a=True, ws=True)
                    cmds.group(n=("%s_ctrl_grp"%fingers[i]), em=True)
                    cmds.move(0, 0, (2 - i), ("%s_ctrl_grp"%fingers[i]), a=True, ws=True)
                    cmds.setDrivenKeyframe(("%s_ctrl_intermediaire_grp.translateY"%fingers[i]), cd=("%s.translateZ"%uCtrl), dv=(6 - i), dn=True, v=0)
                    cmds.setDrivenKeyframe(("%s_ctrl_intermediaire_grp.translateY"%fingers[i]), cd=("%s.translateZ"%uCtrl), dv=(2 - i), dn=True, v=2)
                    cmds.setDrivenKeyframe(("%s_ctrl_intermediaire_grp.translateY"%fingers[i]), cd=("%s.translateZ"%uCtrl), dv=(-2 - i), dn=True, v=0)
                    cmds.expression(s=("%s_ctrl_grp.translateY = %s_ctrl_intermediaire_grp.translateY * - %s.translateY / 4"%(fingers[i], fingers[i], uCtrl)), o=("%s_ctrl_grp"%fingers[i]), ae=True, uc="all")
                    cmds.addAttr(uCtrl, ln=fingersName[i], at="double", min=0, max=10, dv=10, k=True, h=False)
                # separateur
                cmds.addAttr(uCtrl, ln="Phalanx_Influence", at="enum", en="-----:")
                cmds.setAttr(("%s.Phalanx_Influence"%uCtrl), e=True, cb=True)
                for i in range(1, 4):
                    cmds.addAttr(uCtrl, ln=("Phalanx_0%i"%i), at="double", min=0, max=10, dv=10, k=True, h=False)
                for i in range(0, 5):
                    for j in range(1,4):
                        cmds.group(n=("%s0%i_rZ_grp"%(fingers[i], j)), em=True)
                        cmds.parent(("%s0%i_rZ_grp"%(fingers[i], j)), ("%s_ctrl_grp"%fingers[i]))
                        cmds.setDrivenKeyframe(("%s0%i_rZ_grp.rotateZ"%(fingers[i], j)), cd=("%s_ctrl_grp.translateY"%fingers[i]), dv=0, dn=True, v=0)
                        cmds.setDrivenKeyframe(("%s0%i_rZ_grp.rotateZ"%(fingers[i], j)), cd=("%s_ctrl_grp.translateY"%fingers[i]), dv=1, dn=True, v=-70)
                cmds.group(("%s_ctrl_intermediaire_grp"%thumb), ("%s_ctrl_grp"%thumb), ("%s_ctrl_intermediaire_grp"%index), ("%s_ctrl_grp"%index), ("%s_ctrl_intermediaire_grp"%middle), ("%s_ctrl_grp"%middle), ("%s_ctrl_intermediaire_grp"%ring), ("%s_ctrl_grp"%ring), ("%s_ctrl_intermediaire_grp"%pinky), ("%s_ctrl_grp"%pinky), ("%s_%s_Ultim_Hand_grp"%(perso, cote)), n=("%s_%s_Ultim_Hand_ctrl_grp"%(perso, cote)))
                cmds.scale((.2 * scale[0]), (.2 * scale[0]), (.2 * scale[0]), ("%s_%s_Ultim_Hand_ctrl_grp"%(perso, cote)), r=True, os=True)
                cmds.delete(cmds.parentConstraint(("%s_jnt"%wrist), ("%s_%s_Ultim_Hand_ctrl_grp"%(perso, cote)), n=("%s_%s_Ultim_Hand_ctrl_contrainte"%(perso, cote))))
                if cote == "L":
                    cmds.move((.5 * scale[0]), (1.5 * scale[0]), 0, ("%s_%s_Ultim_Hand_ctrl_grp"%(perso, cote)), r=True, os=True, wd=True)
                else:
                    cmds.move((-.5 * scale[0]), (-1.5 * scale[0]), 0, ("%s_%s_Ultim_Hand_ctrl_grp"%(perso, cote)), r=True, os=True, wd=True)
                    cmds.rotate(180, 0, 0, ("%s_%s_Ultim_Hand_ctrl_grp"%(perso, cote)), r=True, os=True)
                cmds.transformLimits(uCtrl, ty=(-4, 0), ety=(True, True), tz=(-6, 6), etz=(True, True))
                colorize(cote, ["%s_%s_Ultim_Hand_ctrl_grp"%(perso, cote)])
            # FK
            if fk:
                for i in range(0, 5):
                    for j in range(1, 4):
                        cmds.circle(c=(0, 0, 0), nr=(1, 0, 0), r=(scale[0] * .3), s=8, n=("%s0%i_FK_ctrl"%(fingers[i], j)))
                        cmds.group(("%s0%i_FK_ctrl"%(fingers[i], j)), n=("%s0%i_FK_grp"%(fingers[i], j)))
                        cmds.group(("%s0%i_FK_grp"%(fingers[i], j)), n=("%s0%i_FK_pos_grp"%(fingers[i], j)))
                        cmds.delete(cmds.parentConstraint(("%s0%i_jnt"%(fingers[i], j)), ("%s0%i_FK_pos_grp"%(fingers[i], j)), n=("%s0%i_FK_contrainte"%(fingers[i], j))))
                        cmds.expression(s=("%s0%i_FK_grp.rotateX = %s0%i_jnt.rotateX - %s0%i_FK_ctrl.rotateX"%(fingers[i], j, fingers[i], j, fingers[i], j)), o=("%s0%i_FK_grp"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_x_FK_expression"))
                        cmds.expression(s=("%s0%i_FK_grp.rotateY = %s0%i_jnt.rotateY - %s0%i_FK_ctrl.rotateY"%(fingers[i], j, fingers[i], j, fingers[i], j)), o=("%s0%i_FK_grp"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_y_FK_expression"))
                        cmds.expression(s=("%s0%i_FK_grp.rotateZ = %s0%i_jnt.rotateZ - %s0%i_FK_ctrl.rotateZ"%(fingers[i], j, fingers[i], j, fingers[i], j)), o=("%s0%i_FK_grp"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_z_FK_expression"))
                        colorize(cote, ["%s0%i_FK_ctrl"%(fingers[i], j)])
                        lockAndHide(["%s0%i_FK_ctrl"%(fingers[i], j)], True, True, ["tx", "ty", "tz", "sx", "sy", "sz", "v"])
                    cmds.parent(("%s03_FK_pos_grp"%fingers[i]), ("%s02_FK_ctrl"%fingers[i]))
                    cmds.parent(("%s02_FK_pos_grp"%fingers[i]), ("%s01_FK_ctrl"%fingers[i]))
            for i in range(0, 5):
                for j in range(1, 4):
                    if not ctrl and not fk and ultim:
                        cmds.expression(s=("%s0%i_jnt.rotateZ=%s0%i_rZ_grp.rotateZ * %s.Phalanx_0%i / 10 * %s.%s / 10"%(fingers[i], j, fingers[i], j, uCtrl, j, uCtrl, fingersName[i])), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_ecpression"%(fingersName[i], j)))
                    elif not ctrl and fk and not ultim:
                        cmds.expression(s=("%s0%i_jnt.rotateX = %s0%i_FK_ctrl.rotateX"%(fingers[i], j, fingers[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_Rx_FK_expression"%(fingersName[i], j)))
                        cmds.expression(s=("%s0%i_jnt.rotateY = %s0%i_FK_ctrl.rotateY"%(fingers[i], j, fingers[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_Ry_FK_expression"%(fingersName[i], j)))
                        cmds.expression(s=("%s0%i_jnt.rotateZ = %s0%i_FK_ctrl.rotateZ"%(fingers[i], j, fingers[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_Rz_FK_expression"%(fingersName[i], j)))
                    elif ctrl and not fk and not ultim:
                        cmds.expression(s=("%s0%i_jnt.rotateZ = %s.%s_0%i * -9"%(fingers[i], j, hCtrl, fingersName[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_expression"%(fingersName[i], j)))
                        if j == 1:
                            cmds.expression(s=("%s0%i_jnt.rotateY = %s.%s_Pivot * 4.5"%(fingers[i], j, hCtrl, fingersName[i])), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_pi_expression"%(fingersName[i], j)))
                            cmds.expression(s=("%s0%i_jnt.rotateX = %s.%s_Twist * 4.5"%(fingers[i], j, hCtrl, fingersName[i])), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_tw_expression"%(fingersName[i], j)))
                    elif ctrl and not fk and ultim:
                        cmds.expression(s=("%s0%i_jnt.rotateZ = %s0%i_rZ_grp.rotateZ * %s.Phalanx_0%i / 10 * %s.%s / 10 + %s.%s_0%i * -9"%(fingers[i], j, fingers[i], j, uCtrl, j, uCtrl, fingersName[i], hCtrl, fingersName[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_expression"%(fingersName[i], j)))
                        if j == 1:
                            cmds.expression(s=("%s0%i_jnt.rotateY = %s.%s_Pivot * 4.5"%(fingers[i], j, hCtrl, fingersName[i])), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_pi_expression"%(fingersName[i], j)))
                            cmds.expression(s=("%s0%i_jnt.rotateX = %s.%s_Twist * 4.5"%(fingers[i], j, hCtrl, fingersName[i])), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_tw_expression"%(fingersName[i], j)))
                    elif ctrl and fk and not ultim:
                        cmds.expression(s=("%s0%i_jnt.rotateZ = %s0%i_FK_ctrl.rotateZ + %s.%s_0%i * -9"%(fingers[i], j, fingers[i], j, hCtrl, fingersName[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_expression"%(fingersName[i], j)))
                        if j == 1:
                            cmds.expression(s=("%s0%i_jnt.rotateY = %s.%s_Pivot * 4.5 + %s0%i_FK_ctrl.rotateY"%(fingers[i], j, hCtrl, fingersName[i], fingers[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_pi_expression"%(fingersName[i], j)))
                            cmds.expression(s=("%s0%i_jnt.rotateX = %s.%s_Twist * 4.5 + %s0%i_FK_ctrl.rotateX"%(fingers[i], j, hCtrl, fingersName[i], fingers[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_tw_expression"%(fingersName[i], j)))
                            lockAndHide([hCtrl], True, True, ["Thumb_Pivot", "Thumb_Twist", "Index_Pivot", "Index_Twist", "Middle_Pivot", "Middle_Twist", "Ring_Pivot", "Ring_Twist", "Pinky_Pivot", "Pinky_Twist"])
                        else:
                            cmds.expression(s=("%s0%i_jnt.rotateY = %s0%i_FK_ctrl.rotateY"%(fingers[i], j, fingers[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_Ry_FK_expression"%(fingersName[i], j)))
                            cmds.expression(s=("%s0%i_jnt.rotateX = %s0%i_FK_ctrl.rotateX"%(fingers[i], j, fingers[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_Rx_FK_expression"%(fingersName[i], j)))
                    elif not ctrl and fk and ultim:
                        cmds.expression(s=("%s0%i_jnt.rotateX = %s0%i_FK_ctrl.rotateX"%(fingers[i], j, fingers[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_Rx_FK_expression"%(fingersName[i], j)))
                        cmds.expression(s=("%s0%i_jnt.rotateY = %s0%i_FK_ctrl.rotateY"%(fingers[i], j, fingers[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_Ry_FK_expression"%(fingersName[i], j)))
                        cmds.expression(s=("%s0%i_jnt.rotateZ = %s0%i_FK_ctrl.rotateZ + %s0%i_rZ_grp.rotateZ * %s.Phalanx_0%i /10 * %s.%s /10"%(fingers[i], j, fingers[i], j, fingers[i], j, uCtrl, j, uCtrl, fingersName[i])), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_expression"%(fingersName[i], j)))
                    elif ctrl and fk and ultim:
                        cmds.expression(s=("%s0%i_jnt.rotateZ = %s0%i_FK_ctrl.rotateZ + %s.%s_0%i * -9 + %s0%i_rZ_grp.rotateZ * %s.Phalanx_0%i /10 * %s.%s /10"%(fingers[i], j, fingers[i], j, hCtrl, fingersName[i], j, fingers[i], j, uCtrl, j, uCtrl, fingersName[i])), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_expression"%(fingersName[i], j)))
                        if i == 1:
                            cmds.expression(s=("%s0%i_jnt.rotateY = %s.%s_Pivot * 4.5 + %s0%i_FK_ctrl.rotateY"%(fingers[i], j, hCtrl, fingersName[i], fingers[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_pi_expression"%(fingersName[i], j)))
                            cmds.expression(s=("%s0%i_jnt.rotateX = %s.%s_Twist * 4.5 + %s0%i_FK_ctrl.rotateX"%(fingers[i], j, hCtrl, fingersName[i], fingers[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_tw_expression"%(fingersName[i], j)))
                            lockAndHide([hCtrl], True, True, ["Thumb_Pivot", "Thumb_Twist", "Index_Pivot", "Index_Twist", "Middle_Pivot", "Middle_Twist", "Ring_Pivot", "Ring_Twist", "Pinky_Pivot", "Pinky_Twist"])
                        else:
                            cmds.expression(s=("%s0%i_jnt.rotateY = %s0%i_FK_ctrl.rotateY"%(fingers[i], j, fingers[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_Ry_FK_expression"%(fingersName[i], j)))
                            cmds.expression(s=("%s0%i_jnt.rotateX = %s0%i_FK_ctrl.rotateX"%(fingers[i], j, fingers[i], j)), o=("%s0%i_jnt"%(fingers[i], j)), ae=True, uc="all", n=("%s_0%i_Rx_FK_expression"%(fingersName[i], j)))
            # clavicule
            cmds.circle(c=(0, 0, 0), nr=(0, 0, 1), sw=360, r=(3*scale[0]), s=16, n=("%s_ctrl"%clavicle))
            cmds.scale(.52, .52, .52, ("%s_ctrl.cv[1]"%clavicle), ("%s_ctrl.cv[3]"%clavicle), ("%s_ctrl.cv[5]"%clavicle), ("%s_ctrl.cv[7]"%clavicle), ("%s_ctrl.cv[9]"%clavicle), ("%s_ctrl.cv[11]"%clavicle), ("%s_ctrl.cv[13]"%clavicle), ("%s_ctrl.cv[15]"%clavicle), r=True, p=(0, 0, 0))
            cmds.rotate(0, 0, 90, ("%s_ctrl"%clavicle), r=True)
            cmds.scale(.2, .2, .2, ("%s_ctrl"%clavicle), r=True, os=True)
            cmds.group(("%s_ctrl"%clavicle), n=("%s_grp"%clavicle))
            cmds.delete(cmds.parentConstraint(("%s_jnt"%clavicle), ("%s_grp"%clavicle), n=("%s_contrainte"%clavicle)))
            signe = 1
            if cote == "R":
                signe = -1
            cmds.move(0, 0, (7 * scale[0] * signe), ("%s_ctrl.cv[0:15]"%clavicle), r=True, os=True)
            cmds.makeIdentity(("%s_ctrl"%clavicle), a=True, t=True, r=True, s=True, n=False)
            cmds.delete(("%s_ctrl"%clavicle), ch=True)
            cmds.orientConstraint(("%s_ctrl"%clavicle), ("%s_jnt"%clavicle), mo=True, n=("%s_contrainte"%clavicle))
            if FKarm:
                cmds.parent(("%s_%s_ShoulderFK_grp"%(perso, cote)), ("%s_ctrl"%clavicle))
            colorize(cote, ["%s_ctrl"%clavicle])
            lockAndHide(["%s_ctrl"%clavicle], True, True, ["tx", "ty", "tz", "sx", "sy", "sz", "v"])
    # end def fingersAndClavicle

    # def parentFigers
    def parentFingers(self, perso, cotes, IKarm, FKarm, CTRLhand, FKhand, ULTIMhand):
        for cote in cotes:
            # variables
            thumb = "%s_%s_Thumb01_jnt"%(perso, cote)
            index = "%s_%s_Index01_jnt"%(perso, cote)
            middle = "%s_%s_Middle01_jnt"%(perso, cote)
            ring = "%s_%s_Ring01_jnt"%(perso, cote)
            pinky = "%s_%s_Pinky01_jnt"%(perso, cote)
            fingers = [thumb, index, middle, ring, pinky]
            wrist = "%s_%s_Wrist"%(perso, cote)
            if IKarm and FKarm:
                for finger in fingers:
                    cmds.parent(finger, ("%s_jnt"%wrist))
                cmds.parentConstraint(("%s_jnt"%wrist), ("%s_%s_Hand_ctrl"%(perso, cote)), mo=True, n=("%s_%s_Hand_contrainte"%(perso, cote)))
                if FKhand:
                    cmds.parentConstraint(("%s_jnt"%wrist), ("%s_%s_Thumb01_FK_pos_grp"%(perso, cote)), mo=True, n=("%s_%s_Thumb_contrainte"%(perso, cote)))
                    cmds.parentConstraint(("%s_jnt"%wrist), ("%s_%s_Index01_FK_pos_grp"%(perso, cote)), mo=True, n=("%s_%s_Index_contrainte"%(perso, cote)))
                    cmds.parentConstraint(("%s_jnt"%wrist), ("%s_%s_Middle01_FK_pos_grp"%(perso, cote)), mo=True, n=("%s_%s_Middle_contrainte"%(perso, cote)))
                    cmds.parentConstraint(("%s_jnt"%wrist), ("%s_%s_Ring01_FK_pos_grp"%(perso, cote)), mo=True, n=("%s_%s_Ring_contrainte"%(perso, cote)))
                    cmds.parentConstraint(("%s_jnt"%wrist), ("%s_%s_Pinky01_FK_pos_grp"%(perso, cote)), mo=True, n=("%s_%s_Pinky_contrainte"%(perso, cote)))
                if ULTIMhand:
                    cmds.parentConstraint(("%s_jnt"%wrist), ("%s_%s_Ultim_Hand_ctrl_grp"%(perso, cote)), mo=True, n=("%s_%s_Ultim_Hand_contrainte"%(perso, cote)))
            elif IKarm:
                for finger in fingers:
                    cmds.parent(finger, ("%sIK_jnt"%wrist))
                if CTRLhand:
                    cmds.parentConstraint(("%sIK_jnt"%wrist), ("%s_%s_Hand_ctrl"%(perso, cote)), mo=True, n=("%s_%s_Hand_contrainte"%(perso, cote)))
                if FKhand:
                    cmds.parentConstraint(("%sIK_jnt"%wrist), ("%s_%s_Thumb01_FK_pos_grp"%(perso, cote)), mo=True, n=("%s_%s_Thumb_contrainte"%(perso, cote)))
                    cmds.parentConstraint(("%sIK_jnt"%wrist), ("%s_%s_Index01_FK_pos_grp"%(perso, cote)), mo=True, n=("%s_%s_Index_contrainte"%(perso, cote)))
                    cmds.parentConstraint(("%sIK_jnt"%wrist), ("%s_%s_Middle01_FK_pos_grp"%(perso, cote)), mo=True, n=("%s_%s_Middle_contrainte"%(perso, cote)))
                    cmds.parentConstraint(("%sIK_jnt"%wrist), ("%s_%s_Ring01_FK_pos_grp"%(perso, cote)), mo=True, n=("%s_%s_Ring_contrainte"%(perso, cote)))
                    cmds.parentConstraint(("%sIK_jnt"%wrist), ("%s_%s_Pinky01_FK_pos_grp"%(perso, cote)), mo=True, n=("%s_%s_Pinky_contrainte"%(perso, cote)))
                if ULTIMhand:
                    cmds.parentConstraint(("%sIK_jnt"%wrist), ("%s_%s_Ultim_Hand_ctrl_grp"%(perso, cote)), mo=True, n=("%s_%s_Ultim_Hand_contrainte"%(perso, cote)))
            else:
                for finger in fingers:
                    cmds.parent(finger, ("%sFK_jnt"%wrist))
                if CTRLhand:
                    cmds.parentConstraint(("%sFK_jnt"%wrist), ("%s_%s_Hand_ctrl"%(perso, cote)), mo=True, n=("%s_%s_Hand_contrainte"%(perso, cote)))
                if FKhand:
                    cmds.parentConstraint(("%sFK_jnt"%wrist), ("%s_%s_Thumb01_FK_pos_grp"%(perso, cote)), mo=True, n=("%s_%s_Thumb_contrainte"%(perso, cote)))
                    cmds.parentConstraint(("%sFK_jnt"%wrist), ("%s_%s_Index01_FK_pos_grp"%(perso, cote)), mo=True, n=("%s_%s_Index_contrainte"%(perso, cote)))
                    cmds.parentConstraint(("%sFK_jnt"%wrist), ("%s_%s_Middle01_FK_pos_grp"%(perso, cote)), mo=True, n=("%s_%s_Middle_contrainte"%(perso, cote)))
                    cmds.parentConstraint(("%sFK_jnt"%wrist), ("%s_%s_Ring01_FK_pos_grp"%(perso, cote)), mo=True, n=("%s_%s_Ring_contrainte"%(perso, cote)))
                    cmds.parentConstraint(("%sFK_jnt"%wrist), ("%s_%s_Pinky01_FK_pos_grp"%(perso, cote)), mo=True, n=("%s_%s_Pinky_contrainte"%(perso, cote)))
                if ULTIMhand:
                    cmds.parentConstraint(("%sFK_jnt"%wrist), ("%s_%s_Ultim_Hand_ctrl_grp"%(perso, cote)), mo=True, n=("%s_%s_Ultim_Hand_contrainte"%(perso, cote)))
            if CTRLhand or (IKarm and FKarm):
                lockAndHide(["%s_%s_Hand_ctrl"%(perso, cote)], True, True, ["tx", "ty", "tz", "rx", "ry", "rz", "sx", "sy", "sz", "v"])
            if ULTIMhand:
                lockAndHide(["%s_%s_Ultim_Hand_ctrl"%(perso, cote)], True, True, ["tx", "rx", "ry", "rz", "sx", "sy", "sz", "v"])
    # end def parentFingers

    # def spineIK
    def spineIK(self, perso):
        # variables
        spine01 = "%s_C_Spine01"%perso
        spine02 = "%s_C_Spine02"%perso
        spine03 = "%s_C_Spine03"%perso
        spine04 = "%s_C_Spine04"%perso
        spine05 = "%s_C_Spine05"%perso
        spine06 = "%s_C_Spine06"%perso
        spine07 = "%s_C_Spine07"%perso
        spine08 = "%s_C_Spine08"%perso
        spines = [spine01, spine02, spine03, spine04, spine05, spine06, spine07, spine08]
        root = "%s_C_Root"%perso
        pelvis = "%s_C_Pelvis"%perso
        # ikhandle
        cmds.hide(cmds.ikHandle(sj=("%s_jnt"%root), ee=("%s_jnt"%spine08), sol="ikSplineSolver", ccv=True, roc=False, tws="linear", cra=True, pcv=True, ns=2, n=("%s_C_Spine_ikhl"%perso)))
        transformGrp = cmds.listRelatives(("%s_jnt"%root), p=True)
        cmds.rename(transformGrp[0], ("%s_C_Spine_Transform_grp"%perso))
        curve = cmds.listRelatives(("%s_C_Spine_Transform_grp"%perso), c=True)
        cmds.rename(curve[1], ("%s_C_Spine_crv"%perso))
        cmds.parent(("%s_C_Spine_crv"%perso), w=True)
        cmds.group(("%s_C_Spine_Transform_grp"%perso), n=("%s_C_Spine_grp"%perso))
        cmds.select("%s_C_Spine_crv"%perso)
        # clusterCurve
        clusters = []
        cvs = cmds.getAttr("%s_C_Spine_crv.cp"%perso, s=True)
        for cv in range(cvs):
            clus = cmds.cluster('%s_C_Spine_crv.cv[%s]' %(perso, cv), relative=False)
            clusters.append(clus)
        lesClusters = []
        for i in range(0, len(clusters)):
            cmds.rename(clusters[i][1], ("%s_C_Spine0%i_cls"%(perso, (i+1))))
            clusters[i][1] = "%s_C_Spine0%i_cls"%(perso, (i+1))
            lesClusters.append(clusters[i][1])
        cmds.hide(lesClusters)
        scale = cmds.xform(("%s_Scale_ctrl"%perso), q=True, r=True, s=True)
        # ctrl FK
        # root
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=(3.5 * scale[0]), s=8, n=("%s_C_COG_ctrl"%perso))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%root), ("%s_C_COG_ctrl"%perso), sr=["x", "y", "z"]))
        cmds.makeIdentity(("%s_C_COG_ctrl"%perso), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_C_COG_ctrl"%perso), ch=True)
        cmds.move(0, (-1.5 * scale[0]), 0, ("%s_C_COG_ctrlShape.cv[7]"%perso), ("%s_C_COG_ctrlShape.cv[3]"%perso), r=True, os=True, wd=True)
        # spineMid
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=(2.55 * scale[0]), s=8, n=("%s_C_SpineMidFK_ctrl"%perso))
        cmds.delete(cmds.parentConstraint((lesClusters[2]), ("%s_C_SpineMidFK_ctrl"%perso), sr=["x", "y", "z"]))
        cmds.makeIdentity(("%s_C_SpineMidFK_ctrl"%perso), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_C_SpineMidFK_ctrl"%perso), ch=True)
        # spineUp
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=(2.55 * scale[0]), s=8, n=("%s_C_SpineUpFK_ctrl"%perso))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%spine08), ("%s_C_SpineUpFK_ctrl"%perso), sr=["x", "y", "z"]))
        cmds.makeIdentity(("%s_C_SpineUpFK_ctrl"%perso), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_C_SpineUpFK_ctrl"%perso), ch=True)
        cmds.move(0, (.6 * scale[0]), 0, ("%s_C_SpineUpFK_ctrlShape.cv[7]"%perso), ("%s_C_SpineUpFK_ctrlShape.cv[3]"%perso), r=True, os=True, wd=True)
        # parentage
        cmds.parent(("%s_C_SpineUpFK_ctrl"%perso), ("%s_C_SpineMidFK_ctrl"%perso))
        cmds.parent(("%s_C_SpineMidFK_ctrl"%perso), ("%s_C_COG_ctrl"%perso))
        # ctrl IK
        # spineLow
        cmds.curve(d=True, p=[(-3, 0, -3), (-3, 0, 3), (3, 0, 3), (3, 0, -3), (-3, 0, -3)], n=("%s_C_SpineLowIK_ctrl"%perso))
        cmds.scale((.85 * scale[0]), (.85 * scale[0]), (.85 * scale[0]), ("%s_C_SpineLowIK_ctrl"%perso))
        cmds.makeIdentity(("%s_C_SpineLowIK_ctrl"%perso), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_C_SpineLowIK_ctrl"%perso), ch=True)
        cmds.group(("%s_C_SpineLowIK_ctrl"%perso), n=("%s_C_SpineLowIK_grp"%perso))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%root), ("%s_C_SpineLowIK_grp"%perso), sr=["x", "y", "z"]))
        # spineMid
        cmds.curve(d=True, p=[(-3, 0, -3), (-3, 0, 3), (3, 0, 3), (3, 0, -3), (-3, 0, -3)], n=("%s_C_SpineMidIK_ctrl"%perso))
        cmds.scale((.65 * scale[0]), (.65 * scale[0]), (.65 * scale[0]), ("%s_C_SpineMidIK_ctrl"%perso))
        cmds.makeIdentity(("%s_C_SpineMidIK_ctrl"%perso), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_C_SpineMidIK_ctrl"%perso), ch=True)
        cmds.group(("%s_C_SpineMidIK_ctrl"%perso), n=("%s_C_SpineMidIK_grp"%perso))
        cmds.delete(cmds.parentConstraint((lesClusters[2]), ("%s_C_SpineMidIK_grp"%perso), sr=["x", "y", "z"]))
        # spineUp
        cmds.curve(d=True, p=[(-3, 0, -3), (-3, 0, 3), (3, 0, 3), (3, 0, -3), (-3, 0, -3)], n=("%s_C_SpineUpIK_ctrl"%perso))
        cmds.scale((.75 * scale[0]), (.75 * scale[0]), (.75 * scale[0]), ("%s_C_SpineUpIK_ctrl"%perso))
        cmds.makeIdentity(("%s_C_SpineUpIK_ctrl"%perso), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_C_SpineUpIK_ctrl"%perso), ch=True)
        cmds.group(("%s_C_SpineUpIK_ctrl"%perso), n=("%s_C_SpineUpIK_grp"%perso))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%spine08), ("%s_C_SpineUpIK_grp"%perso), sr=["x", "y", "z"]))
        # freeze
        cmds.makeIdentity(("%s_C_SpineUpIK_grp"%perso), a=True, t=True, r=True, s=True, n=False)
        cmds.makeIdentity(("%s_C_SpineLowIK_grp"%perso), a=True, t=True, r=True, s=True, n=False)
        cmds.makeIdentity(("%s_C_SpineMidIK_grp"%perso), a=True, t=True, r=True, s=True, n=False)
        # parentage
        cmds.parentConstraint(("%s_C_COG_ctrl"%perso), ("%s_C_SpineLowIK_grp"%perso), n=("%s_C_COG_constrainte"%perso))
        cmds.parentConstraint(("%s_C_SpineMidFK_ctrl"%perso), ("%s_C_SpineMidIK_grp"%perso), n=("%s_C_SpineMidFK_constrainte"%perso))
        cmds.parentConstraint(("%s_C_SpineUpFK_ctrl"%perso), ("%s_C_SpineUpIK_grp"%perso), n=("%s_C_SpineUpFK_constrainte"%perso))
        cmds.parentConstraint(("%s_C_SpineLowIK_ctrl"%perso), ("%s_C_Spine_Transform_grp"%perso), n=("%s_C_SpineLowIK_constrainte"%perso))
        cmds.parent(lesClusters[0], lesClusters[1], ("%s_C_SpineLowIK_ctrl"%perso))
        cmds.parent(lesClusters[2], ("%s_C_SpineMidIK_ctrl"%perso))
        cmds.parent(lesClusters[3], lesClusters[4], ("%s_C_SpineUpIK_ctrl"%perso))
        for i in range(0, len(lesClusters)):
            cmds.setAttr(("%sCluster.relative"%lesClusters[i]), 0)
        # pelvis
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=(2.75 * scale[0]), s=8, n=("%s_ctrl"%pelvis))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%pelvis), ("%s_ctrl"%pelvis), sr=["x", "y", "z"]))
        cmds.makeIdentity(("%s_ctrl"%pelvis), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%pelvis), ch=True)
        cmds.move(0, (-.4 * scale[0]), 0, ("%s_ctrlShape.cv[7]"%pelvis), ("%s_ctrlShape.cv[3]"%pelvis), r=True, os=True, wd=True)
        cmds.parentConstraint(("%s_ctrl"%pelvis), ("%s_jnt"%pelvis), n=("%s_constrainte"%pelvis), mo=True)
        cmds.parent(("%s_ctrl"%pelvis), ("%s_C_COG_ctrl"%perso))
        colorize("C", [("%s_ctrl"%pelvis), ("%s_C_COG_ctrl"%perso), ("%s_C_SpineMidFK_ctrl"%perso), ("%s_C_SpineUpFK_ctrl"%perso), ("%s_C_SpineLowIK_ctrl"%perso), ("%s_C_SpineMidIK_ctrl"%perso), ("%s_C_SpineUpIK_ctrl"%perso)])
        # lockAndHide
        lockAndHide(["%s_C_COG_ctrl"%perso], True, True, ["sx", "sy", "sz", "v"])
        lockAndHide(["%s_ctrl"%pelvis], True, True, ["tx", "ty", "tz", "sx", "sy", "sz", "v"])
        # spineIK twiste
        cmds.shadingNode("plusMinusAverage", n=("%s_C_PMAvg01_twist"%perso), au=True)
        cmds.connectAttr(("%s_C_SpineMidFK_ctrl.rotateY"%perso), ("%s_C_PMAvg01_twist.input1D[0]"%perso), f=True)
        cmds.connectAttr(("%s_C_SpineMidIK_ctrl.rotateY"%perso), ("%s_C_PMAvg01_twist.input1D[1]"%perso), f=True)
        cmds.shadingNode("plusMinusAverage", n=("%s_C_PMAvg02_twist"%perso), au=True)
        cmds.connectAttr(("%s_C_PMAvg01_twist.output1D"%perso), ("%s_C_PMAvg02_twist.input1D[0]"%perso), f=True)
        cmds.connectAttr(("%s_C_SpineUpFK_ctrl.rotateY"%perso), ("%s_C_PMAvg02_twist.input1D[1]"%perso), f=True)
        cmds.shadingNode("plusMinusAverage", n=("%s_C_PMAvg03_twist"%perso), au=True)
        cmds.connectAttr(("%s_C_PMAvg02_twist.output1D"%perso), ("%s_C_PMAvg03_twist.input1D[0]"%perso), f=True)
        cmds.connectAttr(("%s_C_SpineUpIK_ctrl.rotateY"%perso), ("%s_C_PMAvg03_twist.input1D[1]"%perso), f=True)
        cmds.connectAttr(("%s_C_PMAvg03_twist.output1D"%perso), ("%s_C_Spine_ikhl.twist"%perso), f=True)
        # spineIK stretch
        cmds.arclen(("%s_C_Spine_crv"%perso), ch=True)
        curveInfo = cmds.listConnections(("%s_C_Spine_crvShape"%perso), s=False)
        curveLength = cmds.getAttr("%s.arcLength"%curveInfo[0])
        cmds.shadingNode("condition", n="%s_C_SpineStretch_cnd"%perso, au=True)
        cmds.setAttr(("%s_C_SpineStretch_cnd.operation"%perso), 2)
        cmds.connectAttr(("%s.arcLength"%curveInfo[0]), ("%s_C_SpineStretch_cnd.firstTerm"%perso))
        cmds.setAttr(("%s_C_SpineStretch_cnd.secondTerm"%perso), curveLength)
        cmds.shadingNode("multiplyDivide", n="%s_C_SpineStretch_md"%perso, au=True)
        cmds.setAttr(("%s_C_SpineStretch_md.operation"%perso), 2)
        cmds.connectAttr(("%s.arcLength"%curveInfo[0]), ("%s_C_SpineStretch_md.input1X"%perso))
        cmds.setAttr(("%s_C_SpineStretch_md.input2X"%perso), curveLength)
        cmds.connectAttr(("%s_C_SpineStretch_md.outputX"%perso), ("%s_C_SpineStretch_cnd.colorIfTrueR"%perso))
        cmds.setAttr(("%s_C_SpineStretch_cnd.colorIfFalseR"%perso), 1)
        cmds.connectAttr(("%s_C_SpineStretch_cnd.outColorR"%perso), ("%s_jnt.scaleX"%root))
        for spine in spines:
            cmds.connectAttr(("%s_C_SpineStretch_cnd.outColorR"%perso), ("%s_jnt.scaleX"%spine))
    # end def spineIK

    # def spineFK
    def spineFK(self, perso):
        # variables
        scale = cmds.xform(("%s_Scale_ctrl"%perso), q=True, r=True, s=True)
        root = ("%s_C_Root"%perso)
        middle = ("%s_C_Middle"%perso)
        chest = ("%s_C_Chest"%perso)
        pelvis = ("%s_C_Pelvis"%perso)
        cmds.parent(("%s_jnt"%middle), w=True)
        cmds.parent(("%s_jnt"%chest), w=True)
        # ctrl
        # root
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=(3.5 * scale[0]), s=8, n=("%s_ctrl"%root))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%root), ("%s_ctrl"%root), sr=["x", "y", "z"]))
        cmds.makeIdentity(("%s_ctrl"%root), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%root), ch=True)
        cmds.move(0, (-1.5 * scale[0]), 0, ("%s_ctrlShape.cv[7]"%root), ("%s_ctrlShape.cv[3]"%root), r=True, os=True, wd=True)
        # middle
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=(2.55 * scale[0]), s=8, n=("%s_ctrl"%middle))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%middle), ("%s_ctrl"%middle), sr=["x", "y", "z"]))
        cmds.makeIdentity(("%s_ctrl"%middle), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%middle), ch=True)
        # chest
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=(3 * scale[0]), s=8, n=("%s_ctrl"%chest))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%chest), ("%s_ctrl"%chest), sr=["x", "y", "z"]))
        cmds.makeIdentity(("%s_ctrl"%chest), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%chest), ch=True)
        cmds.move(0, (.6 * scale[0]), 0, ("%s_ctrlShape.cv[7]"%chest), ("%s_ctrlShape.cv[3]"%chest), r=True, os=True, wd=True)
        # pelvis
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=(2.75 * scale[0]), s=8, n=("%s_ctrl"%pelvis))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%pelvis), ("%s_ctrl"%pelvis), sr=["x", "y", "z"]))
        cmds.makeIdentity(("%s_ctrl"%pelvis), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%pelvis), ch=True)
        cmds.move(0, (-.4 * scale[0]), 0, ("%s_ctrlShape.cv[7]"%pelvis), ("%s_ctrlShape.cv[3]"%pelvis), r=True, os=True, wd=True)
        tr = cmds.xform(("%s_jnt"%pelvis), q=True, t=True)
        cmds.move(tr[0], tr[1], tr[2], ("%s_ctrl.scalePivot"%pelvis), ("%s_ctrl.rotatePivot"%pelvis))
        cmds.parent(("%s_jnt"%pelvis), ("%s_jnt"%root))
        colorize("C", [("%s_ctrl"%root), ("%s_ctrl"%middle), ("%s_ctrl"%chest), ("%s_ctrl"%pelvis)])
        # parentage
        cmds.parent(("%s_ctrl"%chest), ("%s_ctrl"%middle))
        cmds.parent(("%s_ctrl"%middle), ("%s_ctrl"%root))
        cmds.parent(("%s_ctrl"%pelvis), ("%s_ctrl"%root))
        # contrainte
        cmds.parentConstraint(("%s_ctrl"%chest), ("%s_jnt"%chest), n=("%s_contrainte"%chest), mo=True)
        cmds.parentConstraint(("%s_ctrl"%root), ("%s_jnt"%root), n=("%s_contrainte"%root), mo=True)
        cmds.parentConstraint(("%s_ctrl"%pelvis), ("%s_jnt"%pelvis), n=("%s_contrainte"%pelvis), mo=True)
        # middle
        cmds.group(("%s_jnt"%middle), n=("%s_UpAvg_grp"%middle))
        tr = cmds.xform(("%s_jnt"%middle), q=True, t=True)
        cmds.move(tr[0], tr[1], tr[2], ("%s_UpAvg_grp.scalePivot"%middle), ("%s_UpAvg_grp.rotatePivot"%middle))
        cmds.group(("%s_UpAvg_grp"%middle), n=("%s_LowAvg_grp"%middle))
        cmds.move(tr[0], tr[1], tr[2], ("%s_LowAvg_grp.scalePivot"%middle), ("%s_LowAvg_grp.rotatePivot"%middle))
        cmds.group(("%s_LowAvg_grp"%middle), n=("%s_grp"%middle))
        cmds.move(tr[0], tr[1], tr[2], ("%s_grp.scalePivot"%middle), ("%s_grp.rotatePivot"%middle))
        cmds.parentConstraint(("%s_ctrl"%middle), ("%s_grp"%middle), n=("%s_contrainte"%middle), mo=True)
        # middle auto rotation
        cmds.shadingNode("multiplyDivide", n=("%s_Up_MD"%middle), au=True)
        cmds.connectAttr(("%s_ctrl.rotateY"%chest), ("%s_Up_MD.input1X"%middle), f=True)
        cmds.connectAttr(("%s_Up_MD.outputX"%middle), ("%s_UpAvg_grp.rotateY"%middle), f=True)
        cmds.setAttr(("%s_Up_MD.input2X"%middle), .5)
        cmds.shadingNode("multiplyDivide", n=("%s_Low_MD"%middle), au=True)
        cmds.connectAttr(("%s_ctrl.rotateY"%pelvis), ("%s_Low_MD.input1X"%middle), f=True)
        cmds.connectAttr(("%s_Low_MD.outputX"%middle), ("%s_LowAvg_grp.rotateY"%middle), f=True)
        cmds.setAttr(("%s_Low_MD.input2X"%middle), .5)
        # clean scene
        lockAndHide([("%s_ctrl"%root), ("%s_ctrl"%middle), ("%s_ctrl"%chest)], True, True, ["sx", "sy", "sz", "v"])
        lockAndHide([("%s_ctrl"%pelvis)], True, True, ["sx", "sy", "sz", "tx", "ty", "tz", "v"])
    # end spineFK
    
    # def spineRibbon
    def spineRibbon(self, perso):
        # variables
        scale = cmds.xform(("%s_Scale_ctrl"%perso), q=True, r=True, s=True)
        root = "%s_C_Root"%perso
        spineJnt = "%s_C_Spine_RibbnDriver_mid_jnt"%perso
        spineCtrl = "%s_C_Spine_ctrl"%perso
        spineContrainte = "%s_C_Spine_contrainte"%perso
        chest = "%s_C_Chest"%perso
        spineOffCtrl = "%s_C_SpineOff_ctrl"%perso
        spineOffGrp = "%s_C_SpineOff_grp"%perso
        spineLoc = "%s_C_Spine_RibbnOffset_mid_loc"%perso
        pelvis = "%s_C_Pelvis"%perso
        # ctrl
        # root
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=(3.5 * scale[0]), s=8, n=("%s_ctrl"%root))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%root), ("%s_ctrl"%root), sr=["x", "y", "z"]))
        cmds.makeIdentity(("%s_ctrl"%root), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%root), ch=True)
        cmds.move(0, (-1.5 * scale[0]), 0, ("%s_ctrlShape.cv[7]"%root), ("%s_ctrlShape.cv[3]"%root), r=True, os=True, wd=True)
        # spine
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=(2.85 * scale[0]), s=8, n=spineCtrl)
        cmds.delete(cmds.parentConstraint(spineJnt, spineCtrl, sr=["x", "y", "z"]))
        cmds.makeIdentity(spineCtrl, a=True, t=True, r=True, s=True, n=False)
        cmds.delete(spineCtrl, ch=True)
        cmds.scale(.62, .62, .62, ("%sShape.cv[0]"%spineCtrl), ("%sShape.cv[2]"%spineCtrl), ("%sShape.cv[4]"%spineCtrl), ("%sShape.cv[6]"%spineCtrl), r=True)
        cmds.scale(1.52, 1, 1, "%sShape.cv[0:7]"%spineCtrl, r=True)
        # chest
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=(3 * scale[0]), s=8, n=("%s_ctrl"%chest))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%chest), ("%s_ctrl"%chest), sr=["x", "y", "z"]))
        cmds.makeIdentity(("%s_ctrl"%chest), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%chest), ch=True)
        cmds.move(0, (.6 * scale[0]), 0, ("%s_ctrlShape.cv[7]"%chest), ("%s_ctrlShape.cv[3]"%chest), r=True, os=True, wd=True)
        # pelvis
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=(2.75 * scale[0]), s=8, n=("%s_ctrl"%pelvis))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%pelvis), ("%s_ctrl"%pelvis), sr=["x", "y", "z"]))
        cmds.makeIdentity(("%s_ctrl"%pelvis), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%pelvis), ch=True)
        cmds.move(0, (-.4 * scale[0]), 0, ("%s_ctrlShape.cv[7]"%pelvis), ("%s_ctrlShape.cv[3]"%pelvis), r=True, os=True, wd=True)
        # parentage
        cmds.parent(("%s_ctrl"%chest), spineCtrl)
        cmds.parent(spineCtrl, ("%s_ctrl"%root))
        cmds.parent(("%s_ctrl"%pelvis), ("%s_ctrl"%root))
        # spineOff
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=(2.55 * scale[0]), s=8, n=spineOffCtrl)
        cmds.group(spineOffCtrl, n=spineOffGrp)
        cmds.delete(cmds.parentConstraint(spineJnt, spineOffGrp, sr=["x", "y", "z"]))
        cmds.parent(spineOffGrp, spineLoc)
        cmds.parent(spineJnt, spineOffCtrl)
        cmds.scale(.73, .73, .73, ("%sShape.cv[0]"%spineOffCtrl), ("%sShape.cv[2]"%spineOffCtrl), ("%sShape.cv[4]"%spineOffCtrl), ("%sShape.cv[6]"%spineOffCtrl), r=True)
        # contraintes
        cmds.parentConstraint(("%s_ctrl"%root), ("%s_jnt"%root), n=("%s_contrainte"%root), mo=True)
        cmds.parentConstraint(("%s_ctrl"%chest), ("%s_jnt"%chest), n=("%s_contrainte"%chest), mo=True)
        cmds.pointConstraint(spineCtrl, spineOffGrp, n=spineContrainte)
        cmds.parentConstraint(("%s_ctrl"%pelvis), ("%s_jnt"%pelvis), n=("%s_contrainte"%pelvis), mo=True)
        # clean scene
        colorize("C", [("%s_ctrl"%root), ("%s_ctrl"%chest), spineCtrl, spineOffCtrl])
        lockAndHide([("%s_ctrl"%root), ("%s_ctrl"%chest), spineCtrl, spineOffCtrl], True, True, ["sx", "sy", "sz", "v"])
        lockAndHide([("%s_ctrl"%pelvis)], True, True, ["sx", "sy", "sz", "tx", "ty", "tz", "v"])
    # end def spineRibbon

    # def headIK
    def headIK(self, perso, spine):
        # variables
        scale = cmds.xform(("%s_Scale_ctrl"%perso), q=True, r=True, s=True)
        neck = ("%s_C_Neck"%perso)
        head = ("%s_C_Head"%perso)
        lEye = ("%s_L_Eye"%perso)
        rEye = ("%s_R_Eye"%perso)
        eyes = ("%s_C_Eyes"%perso)
        if spine == "FK":
            cmds.parent(("%s_jnt"%head), ("%s_jnt"%neck))
        # ctrls
        # head
        cmds.hide(cmds.ikHandle(sj=("%s_jnt"%neck), ee=("%s_jnt"%head), sol="ikSCsolver", n=("%s_ikhl"%neck)))
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=1.2, s=8, n=("%s_ctrl"%head))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%head), ("%s_ctrl"%head), sr=["x", "y", "z"]))
        cmds.move(0, 3, 0, ("%s_ctrlShape.cv[1]"%head), ("%s_ctrlShape.cv[5]"%head), r=True, os=True, wd=True)
        cmds.scale(.1, ("%s_ctrlShape.cv[1]"%head), ("%s_ctrlShape.cv[5]"%head), z=True, r=True, os=True)
        cmds.move(0, -1, 0, ("%s_ctrlShape.cv[7]"%head), ("%s_ctrlShape.cv[3]"%head), r=True, os=True, wd=True)
        cmds.move(0, 1.7, 0, ("%s_ctrlShape.cv[0]"%head), ("%s_ctrlShape.cv[2]"%head), ("%s_ctrlShape.cv[4]"%head), ("%s_ctrlShape.cv[6]"%head), r=True, os=True, wd=True)
        cmds.scale(1.7, ("%s_ctrlShape.cv[0]"%head), ("%s_ctrlShape.cv[2]"%head), ("%s_ctrlShape.cv[4]"%head), ("%s_ctrlShape.cv[6]"%head), x=True, r=True, os=True)
        cmds.scale(scale[0], scale[0], scale[0], ("%s_ctrl"%head))
        cmds.makeIdentity(("%s_ctrl"%head), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%head), ch=True)
        cmds.pointConstraint(("%s_ctrl"%head), ("%s_ikhl"%neck), n=("%s_p_contrainte"%head))
        # L eye
        cmds.circle(c=(0, 0, 0), nr=(0, 0, 1), r=(.3 * scale[0]), s=8, n=("%s_ctrl"%lEye))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%lEye), ("%s_ctrl"%lEye)))
        cmds.move((3 * scale[0]), ("%s_ctrl"%lEye), z=True, r=True, os=True, wd=True)
        cmds.makeIdentity(("%s_ctrl"%lEye), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%lEye), ch=True)
        colorize("L", ["%s_ctrl"%lEye])
        # R eye
        cmds.circle(c=(0, 0, 0), nr=(0, 0, 1), r=(.3 * scale[0]), s=8, n=("%s_ctrl"%rEye))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%rEye), ("%s_ctrl"%rEye)))
        cmds.move((3 * scale[0]), ("%s_ctrl"%rEye), z=True, r=True, os=True, wd=True)
        cmds.makeIdentity(("%s_ctrl"%rEye), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%rEye), ch=True)
        colorize("R", ["%s_ctrl"%rEye])
        # eyes
        cmds.circle(c=(0, 0, 0), nr=(0, 0, 1), r=(.8 * scale[0]), s=8, n=("%s_ctrl"%eyes))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%rEye), ("%s_ctrl"%eyes)))
        cmds.move((3 * scale[0]), ("%s_ctrl"%eyes), z=True, r=True, os=True, wd=True)
        cmds.move(0, ("%s_ctrl"%eyes), x=True, ws=True, a=True)
        cmds.makeIdentity(("%s_ctrl"%eyes), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%eyes), ch=True)
        colorize("C", [("%s_ctrl"%eyes), ("%s_ctrl"%head)])
        cmds.parent(("%s_ctrl"%lEye), ("%s_ctrl"%eyes))
        cmds.parent(("%s_ctrl"%rEye), ("%s_ctrl"%eyes))
        cmds.group(("%s_ctrl"%eyes), n=("%s_grp"%eyes))
        tr = cmds.xform(("%s_jnt"%head), q=True, t=True)
        cmds.move(tr[0], tr[1], tr[2], ("%s_grp.scalePivot"%eyes), ("%s_grp.rotatePivot"%eyes))
        cmds.parent(("%s_grp"%eyes), ("%s_ctrl"%head))
        cmds.orientConstraint(("%s_ctrl"%head), ("%s_jnt"%head), mo=True, n=("%s_o_contrainte"%head))
        cmds.aimConstraint(("%s_ctrl"%lEye), ("%s_jnt"%lEye), aim=[0, 0, 1], u=[0, 1, 0], wu=[0, 1, 0], n=("%s_contrainte"%lEye))
        cmds.aimConstraint(("%s_ctrl"%rEye), ("%s_jnt"%rEye), aim=[0, 0, 1], u=[0, 1, 0], wu=[0, 1, 0], n=("%s_contrainte"%rEye))
        # clean scene
        lockAndHide(["%s_ctrl"%head], True, True, ["sx", "sy", "sz", "v"])
        lockAndHide([("%s_ctrl"%eyes), ("%s_ctrl"%lEye), ("%s_ctrl"%rEye)], True, True, ["rx", "ry", "rz", "sx", "sy", "sz", "v"])
    # end def headIK

    # def headFK
    def headFK(self, perso, spine):
        # variables
        scale = cmds.xform(("%s_Scale_ctrl"%perso), q=True, r=True, s=True)
        neck = ("%s_C_Neck"%perso)
        head = ("%s_C_Head"%perso)
        lEye = ("%s_L_Eye"%perso)
        rEye = ("%s_R_Eye"%perso)
        eyes = ("%s_C_Eyes"%perso)
        if spine == "FK":
            cmds.parent(("%s_jnt"%head), ("%s_jnt"%neck))
        # ctrls
        # neck
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=1.5, s=8, n=("%s_ctrl"%neck))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%neck), ("%s_ctrl"%neck), sr=["x", "y", "z"]))
        cmds.move(0, .5, 0, ("%s_ctrlShape.cv[3]"%neck), ("%s_ctrlShape.cv[7]"%neck), r=True, os=True, wd=True)
        cmds.move(0, -.5, 0, ("%s_ctrlShape.cv[1]"%neck), ("%s_ctrlShape.cv[5]"%neck), r=True, os=True, wd=True)
        cmds.scale(scale[0], scale[0], scale[0], ("%s_ctrl"%neck), r=True, os=True)
        cmds.makeIdentity(("%s_ctrl"%neck), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%neck), ch=True)
        cmds.orientConstraint(("%s_ctrl"%neck), ("%s_jnt"%neck), mo=True, n=("%s_contrainte"%neck))
        # head
        cmds.circle(c=(0, 0, 0), nr=(0, 1, 0), r=1.2, s=8, n=("%s_ctrl"%head))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%head), ("%s_ctrl"%head), sr=["x", "y", "z"]))
        cmds.move(0, 3, 0, ("%s_ctrlShape.cv[1]"%head), ("%s_ctrlShape.cv[5]"%head), r=True, os=True, wd=True)
        cmds.scale(.1, ("%s_ctrlShape.cv[1]"%head), ("%s_ctrlShape.cv[5]"%head), z=True, r=True, os=True)
        cmds.move(0, -1, 0, ("%s_ctrlShape.cv[7]"%head), ("%s_ctrlShape.cv[3]"%head), r=True, os=True, wd=True)
        cmds.move(0, 1.7, 0, ("%s_ctrlShape.cv[0]"%head), ("%s_ctrlShape.cv[2]"%head), ("%s_ctrlShape.cv[4]"%head), ("%s_ctrlShape.cv[6]"%head), r=True, os=True, wd=True)
        cmds.scale(1.7, ("%s_ctrlShape.cv[0]"%head), ("%s_ctrlShape.cv[2]"%head), ("%s_ctrlShape.cv[4]"%head), ("%s_ctrlShape.cv[6]"%head), x=True, r=True, os=True)
        cmds.scale(scale[0], scale[0], scale[0], ("%s_ctrl"%head))
        cmds.makeIdentity(("%s_ctrl"%head), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%head), ch=True)
        # L eye
        cmds.circle(c=(0, 0, 0), nr=(0, 0, 1), r=(.3 * scale[0]), s=8, n=("%s_ctrl"%lEye))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%lEye), ("%s_ctrl"%lEye)))
        cmds.move((3 * scale[0]), ("%s_ctrl"%lEye), z=True, r=True, os=True, wd=True)
        cmds.makeIdentity(("%s_ctrl"%lEye), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%lEye), ch=True)
        colorize("L", ["%s_ctrl"%lEye])
        # R eye
        cmds.circle(c=(0, 0, 0), nr=(0, 0, 1), r=(.3 * scale[0]), s=8, n=("%s_ctrl"%rEye))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%rEye), ("%s_ctrl"%rEye)))
        cmds.move((3 * scale[0]), ("%s_ctrl"%rEye), z=True, r=True, os=True, wd=True)
        cmds.makeIdentity(("%s_ctrl"%rEye), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%rEye), ch=True)
        colorize("R", ["%s_ctrl"%rEye])
        # eyes
        cmds.circle(c=(0, 0, 0), nr=(0, 0, 1), r=(.8 * scale[0]), s=8, n=("%s_ctrl"%eyes))
        cmds.delete(cmds.parentConstraint(("%s_jnt"%rEye), ("%s_ctrl"%eyes)))
        cmds.move((3 * scale[0]), ("%s_ctrl"%eyes), z=True, r=True, os=True, wd=True)
        cmds.move(0, ("%s_ctrl"%eyes), x=True, ws=True, a=True)
        cmds.makeIdentity(("%s_ctrl"%eyes), a=True, t=True, r=True, s=True, n=False)
        cmds.delete(("%s_ctrl"%eyes), ch=True)
        colorize("C", [("%s_ctrl"%eyes), ("%s_ctrl"%head), ("%s_ctrl"%neck)])
        cmds.parent(("%s_ctrl"%lEye), ("%s_ctrl"%eyes))
        cmds.parent(("%s_ctrl"%rEye), ("%s_ctrl"%eyes))
        cmds.parent(("%s_ctrl"%head), ("%s_ctrl"%neck))
        cmds.group(("%s_ctrl"%eyes), n=("%s_grp"%eyes))
        tr = cmds.xform(("%s_jnt"%head), q=True, t=True)
        cmds.move(tr[0], tr[1], tr[2], ("%s_grp.scalePivot"%eyes), ("%s_grp.rotatePivot"%eyes))
        cmds.parent(("%s_grp"%eyes), ("%s_ctrl"%head))
        cmds.orientConstraint(("%s_ctrl"%head), ("%s_jnt"%head), mo=True, n=("%s_o_contrainte"%head))
        cmds.aimConstraint(("%s_ctrl"%lEye), ("%s_jnt"%lEye), aim=[0, 0, 1], u=[0, 1, 0], wu=[0, 1, 0], n=("%s_contrainte"%lEye))
        cmds.aimConstraint(("%s_ctrl"%rEye), ("%s_jnt"%rEye), aim=[0, 0, 1], u=[0, 1, 0], wu=[0, 1, 0], n=("%s_contrainte"%rEye))
        # clean scene
        lockAndHide([("%s_ctrl"%head), ("%s_ctrl"%lEye), ("%s_ctrl"%rEye), ("%s_ctrl"%eyes)], True, True, ["rx", "ry", "rz", "sx", "sy", "sz", "v"])
    # end def headFK
    
    # def stretchArm
    def stretchArm(self, perso, cotes):
        for cote in cotes:
            # variable
            shoulder = "%s_%s_ShoulderIK_jnt"%(perso, cote)
            elbow = "%s_%s_ElbowIK_jnt"%(perso, cote)
            foreArm = "%s_%s_ForeArmIK_jnt"%(perso, cote)
            wrist = "%s_%s_WristIK_jnt"%(perso, cote)
            wristCtrl = "%s_%s_ArmIK_ctrl"%(perso, cote)
            # attr
            cmds.addAttr(wristCtrl, k=True, h=False, ln="Arm", at="enum", en="-----:")
            cmds.addAttr(wristCtrl, k=True, h=False, ln="Scale", at="double", min=0, max=10, dv=0)
            cmds.addAttr(wristCtrl, k=True, h=False, ln="Stretch", at="double", min=0, max=10, dv=0)
            # locators
            cmds.hide(cmds.spaceLocator(n="%s_%s_Shoulder_loc"%(perso, cote)))
            cmds.hide(cmds.spaceLocator(n="%s_%s_Elbow_loc"%(perso, cote)))
            cmds.hide(cmds.spaceLocator(n="%s_%s_Wrist_loc"%(perso, cote)))
            cmds.hide(cmds.spaceLocator(n="%s_%s_Wrist_ctrl_loc"%(perso, cote)))
            cmds.delete(cmds.parentConstraint(shoulder, "%s_%s_Shoulder_loc"%(perso, cote)))
            cmds.delete(cmds.parentConstraint(elbow, "%s_%s_Elbow_loc"%(perso, cote)))
            cmds.delete(cmds.parentConstraint(wrist, "%s_%s_Wrist_loc"%(perso, cote)))
            cmds.delete(cmds.parentConstraint(wrist, "%s_%s_Wrist_ctrl_loc"%(perso, cote)))
            # parentage
            cmds.parent("%s_%s_Shoulder_loc"%(perso, cote), shoulder)
            cmds.parent("%s_%s_Elbow_loc"%(perso, cote), elbow)
            cmds.parent("%s_%s_Wrist_loc"%(perso, cote), wrist)
            cmds.parent("%s_%s_Wrist_ctrl_loc"%(perso, cote), wristCtrl)
            # distanceTool
            se_dt = cmds.distanceDimension("%s_%s_Shoulder_loc"%(perso, cote), "%s_%s_Elbow_loc"%(perso, cote))
            ew_dt = cmds.distanceDimension("%s_%s_Elbow_loc"%(perso, cote), "%s_%s_Wrist_loc"%(perso, cote))
            sw_dt = cmds.distanceDimension("%s_%s_Shoulder_loc"%(perso, cote), "%s_%s_Wrist_ctrl_loc"%(perso, cote))
            # renommage
            dt = se_dt[:se_dt.rfind("Shape")]
            num = se_dt[se_dt.rfind("Shape")+5:]
            cmds.rename("%s%s"%(dt, num), "%s_%s_ShoulderElbow_dt"%(perso, cote))
            se_dt = "%s_%s_ShoulderElbow_dtShape"%(perso, cote)
            dt = ew_dt[:ew_dt.rfind("Shape")]
            num = ew_dt[ew_dt.rfind("Shape")+5:]
            cmds.rename("%s%s"%(dt, num), "%s_%s_ElbowWrist_dt"%(perso, cote))
            ew_dt = "%s_%s_ElbowWrist_dtShape"%(perso, cote)
            dt = sw_dt[:sw_dt.rfind("Shape")]
            num = sw_dt[sw_dt.rfind("Shape")+5:]
            cmds.rename("%s%s"%(dt, num), "%s_%s_ShoulderWrist_dt"%(perso, cote))
            sw_dt = "%s_%s_ShoulderWrist_dtShape"%(perso, cote)
            # grouage et hidage
            cmds.hide(cmds.group("%s_%s_ShoulderElbow_dt"%(perso, cote), "%s_%s_ElbowWrist_dt"%(perso, cote), "%s_%s_ShoulderWrist_dt"%(perso, cote), n="%s_%s_ArmMeasureTools_grp"%(perso, cote)))
            cmds.parent("%s_%s_ArmMeasureTools_grp"%(perso, cote), "%s_XTRAS"%perso)
            # distance original * scale
            cmds.shadingNode("multiplyDivide", n="%s_%s_se_d_scale_MD"%(perso, cote), au=True)
            cmds.connectAttr("%s_C_Ultimate_ctrl.scaleX"%perso, "%s_%s_se_d_scale_MD.input1X"%(perso, cote), f=True)
            se_d = cmds.getAttr("%s.distance"%se_dt)
            cmds.setAttr("%s_%s_se_d_scale_MD.input2X"%(perso, cote), se_d)
            cmds.shadingNode("multiplyDivide", n="%s_%s_ew_d_scale_MD"%(perso, cote), au=True)
            cmds.connectAttr("%s_C_Ultimate_ctrl.scaleX"%perso, "%s_%s_ew_d_scale_MD.input1X"%(perso, cote), f=True)
            ew_d = cmds.getAttr("%s.distance"%ew_dt)
            cmds.setAttr("%s_%s_ew_d_scale_MD.input2X"%(perso, cote), ew_d)
            # armLength
            cmds.shadingNode("plusMinusAverage", n="%s_%s_armLength_PMA"%(perso, cote), au=True)
            cmds.connectAttr("%s_%s_se_d_scale_MD.outputX"%(perso, cote), "%s_%s_armLength_PMA.input1D[0]"%(perso, cote), f=True)
            cmds.connectAttr("%s_%s_ew_d_scale_MD.outputX"%(perso, cote), "%s_%s_armLength_PMA.input1D[1]"%(perso, cote), f=True)
            # si dist ctrl > armLength
            cmds.shadingNode("condition", n="%s_%s_armLength_gt_sw_d_COND"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_armLength_gt_sw_d_COND.operation"%(perso, cote), 2)
            cmds.connectAttr("%s.distance"%sw_dt, "%s_%s_armLength_gt_sw_d_COND.firstTerm"%(perso, cote))
            cmds.connectAttr("%s_%s_armLength_PMA.output1D"%(perso, cote), "%s_%s_armLength_gt_sw_d_COND.secondTerm"%(perso, cote))
            # scale
            cmds.shadingNode("multiplyDivide", n="%s_%s_armScale_MD"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_armScale_MD.operation"%(perso, cote), 2)
            cmds.connectAttr("%s.distance"%sw_dt, "%s_%s_armScale_MD.input1X"%(perso, cote))
            cmds.connectAttr("%s_%s_armLength_PMA.output1D"%(perso, cote), "%s_%s_armScale_MD.input2X"%(perso, cote))
            # reglage joint Scale
            cmds.shadingNode("multiplyDivide", n="%s_%s_armScaleReg01_MD"%(perso, cote), au=True)
            cmds.connectAttr("%s.Scale"%wristCtrl, "%s_%s_armScaleReg01_MD.input1X"%(perso, cote))
            cmds.connectAttr("%s_%s_armScale_MD.outputX"%(perso, cote), "%s_%s_armScaleReg01_MD.input2X"%(perso, cote))
            
            cmds.shadingNode("plusMinusAverage", n="%s_%s_armScaleReg02_PMA"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_armScaleReg02_PMA.operation"%(perso, cote), 2)
            cmds.setAttr("%s_%s_armScaleReg02_PMA.input1D[0]"%(perso, cote), 10)
            cmds.connectAttr("%s.Scale"%wristCtrl, "%s_%s_armScaleReg02_PMA.input1D[1]"%(perso, cote))
            
            cmds.shadingNode("plusMinusAverage", n="%s_%s_armScaleReg03_PMA"%(perso, cote), au=True)
            cmds.connectAttr("%s_%s_armScaleReg01_MD.outputX"%(perso, cote), "%s_%s_armScaleReg03_PMA.input1D[0]"%(perso, cote))
            cmds.connectAttr("%s_%s_armScaleReg02_PMA.output1D"%(perso, cote), "%s_%s_armScaleReg03_PMA.input1D[1]"%(perso, cote))
            
            cmds.shadingNode("multiplyDivide", n="%s_%s_armScaleReg04_MD"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_armScaleReg04_MD.operation"%(perso, cote), 2)
            cmds.connectAttr("%s_%s_armScaleReg03_PMA.output1D"%(perso, cote), "%s_%s_armScaleReg04_MD.input1X"%(perso, cote))
            cmds.setAttr("%s_%s_armScaleReg04_MD.input2X"%(perso, cote), 10)
            cmds.connectAttr("%s_%s_armScaleReg04_MD.outputX"%(perso, cote), "%s_%s_armLength_gt_sw_d_COND.colorIfTrueR"%(perso, cote), f=True)
            # joint scale
            cmds.connectAttr("%s_%s_armLength_gt_sw_d_COND.outColorR"%(perso, cote), "%s.scaleX"%shoulder)
            cmds.connectAttr("%s_%s_armLength_gt_sw_d_COND.outColorR"%(perso, cote), "%s.scaleX"%elbow)
            cmds.connectAttr("%s_%s_armLength_gt_sw_d_COND.outColorR"%(perso, cote), "%s.scaleX"%foreArm)
            # si new dist > old dist
            cmds.shadingNode("condition", n="%s_%s_new_gt_old_COND"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_new_gt_old_COND.operation"%(perso, cote), 2)
            cmds.connectAttr("%s.distance"%sw_dt, "%s_%s_new_gt_old_COND.firstTerm"%(perso, cote))
            cmds.connectAttr("%s_%s_armLength_PMA.output1D"%(perso, cote), "%s_%s_new_gt_old_COND.secondTerm"%(perso, cote))
            cmds.connectAttr("%s_%s_armScale_MD.outputX"%(perso, cote), "%s_%s_new_gt_old_COND.colorIfTrueR"%(perso, cote), f=True)
            # Racine
            cmds.shadingNode("multiplyDivide", n="%s_%s_racine_MD"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_racine_MD.operation"%(perso, cote), 3)
            cmds.setAttr("%s_%s_racine_MD.input2X"%(perso, cote), .5)
            cmds.connectAttr("%s_%s_new_gt_old_COND.outColorR"%(perso, cote), "%s_%s_racine_MD.input1X"%(perso, cote), f=True)
            # Stretch
            cmds.shadingNode("multiplyDivide", n="%s_%s_stretch_MD"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_stretch_MD.operation"%(perso, cote), 2)
            cmds.setAttr("%s_%s_stretch_MD.input1X"%(perso, cote), 1)
            cmds.connectAttr("%s_%s_racine_MD.outputX"%(perso, cote), "%s_%s_stretch_MD.input2X"%(perso, cote))
            # reglage Stretch
            cmds.shadingNode("multiplyDivide", n="%s_%s_armStretchReg01_MD"%(perso, cote), au=True)
            cmds.connectAttr("%s.Stretch"%wristCtrl, "%s_%s_armStretchReg01_MD.input1X"%(perso, cote))
            cmds.connectAttr("%s_%s_stretch_MD.outputX"%(perso, cote), "%s_%s_armStretchReg01_MD.input2X"%(perso, cote))
            
            cmds.shadingNode("plusMinusAverage", n="%s_%s_armStretchReg02_PMA"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_armStretchReg02_PMA.operation"%(perso, cote), 2)
            cmds.setAttr("%s_%s_armStretchReg02_PMA.input1D[0]"%(perso, cote), 10)
            cmds.connectAttr("%s.Stretch"%wristCtrl, "%s_%s_armStretchReg02_PMA.input1D[1]"%(perso, cote))
            
            cmds.shadingNode("plusMinusAverage", n="%s_%s_armStretchReg03_PMA"%(perso, cote), au=True)
            cmds.connectAttr("%s_%s_armStretchReg01_MD.outputX"%(perso, cote), "%s_%s_armStretchReg03_PMA.input1D[0]"%(perso, cote))
            cmds.connectAttr("%s_%s_armStretchReg02_PMA.output1D"%(perso, cote), "%s_%s_armStretchReg03_PMA.input1D[1]"%(perso, cote))
            
            cmds.shadingNode("multiplyDivide", n="%s_%s_armStretchReg04_MD"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_armStretchReg04_MD.operation"%(perso, cote), 2)
            cmds.connectAttr("%s_%s_armStretchReg03_PMA.output1D"%(perso, cote), "%s_%s_armStretchReg04_MD.input1X"%(perso, cote))
            cmds.setAttr("%s_%s_armStretchReg04_MD.input2X"%(perso, cote), 10)
            
            cmds.shadingNode("multiplyDivide", n="%s_%s_armStretchReg05_MD"%(perso, cote), au=True)
            cmds.connectAttr("%s.Scale"%wristCtrl, "%s_%s_armStretchReg05_MD.input1X"%(perso, cote))
            cmds.connectAttr("%s_%s_armStretchReg04_MD.outputX"%(perso, cote), "%s_%s_armStretchReg05_MD.input2X"%(perso, cote))
            
            cmds.shadingNode("plusMinusAverage", n="%s_%s_armStretchReg06_PMA"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_armStretchReg06_PMA.operation"%(perso, cote), 2)
            cmds.setAttr("%s_%s_armStretchReg06_PMA.input1D[0]"%(perso, cote), 10)
            cmds.connectAttr("%s.Scale"%wristCtrl, "%s_%s_armStretchReg06_PMA.input1D[1]"%(perso, cote))
            
            cmds.shadingNode("plusMinusAverage", n="%s_%s_armStretchReg07_PMA"%(perso, cote), au=True)
            cmds.connectAttr("%s_%s_armStretchReg05_MD.outputX"%(perso, cote), "%s_%s_armStretchReg07_PMA.input1D[0]"%(perso, cote))
            cmds.connectAttr("%s_%s_armStretchReg06_PMA.output1D"%(perso, cote), "%s_%s_armStretchReg07_PMA.input1D[1]"%(perso, cote))
            
            cmds.shadingNode("multiplyDivide", n="%s_%s_armStretchReg08_MD"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_armStretchReg08_MD.operation"%(perso, cote), 2)
            cmds.connectAttr("%s_%s_armStretchReg07_PMA.output1D"%(perso, cote), "%s_%s_armStretchReg08_MD.input1X"%(perso, cote))
            cmds.setAttr("%s_%s_armStretchReg08_MD.input2X"%(perso, cote), 10)
            # extreme joints
            cmds.connectAttr("%s_%s_armStretchReg08_MD.outputX"%(perso, cote), "%s_%s_UpperArm_Ribbn01_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_armStretchReg08_MD.outputX"%(perso, cote), "%s_%s_UpperArm_Ribbn01_jnt.scaleZ"%(perso, cote))
            cmds.connectAttr("%s_%s_armStretchReg08_MD.outputX"%(perso, cote), "%s_%s_LowerArm_Ribbn05_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_armStretchReg08_MD.outputX"%(perso, cote), "%s_%s_LowerArm_Ribbn05_jnt.scaleZ"%(perso, cote))
            # puissances
            for i in range(2,5):
                cmds.shadingNode("multiplyDivide", n="%s_%s_puissance%i_MD"%(perso, cote, i), au=True)
                cmds.setAttr("%s_%s_puissance%i_MD.operation"%(perso, cote, i), 3)
                cmds.setAttr("%s_%s_puissance%i_MD.input2X"%(perso, cote, i), i)
                cmds.connectAttr("%s_%s_armStretchReg08_MD.outputX"%(perso, cote), "%s_%s_puissance%i_MD.input1X"%(perso, cote, i), f=True)
            # others joints
            cmds.connectAttr("%s_%s_puissance2_MD.outputX"%(perso, cote), "%s_%s_UpperArm_Ribbn02_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_puissance2_MD.outputX"%(perso, cote), "%s_%s_UpperArm_Ribbn02_jnt.scaleZ"%(perso, cote))
            cmds.connectAttr("%s_%s_puissance2_MD.outputX"%(perso, cote), "%s_%s_LowerArm_Ribbn04_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_puissance2_MD.outputX"%(perso, cote), "%s_%s_LowerArm_Ribbn04_jnt.scaleZ"%(perso, cote))
            
            cmds.connectAttr("%s_%s_puissance3_MD.outputX"%(perso, cote), "%s_%s_UpperArm_Ribbn03_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_puissance3_MD.outputX"%(perso, cote), "%s_%s_UpperArm_Ribbn03_jnt.scaleZ"%(perso, cote))
            cmds.connectAttr("%s_%s_puissance3_MD.outputX"%(perso, cote), "%s_%s_LowerArm_Ribbn03_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_puissance3_MD.outputX"%(perso, cote), "%s_%s_LowerArm_Ribbn03_jnt.scaleZ"%(perso, cote))
            cmds.connectAttr("%s_%s_puissance3_MD.outputX"%(perso, cote), "%s_%s_UpperArm_Ribbn05_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_puissance3_MD.outputX"%(perso, cote), "%s_%s_UpperArm_Ribbn05_jnt.scaleZ"%(perso, cote))
            cmds.connectAttr("%s_%s_puissance3_MD.outputX"%(perso, cote), "%s_%s_LowerArm_Ribbn01_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_puissance3_MD.outputX"%(perso, cote), "%s_%s_LowerArm_Ribbn01_jnt.scaleZ"%(perso, cote))
            
            cmds.connectAttr("%s_%s_puissance4_MD.outputX"%(perso, cote), "%s_%s_UpperArm_Ribbn04_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_puissance4_MD.outputX"%(perso, cote), "%s_%s_UpperArm_Ribbn04_jnt.scaleZ"%(perso, cote))
            cmds.connectAttr("%s_%s_puissance4_MD.outputX"%(perso, cote), "%s_%s_LowerArm_Ribbn02_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_puissance4_MD.outputX"%(perso, cote), "%s_%s_LowerArm_Ribbn02_jnt.scaleZ"%(perso, cote))
    # end def stretchArm

    # def stretchLeg
    def stretchLeg(self, perso, cotes):
        for cote in cotes:
            # variable
            leg = "%s_%s_LegIK_jnt"%(perso, cote)
            knee = "%s_%s_KneeIK_jnt"%(perso, cote)
            ankle = "%s_%s_AnkleIK_jnt"%(perso, cote)
            ankleCtrl = "%s_%s_Foot_ctrl"%(perso, cote)
            # attr
            cmds.addAttr(ankleCtrl, k=True, h=False, ln="Leg", at="enum", en="-----:")
            cmds.addAttr(ankleCtrl, k=True, h=False, ln="Scale", at="double", min=0, max=10, dv=0)
            cmds.addAttr(ankleCtrl, k=True, h=False, ln="Stretch", at="double", min=0, max=10, dv=0)
            # locators
            cmds.hide(cmds.spaceLocator(n="%s_%s_Leg_loc"%(perso, cote)))
            cmds.hide(cmds.spaceLocator(n="%s_%s_Knee_loc"%(perso, cote)))
            cmds.hide(cmds.spaceLocator(n="%s_%s_Ankle_loc"%(perso, cote)))
            cmds.hide(cmds.spaceLocator(n="%s_%s_Ankle_ctrl_loc"%(perso, cote)))
            cmds.delete(cmds.parentConstraint(leg, "%s_%s_Leg_loc"%(perso, cote)))
            cmds.delete(cmds.parentConstraint(knee, "%s_%s_Knee_loc"%(perso, cote)))
            cmds.delete(cmds.parentConstraint(ankle, "%s_%s_Ankle_loc"%(perso, cote)))
            cmds.delete(cmds.parentConstraint(ankle, "%s_%s_Ankle_ctrl_loc"%(perso, cote)))
            # parentage
            cmds.parent("%s_%s_Leg_loc"%(perso, cote), leg)
            cmds.parent("%s_%s_Knee_loc"%(perso, cote), knee)
            cmds.parent("%s_%s_Ankle_loc"%(perso, cote), ankle)
            cmds.parent("%s_%s_Ankle_ctrl_loc"%(perso, cote), ankleCtrl)
            # distanceTool
            lk_dt = cmds.distanceDimension("%s_%s_Leg_loc"%(perso, cote), "%s_%s_Knee_loc"%(perso, cote))
            ka_dt = cmds.distanceDimension("%s_%s_Knee_loc"%(perso, cote), "%s_%s_Ankle_loc"%(perso, cote))
            la_dt = cmds.distanceDimension("%s_%s_Leg_loc"%(perso, cote), "%s_%s_Ankle_ctrl_loc"%(perso, cote))
            # renommage
            dt = lk_dt[:lk_dt.rfind("Shape")]
            num = lk_dt[lk_dt.rfind("Shape")+5:]
            cmds.rename("%s%s"%(dt, num), "%s_%s_LegKnee_dt"%(perso, cote))
            lk_dt = "%s_%s_LegKnee_dtShape"%(perso, cote)
            dt = ka_dt[:ka_dt.rfind("Shape")]
            num = ka_dt[ka_dt.rfind("Shape")+5:]
            cmds.rename("%s%s"%(dt, num), "%s_%s_KneeAnkle_dt"%(perso, cote))
            ka_dt = "%s_%s_KneeAnkle_dtShape"%(perso, cote)
            dt = la_dt[:la_dt.rfind("Shape")]
            num = la_dt[la_dt.rfind("Shape")+5:]
            cmds.rename("%s%s"%(dt, num), "%s_%s_LegAnkle_dt"%(perso, cote))
            la_dt = "%s_%s_LegAnkle_dtShape"%(perso, cote)
            # grouage et hidage
            cmds.hide(cmds.group("%s_%s_LegKnee_dt"%(perso, cote), "%s_%s_KneeAnkle_dt"%(perso, cote), "%s_%s_LegAnkle_dt"%(perso, cote), n="%s_%s_LegMeasureTools_grp"%(perso, cote)))
            cmds.parent("%s_%s_LegMeasureTools_grp"%(perso, cote), "%s_XTRAS"%perso)
            # distance original * scale
            cmds.shadingNode("multiplyDivide", n="%s_%s_lk_d_scale_MD"%(perso, cote), au=True)
            cmds.connectAttr("%s_C_Ultimate_ctrl.scaleX"%perso, "%s_%s_lk_d_scale_MD.input1X"%(perso, cote), f=True)
            lk_d = cmds.getAttr("%s.distance"%lk_dt)
            cmds.setAttr("%s_%s_lk_d_scale_MD.input2X"%(perso, cote), lk_d)
            cmds.shadingNode("multiplyDivide", n="%s_%s_ka_d_scale_MD"%(perso, cote), au=True)
            cmds.connectAttr("%s_C_Ultimate_ctrl.scaleX"%perso, "%s_%s_ka_d_scale_MD.input1X"%(perso, cote), f=True)
            ka_d = cmds.getAttr("%s.distance"%ka_dt)
            cmds.setAttr("%s_%s_ka_d_scale_MD.input2X"%(perso, cote), ka_d)
            # legLength
            cmds.shadingNode("plusMinusAverage", n="%s_%s_legLength_PMA"%(perso, cote), au=True)
            cmds.connectAttr("%s_%s_lk_d_scale_MD.outputX"%(perso, cote), "%s_%s_legLength_PMA.input1D[0]"%(perso, cote), f=True)
            cmds.connectAttr("%s_%s_ka_d_scale_MD.outputX"%(perso, cote), "%s_%s_legLength_PMA.input1D[1]"%(perso, cote), f=True)
            # si dist ctrl > legLength
            cmds.shadingNode("condition", n="%s_%s_legLength_gt_la_d_COND"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_legLength_gt_la_d_COND.operation"%(perso, cote), 2)
            cmds.connectAttr("%s.distance"%la_dt, "%s_%s_legLength_gt_la_d_COND.firstTerm"%(perso, cote))
            cmds.connectAttr("%s_%s_legLength_PMA.output1D"%(perso, cote), "%s_%s_legLength_gt_la_d_COND.secondTerm"%(perso, cote))
            # scale
            cmds.shadingNode("multiplyDivide", n="%s_%s_legScale_MD"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_legScale_MD.operation"%(perso, cote), 2)
            cmds.connectAttr("%s.distance"%la_dt, "%s_%s_legScale_MD.input1X"%(perso, cote))
            cmds.connectAttr("%s_%s_legLength_PMA.output1D"%(perso, cote), "%s_%s_legScale_MD.input2X"%(perso, cote))
            # reglage joint Scale
            cmds.shadingNode("multiplyDivide", n="%s_%s_legScaleReg01_MD"%(perso, cote), au=True)
            cmds.connectAttr("%s.Scale"%ankleCtrl, "%s_%s_legScaleReg01_MD.input1X"%(perso, cote))
            cmds.connectAttr("%s_%s_legScale_MD.outputX"%(perso, cote), "%s_%s_legScaleReg01_MD.input2X"%(perso, cote))
            
            cmds.shadingNode("plusMinusAverage", n="%s_%s_legScaleReg02_PMA"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_legScaleReg02_PMA.operation"%(perso, cote), 2)
            cmds.setAttr("%s_%s_legScaleReg02_PMA.input1D[0]"%(perso, cote), 10)
            cmds.connectAttr("%s.Scale"%ankleCtrl, "%s_%s_legScaleReg02_PMA.input1D[1]"%(perso, cote))
            
            cmds.shadingNode("plusMinusAverage", n="%s_%s_legScaleReg03_PMA"%(perso, cote), au=True)
            cmds.connectAttr("%s_%s_legScaleReg01_MD.outputX"%(perso, cote), "%s_%s_legScaleReg03_PMA.input1D[0]"%(perso, cote))
            cmds.connectAttr("%s_%s_legScaleReg02_PMA.output1D"%(perso, cote), "%s_%s_legScaleReg03_PMA.input1D[1]"%(perso, cote))
            
            cmds.shadingNode("multiplyDivide", n="%s_%s_legScaleReg04_MD"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_legScaleReg04_MD.operation"%(perso, cote), 2)
            cmds.connectAttr("%s_%s_legScaleReg03_PMA.output1D"%(perso, cote), "%s_%s_legScaleReg04_MD.input1X"%(perso, cote))
            cmds.setAttr("%s_%s_legScaleReg04_MD.input2X"%(perso, cote), 10)
            cmds.connectAttr("%s_%s_legScaleReg04_MD.outputX"%(perso, cote), "%s_%s_legLength_gt_la_d_COND.colorIfTrueR"%(perso, cote), f=True)
            # joint scale
            cmds.connectAttr("%s_%s_legLength_gt_la_d_COND.outColorR"%(perso, cote), "%s.scaleX"%leg)
            cmds.connectAttr("%s_%s_legLength_gt_la_d_COND.outColorR"%(perso, cote), "%s.scaleX"%knee)
            # si new dist > old dist
            cmds.shadingNode("condition", n="%s_%s_legnew_gt_old_COND"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_legnew_gt_old_COND.operation"%(perso, cote), 2)
            cmds.connectAttr("%s.distance"%la_dt, "%s_%s_legnew_gt_old_COND.firstTerm"%(perso, cote))
            cmds.connectAttr("%s_%s_legLength_PMA.output1D"%(perso, cote), "%s_%s_legnew_gt_old_COND.secondTerm"%(perso, cote))
            cmds.connectAttr("%s_%s_legScale_MD.outputX"%(perso, cote), "%s_%s_legnew_gt_old_COND.colorIfTrueR"%(perso, cote), f=True)
            # Racine
            cmds.shadingNode("multiplyDivide", n="%s_%s_legracine_MD"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_legracine_MD.operation"%(perso, cote), 3)
            cmds.setAttr("%s_%s_legracine_MD.input2X"%(perso, cote), .5)
            cmds.connectAttr("%s_%s_legnew_gt_old_COND.outColorR"%(perso, cote), "%s_%s_legracine_MD.input1X"%(perso, cote), f=True)
            # Stretch
            cmds.shadingNode("multiplyDivide", n="%s_%s_legstretch_MD"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_legstretch_MD.operation"%(perso, cote), 2)
            cmds.setAttr("%s_%s_legstretch_MD.input1X"%(perso, cote), 1)
            cmds.connectAttr("%s_%s_legracine_MD.outputX"%(perso, cote), "%s_%s_legstretch_MD.input2X"%(perso, cote))
            # reglage Stretch
            cmds.shadingNode("multiplyDivide", n="%s_%s_legStretchReg01_MD"%(perso, cote), au=True)
            cmds.connectAttr("%s.Stretch"%ankleCtrl, "%s_%s_legStretchReg01_MD.input1X"%(perso, cote))
            cmds.connectAttr("%s_%s_legstretch_MD.outputX"%(perso, cote), "%s_%s_legStretchReg01_MD.input2X"%(perso, cote))
            
            cmds.shadingNode("plusMinusAverage", n="%s_%s_legStretchReg02_PMA"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_legStretchReg02_PMA.operation"%(perso, cote), 2)
            cmds.setAttr("%s_%s_legStretchReg02_PMA.input1D[0]"%(perso, cote), 10)
            cmds.connectAttr("%s.Stretch"%ankleCtrl, "%s_%s_legStretchReg02_PMA.input1D[1]"%(perso, cote))
            
            cmds.shadingNode("plusMinusAverage", n="%s_%s_legStretchReg03_PMA"%(perso, cote), au=True)
            cmds.connectAttr("%s_%s_legStretchReg01_MD.outputX"%(perso, cote), "%s_%s_legStretchReg03_PMA.input1D[0]"%(perso, cote))
            cmds.connectAttr("%s_%s_legStretchReg02_PMA.output1D"%(perso, cote), "%s_%s_legStretchReg03_PMA.input1D[1]"%(perso, cote))
            
            cmds.shadingNode("multiplyDivide", n="%s_%s_legStretchReg04_MD"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_legStretchReg04_MD.operation"%(perso, cote), 2)
            cmds.connectAttr("%s_%s_legStretchReg03_PMA.output1D"%(perso, cote), "%s_%s_legStretchReg04_MD.input1X"%(perso, cote))
            cmds.setAttr("%s_%s_legStretchReg04_MD.input2X"%(perso, cote), 10)
            
            cmds.shadingNode("multiplyDivide", n="%s_%s_legStretchReg05_MD"%(perso, cote), au=True)
            cmds.connectAttr("%s.Scale"%ankleCtrl, "%s_%s_legStretchReg05_MD.input1X"%(perso, cote))
            cmds.connectAttr("%s_%s_legStretchReg04_MD.outputX"%(perso, cote), "%s_%s_legStretchReg05_MD.input2X"%(perso, cote))
            
            cmds.shadingNode("plusMinusAverage", n="%s_%s_legStretchReg06_PMA"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_legStretchReg06_PMA.operation"%(perso, cote), 2)
            cmds.setAttr("%s_%s_legStretchReg06_PMA.input1D[0]"%(perso, cote), 10)
            cmds.connectAttr("%s.Scale"%ankleCtrl, "%s_%s_legStretchReg06_PMA.input1D[1]"%(perso, cote))
            
            cmds.shadingNode("plusMinusAverage", n="%s_%s_legStretchReg07_PMA"%(perso, cote), au=True)
            cmds.connectAttr("%s_%s_legStretchReg05_MD.outputX"%(perso, cote), "%s_%s_legStretchReg07_PMA.input1D[0]"%(perso, cote))
            cmds.connectAttr("%s_%s_legStretchReg06_PMA.output1D"%(perso, cote), "%s_%s_legStretchReg07_PMA.input1D[1]"%(perso, cote))
            
            cmds.shadingNode("multiplyDivide", n="%s_%s_legStretchReg08_MD"%(perso, cote), au=True)
            cmds.setAttr("%s_%s_legStretchReg08_MD.operation"%(perso, cote), 2)
            cmds.connectAttr("%s_%s_legStretchReg07_PMA.output1D"%(perso, cote), "%s_%s_legStretchReg08_MD.input1X"%(perso, cote))
            cmds.setAttr("%s_%s_legStretchReg08_MD.input2X"%(perso, cote), 10)
            # extreme joints
            cmds.connectAttr("%s_%s_legStretchReg08_MD.outputX"%(perso, cote), "%s_%s_UpperLeg_Ribbn01_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_legStretchReg08_MD.outputX"%(perso, cote), "%s_%s_UpperLeg_Ribbn01_jnt.scaleZ"%(perso, cote))
            cmds.connectAttr("%s_%s_legStretchReg08_MD.outputX"%(perso, cote), "%s_%s_LowerLeg_Ribbn05_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_legStretchReg08_MD.outputX"%(perso, cote), "%s_%s_LowerLeg_Ribbn05_jnt.scaleZ"%(perso, cote))
            # puissances
            for i in range(2,5):
                cmds.shadingNode("multiplyDivide", n="%s_%s_legpuissance%i_MD"%(perso, cote, i), au=True)
                cmds.setAttr("%s_%s_legpuissance%i_MD.operation"%(perso, cote, i), 3)
                cmds.setAttr("%s_%s_legpuissance%i_MD.input2X"%(perso, cote, i), i)
                cmds.connectAttr("%s_%s_legStretchReg08_MD.outputX"%(perso, cote), "%s_%s_legpuissance%i_MD.input1X"%(perso, cote, i), f=True)
            # others joints
            cmds.connectAttr("%s_%s_legpuissance2_MD.outputX"%(perso, cote), "%s_%s_UpperLeg_Ribbn02_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_legpuissance2_MD.outputX"%(perso, cote), "%s_%s_UpperLeg_Ribbn02_jnt.scaleZ"%(perso, cote))
            cmds.connectAttr("%s_%s_legpuissance2_MD.outputX"%(perso, cote), "%s_%s_LowerLeg_Ribbn04_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_legpuissance2_MD.outputX"%(perso, cote), "%s_%s_LowerLeg_Ribbn04_jnt.scaleZ"%(perso, cote))
            
            cmds.connectAttr("%s_%s_legpuissance3_MD.outputX"%(perso, cote), "%s_%s_UpperLeg_Ribbn03_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_legpuissance3_MD.outputX"%(perso, cote), "%s_%s_UpperLeg_Ribbn03_jnt.scaleZ"%(perso, cote))
            cmds.connectAttr("%s_%s_legpuissance3_MD.outputX"%(perso, cote), "%s_%s_LowerLeg_Ribbn03_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_legpuissance3_MD.outputX"%(perso, cote), "%s_%s_LowerLeg_Ribbn03_jnt.scaleZ"%(perso, cote))
            cmds.connectAttr("%s_%s_legpuissance3_MD.outputX"%(perso, cote), "%s_%s_UpperLeg_Ribbn05_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_legpuissance3_MD.outputX"%(perso, cote), "%s_%s_UpperLeg_Ribbn05_jnt.scaleZ"%(perso, cote))
            cmds.connectAttr("%s_%s_legpuissance3_MD.outputX"%(perso, cote), "%s_%s_LowerLeg_Ribbn01_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_legpuissance3_MD.outputX"%(perso, cote), "%s_%s_LowerLeg_Ribbn01_jnt.scaleZ"%(perso, cote))
            
            cmds.connectAttr("%s_%s_legpuissance4_MD.outputX"%(perso, cote), "%s_%s_UpperLeg_Ribbn04_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_legpuissance4_MD.outputX"%(perso, cote), "%s_%s_UpperLeg_Ribbn04_jnt.scaleZ"%(perso, cote))
            cmds.connectAttr("%s_%s_legpuissance4_MD.outputX"%(perso, cote), "%s_%s_LowerLeg_Ribbn02_jnt.scaleY"%(perso, cote))
            cmds.connectAttr("%s_%s_legpuissance4_MD.outputX"%(perso, cote), "%s_%s_LowerLeg_Ribbn02_jnt.scaleZ"%(perso, cote))
    # end def stretchLeg
    
    # def stretchSpine
    def stretchSpine(self, perso):
        # variable
        root = "%s_C_Root_jnt"%perso
        chest = "%s_C_Chest_jnt"%perso
        ctrlStretch = "%s_C_Chest_ctrl"%perso
        # attr
        cmds.addAttr(ctrlStretch, k=True, h=False, ln="Spine", at="enum", en="-----:")
        cmds.addAttr(ctrlStretch, k=True, h=False, ln="Stretch", at="double", min=0, max=10, dv=0)
        # locators
        cmds.hide(cmds.spaceLocator(n="%s_C_Root_loc"%perso))
        cmds.hide(cmds.spaceLocator(n="%s_C_Chest_loc"%perso))
        cmds.delete(cmds.parentConstraint(root, "%s_C_Root_loc"%perso))
        cmds.delete(cmds.parentConstraint(chest, "%s_C_Chest_loc"%perso))
        # parentage
        cmds.parent("%s_C_Root_loc"%perso, root)
        cmds.parent("%s_C_Chest_loc"%perso, chest)
        # distanceTool
        rc_dt = cmds.distanceDimension("%s_C_Root_loc"%perso, "%s_C_Chest_loc"%perso)
        # renommage
        dt = rc_dt[:rc_dt.rfind("Shape")]
        num = rc_dt[rc_dt.rfind("Shape")+5:]
        cmds.rename("%s%s"%(dt, num), "%s_C_RootChest_dt"%perso)
        rc_dt = "%s_C_RootChest_dtShape"%perso
        # grouage et hidage
        cmds.hide(cmds.group("%s_C_RootChest_dt"%perso, n="%s_C_SpineMeasureTools_grp"%perso))
        cmds.parent("%s_C_SpineMeasureTools_grp"%perso, "%s_XTRAS"%perso)
        # distance original * scale
        cmds.shadingNode("multiplyDivide", n="%s_C_rc_d_scale_MD"%perso, au=True)
        cmds.connectAttr("%s_C_Ultimate_ctrl.scaleX"%perso, "%s_C_rc_d_scale_MD.input1X"%perso, f=True)
        rc_d = cmds.getAttr("%s.distance"%rc_dt)
        cmds.setAttr("%s_C_rc_d_scale_MD.input2X"%perso, rc_d)
        # si dist ctrl > spineLength
        cmds.shadingNode("condition", n="%s_C_spinLength_gt_cr_d_COND"%perso, au=True)
        cmds.setAttr("%s_C_spinLength_gt_cr_d_COND.operation"%perso, 2)
        cmds.connectAttr("%s.distance"%rc_dt, "%s_C_spinLength_gt_cr_d_COND.firstTerm"%perso)
        cmds.connectAttr("%s_C_rc_d_scale_MD.outputX"%perso, "%s_C_spinLength_gt_cr_d_COND.secondTerm"%perso)
        # scale
        cmds.shadingNode("multiplyDivide", n="%s_C_spineScale_MD"%perso, au=True)
        cmds.setAttr("%s_C_spineScale_MD.operation"%perso, 2)
        cmds.connectAttr("%s.distance"%rc_dt, "%s_C_spineScale_MD.input1X"%perso)
        cmds.connectAttr("%s_C_rc_d_scale_MD.outputX"%perso, "%s_C_spineScale_MD.input2X"%perso)
        cmds.connectAttr("%s_C_spineScale_MD.outputX"%perso, "%s_C_spinLength_gt_cr_d_COND.colorIfTrueR"%perso, f=True)
        # Racine
        cmds.shadingNode("multiplyDivide", n="%s_C_spineracine_MD"%perso, au=True)
        cmds.setAttr("%s_C_spineracine_MD.operation"%perso, 3)
        cmds.setAttr("%s_C_spineracine_MD.input2X"%perso, .5)
        cmds.connectAttr("%s_C_spinLength_gt_cr_d_COND.outColorR"%perso, "%s_C_spineracine_MD.input1X"%perso, f=True)
        # Stretch
        cmds.shadingNode("multiplyDivide", n="%s_C_spinestretch_MD"%perso, au=True)
        cmds.setAttr("%s_C_spinestretch_MD.operation"%perso, 2)
        cmds.setAttr("%s_C_spinestretch_MD.input1X"%perso, 1)
        cmds.connectAttr("%s_C_spineracine_MD.outputX"%perso, "%s_C_spinestretch_MD.input2X"%perso)
        # reglage Stretch
        cmds.shadingNode("multiplyDivide", n="%s_C_spineStretchReg01_MD"%perso, au=True)
        cmds.connectAttr("%s.Stretch"%ctrlStretch, "%s_C_spineStretchReg01_MD.input1X"%perso)
        cmds.connectAttr("%s_C_spinestretch_MD.outputX"%perso, "%s_C_spineStretchReg01_MD.input2X"%perso)
        
        cmds.shadingNode("plusMinusAverage", n="%s_C_spineStretchReg02_PMA"%perso, au=True)
        cmds.setAttr("%s_C_spineStretchReg02_PMA.operation"%perso, 2)
        cmds.setAttr("%s_C_spineStretchReg02_PMA.input1D[0]"%perso, 10)
        cmds.connectAttr("%s.Stretch"%ctrlStretch, "%s_C_spineStretchReg02_PMA.input1D[1]"%perso)
        
        cmds.shadingNode("plusMinusAverage", n="%s_C_spineStretchReg03_PMA"%perso, au=True)
        cmds.connectAttr("%s_C_spineStretchReg01_MD.outputX"%perso, "%s_C_spineStretchReg03_PMA.input1D[0]"%perso)
        cmds.connectAttr("%s_C_spineStretchReg02_PMA.output1D"%perso, "%s_C_spineStretchReg03_PMA.input1D[1]"%perso)
        
        cmds.shadingNode("multiplyDivide", n="%s_C_spineStretchReg04_MD"%perso, au=True)
        cmds.setAttr("%s_C_spineStretchReg04_MD.operation"%perso, 2)
        cmds.connectAttr("%s_C_spineStretchReg03_PMA.output1D"%perso, "%s_C_spineStretchReg04_MD.input1X"%perso)
        cmds.setAttr("%s_C_spineStretchReg04_MD.input2X"%perso, 10)
        # extreme joints
        cmds.connectAttr("%s_C_spineStretchReg04_MD.outputX"%perso, "%s_C_Spine_Ribbn01_jnt.scaleY"%perso)
        cmds.connectAttr("%s_C_spineStretchReg04_MD.outputX"%perso, "%s_C_Spine_Ribbn01_jnt.scaleZ"%perso)
        cmds.connectAttr("%s_C_spineStretchReg04_MD.outputX"%perso, "%s_C_Spine_Ribbn05_jnt.scaleY"%perso)
        cmds.connectAttr("%s_C_spineStretchReg04_MD.outputX"%perso, "%s_C_Spine_Ribbn05_jnt.scaleZ"%perso)
        # puissances
        for i in range(2,4):
            cmds.shadingNode("multiplyDivide", n="%s_C_spinepuissance%i_MD"%(perso, i), au=True)
            cmds.setAttr("%s_C_spinepuissance%i_MD.operation"%(perso, i), 3)
            cmds.setAttr("%s_C_spinepuissance%i_MD.input2X"%(perso, i), i)
            cmds.connectAttr("%s_C_spineStretchReg04_MD.outputX"%perso, "%s_C_spinepuissance%i_MD.input1X"%(perso, i), f=True)
        # others joints
        cmds.connectAttr("%s_C_spinepuissance2_MD.outputX"%perso, "%s_C_Spine_Ribbn02_jnt.scaleY"%perso)
        cmds.connectAttr("%s_C_spinepuissance2_MD.outputX"%perso, "%s_C_Spine_Ribbn02_jnt.scaleZ"%perso)
        cmds.connectAttr("%s_C_spinepuissance2_MD.outputX"%perso, "%s_C_Spine_Ribbn04_jnt.scaleY"%perso)
        cmds.connectAttr("%s_C_spinepuissance2_MD.outputX"%perso, "%s_C_Spine_Ribbn04_jnt.scaleZ"%perso)
        
        cmds.connectAttr("%s_C_spinepuissance3_MD.outputX"%perso, "%s_C_Spine_Ribbn03_jnt.scaleY"%perso)
        cmds.connectAttr("%s_C_spinepuissance3_MD.outputX"%perso, "%s_C_Spine_Ribbn03_jnt.scaleZ"%perso)
    # end def stretchSpine

    # def jointsSet
    def jointsSet(self, perso, IKleg, FKleg, RibbonLeg, IKarm, FKarm, RibbonArm, head, spine):
        bones = []
        if IKleg and FKleg:
            if not RibbonLeg:
                bones.extend([("%s_L_Leg_jnt"%perso), ("%s_R_Leg_jnt"%perso), ("%s_L_Knee_jnt"%perso), ("%s_R_Knee_jnt"%perso), ("%s_L_Ankle_jnt"%perso), ("%s_R_Ankle_jnt"%perso), ("%s_L_Ball_jnt"%perso), ("%s_R_Ball_jnt"%perso)])
            else:
                bones.extend([("%s_L_Ankle_jnt"%perso), ("%s_R_Ankle_jnt"%perso), ("%s_L_Ball_jnt"%perso), ("%s_R_Ball_jnt"%perso)])
        elif IKleg:
            if not RibbonLeg:
                bones.extend([("%s_L_LegIK_jnt"%perso), ("%s_R_LegIK_jnt"%perso), ("%s_L_KneeIK_jnt"%perso), ("%s_R_KneeIK_jnt"%perso), ("%s_L_AnkleIK_jnt"%perso), ("%s_R_AnkleIK_jnt"%perso), ("%s_L_BallIK_jnt"%perso), ("%s_R_BallIK_jnt"%perso)])
            else:
                bones.extend([("%s_L_AnkleIK_jnt"%perso), ("%s_R_AnkleIK_jnt"%perso), ("%s_L_BallIK_jnt"%perso), ("%s_R_BallIK_jnt"%perso)])
        elif FKleg:
            if not RibbonLeg:
                bones.extend([("%s_L_LegFK_jnt"%perso), ("%s_R_LegFK_jnt"%perso), ("%s_L_KneeFK_jnt"%perso), ("%s_R_KneeFK_jnt"%perso), ("%s_L_AnkleFK_jnt"%perso), ("%s_R_AnkleFK_jnt"%perso), ("%s_L_BallFK_jnt"%perso), ("%s_R_BallFK_jnt"%perso)])
            else:
                bones.extend([("%s_L_AnkleFK_jnt"%perso), ("%s_R_AnkleFK_jnt"%perso), ("%s_L_BallFK_jnt"%perso), ("%s_R_BallFK_jnt"%perso)])
        if RibbonLeg:
            cs = ["L_UpperLeg", "R_UpperLeg", "L_LowerLeg", "R_LowerLeg"]
            for c in cs:
                for i in range(1, 6):
                    bones.extend(["%s_%s_Ribbn0%i_jnt"%(perso, c, i)])
        if IKarm and FKarm:
            if not RibbonArm:
                bones.extend([("%s_L_Clavicle_jnt"%perso), ("%s_R_Clavicle_jnt"%perso), ("%s_L_Shoulder_jnt"%perso), ("%s_R_Shoulder_jnt"%perso), ("%s_L_Elbow_jnt"%perso), ("%s_R_Elbow_jnt"%perso), ("%s_L_ForeArm_jnt"%perso), ("%s_R_ForeArm_jnt"%perso), ("%s_L_Wrist_jnt"%perso), ("%s_R_Wrist_jnt"%perso)])
            else:
                bones.extend([("%s_L_Wrist_jnt"%perso), ("%s_R_Wrist_jnt"%perso)])
        elif IKarm:
            if not RibbonArm:
                bones.extend([("%s_L_Clavicle_jnt"%perso), ("%s_R_Clavicle_jnt"%perso), ("%s_L_ShoulderIK_jnt"%perso), ("%s_R_ShoulderIK_jnt"%perso), ("%s_L_ElbowIK_jnt"%perso), ("%s_R_ElbowIK_jnt"%perso), ("%s_L_ForeArmIK_jnt"%perso), ("%s_R_ForeArmIK_jnt"%perso), ("%s_L_WristIK_jnt"%perso), ("%s_R_WristIK_jnt"%perso)])
            else:
                bones.extend([("%s_L_WristIK_jnt"%perso), ("%s_R_WristIK_jnt"%perso)])
        elif FKarm:
            if not RibbonArm:
                bones.extend([("%s_L_Clavicle_jnt"%perso), ("%s_R_Clavicle_jnt"%perso), ("%s_L_ShoulderFK_jnt"%perso), ("%s_R_ShoulderFK_jnt"%perso), ("%s_L_ElbowFK_jnt"%perso), ("%s_R_ElbowFK_jnt"%perso), ("%s_L_ForeArmFK_jnt"%perso), ("%s_R_ForeArmFK_jnt"%perso), ("%s_L_WristFK_jnt"%perso), ("%s_R_WristFK_jnt"%perso)])
            else:
                bones.extend([("%s_L_WristFK_jnt"%perso), ("%s_R_WristFK_jnt"%perso)])
        if RibbonArm:
            cs = ["L_UpperArm", "R_UpperArm", "L_LowerArm", "R_LowerArm"]
            for c in cs:
                for i in range(1, 6):
                    bones.extend(["%s_%s_Ribbn0%i_jnt"%(perso, c, i)])
        if spine == "IK":
            bones.extend([("%s_C_Root_jnt"%perso), ("%s_C_Spine01_jnt"%perso), ("%s_C_Spine02_jnt"%perso), ("%s_C_Spine03_jnt"%perso), ("%s_C_Spine04_jnt"%perso), ("%s_C_Spine05_jnt"%perso), ("%s_C_Spine06_jnt"%perso), ("%s_C_Spine07_jnt"%perso)])
        elif spine == "FK":
            bones.extend([("%s_C_Root_jnt"%perso), ("%s_C_MidChest_jnt"%perso), ("%s_C_Chest_jnt"%perso), ("%s_C_Middle_jnt"%perso)])
        elif spine == "Ribbon":
            bones.extend([("%s_C_Root_jnt"%perso), ("%s_C_MidChest_jnt"%perso), ("%s_C_Chest_jnt"%perso)])
            for i in range(1, 6):
                bones.extend(["%s_C_Spine_Ribbn0%i_jnt"%(perso, i)])
        bones.extend([("%s_C_Neck_jnt"%perso), ("%s_C_Head_jnt"%perso), ("%s_C_Jaw_jnt"%perso), ("%s_C_Pelvis_jnt"%perso)])
        cotes = ["L", "R"]
        for cote in cotes:
            for i in range(1, 4):
                thumb = "%s_%s_Thumb0%i_jnt"%(perso, cote, i)
                index = "%s_%s_Index0%i_jnt"%(perso, cote, i)
                middle = "%s_%s_Middle0%i_jnt"%(perso, cote, i)
                ring = "%s_%s_Ring0%i_jnt"%(perso, cote, i)
                pinky = "%s_%s_Pinky0%i_jnt"%(perso, cote, i)
                fingers = [thumb, index, middle, ring, pinky]
                for finger in fingers:
                    bones.append(finger)
        cmds.sets(bones, n=("%s_SkinningJoints"%perso), t="gCharacterSet")
    # end def jointsSet
#end class auto

# class personnage
class perso:
    # var
    nom = ""
    spine = "IK"
    legFK = False
    legIK = True
    legRibbon = False
    armFK = True
    armIK = False
    armRibbon = False
    handCtrl = True
    handFK = False
    handUltimate = False
    head = "FK"
    spheres = []
    tempoJnts = []
    joints = []
    ctrls = []
    
    jp = False
    cj = False
    ar = False
    
    # def init
    def __init__(self, nom):
        self.nom = nom
        print "New character created : %s" %self.nom
    # end def init
    
    # def changeSpine
    def changeSpine(self):
        if cmds.radioCollection("spineRadioCollection", q=True, sl=True) == "FKSpine":
            self.spine = "FK"
        elif cmds.radioCollection("spineRadioCollection", q=True, sl=True) == "IKSpine":
            self.spine = "IK"
        elif cmds.radioCollection("spineRadioCollection", q=True, sl=True) == "RibbonSpine":
            self.spine = "Ribbon"

    # def changeLeg
    def changeLeg(self, imp):
        if imp == "FK":
            self.legFK = cmds.checkBox("FKLeg", q=True, v=True)
        if imp == "IK":
            self.legIK = cmds.checkBox("IKLeg", q=True, v=True)
        if imp == "Ribbon":
            self.legRibbon = cmds.checkBox("RibbonLeg", q=True, v=True)
            
    # def changeArm
    def changeArm(self, imp):
        if imp == "FK":
            self.armFK = cmds.checkBox("FKArm", q=True, v=True)
        if imp == "IK":
            self.armIK = cmds.checkBox("IKArm", q=True, v=True)
        if imp == "Ribbon":
            self.armRibbon = cmds.checkBox("RibbonArm", q=True, v=True)
            
    # def changeHand
    def changeHand(self, imp):
        if imp == "ctrl":
            self.handCtrl = cmds.checkBox("CTRLHand", q=True, v=True)
        if imp == "FK":
            self.handFK = cmds.checkBox("FKHand", q=True, v=True)
        if imp == "ultim":
            self.handUltimate = cmds.checkBox("ULTIMHand", q=True, v=True)

    # def changeHead
    def changeHead(self):
        if cmds.radioCollection("headRadioCollection", q=True, sl=True) == "FKHead":
            self.head = "FK"
        elif cmds.radioCollection("headRadioCollection", q=True, sl=True) == "IKHead":
            self.head = "IK"
    
    # def sph
    def sph(self, cote, name, x, y, z, sc):
        sphName = ("%s_%s_%s_sph"%(self.nom, cote, name))
        cmds.sphere(n=sphName)
        cmds.move(x, y, z, sphName, a=True)
        cmds.scale(sc, sc, sc, sphName, r=True, os=True)
        colorize(cote, [sphName])
        cmds.makeIdentity(sphName, a=True, t=True, r=True, s=True, n=False)
        if cote == "C":
            lockAndHide([sphName], True, True, ["tx", "rx", "ry", "rz", "sx", "sy", "sz"])
        cmds.delete(sphName, ch=True)
        self.spheres.append(sphName)
        return sphName
    # end def sph
    
    # def symSph
    def symSph(self, name, x, y, z, sc):
        sphNameL = self.sph("L", name, x, y, z, sc)
        sphNameR = self.sph("R", name, -x, y, z, sc)
        lockAndHide([sphNameL, sphNameR], True, True, ["sx", "sy", "sz"])
        cmds.expression(s=("%s.translateX = -%s.translateX")%(sphNameR, sphNameL))
        cmds.expression(s=("%s.translateY = %s.translateY")%(sphNameR, sphNameL))
        cmds.expression(s=("%s.translateZ = %s.translateZ")%(sphNameR, sphNameL))
    # end def symSph

    # def posJoints
    def posJoints(self):
        # majWin
        self.jp = True
        win.majWin()
        # spheres
        self.spheres = []
        self.sph("C", "Pelvis", 0, 12.73, 0, .3);
        if self.spine == "FK" or self.spine == "Ribbon":
            self.sph("C", "Root", 0, 14, 0, .3);
            if self.spine == "Ribbon":
                self.sph("C", "Middle", 0, 16.24, 0.19, .2);
            else:
                self.sph("C", "Middle", 0, 16.76, -0.06, .3);
            self.sph("C", "Chest", 0, 18.58, -0.35, .3);
            self.sph("C", "MidChest", 0, 19.92, -0.57, .3);
            self.sph("C", "Neck", 0, 21.06, -0.64, .3);
        elif self.spine == "IK":
            self.sph("C", "Root", 0, 13.87, -0.04, .3);
            self.sph("C", "Spine01", 0, 14.83, 0.21, .15);
            self.sph("C", "Spine02", 0, 15.68, 0.24, .15);
            self.sph("C", "Spine03", 0, 16.58, 0.15, .15);
            self.sph("C", "Spine04", 0, 17.42, -0.08, .15);
            self.sph("C", "Spine05", 0, 18.23, -0.39, .15);
            self.sph("C", "Spine06", 0, 19.17, -0.68, .15);
            self.sph("C", "Spine07", 0, 20.07, -0.77, .15);
            self.sph("C", "Spine08", 0, 21.1, -0.63, .15);
            self.sph("C", "Neck", 0, 21.1, -0.63, .3);
            cmds.expression(s=("%s_C_Spine08_sph.translateY = %s_C_Neck_sph.translateY"%(self.nom,self.nom)));
            cmds.expression(s=("%s_C_Spine08_sph.translateZ = %s_C_Neck_sph.translateZ"%(self.nom,self.nom)));
        self.sph("C", "Head", 0, 22.65, -0.3, .15);
        self.sph("C", "HeadEnd", 0, 24.98, -0.09, .15);
        self.sph("C", "Jaw", 0, 22.58, 0.06, .15);
        self.sph("C", "JawEnd", 0, 21.91, 1.2, .15);
        # Sphere R-L
        self.symSph("Leg", 1.1, 13.32, -.23, .4);
        self.symSph("Knee", 1.57, 6.92, -.08, .4);
        self.symSph("Ankle", 1.57, 1.38, -1.09, .35);
        self.symSph("Ball", 1.57, .41, .35, .3);
        self.symSph("Toe", 1.57, .3, 1.79, .3);
        self.symSph("Clavicle", .63, 20.6, .15, .25);
        self.symSph("Shoulder", 2.39, 20.6, -.72, .25);
        self.symSph("Elbow", 5.06, 17.01, -1.07, .25);
        self.symSph("ForeArm", 6.26, 15.895, -0.835, .12);
        self.symSph("Wrist", 7.46, 14.78, -0.6, .2);
        cmds.expression(s=("%s_L_ForeArm_sph.translateX = (%s_L_Wrist_sph.translateX + %s_L_Elbow_sph.translateX) / 2"%(self.nom, self.nom, self.nom)))
        cmds.expression(s=("%s_L_ForeArm_sph.translateY = (%s_L_Wrist_sph.translateY + %s_L_Elbow_sph.translateY) / 2"%(self.nom, self.nom, self.nom)))
        cmds.expression(s=("%s_L_ForeArm_sph.translateZ = (%s_L_Wrist_sph.translateZ + %s_L_Elbow_sph.translateZ) / 2"%(self.nom, self.nom, self.nom)))
        self.symSph("Thumb01", 7.96, 14.75, -0.7, .07);
        self.symSph("Thumb02", 8.629, 14.85, -0.74, .07);
        self.symSph("Thumb03", 9.09, 14.69, -0.67, .07);
        self.symSph("Thumb04", 9.5, 14.62, -0.69, .07);
        self.symSph("Index01", 8.85, 14.2, -0.9, .07);
        self.symSph("Index02", 9.25, 13.99, -0.87, .07);
        self.symSph("Index03", 9.57, 13.85, -0.86, .07);
        self.symSph("Index04", 9.88, 13.68, -0.92, .07);
        self.symSph("Middle01", 8.68, 13.93, -0.78, .07);
        self.symSph("Middle02", 9.09, 13.63, -0.75, .07);
        self.symSph("Middle03", 9.42, 13.42, -0.72, .07);
        self.symSph("Middle04", 9.73, 13.19, -0.78, .07);
        self.symSph("Ring01", 8.45, 13.69, -0.64, .07);
        self.symSph("Ring02", 8.8, 13.35, -0.62, .07);
        self.symSph("Ring03", 9.1, 13.11, -0.56, .07);
        self.symSph("Ring04", 9.34, 12.9, -0.56, .07);
        self.symSph("Pinky01", 8.18, 13.55, -0.46, .07);
        self.symSph("Pinky02", 8.37, 13.27, -0.43, .07);
        self.symSph("Pinky03", 8.55, 13.05, -0.37, .07);
        self.symSph("Pinky04", 8.72, 12.82, -0.39, .07);
        self.symSph("Eye", .41, 23.54, 0.9, .25);
        # ctrl
        cmds.circle(c=(0,0,0), nr=(0,1,0), r=1, s=8, n=("%s_Wrist_ctrl"%self.nom))
        cmds.group(("%s_Wrist_ctrl"%self.nom), n="%s_Wrist_grp"%self.nom)
        cmds.delete(cmds.parentConstraint(("%s_L_Wrist_sph"%self.nom), ("%s_Wrist_grp"%self.nom)))
        cmds.setAttr(("%s_Wrist_grp.rotateZ"%self.nom), 48)
        cmds.parentConstraint(("%s_Wrist_ctrl"%self.nom), ("%s_L_Wrist_sph"%self.nom), mo=True)
        lockAndHide([("%s_Wrist_ctrl"%self.nom)], True, True, ["sx", "sy", "sz"])
        colorize("L", [("%s_Wrist_ctrl"%self.nom)])
        
        cmds.circle(c=(0,0,0), nr=(0,1,0), r=4, s=8, n=("%s_Scale_ctrl"%self.nom))
        lockAndHide([("%s_Scale_ctrl"%self.nom)], True, True, ["tx", "ty", "tz", "rx", "ry", "rz"])
        cmds.parent(self.spheres, ("%s_Scale_ctrl"%self.nom))
        cmds.parent(("%s_Wrist_grp"%self.nom), ("%s_Scale_ctrl"%self.nom))
        cmds.group(("%s_L_Thumb01_sph"%self.nom), ("%s_L_Thumb02_sph"%self.nom), ("%s_L_Thumb03_sph"%self.nom), ("%s_L_Thumb04_sph"%self.nom), ("%s_L_Index01_sph"%self.nom), ("%s_L_Index02_sph"%self.nom), ("%s_L_Index03_sph"%self.nom), ("%s_L_Index04_sph"%self.nom), ("%s_L_Middle01_sph"%self.nom), ("%s_L_Middle02_sph"%self.nom), ("%s_L_Middle03_sph"%self.nom), ("%s_L_Middle04_sph"%self.nom), ("%s_L_Ring01_sph"%self.nom), ("%s_L_Ring02_sph"%self.nom), ("%s_L_Ring03_sph"%self.nom), ("%s_L_Ring04_sph"%self.nom), ("%s_L_Pinky01_sph"%self.nom), ("%s_L_Pinky02_sph"%self.nom), ("%s_L_Pinky03_sph"%self.nom), ("%s_L_Pinky04_sph"%self.nom), n=("%s_L_Doigts_grp"%self.nom))
        cmds.parent(("%s_L_Doigts_grp"%self.nom), ("%s_L_Wrist_sph"%self.nom))
        cmds.group(("%s_R_Thumb01_sph"%self.nom), ("%s_R_Thumb02_sph"%self.nom), ("%s_R_Thumb03_sph"%self.nom), ("%s_R_Thumb04_sph"%self.nom), ("%s_R_Index01_sph"%self.nom), ("%s_R_Index02_sph"%self.nom), ("%s_R_Index03_sph"%self.nom), ("%s_R_Index04_sph"%self.nom), ("%s_R_Middle01_sph"%self.nom), ("%s_R_Middle02_sph"%self.nom), ("%s_R_Middle03_sph"%self.nom), ("%s_R_Middle04_sph"%self.nom), ("%s_R_Ring01_sph"%self.nom), ("%s_R_Ring02_sph"%self.nom), ("%s_R_Ring03_sph"%self.nom), ("%s_R_Ring04_sph"%self.nom), ("%s_R_Pinky01_sph"%self.nom), ("%s_R_Pinky02_sph"%self.nom), ("%s_R_Pinky03_sph"%self.nom), ("%s_R_Pinky04_sph"%self.nom), n=("%s_R_Doigts_grp"%self.nom))
        cmds.parent(("%s_R_Doigts_grp"%self.nom), ("%s_R_Wrist_sph"%self.nom))
        cmds.expression(s=("%s_R_Wrist_sph.rotateX = %s_L_Wrist_sph.rotateX"%(self.nom, self.nom)))
        cmds.expression(s=("%s_R_Wrist_sph.rotateY = -%s_L_Wrist_sph.rotateY"%(self.nom, self.nom)))
        cmds.expression(s=("%s_R_Wrist_sph.rotateZ = -%s_L_Wrist_sph.rotateZ"%(self.nom, self.nom)))
        cmds.expression(s=("%s_Scale_ctrl.scaleX = %s_Scale_ctrl.scaleY = %s_Scale_ctrl.scaleZ"%(self.nom, self.nom, self.nom)))
        cmds.select(cl=True)
        colorize("C", [("%s_Scale_ctrl"%self.nom)])
        print "Spheres for %s created !"%self.nom
    # end def posJoints
    
    # def jointParent
    def jointParent(self, jEnfant, jParent, rad):
        scale = cmds.xform(("%s_Scale_ctrl"%self.nom), q=True, r=True, s=True)
        cmds.select(cl=True)
        jPos = cmds.xform(("%s_%s_sph"%(self.nom,jEnfant)), q=True, ws=True, rp=True)
        cmds.joint(n=("%s_%s_jnt"%(self.nom, jEnfant)), rad=(rad * scale[0]), p=(jPos[0], jPos[1], jPos[2]))
        if jParent != "":
            cmds.parent(("%s_%s_jnt"%(self.nom, jEnfant)), ("%s_%s_jnt"%(self.nom, jParent)))
            cmds.joint(("%s_%s_jnt"%(self.nom, jParent)), e=True, zso=True, oj="xyz", sao="xdown")
    # end def jointParent

    # def doigtsJointParent
    def doigtsJointParent(self, joint, rad):
        scale = cmds.xform(("%s_Scale_ctrl"%self.nom), q=True, r=True, s=True)
        for i in range(1, 5):
            cmds.select(cl=True)
            jPos = cmds.xform(("%s_%s0%i_sph"%(self.nom, joint, i)), q=True, ws=True, rp=True)
            cmds.joint(n=("%s_%s0%i_jnt"%(self.nom, joint, i)), rad=(rad * scale[0]), p=(jPos[0], jPos[1], jPos[2]))
            if i != 1:
                cmds.parent(("%s_%s0%i_jnt"%(self.nom, joint, i)), ("%s_%s0%i_jnt"%(self.nom, joint, (i-1))))
                cmds.joint(("%s_%s0%i_jnt"%(self.nom, joint, (i-1))), e=True, zso=True, oj="xyz", sao="xdown")
    # end def doigtsJointParent

    # def angleRotationArm
    def angleRotationArm(self):
        # arm and fingers joints
        shoulder = "%s_L_Shoulder"%self.nom
        elbow = "%s_L_Elbow"%self.nom
        wrist = "%s_L_Wrist"%self.nom
        index = "%s_L_Index01"%self.nom
        pinky = "%s_L_Pinky01"%self.nom
        middle = "%s_L_Middle04"%self.nom
        shoulderPos = cmds.xform(("%s_jnt"%shoulder), q=True, ws=True, rp=True)
        elbowPos = cmds.xform(("%s_jnt"%elbow), q=True, ws=True, rp=True)
        wristPos = cmds.xform(("%s_jnt"%wrist), q=True, ws=True, rp=True)
        indexPos = cmds.xform(("%s_jnt"%index), q=True, ws=True, rp=True)
        pinkyPos = cmds.xform(("%s_jnt"%pinky), q=True, ws=True, rp=True)
        middlePos = cmds.xform(("%s_jnt"%middle), q=True, ws=True, rp=True)
        # vecteurs
        shoulderElbow = MVector((elbowPos[0] - shoulderPos[0]), (elbowPos[1] - shoulderPos[1]), (elbowPos[2] - shoulderPos[2]))
        elbowWrist = MVector((wristPos[0] - elbowPos[0]), (wristPos[1] - elbowPos[1]), (wristPos[2] - elbowPos[2]))
        indexPinky = MVector((pinkyPos[0] - indexPos[0]), (pinkyPos[1] - indexPos[1]), (pinkyPos[2] - indexPos[2]))
        pinkyMiddle = MVector((middlePos[0] - pinkyPos[0]), (middlePos[1] - pinkyPos[1]), (middlePos[2] - pinkyPos[2]))
        # plane designed by the arm
        plane1x = shoulderElbow.y * elbowWrist.z - elbowWrist.y * shoulderElbow.z
        plane1y = shoulderElbow.z * elbowWrist.x - elbowWrist.z * shoulderElbow.x
        plane1z = shoulderElbow.x * elbowWrist.y - elbowWrist.x * shoulderElbow.y
        plane1 = MVector(plane1x, plane1y, plane1z)
        # plane designed by the fingers
        plane2x = indexPinky.y * pinkyMiddle.z - pinkyMiddle.y * indexPinky.z
        plane2y = indexPinky.z * pinkyMiddle.x - pinkyMiddle.z * indexPinky.x
        plane2z = indexPinky.x * pinkyMiddle.y - pinkyMiddle.x * indexPinky.y
        plane2 = MVector(plane2x, plane2y, plane2z)
        angleBetween = math.degrees(MVector.angle(plane1, plane2))
        return angleBetween/2
    # end def angleRotationArm

    # def razRotateAxes
    def razRotateAxes(self, joint):
        cmds.select(("%s_%s_jnt"%(self.nom, joint)), hi=True)
        selectedObj = cmds.ls(sl=True)
        if(len(selectedObj) > 1):
            cmds.parent(w=True)
            for i in range(1, len(selectedObj)):
                cmds.setAttr(("%s.rotateAxis"%selectedObj[i-1]), 0, 0, 0, type="double3")
                cmds.parent(selectedObj[i], selectedObj[i-1])
            cmds.setAttr(("%s.rotateAxis"%selectedObj[i]), 0, 0, 0, type="double3")
        else:
            cmds.setAttr(("%s_%s_jnt.rotateAxis"%(self.nom, joint)), 0, 0, 0, type="double3")
    # end def razRotateAxes
    
    # def rotateLRA
    def rotateLRA(self, joint, angle):
        cmds.select(("%s_%s_jnt"%(self.nom, joint)), hi=True)
        selectedObj = cmds.ls(sl=True)
        for obj in selectedObj:
            newJO = cmds.getAttr("%s.jointOrientX"%obj) - float(angle)
            cmds.setAttr(("%s.jointOrientX"%obj), newJO)
            newRA = cmds.getAttr("%s.rotateAxisX"%obj) + float(angle)
            cmds.setAttr(("%s.rotateAxisX"%obj), newRA)
        parent = "%s_%s_jnt"%(self.nom, joint)
        newJO = cmds.getAttr("%s.jointOrientX"%parent) % 360
        sansVirgule = int(cmds.getAttr("%s.jointOrientX"%parent))
        virgule = cmds.getAttr("%s.jointOrientX"%parent) - sansVirgule
        cmds.setAttr(("%s.jointOrientX"%parent), newJO + virgule)
        self.razRotateAxes(joint)
    # end def rotateLRA

    # def reorientJoint
    def reorientJoint(self, joint):
        cmds.select(("%s_%s_jnt"%(self.nom, joint)), hi=True)
        selectedObj = cmds.ls(sl=True)
        cmds.parent(w=True)
        for i in range(1, len(selectedObj)):
            cmds.select(selectedObj[i-1], r=True)
            cmds.parent(selectedObj[i])
            cmds.joint(selectedObj[i-1], e=True, zso=True, oj="xyz", sao="xdown")
        cmds.setAttr(("%s.jointOrient"%(lastChild(selectedObj[0]))), 0, 0, 0, type="double3")
        for i in range((len(selectedObj)-1), 1, -1):
            tJO = cmds.getAttr("%s.jointOrientX"%selectedObj[i-1])
            for j in range((i-1), len(selectedObj)):
                newJO = cmds.getAttr("%s.jointOrientX"%selectedObj[j]) - float(tJO)
                cmds.setAttr(("%s.jointOrientX"%selectedObj[j]), newJO)
                newRA = cmds.getAttr("%s.rotateAxisX"%selectedObj[j]) + float(tJO)
                cmds.setAttr(("%s.rotateAxisX"%selectedObj[j]), newRA)
        cmds.select(selectedObj[0], hi=True)
        cmds.parent(w=True)
        for i in range(1, len(selectedObj)):
            cmds.setAttr(("%s.rotateAxis"%selectedObj[i-1]), 0, 0, 0, type="double3")
            cmds.parent(selectedObj[i], selectedObj[i-1])
        cmds.setAttr(("%s.rotateAxis"%selectedObj[i-1]), 0, 0, 0, type="double3")
        self.rotateLRA(joint, 90);
    # end def reorientJoint
    
    # def autoRibbon
    def autoRibbon(self, cotes, nom):
        scale = cmds.xform(("%s_Scale_ctrl"%self.nom), q=True, r=True, s=True)
        for cote in cotes:
            if nom == "Spine":
                # nurbsPlane
                cmds.nurbsPlane(p=(0, 0, 0), ax=(0, 0, 1), w=.5*scale[0], lr=10, d=3, u=1, v=5, ch=True, n="%s_%s_%s_Ribbn_GEO"%(self.nom, cote, nom))
                cmds.rebuildSurface("%s_%s_%s_Ribbn_GEO"%(self.nom, cote, nom), ch=True, rpo=True, rt=0, end=1, kr=0, kcp=False, kc=False, su=1, du=1, sv=5, dv=3, tol=.01, fr=0, dir=2)
                cmds.delete("%s_%s_%s_Ribbn_GEO"%(self.nom, cote, nom), ch=True)
                # follicle
                follicles = []
                for i in range(0,5):
                    fol = cmds.createNode("follicle", n="%s_%s_%s_Ribbn0%i_folShape"%(self.nom, cote, nom, (i+1)))
                    follicles.append("%s_%s_%s_Ribbn0%i_fol"%(self.nom, cote, nom, (i+1)))
                    cmds.connectAttr("%s_%s_%s_Ribbn_GEOShape.local"%(self.nom, cote, nom), "%s_%s_%s_Ribbn0%i_folShape.inputSurface"%(self.nom, cote, nom, (i+1)), f=True)
                    cmds.connectAttr("%s_%s_%s_Ribbn_GEOShape.worldMatrix[0]"%(self.nom, cote, nom), "%s_%s_%s_Ribbn0%i_folShape.inputWorldMatrix"%(self.nom, cote, nom, (i+1)), f=True)
                    cmds.connectAttr("%s_%s_%s_Ribbn0%i_folShape.outRotate"%(self.nom, cote, nom, (i+1)), "%s_%s_%s_Ribbn0%i_fol.rotate"%(self.nom, cote, nom, (i+1)), f=True)
                    cmds.connectAttr("%s_%s_%s_Ribbn0%i_folShape.outTranslate"%(self.nom, cote, nom, (i+1)), "%s_%s_%s_Ribbn0%i_fol.translate"%(self.nom, cote, nom, (i+1)), f=True)
                    cmds.setAttr("%s_%s_%s_Ribbn0%i_folShape.parameterU"%(self.nom, cote, nom, (i+1)), .5)
                    cmds.setAttr("%s_%s_%s_Ribbn0%i_folShape.parameterV"%(self.nom, cote, nom, (i+1)), (float(i) / 5 + .1))
                    lockAndHide(["%s_%s_%s_Ribbn0%i_fol"%(self.nom, cote, nom, (i+1))], True, False, ["tx", "ty", "tz", "rx", "ry", "rz"])
                cmds.group(follicles, n="%s_%s_%s_Ribbn_fol_grp"%(self.nom, cote, nom))
                # joints
                for i in range(0,5):
                    trY = cmds.getAttr("%s.translateY"%follicles[i])
                    cmds.select(cl=True)
                    cmds.joint(n="%s_%s_%s_Ribbn0%i_jnt"%(self.nom, cote, nom, (i+1)), rad=(.25 * scale[0]), p=(0, trY, 0))
                    cmds.parent("%s_%s_%s_Ribbn0%i_jnt"%(self.nom, cote, nom, (i+1)), "%s_%s_%s_Ribbn0%i_fol"%(self.nom, cote, nom, (i+1)))
                    cmds.setAttr("%s_%s_%s_Ribbn0%i_jnt.jointOrientZ"%(self.nom, cote, nom, (i+1)), 90)
                # driver joints
                cmds.select(cl=True)
                cmds.joint(n="%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, nom), rad=(.3 * scale[0]), p=(0, 2.5 * scale[0], 0))
                cmds.joint(n="%s_%s_%s_RibbnDriverEnd_hi_jnt"%(self.nom, cote, nom), rad=(.3 * scale[0]), p=(0, 1.5 * scale[0], 0))
                cmds.select(cl=True)
                cmds.joint(n="%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, nom), rad=(.3 * scale[0]), p=(0, -2.5 * scale[0], 0))
                cmds.joint(n="%s_%s_%s_RibbnDriverEnd_lox_jnt"%(self.nom, cote, nom), rad=(.3 * scale[0]), p=(0, -1.5 * scale[0], 0))
                cmds.select(cl=True)
                cmds.joint(n="%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, nom), rad=(.3 * scale[0]), p=(0, 0, 0))
                # locators
                cmds.spaceLocator(n="%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, nom))
                cmds.spaceLocator(n="%s_%s_%s_RibbnAim_hi_loc"%(self.nom, cote, nom))
                cmds.spaceLocator(n="%s_%s_%s_RibbnUp_hi_loc"%(self.nom, cote, nom))
                cmds.parent("%s_%s_%s_RibbnAim_hi_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, nom))
                cmds.parent("%s_%s_%s_RibbnUp_hi_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, nom))
                cmds.move(0, 2.5 * scale[0], 0, "%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, nom), a=True)
                cmds.move(5 * scale[0], 0, 0, "%s_%s_%s_RibbnUp_hi_loc"%(self.nom, cote, nom), r=True)
                cmds.spaceLocator(n="%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, nom))
                cmds.spaceLocator(n="%s_%s_%s_RibbnAim_mid_loc"%(self.nom, cote, nom))
                cmds.spaceLocator(n="%s_%s_%s_RibbnUp_mid_loc"%(self.nom, cote, nom))
                cmds.parent("%s_%s_%s_RibbnAim_mid_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, nom))
                cmds.parent("%s_%s_%s_RibbnUp_mid_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, nom))
                cmds.move(0, 0, 0, "%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, nom), a=True)
                cmds.move(5 * scale[0], 0, 0, "%s_%s_%s_RibbnUp_mid_loc"%(self.nom, cote, nom), r=True)
                cmds.spaceLocator(n="%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, nom))
                cmds.spaceLocator(n="%s_%s_%s_RibbnAim_low_loc"%(self.nom, cote, nom))
                cmds.spaceLocator(n="%s_%s_%s_RibbnUp_low_loc"%(self.nom, cote, nom))
                cmds.parent("%s_%s_%s_RibbnAim_low_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, nom))
                cmds.parent("%s_%s_%s_RibbnUp_low_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, nom))
                cmds.move(0, -2.5 * scale[0], 0, "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, nom), a=True)
                cmds.move(5 * scale[0], 0, 0, "%s_%s_%s_RibbnUp_low_loc"%(self.nom, cote, nom), r=True)
                # contraintes
                cmds.pointConstraint("%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, nom), mo=True, n="%s_%s_%s_RibbnPos_mid_loc_pointContrainte1"%(self.nom, cote, nom))
                cmds.pointConstraint("%s_%s_%s_RibbnUp_hi_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnUp_low_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnUp_mid_loc"%(self.nom, cote, nom), mo=True, n="%s_%s_%s_RibbnPos_mid_loc_pointContrainte2"%(self.nom, cote, nom))
                cmds.aimConstraint("%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnAim_low_loc"%(self.nom, cote, nom), aim=(0, 1, 0), u=(1, 0, 0), wut="object", wuo="%s_%s_%s_RibbnUp_low_loc"%(self.nom, cote, nom), n="%s_%s_%s_RibbnAim_low_loc_aimContrainte"%(self.nom, cote, nom))
                cmds.aimConstraint("%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnAim_mid_loc"%(self.nom, cote, nom), aim=(0, 1, 0), u=(1, 0, 0), wut="object", wuo="%s_%s_%s_RibbnUp_mid_loc"%(self.nom, cote, nom), n="%s_%s_%s_RibbnAim_mid_loc_aimContrainte"%(self.nom, cote, nom))
                cmds.aimConstraint("%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnAim_hi_loc"%(self.nom, cote, nom), aim=(0, -1, 0), u=(1, 0, 0), wut="object", wuo="%s_%s_%s_RibbnUp_hi_loc"%(self.nom, cote, nom), n="%s_%s_%s_RibbnAim_hi_loc_aimContrainte"%(self.nom, cote, nom))
                # locator offset
                cmds.spaceLocator(n="%s_%s_%s_RibbnOffset_mid_loc"%(self.nom, cote, nom))
                cmds.parent("%s_%s_%s_RibbnOffset_mid_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnAim_mid_loc"%(self.nom, cote, nom))
                # parentage
                cmds.parent("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, nom), "%s_%s_%s_RibbnAim_hi_loc"%(self.nom, cote, nom))
                cmds.parent("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, nom), "%s_%s_%s_RibbnOffset_mid_loc"%(self.nom, cote, nom))
                cmds.parent("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, nom), "%s_%s_%s_RibbnAim_low_loc"%(self.nom, cote, nom))
                # skin
                cmds.skinCluster("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, nom), "%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, nom), "%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, nom), "%s_%s_%s_Ribbn_GEO"%(self.nom, cote, nom), tsb=True, sm=0, nw=1, mi=2, dr=4, n="%s_%s_%s_Ribbn_skin"%(self.nom, cote, nom))
                cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, nom), "%s_%s_%s_Ribbn_GEO.cv[0:1][7]"%(self.nom, cote, nom), tv=[("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, nom), 1)])
                cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, nom), "%s_%s_%s_Ribbn_GEO.cv[0:1][6]"%(self.nom, cote, nom), tv=[("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, nom), .75), ("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, nom), .25)])
                cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, nom), "%s_%s_%s_Ribbn_GEO.cv[0:1][5]"%(self.nom, cote, nom), tv=[("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, nom), .5), ("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, nom), .5)])
                cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, nom), "%s_%s_%s_Ribbn_GEO.cv[0:1][4]"%(self.nom, cote, nom), tv=[("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, nom), .25), ("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, nom), .75)])
                cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, nom), "%s_%s_%s_Ribbn_GEO.cv[0:1][3]"%(self.nom, cote, nom), tv=[("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, nom), .25), ("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, nom), .75)])
                cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, nom), "%s_%s_%s_Ribbn_GEO.cv[0:1][2]"%(self.nom, cote, nom), tv=[("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, nom), .5), ("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, nom), .5)])
                cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, nom), "%s_%s_%s_Ribbn_GEO.cv[0:1][1]"%(self.nom, cote, nom), tv=[("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, nom), .75), ("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, nom), .25)])
                cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, nom), "%s_%s_%s_Ribbn_GEO.cv[0:1][0]"%(self.nom, cote, nom), tv=[("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, nom), 1)])
                # clean
                cmds.toggle("%s_%s_%s_Ribbn_GEO"%(self.nom, cote, nom), te=True)
                cmds.group("%s_%s_%s_Ribbn_GEO"%(self.nom, cote, nom), "%s_%s_%s_Ribbn_fol_grp"%(self.nom, cote, nom), "%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, nom), n="%s_%s_%s_Ribbn_GRP"%(self.nom, cote, nom))
                cmds.hide("%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, nom), "%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, nom))
                cmds.setAttr("%s_%s_%s_RibbnPos_mid_locShape.visibility"%(self.nom, cote, nom), False)
                cmds.setAttr("%s_%s_%s_RibbnAim_mid_locShape.visibility"%(self.nom, cote, nom), False)
                cmds.setAttr("%s_%s_%s_RibbnUp_mid_locShape.visibility"%(self.nom, cote, nom), False)
                cmds.setAttr("%s_%s_%s_RibbnOffset_mid_locShape.visibility"%(self.nom, cote, nom), False)
                # mise en position
                cmds.delete(cmds.pointConstraint("%s_C_Chest_jnt"%self.nom, "%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, nom)))
                cmds.parent("%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, nom), "%s_C_Chest_jnt"%self.nom)
                cmds.delete(cmds.pointConstraint("%s_C_Root_jnt"%self.nom, "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, nom)))
                cmds.parent("%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, nom), "%s_C_Root_jnt"%self.nom)
                cmds.delete(cmds.pointConstraint("%s_C_Middle_jnt"%self.nom, "%s_%s_%s_RibbnOffset_mid_loc"%(self.nom, cote, nom), sk=["x", "y"]))
                cmds.parent("%s_C_Chest_jnt"%self.nom, w=True)
                cmds.delete("%s_C_Middle_jnt"%self.nom)
                cmds.parent(("%s_C_Pelvis_jnt"%self.nom), ("%s_C_Root_jnt"%self.nom))
            elif nom == "Arm":
                nomRibbn = ["UpperArm", "LowerArm"]
                for name in nomRibbn:
                    # nurbsPlane
                    cmds.nurbsPlane(p=(0, 0, 0), ax=(0, 1, 0), w=5*scale[0], lr=.1, d=3, u=5, v=1, ch=True, n="%s_%s_%s_Ribbn_GEO"%(self.nom, cote, name))
                    cmds.rebuildSurface("%s_%s_%s_Ribbn_GEO"%(self.nom, cote, name), ch=True, rpo=True, rt=0, end=1, kr=0, kcp=False, kc=False, su=5, du=3, sv=1, dv=1, tol=.01, fr=0, dir=2)
                    cmds.delete("%s_%s_%s_Ribbn_GEO"%(self.nom, cote, name), ch=True)
                    # follicle
                    follicles = []
                    for i in range(0,5):
                        fol = cmds.createNode("follicle", n="%s_%s_%s_Ribbn0%i_folShape"%(self.nom, cote, name, (i+1)))
                        follicles.append("%s_%s_%s_Ribbn0%i_fol"%(self.nom, cote, name, (i+1)))
                        cmds.connectAttr("%s_%s_%s_Ribbn_GEOShape.local"%(self.nom, cote, name), "%s_%s_%s_Ribbn0%i_folShape.inputSurface"%(self.nom, cote, name, (i+1)), f=True)
                        cmds.connectAttr("%s_%s_%s_Ribbn_GEOShape.worldMatrix[0]"%(self.nom, cote, name), "%s_%s_%s_Ribbn0%i_folShape.inputWorldMatrix"%(self.nom, cote, name, (i+1)), f=True)
                        cmds.connectAttr("%s_%s_%s_Ribbn0%i_folShape.outRotate"%(self.nom, cote, name, (i+1)), "%s_%s_%s_Ribbn0%i_fol.rotate"%(self.nom, cote, name, (i+1)), f=True)
                        cmds.connectAttr("%s_%s_%s_Ribbn0%i_folShape.outTranslate"%(self.nom, cote, name, (i+1)), "%s_%s_%s_Ribbn0%i_fol.translate"%(self.nom, cote, name, (i+1)), f=True)
                        cmds.setAttr("%s_%s_%s_Ribbn0%i_folShape.parameterU"%(self.nom, cote, name, (i+1)), (float(i) / 5 + .1))
                        cmds.setAttr("%s_%s_%s_Ribbn0%i_folShape.parameterV"%(self.nom, cote, name, (i+1)), .5)
                        lockAndHide(["%s_%s_%s_Ribbn0%i_fol"%(self.nom, cote, name, (i+1))], True, False, ["tx", "ty", "tz", "rx", "ry", "rz"])
                    cmds.group(follicles, n="%s_%s_%s_Ribbn_fol_grp"%(self.nom, cote, name))
                    # joints
                    for i in range(0,5):
                        trX = cmds.getAttr("%s.translateX"%follicles[i])
                        cmds.select(cl=True)
                        cmds.joint(n="%s_%s_%s_Ribbn0%i_jnt"%(self.nom, cote, name, (i+1)), rad=(.25 * scale[0]), p=(trX, 0, 0))
                        cmds.parent("%s_%s_%s_Ribbn0%i_jnt"%(self.nom, cote, name, (i+1)), "%s_%s_%s_Ribbn0%i_fol"%(self.nom, cote, name, (i+1)))
                        if cote == "L":
                            cmds.setAttr("%s_%s_%s_Ribbn0%i_jnt.jointOrientX"%(self.nom, cote, name, (i+1)), 90)
                        else:
                            cmds.setAttr("%s_%s_%s_Ribbn0%i_jnt.jointOrientX"%(self.nom, cote, name, (i+1)), 90)
                            cmds.setAttr("%s_%s_%s_Ribbn0%i_jnt.jointOrientZ"%(self.nom, cote, name, (i+1)), 180)
                    # driver joints
                    cmds.select(cl=True)
                    cmds.joint(n="%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), rad=(.3 * scale[0]), p=(-2.5 * scale[0], 0, 0))
                    cmds.joint(n="%s_%s_%s_RibbnDriverEnd_hi_jnt"%(self.nom, cote, name), rad=(.3 * scale[0]), p=(-1.5 * scale[0], 0, 0))
                    cmds.select(cl=True)
                    cmds.joint(n="%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), rad=(.3 * scale[0]), p=(2.5 * scale[0], 0, 0))
                    cmds.joint(n="%s_%s_%s_RibbnDriverEnd_lox_jnt"%(self.nom, cote, name), rad=(.3 * scale[0]), p=(1.5 * scale[0], 0, 0))
                    cmds.select(cl=True)
                    cmds.joint(n="%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name), rad=(.3 * scale[0]), p=(0, 0, 0))
                    # locators
                    cmds.spaceLocator(n="%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, name))
                    cmds.spaceLocator(n="%s_%s_%s_RibbnAim_hi_loc"%(self.nom, cote, name))
                    cmds.spaceLocator(n="%s_%s_%s_RibbnUp_hi_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnAim_hi_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnUp_hi_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, name))
                    cmds.move(-2.5 * scale[0], 0, 0, "%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, name), a=True)
                    cmds.move(0, 5 * scale[0], 0, "%s_%s_%s_RibbnUp_hi_loc"%(self.nom, cote, name), r=True)
                    cmds.spaceLocator(n="%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, name))
                    cmds.spaceLocator(n="%s_%s_%s_RibbnAim_mid_loc"%(self.nom, cote, name))
                    cmds.spaceLocator(n="%s_%s_%s_RibbnUp_mid_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnAim_mid_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnUp_mid_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, name))
                    cmds.move(0, 0, 0, "%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, name), a=True)
                    cmds.move(0, 5 * scale[0], 0, "%s_%s_%s_RibbnUp_mid_loc"%(self.nom, cote, name), r=True)
                    cmds.spaceLocator(n="%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name))
                    cmds.spaceLocator(n="%s_%s_%s_RibbnAim_low_loc"%(self.nom, cote, name))
                    cmds.spaceLocator(n="%s_%s_%s_RibbnUp_low_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnAim_low_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnUp_low_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name))
                    cmds.move(2.5 * scale[0], 0, 0, "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name), a=True)
                    cmds.move(0, 5 * scale[0], 0, "%s_%s_%s_RibbnUp_low_loc"%(self.nom, cote, name), r=True)
                    # contraintes
                    cmds.pointConstraint("%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, name), mo=True, n="%s_%s_%s_RibbnPos_mid_loc_pointContrainte1"%(self.nom, cote, name))
                    cmds.pointConstraint("%s_%s_%s_RibbnUp_hi_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnUp_low_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnUp_mid_loc"%(self.nom, cote, name), mo=True, n="%s_%s_%s_RibbnPos_mid_loc_pointContrainte2"%(self.nom, cote, name))
                    cmds.aimConstraint("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name), "%s_%s_%s_RibbnAim_hi_loc"%(self.nom, cote, name), aim=(1, 0, 0), u=(0, 1, 0), wut="object", wuo="%s_%s_%s_RibbnUp_hi_loc"%(self.nom, cote, name), n="%s_%s_%s_RibbnDriver_hi_jnt_aimContrainte"%(self.nom, cote, name))
                    cmds.aimConstraint("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name), "%s_%s_%s_RibbnAim_low_loc"%(self.nom, cote, name), aim=(-1, 0, 0), u=(0, 1, 0), wut="object", wuo="%s_%s_%s_RibbnUp_low_loc"%(self.nom, cote, name), n="%s_%s_%s_RibbnDriver_low_jnt_aimContrainte"%(self.nom, cote, name))
                    cmds.aimConstraint("%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnAim_mid_loc"%(self.nom, cote, name), aim=(1, 0, 0), u=(0, 1, 0), wut="object", wuo="%s_%s_%s_RibbnUp_mid_loc"%(self.nom, cote, name), n="%s_%s_%s_RibbnAim_mid_loc_aimContrainte"%(self.nom, cote, name))
                    # parentage
                    cmds.parent("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), "%s_%s_%s_RibbnAim_hi_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name), "%s_%s_%s_RibbnAim_mid_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), "%s_%s_%s_RibbnAim_low_loc"%(self.nom, cote, name))
                    # skin
                    cmds.skinCluster("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), "%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name), "%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO"%(self.nom, cote, name), tsb=True, sm=0, nw=1, mi=2, dr=4, n="%s_%s_%s_Ribbn_skin"%(self.nom, cote, name))
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][7]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), 1)])
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][6]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), 1)])
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][5]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), 1)])
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][4]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), .49), ("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name), .49), ("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), .02)])
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][3]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), .49), ("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name), .49), ("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), .02)])
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][2]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), 1)])
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][1]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), 1)])
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][0]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), 1)])
                    # clean
                    cmds.toggle("%s_%s_%s_Ribbn_GEO"%(self.nom, cote, name), te=True)
                    cmds.group("%s_%s_%s_Ribbn_GEO"%(self.nom, cote, name), "%s_%s_%s_Ribbn_fol_grp"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name), n="%s_%s_%s_Ribbn_GRP"%(self.nom, cote, name))
                    cmds.hide("%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name))
                    cmds.setAttr("%s_%s_%s_RibbnPos_mid_locShape.visibility"%(self.nom, cote, name), False)
                    cmds.setAttr("%s_%s_%s_RibbnAim_mid_locShape.visibility"%(self.nom, cote, name), False)
                    cmds.setAttr("%s_%s_%s_RibbnUp_mid_locShape.visibility"%(self.nom, cote, name), False)
            elif nom == "Leg":
                nomRibbn = ["UpperLeg", "LowerLeg"]
                for name in nomRibbn:
                    # nurbsPlane
                    cmds.nurbsPlane(p=(0, 0, 0), ax=(0, 0, 1), w=.5*scale[0], lr=10, d=3, u=1, v=5, ch=True, n="%s_%s_%s_Ribbn_GEO"%(self.nom, cote, name))
                    cmds.rebuildSurface("%s_%s_%s_Ribbn_GEO"%(self.nom, cote, name), ch=True, rpo=True, rt=0, end=1, kr=0, kcp=False, kc=False, su=1, du=1, sv=5, dv=3, tol=.01, fr=0, dir=2)
                    cmds.delete("%s_%s_%s_Ribbn_GEO"%(self.nom, cote, name), ch=True)
                    # follicle
                    follicles = []
                    for i in range(0,5):
                        fol = cmds.createNode("follicle", n="%s_%s_%s_Ribbn0%i_folShape"%(self.nom, cote, name, (i+1)))
                        follicles.append("%s_%s_%s_Ribbn0%i_fol"%(self.nom, cote, name, (i+1)))
                        cmds.connectAttr("%s_%s_%s_Ribbn_GEOShape.local"%(self.nom, cote, name), "%s_%s_%s_Ribbn0%i_folShape.inputSurface"%(self.nom, cote, name, (i+1)), f=True)
                        cmds.connectAttr("%s_%s_%s_Ribbn_GEOShape.worldMatrix[0]"%(self.nom, cote, name), "%s_%s_%s_Ribbn0%i_folShape.inputWorldMatrix"%(self.nom, cote, name, (i+1)), f=True)
                        cmds.connectAttr("%s_%s_%s_Ribbn0%i_folShape.outRotate"%(self.nom, cote, name, (i+1)), "%s_%s_%s_Ribbn0%i_fol.rotate"%(self.nom, cote, name, (i+1)), f=True)
                        cmds.connectAttr("%s_%s_%s_Ribbn0%i_folShape.outTranslate"%(self.nom, cote, name, (i+1)), "%s_%s_%s_Ribbn0%i_fol.translate"%(self.nom, cote, name, (i+1)), f=True)
                        cmds.setAttr("%s_%s_%s_Ribbn0%i_folShape.parameterU"%(self.nom, cote, name, (i+1)), .5)
                        cmds.setAttr("%s_%s_%s_Ribbn0%i_folShape.parameterV"%(self.nom, cote, name, (i+1)), (float(i) / 5 + .1))
                        lockAndHide(["%s_%s_%s_Ribbn0%i_fol"%(self.nom, cote, name, (i+1))], True, False, ["tx", "ty", "tz", "rx", "ry", "rz"])
                    cmds.group(follicles, n="%s_%s_%s_Ribbn_fol_grp"%(self.nom, cote, name))
                    # joints
                    for i in range(0,5):
                        trY = cmds.getAttr("%s.translateY"%follicles[i])
                        cmds.select(cl=True)
                        cmds.joint(n="%s_%s_%s_Ribbn0%i_jnt"%(self.nom, cote, name, (5-i)), rad=(.25 * scale[0]), p=(0, trY, 0))
                        cmds.parent("%s_%s_%s_Ribbn0%i_jnt"%(self.nom, cote, name, (5-i)), "%s_%s_%s_Ribbn0%i_fol"%(self.nom, cote, name, (i+1)))
                        if cote == "L":
                            cmds.setAttr("%s_%s_%s_Ribbn0%i_jnt.jointOrientX"%(self.nom, cote, name, (5-i)), -90)
                            cmds.setAttr("%s_%s_%s_Ribbn0%i_jnt.jointOrientZ"%(self.nom, cote, name, (5-i)), -90)
                        else:
                            cmds.setAttr("%s_%s_%s_Ribbn0%i_jnt.jointOrientX"%(self.nom, cote, name, (5-i)), -90)
                            cmds.setAttr("%s_%s_%s_Ribbn0%i_jnt.jointOrientZ"%(self.nom, cote, name, (5-i)), 90)
                    # driver joints
                    cmds.select(cl=True)
                    cmds.joint(n="%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), rad=(.3 * scale[0]), p=(0, 2.5 * scale[0], 0))
                    cmds.joint(n="%s_%s_%s_RibbnDriverEnd_hi_jnt"%(self.nom, cote, name), rad=(.3 * scale[0]), p=(0, 1.5 * scale[0], 0))
                    cmds.select(cl=True)
                    cmds.joint(n="%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), rad=(.3 * scale[0]), p=(0, -2.5 * scale[0], 0))
                    cmds.joint(n="%s_%s_%s_RibbnDriverEnd_lox_jnt"%(self.nom, cote, name), rad=(.3 * scale[0]), p=(0, -1.5 * scale[0], 0))
                    cmds.select(cl=True)
                    cmds.joint(n="%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name), rad=(.3 * scale[0]), p=(0, 0, 0))
                    # locators
                    cmds.spaceLocator(n="%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, name))
                    cmds.spaceLocator(n="%s_%s_%s_RibbnAim_hi_loc"%(self.nom, cote, name))
                    cmds.spaceLocator(n="%s_%s_%s_RibbnUp_hi_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnAim_hi_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnUp_hi_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, name))
                    cmds.move(0, 2.5 * scale[0], 0, "%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, name), a=True)
                    cmds.move(0, 0, 5 * scale[0], "%s_%s_%s_RibbnUp_hi_loc"%(self.nom, cote, name), r=True)
                    cmds.spaceLocator(n="%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, name))
                    cmds.spaceLocator(n="%s_%s_%s_RibbnAim_mid_loc"%(self.nom, cote, name))
                    cmds.spaceLocator(n="%s_%s_%s_RibbnUp_mid_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnAim_mid_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnUp_mid_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, name))
                    cmds.move(0, 0, 0, "%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, name), a=True)
                    cmds.move(0, 0, 5 * scale[0], "%s_%s_%s_RibbnUp_mid_loc"%(self.nom, cote, name), r=True)
                    cmds.spaceLocator(n="%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name))
                    cmds.spaceLocator(n="%s_%s_%s_RibbnAim_low_loc"%(self.nom, cote, name))
                    cmds.spaceLocator(n="%s_%s_%s_RibbnUp_low_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnAim_low_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnUp_low_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name))
                    cmds.move(0, -2.5 * scale[0], 0, "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name), a=True)
                    cmds.move(0, 0, 5 * scale[0], "%s_%s_%s_RibbnUp_low_loc"%(self.nom, cote, name), r=True)
                    # contraintes
                    cmds.pointConstraint("%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, name), mo=True, n="%s_%s_%s_RibbnPos_mid_loc_pointContrainte1"%(self.nom, cote, name))
                    cmds.pointConstraint("%s_%s_%s_RibbnUp_hi_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnUp_low_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnUp_mid_loc"%(self.nom, cote, name), mo=True, n="%s_%s_%s_RibbnPos_mid_loc_pointContrainte2"%(self.nom, cote, name))
                    cmds.aimConstraint("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name), "%s_%s_%s_RibbnAim_hi_loc"%(self.nom, cote, name), aim=(1, 0, 0), u=(0, 0, 1), wut="object", wuo="%s_%s_%s_RibbnUp_hi_loc"%(self.nom, cote, name), n="%s_%s_%s_RibbnDriver_hi_jnt_aimContrainte"%(self.nom, cote, name))
                    cmds.aimConstraint("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name), "%s_%s_%s_RibbnAim_low_loc"%(self.nom, cote, name), aim=(1, 0, 0), u=(0, 0, 1), wut="object", wuo="%s_%s_%s_RibbnUp_low_loc"%(self.nom, cote, name), n="%s_%s_%s_RibbnDriver_low_jnt_aimContrainte"%(self.nom, cote, name))
                    cmds.aimConstraint("%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnAim_mid_loc"%(self.nom, cote, name), aim=(0, -1, 0), u=(0, 0, 1), wut="object", wuo="%s_%s_%s_RibbnUp_mid_loc"%(self.nom, cote, name), n="%s_%s_%s_RibbnAim_mid_loc_aimContrainte"%(self.nom, cote, name))
                    # parentage
                    cmds.parent("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), "%s_%s_%s_RibbnAim_hi_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name), "%s_%s_%s_RibbnAim_mid_loc"%(self.nom, cote, name))
                    cmds.parent("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), "%s_%s_%s_RibbnAim_low_loc"%(self.nom, cote, name))
                    # skin
                    cmds.skinCluster("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), "%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name), "%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO"%(self.nom, cote, name), tsb=True, sm=0, nw=1, mi=2, dr=4, n="%s_%s_%s_Ribbn_skin"%(self.nom, cote, name))
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][7]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), 1)])
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][6]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), 1)])
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][5]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), 1)])
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][4]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), .49), ("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name), .49), ("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), .02)])
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][3]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), .49), ("%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name), .49), ("%s_%s_%s_RibbnDriver_hi_jnt"%(self.nom, cote, name), .02)])
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][2]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), 1)])
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][1]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), 1)])
                    cmds.skinPercent("%s_%s_%s_Ribbn_skin"%(self.nom, cote, name), "%s_%s_%s_Ribbn_GEO.cv[0:1][0]"%(self.nom, cote, name), tv=[("%s_%s_%s_RibbnDriver_low_jnt"%(self.nom, cote, name), 1)])
                    # clean
                    cmds.toggle("%s_%s_%s_Ribbn_GEO"%(self.nom, cote, name), te=True)
                    cmds.group("%s_%s_%s_Ribbn_GEO"%(self.nom, cote, name), "%s_%s_%s_Ribbn_fol_grp"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_mid_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name), n="%s_%s_%s_Ribbn_GRP"%(self.nom, cote, name))
                    cmds.hide("%s_%s_%s_RibbnPos_hi_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnPos_low_loc"%(self.nom, cote, name), "%s_%s_%s_RibbnDriver_mid_jnt"%(self.nom, cote, name))
                    cmds.setAttr("%s_%s_%s_RibbnPos_mid_locShape.visibility"%(self.nom, cote, name), False)
                    cmds.setAttr("%s_%s_%s_RibbnAim_mid_locShape.visibility"%(self.nom, cote, name), False)
                    cmds.setAttr("%s_%s_%s_RibbnUp_mid_locShape.visibility"%(self.nom, cote, name), False)
    # end def autoRibbon
    
    # def creaJoints
    def creaJoints(self):
        # majWin
        self.cj = True
        win.majWin()
        #  joints centraux
        self.tempoJnts = []
        self.jointParent("C_Root", "", .7)
        self.jointParent("C_Pelvis", "C_Root", .7)
        self.reorientJoint("C_Root")
        self.rotateLRA("C_Root", -90)
        cmds.parent(("%s_C_Pelvis_jnt"%self.nom), w=True)
        if self.spine == "FK" or self.spine == "Ribbon":
            self.jointParent("C_Middle", "C_Root", .7)
            self.jointParent("C_Chest", "C_Middle", .7)
            self.jointParent("C_MidChest", "C_Chest", .7)
            self.jointParent("C_Neck", "C_MidChest", .7)
            self.jointParent("C_Head", "C_Neck", .35)
            self.jointParent("C_HeadEnd", "C_Head", .35)
            self.reorientJoint("C_Root")
            self.rotateLRA("C_Root", -90)
        elif self.spine == "IK":
            self.jointParent("C_Spine01", "C_Root", .3)
            self.jointParent("C_Spine02", "C_Spine01", .3)
            self.jointParent("C_Spine03", "C_Spine02", .3)
            self.jointParent("C_Spine04", "C_Spine03", .3)
            self.jointParent("C_Spine05", "C_Spine04", .3)
            self.jointParent("C_Spine06", "C_Spine05", .3)
            self.jointParent("C_Spine07", "C_Spine06", .3)
            self.jointParent("C_Spine08", "C_Spine07", .3)
            self.jointParent("C_Neck", "C_Spine08", .7)
            self.jointParent("C_Head", "C_Neck", .35)
            self.jointParent("C_HeadEnd", "C_Head", .35)
            self.reorientJoint("C_Root")
            self.rotateLRA("C_Root", 90)
        if self.spine == "Ribbon":
            self.autoRibbon(["C"], "Spine")
        self.jointParent("C_Jaw", "", .35)
        self.jointParent("C_JawEnd", "C_Jaw", .35)
        self.reorientJoint("C_Jaw")
        cmds.parent(("%s_C_Jaw_jnt"%self.nom), ("%s_C_Head_jnt"%self.nom))
        self.jointParent("L_Eye", "", .6)
        self.jointParent("R_Eye", "", .6)
        cmds.parent(("%s_L_Eye_jnt"%self.nom), ("%s_C_Head_jnt"%self.nom))
        cmds.parent(("%s_R_Eye_jnt"%self.nom), ("%s_C_Head_jnt"%self.nom))
        # scale
        scale = cmds.xform(("%s_Scale_ctrl"%self.nom), q=True, r=True, s=True)
        # arm joints
        clavicle = "%s_L_Clavicle"%self.nom
        shoulder = "%s_L_Shoulder"%self.nom
        elbow = "%s_L_Elbow"%self.nom
        foreArm = "%s_L_ForeArm"%self.nom
        wrist = "%s_L_Wrist"%self.nom
        claviclePos = cmds.xform(("%s_sph"%clavicle), q=True, ws=True, rp=True)
        shoulderPos = cmds.xform(("%s_sph"%shoulder), q=True, ws=True, rp=True)
        elbowPos = cmds.xform(("%s_sph"%elbow), q=True, ws=True, rp=True)
        foreArmPos = cmds.xform(("%s_sph"%foreArm), q=True, ws=True, rp=True)
        wristPos = cmds.xform(("%s_sph"%wrist), q=True, ws=True, rp=True)
        # distance entre les joints
        dist = cmds.distanceDimension(sp=(shoulderPos[0], shoulderPos[1], shoulderPos[2]), ep=(elbowPos[0], elbowPos[1], elbowPos[2]))
        distShoulderElbow = cmds.getAttr("%s.distance"%dist)
        locators = cmds.listConnections(dist)
        cmds.delete(locators)
        dist = cmds.distanceDimension(sp=(elbowPos[0], elbowPos[1], elbowPos[2]), ep=(foreArmPos[0], foreArmPos[1], foreArmPos[2]))
        distElbowForeArm = cmds.getAttr("%s.distance"%dist)
        locators = cmds.listConnections(dist)
        cmds.delete(locators)
        dist = cmds.distanceDimension(sp=(foreArmPos[0], foreArmPos[1], foreArmPos[2]), ep=(wristPos[0], wristPos[1], wristPos[2]))
        distForeArmWrist = cmds.getAttr("%s.distance"%dist)
        locators = cmds.listConnections(dist)
        cmds.delete(locators)
        # creation des joints
        cmds.joint(n=("%s_jnt"%shoulder), rad=(.6*scale[0]), p=(0, 0, 0))
        cmds.joint(n=("%s_jnt"%elbow), rad=(.6*scale[0]), p=(distShoulderElbow, 0, 0))
        cmds.joint(("%s_jnt"%shoulder), e=True, zso=True, oj="xyz", sao="xdown")
        cmds.joint(n=("%s_jnt"%foreArm), rad=(.55*scale[0]), p=((distShoulderElbow + distElbowForeArm), 0, 0))
        cmds.joint(("%s_jnt"%elbow), e=True, zso=True, oj="xyz", sao="xdown")
        cmds.joint(n=("%s_jnt"%wrist), rad=(.5*scale[0]), p=(distShoulderElbow + distElbowForeArm + distForeArmWrist, 0, 0))
        cmds.joint(("%s_jnt"%foreArm), e=True, zso=True, oj="xyz", sao="xdown")
        # positionnement des joints
        cmds.select(cl=True)
        cmds.move(shoulderPos[0], shoulderPos[1], shoulderPos[2], ("%s_jnt"%shoulder), a=True)
        JOShoulder = cmds.angleBetween(er=True, v1=(1, 0, 0), v2=((elbowPos[0] - shoulderPos[0]), (elbowPos[1] - shoulderPos[1]), (elbowPos[2] - shoulderPos[2])))
        cmds.setAttr(("%s_jnt.jointOrient"%shoulder), JOShoulder[0], JOShoulder[1], JOShoulder[2], type="double3")
        # vecteurs
        shoulderElbow = MVector((elbowPos[0] - shoulderPos[0]), (elbowPos[1] - shoulderPos[1]), (elbowPos[2] - shoulderPos[2]))
        elbowWrist = MVector((wristPos[0] - elbowPos[0]), (wristPos[1] - elbowPos[1]), (wristPos[2] - elbowPos[2]))
        # joint Orient
        JOElbow = (-(math.degrees(MVector.angle(shoulderElbow, elbowWrist))))
        cmds.setAttr(("%s_jnt.jointOrientY"%elbow), JOElbow)
        # plane designed by the spheres
        plane1x = shoulderElbow.y * elbowWrist.z - elbowWrist.y * shoulderElbow.z
        plane1y = shoulderElbow.z * elbowWrist.x - elbowWrist.z * shoulderElbow.x
        plane1z = shoulderElbow.x * elbowWrist.y - elbowWrist.x * shoulderElbow.y
        plane1 = MVector(plane1x, plane1y, plane1z)
        # plane designed by the joints
        shoulderPosJnt = cmds.xform(("%s_jnt"%shoulder), q=True, ws=True, rp=True)
        elbowPosJnt = cmds.xform(("%s_jnt"%elbow), q=True, ws=True, rp=True)
        wristPosJnt = cmds.xform(("%s_jnt"%wrist), q=True, ws=True, rp=True)
        shoulderElbowJnt = MVector((elbowPosJnt[0] - shoulderPosJnt[0]), (elbowPosJnt[1] - shoulderPosJnt[1]), (elbowPosJnt[2] - shoulderPosJnt[2]))
        elbowWristJnt = MVector((wristPosJnt[0] - elbowPosJnt[0]), (wristPosJnt[1] - elbowPosJnt[1]), (wristPosJnt[2] - elbowPosJnt[2]))
        plane2x = shoulderElbowJnt.y * elbowWristJnt.z - elbowWristJnt.y * shoulderElbowJnt.z
        plane2y = shoulderElbowJnt.z * elbowWristJnt.x - elbowWristJnt.z * shoulderElbowJnt.x
        plane2z = shoulderElbowJnt.x * elbowWristJnt.y - elbowWristJnt.x * shoulderElbowJnt.y
        plane2 = MVector(plane2x, plane2y, plane2z)
        # angle entre les planes
        JOxShoulderTempo = -(math.degrees(MVector.angle(plane1, plane2)))
        oldJOxShoulder = cmds.getAttr("%s_jnt.jointOrientX"%shoulder)
        newJOxShoulder = oldJOxShoulder + JOxShoulderTempo
        cmds.setAttr(("%s_jnt.jointOrientX"%shoulder), newJOxShoulder)
        wristPosJnt = cmds.xform(("%s_jnt"%wrist), q=True, ws=True, rp=True)
        dist = cmds.distanceDimension(sp=(wristPos[0], wristPos[1], wristPos[2]), ep=(wristPosJnt[0], wristPosJnt[1], wristPosJnt[2]))
        newDistJntSph = cmds.getAttr("%s.distance"%dist)
        locators = cmds.listConnections(dist)
        cmds.delete(locators)
        if newDistJntSph > .01:
            newJOxShoulder = oldJOxShoulder - JOxShoulderTempo
            cmds.setAttr(("%s_jnt.jointOrientX"%shoulder), newJOxShoulder)
        # clavicle
        cmds.joint(n=("%s_jnt"%clavicle), rad=(.6*scale[0]), p=(claviclePos[0], claviclePos[1], claviclePos[2]))
        cmds.parent(("%s_jnt"%shoulder), ("%s_jnt"%clavicle))
        cmds.joint(("%s_jnt"%clavicle), e=True, zso=True, oj="xyz", sao="yup")
        # doigt joints
        self.doigtsJointParent("L_Thumb", .25)
        self.reorientJoint("L_Thumb01")
        self.doigtsJointParent("L_Index", .25)
        self.reorientJoint("L_Index01")
        self.doigtsJointParent("L_Middle", .25)
        self.reorientJoint("L_Middle01")
        self.doigtsJointParent("L_Ring", .25)
        self.reorientJoint("L_Ring01")
        self.doigtsJointParent("L_Pinky", .25)
        self.reorientJoint("L_Pinky01")
        jThumbPos = cmds.xform(("%s_L_Thumb01_jnt"%self.nom), q=True, ws=True, rp=True)
        jPinkyPos = cmds.xform(("%s_L_Pinky01_jnt"%self.nom), q=True, ws=True, rp=True)
        if (jThumbPos[1] - jPinkyPos[1]) > (jThumbPos[2] - jPinkyPos[2]):
            angleArm = self.angleRotationArm()
            cmds.parent(("%s_L_ForeArm_jnt"%self.nom), w=True)
            self.rotateLRA("L_ForeArm", angleArm)
            cmds.parent(("%s_L_ForeArm_jnt"%self.nom), ("%s_L_Elbow_jnt"%self.nom))
            cmds.parent(("%s_L_Wrist_jnt"%self.nom), w=True)
            self.rotateLRA("L_Wrist", angleArm)
            cmds.parent(("%s_L_Wrist_jnt"%self.nom), ("%s_L_ForeArm_jnt"%self.nom))
            self.rotateLRA("L_Thumb01", -90)
            self.rotateLRA("L_Index01", 180)
            self.rotateLRA("L_Middle01", -170)
            self.rotateLRA("L_Ring01", -155)
            self.rotateLRA("L_Pinky01", -145)
        else:
            self.rotateLRA("L_Thumb01", -20)
            self.rotateLRA("L_Index01", 75)
            self.rotateLRA("L_Middle01", 85)
            self.rotateLRA("L_Ring01", 100)
            self.rotateLRA("L_Pinky01", 110)
        cmds.parent(("%s_L_Thumb01_jnt"%self.nom), ("%s_L_Wrist_jnt"%self.nom))
        cmds.parent(("%s_L_Index01_jnt"%self.nom), ("%s_L_Wrist_jnt"%self.nom))
        cmds.parent(("%s_L_Middle01_jnt"%self.nom), ("%s_L_Wrist_jnt"%self.nom))
        cmds.parent(("%s_L_Ring01_jnt"%self.nom), ("%s_L_Wrist_jnt"%self.nom))
        cmds.parent(("%s_L_Pinky01_jnt"%self.nom), ("%s_L_Wrist_jnt"%self.nom))
        cmds.mirrorJoint(("%s_L_Clavicle_jnt"%self.nom), myz=True, mb=True, sr=("_L_", "_R_"))
        # leg joints
        leg = "%s_L_Leg"%self.nom
        knee = "%s_L_Knee"%self.nom
        ankle = "%s_L_Ankle"%self.nom
        ball = "%s_L_Ball"%self.nom
        toe = "%s_L_Toe"%self.nom
        legPos = cmds.xform(("%s_sph"%leg), q=True, ws=True, rp=True)
        kneePos = cmds.xform(("%s_sph"%knee), q=True, ws=True, rp=True)
        anklePos = cmds.xform(("%s_sph"%ankle), q=True, ws=True, rp=True)
        ballPos = cmds.xform(("%s_sph"%ball), q=True, ws=True, rp=True)
        toePos = cmds.xform(("%s_sph"%toe), q=True, ws=True, rp=True)
        # distance entre les joints
        dist = cmds.distanceDimension(sp=(legPos[0], legPos[1], legPos[2]), ep=(kneePos[0], kneePos[1], kneePos[2]))
        distLegKnee = cmds.getAttr("%s.distance"%dist)
        locators = cmds.listConnections(dist)
        cmds.delete(locators)
        dist = cmds.distanceDimension(sp=(kneePos[0], kneePos[1], kneePos[2]), ep=(anklePos[0], anklePos[1], anklePos[2]))
        distKneeAnkle = cmds.getAttr("%s.distance"%dist)
        locators = cmds.listConnections(dist)
        cmds.delete(locators)
        # creation des joints
        cmds.joint(n=("%s_jnt"%leg), rad=(.9*scale[0]), p=(0, 0, 0))
        cmds.joint(n=("%s_jnt"%knee), rad=(.9*scale[0]), p=(distLegKnee, 0, 0))
        cmds.joint(("%s_jnt"%leg), e=True, zso=True, oj="xyz", sao="xdown")
        cmds.joint(n=("%s_jnt"%ankle), rad=(.8*scale[0]), p=((distLegKnee + distKneeAnkle), 0, 0))
        cmds.joint(("%s_jnt"%knee), e=True, zso=True, oj="xyz", sao="xdown")
        # positionnement des joints
        cmds.select(cl=True)
        cmds.move(legPos[0], legPos[1], legPos[2], ("%s_jnt"%leg), a=True)
        JOLeg = cmds.angleBetween(er=True, v1=(1, 0, 0), v2=((kneePos[0] - legPos[0]), (kneePos[1] - legPos[1]), (kneePos[2] - legPos[2])))
        cmds.setAttr(("%s_jnt.jointOrient"%leg), JOLeg[0], JOLeg[1], JOLeg[2], type="double3")
        # vecteurs
        legKnee = MVector((kneePos[0] - legPos[0]), (kneePos[1] - legPos[1]), (kneePos[2] - legPos[2]))
        kneeAnkle = MVector((anklePos[0] - kneePos[0]), (anklePos[1] - kneePos[1]), (anklePos[2] - kneePos[2]))
        # joint Orient
        JOKnee = (-(math.degrees(MVector.angle(legKnee, kneeAnkle))))
        cmds.setAttr(("%s_jnt.jointOrientY"%knee), JOKnee)
        # plane designed by the spheres
        plane1x = legKnee.y * kneeAnkle.z - kneeAnkle.y * legKnee.z
        plane1y = legKnee.z * kneeAnkle.x - kneeAnkle.z * legKnee.x
        plane1z = legKnee.x * kneeAnkle.y - kneeAnkle.x * legKnee.y
        plane1 = MVector(plane1x, plane1y, plane1z)
        # plane designed by the joints
        legPosJnt = cmds.xform(("%s_jnt"%leg), q=True, ws=True, rp=True)
        kneePosJnt = cmds.xform(("%s_jnt"%knee), q=True, ws=True, rp=True)
        anklePosJnt = cmds.xform(("%s_jnt"%ankle), q=True, ws=True, rp=True)
        legKneeJnt = MVector((kneePosJnt[0] - legPosJnt[0]), (kneePosJnt[1] - legPosJnt[1]), (kneePosJnt[2] - legPosJnt[2]))
        kneeAnkleJnt = MVector((anklePosJnt[0] - kneePosJnt[0]), (anklePosJnt[1] - kneePosJnt[1]), (anklePosJnt[2] - kneePosJnt[2]))
        plane2x = legKneeJnt.y * kneeAnkleJnt.z - kneeAnkleJnt.y * legKneeJnt.z
        plane2y = legKneeJnt.z * kneeAnkleJnt.x - kneeAnkleJnt.z * legKneeJnt.x
        plane2z = legKneeJnt.x * kneeAnkleJnt.y - kneeAnkleJnt.x * legKneeJnt.y
        plane2 = MVector(plane2x, plane2y, plane2z)
        # angle entre les planes
        JOxLegTempo = (math.degrees(MVector.angle(plane1, plane2)))
        oldJOxLeg = cmds.getAttr("%s_jnt.jointOrientX"%leg)
        newJOxLeg = oldJOxLeg + JOxLegTempo
        cmds.setAttr(("%s_jnt.jointOrientX"%leg), newJOxLeg)
        anklePosJnt = cmds.xform(("%s_jnt"%ankle), q=True, ws=True, rp=True)
        dist = cmds.distanceDimension(sp=(anklePos[0], anklePos[1], anklePos[2]), ep=(anklePosJnt[0], anklePosJnt[1], anklePosJnt[2]))
        newDistJntSph = cmds.getAttr("%s.distance"%dist)
        locators = cmds.listConnections(dist)
        cmds.delete(locators)
        if newDistJntSph > .01:
            newJOxLeg = oldJOxLeg - JOxLegTempo
            cmds.setAttr(("%s_jnt.jointOrientX"%leg), JOxLegTempo)
        # suite leg
        self.jointParent("L_Ball", "L_Ankle", .7)
        self.jointParent("L_Toe", "L_Ball", .7)
        self.reorientJoint("L_Ankle")
        self.rotateLRA("L_Ankle",-90)
        cmds.parent(("%s_L_Ankle_jnt"%self.nom), ("%s_L_Knee_jnt"%self.nom))
        self.rotateLRA("L_Leg",180)
        cmds.mirrorJoint(("%s_L_Leg_jnt"%self.nom), myz=True, mb=True, sr=("_L_", "_R_"))
        cmds.parent(("%s_L_Thumb01_jnt"%self.nom), ("%s_L_Index01_jnt"%self.nom), ("%s_L_Middle01_jnt"%self.nom), ("%s_L_Ring01_jnt"%self.nom), ("%s_L_Pinky01_jnt"%self.nom), w=True)
        cmds.parent(("%s_R_Thumb01_jnt"%self.nom), ("%s_R_Index01_jnt"%self.nom), ("%s_R_Middle01_jnt"%self.nom), ("%s_R_Ring01_jnt"%self.nom), ("%s_R_Pinky01_jnt"%self.nom), w=True)
        if self.spine == "FK":
            cmds.parent(("%s_C_Head_jnt"%self.nom), w=True)
            self.tempoJnts = ["%s_C_Root_jnt"%self.nom, "%s_C_Middle_jnt"%self.nom, "%s_C_Chest_jnt"%self.nom, "%s_C_MidChest_jnt"%self.nom, "%s_C_Neck_jnt"%self.nom, "%s_C_Pelvis_jnt"%self.nom, "%s_L_Clavicle_jnt"%self.nom, "%s_L_Shoulder_jnt"%self.nom, "%s_L_Elbow_jnt"%self.nom, "%s_L_ForeArm_jnt"%self.nom, "%s_L_Wrist_jnt"%self.nom, "%s_R_Clavicle_jnt"%self.nom, "%s_R_Shoulder_jnt"%self.nom, "%s_R_Elbow_jnt"%self.nom, "%s_R_ForeArm_jnt"%self.nom, "%s_R_Wrist_jnt"%self.nom, "%s_L_Leg_jnt"%self.nom, "%s_L_Knee_jnt"%self.nom, "%s_L_Ankle_jnt"%self.nom, "%s_L_Ball_jnt"%self.nom, "%s_L_Toe_jnt"%self.nom, "%s_R_Leg_jnt"%self.nom, "%s_R_Knee_jnt"%self.nom, "%s_R_Ankle_jnt"%self.nom, "%s_R_Ball_jnt"%self.nom, "%s_R_Toe_jnt"%self.nom, "%s_L_Thumb01_jnt"%self.nom, "%s_L_Thumb02_jnt"%self.nom, "%s_L_Thumb03_jnt"%self.nom, "%s_L_Thumb04_jnt"%self.nom, "%s_L_Index01_jnt"%self.nom, "%s_L_Index02_jnt"%self.nom, "%s_L_Index03_jnt"%self.nom, "%s_L_Index04_jnt"%self.nom, "%s_L_Middle01_jnt"%self.nom, "%s_L_Middle02_jnt"%self.nom, "%s_L_Middle03_jnt"%self.nom, "%s_L_Middle04_jnt"%self.nom, "%s_L_Ring01_jnt"%self.nom, "%s_L_Ring02_jnt"%self.nom, "%s_L_Ring03_jnt"%self.nom, "%s_L_Ring04_jnt"%self.nom, "%s_L_Pinky01_jnt"%self.nom, "%s_L_Pinky02_jnt"%self.nom, "%s_L_Pinky03_jnt"%self.nom, "%s_L_Pinky04_jnt"%self.nom, "%s_R_Thumb01_jnt"%self.nom, "%s_R_Thumb02_jnt"%self.nom, "%s_R_Thumb03_jnt"%self.nom, "%s_R_Thumb04_jnt"%self.nom, "%s_R_Index01_jnt"%self.nom, "%s_R_Index02_jnt"%self.nom, "%s_R_Index03_jnt"%self.nom, "%s_R_Index04_jnt"%self.nom, "%s_R_Middle01_jnt"%self.nom, "%s_R_Middle02_jnt"%self.nom, "%s_R_Middle03_jnt"%self.nom, "%s_R_Middle04_jnt"%self.nom, "%s_R_Ring01_jnt"%self.nom, "%s_R_Ring02_jnt"%self.nom, "%s_R_Ring03_jnt"%self.nom, "%s_R_Ring04_jnt"%self.nom, "%s_R_Pinky01_jnt"%self.nom, "%s_R_Pinky02_jnt"%self.nom, "%s_R_Pinky03_jnt"%self.nom, "%s_R_Pinky04_jnt"%self.nom, "%s_C_Head_jnt"%self.nom, "%s_C_HeadEnd_jnt"%self.nom, "%s_C_Jaw_jnt"%self.nom, "%s_C_JawEnd_jnt"%self.nom, "%s_L_Eye_jnt"%self.nom, "%s_R_Eye_jnt"%self.nom]
        elif self.spine == "IK":
            cmds.parent(("%s_C_Neck_jnt"%self.nom), w=True)
            self.tempoJnts = ["%s_C_Root_jnt"%self.nom, "%s_C_Spine01_jnt"%self.nom, "%s_C_Spine02_jnt"%self.nom, "%s_C_Spine03_jnt"%self.nom, "%s_C_Spine04_jnt"%self.nom, "%s_C_Spine05_jnt"%self.nom, "%s_C_Spine06_jnt"%self.nom, "%s_C_Spine07_jnt"%self.nom, "%s_C_Spine08_jnt"%self.nom, "%s_C_Pelvis_jnt"%self.nom, "%s_L_Clavicle_jnt"%self.nom, "%s_L_Shoulder_jnt"%self.nom, "%s_L_Elbow_jnt"%self.nom, "%s_L_ForeArm_jnt"%self.nom, "%s_L_Wrist_jnt"%self.nom, "%s_R_Clavicle_jnt"%self.nom, "%s_R_Shoulder_jnt"%self.nom, "%s_R_Elbow_jnt"%self.nom, "%s_R_ForeArm_jnt"%self.nom, "%s_R_Wrist_jnt"%self.nom, "%s_L_Leg_jnt"%self.nom, "%s_L_Knee_jnt"%self.nom, "%s_L_Ankle_jnt"%self.nom, "%s_L_Ball_jnt"%self.nom, "%s_L_Toe_jnt"%self.nom, "%s_R_Leg_jnt"%self.nom, "%s_R_Knee_jnt"%self.nom, "%s_R_Ankle_jnt"%self.nom, "%s_R_Ball_jnt"%self.nom, "%s_R_Toe_jnt"%self.nom, "%s_L_Thumb01_jnt"%self.nom, "%s_L_Thumb02_jnt"%self.nom, "%s_L_Thumb03_jnt"%self.nom, "%s_L_Thumb04_jnt"%self.nom, "%s_L_Index01_jnt"%self.nom, "%s_L_Index02_jnt"%self.nom, "%s_L_Index03_jnt"%self.nom, "%s_L_Index04_jnt"%self.nom, "%s_L_Middle01_jnt"%self.nom, "%s_L_Middle02_jnt"%self.nom, "%s_L_Middle03_jnt"%self.nom, "%s_L_Middle04_jnt"%self.nom, "%s_L_Ring01_jnt"%self.nom, "%s_L_Ring02_jnt"%self.nom, "%s_L_Ring03_jnt"%self.nom, "%s_L_Ring04_jnt"%self.nom, "%s_L_Pinky01_jnt"%self.nom, "%s_L_Pinky02_jnt"%self.nom, "%s_L_Pinky03_jnt"%self.nom, "%s_L_Pinky04_jnt"%self.nom, "%s_R_Thumb01_jnt"%self.nom, "%s_R_Thumb02_jnt"%self.nom, "%s_R_Thumb03_jnt"%self.nom, "%s_R_Thumb04_jnt"%self.nom, "%s_R_Index01_jnt"%self.nom, "%s_R_Index02_jnt"%self.nom, "%s_R_Index03_jnt"%self.nom, "%s_R_Index04_jnt"%self.nom, "%s_R_Middle01_jnt"%self.nom, "%s_R_Middle02_jnt"%self.nom, "%s_R_Middle03_jnt"%self.nom, "%s_R_Middle04_jnt"%self.nom, "%s_R_Ring01_jnt"%self.nom, "%s_R_Ring02_jnt"%self.nom, "%s_R_Ring03_jnt"%self.nom, "%s_R_Ring04_jnt"%self.nom, "%s_R_Pinky01_jnt"%self.nom, "%s_R_Pinky02_jnt"%self.nom, "%s_R_Pinky03_jnt"%self.nom, "%s_R_Pinky04_jnt"%self.nom, "%s_C_Neck_jnt"%self.nom, "%s_C_Head_jnt"%self.nom, "%s_C_HeadEnd_jnt"%self.nom, "%s_C_Jaw_jnt"%self.nom, "%s_C_JawEnd_jnt"%self.nom, "%s_L_Eye_jnt"%self.nom, "%s_R_Eye_jnt"%self.nom]
        cmds.select(cl=True)
        cmds.setAttr(("%s_Scale_ctrl.visibility"%self.nom), 0)
        print "Joints for %s created"%self.nom
    # end def creaJoints
    
    # def autoRig
    def autoRig(self):
        self.ar = True
        win.majWin()
        # debut autoRig
        cmds.symmetricModelling(e=True, s=False)
        cmds.softSelect(sse=False)
        # variables
        self.joints = []
        self.ctrls = []
        scale = cmds.xform(("%s_Scale_ctrl"%self.nom), q=True, r=True, s=True)
        # leg
        if not self.legIK and not self.legFK:
            self.legIK = True
        if self.legIK:
            auto.legIK(self.nom, ["L", "R"])
            self.joints.extend(["%s_L_LegIK_jnt"%self.nom, "%s_R_LegIK_jnt"%self.nom, "%s_L_KneeIK_jnt"%self.nom, "%s_R_KneeIK_jnt"%self.nom, "%s_L_AnkleIK_jnt"%self.nom, "%s_R_AnkleIK_jnt"%self.nom, "%s_L_BallIK_jnt"%self.nom, "%s_R_BallIK_jnt"%self.nom, "%s_L_ToeIK_jnt"%self.nom, "%s_R_ToeIK_jnt"%self.nom])
        if self.legFK:
            auto.legFK(self.nom, ["L", "R"])
            self.joints.extend(["%s_L_LegFK_jnt"%self.nom, "%s_R_LegFK_jnt"%self.nom, "%s_L_KneeFK_jnt"%self.nom, "%s_R_KneeFK_jnt"%self.nom, "%s_L_AnkleFK_jnt"%self.nom, "%s_R_AnkleFK_jnt"%self.nom, "%s_L_BallFK_jnt"%self.nom, "%s_R_BallFK_jnt"%self.nom, "%s_L_ToeFK_jnt"%self.nom, "%s_R_ToeFK_jnt"%self.nom])
        if self.legRibbon:
            self.autoRibbon(["L", "R"], "Leg")
            auto.legRibbon(self.nom, ["L", "R"])
            cs = ["L_UpperLeg", "R_UpperLeg", "L_LowerLeg", "R_LowerLeg"]
            for c in cs:
                for i in range(1,6):
                    self.joints.extend(["%s_%s_Ribbn0%i_jnt"%(self.nom, c, i)])
        if self.legIK and self.legFK:
            auto.switchLeg(self.nom, ["L", "R"])
            self.joints.extend(["%s_L_Leg_jnt"%self.nom, "%s_R_Leg_jnt"%self.nom, "%s_L_Knee_jnt"%self.nom, "%s_R_Knee_jnt"%self.nom, "%s_L_Ankle_jnt"%self.nom, "%s_R_Ankle_jnt"%self.nom, "%s_L_Ball_jnt"%self.nom, "%s_R_Ball_jnt"%self.nom, "%s_L_Toe_jnt"%self.nom, "%s_R_Toe_jnt"%self.nom])
        else:
            cmds.delete(("%s_L_Leg_jnt"%self.nom), ("%s_R_Leg_jnt"%self.nom))
        self.joints.extend(["%s_C_Pelvis_jnt"%self.nom])
        # arm
        if not self.armIK and not self.armFK:
            self.armFK = True
        if self.armFK:
            auto.armFK(self.nom, ["L", "R"])
            self.joints.extend(["%s_L_ShoulderFK_jnt"%self.nom, "%s_R_ShoulderFK_jnt"%self.nom, "%s_L_ElbowFK_jnt"%self.nom, "%s_R_ElbowFK_jnt"%self.nom, "%s_L_ForeArmFK_jnt"%self.nom, "%s_R_ForeArmFK_jnt"%self.nom, "%s_L_WristFK_jnt"%self.nom, "%s_R_WristFK_jnt"%self.nom])
        if self.armIK:
            auto.armIK(self.nom, ["L", "R"])
            self.joints.extend(["%s_L_ShoulderIK_jnt"%self.nom, "%s_R_ShoulderIK_jnt"%self.nom, "%s_L_ElbowIK_jnt"%self.nom, "%s_R_ElbowIK_jnt"%self.nom, "%s_L_ForeArmIK_jnt"%self.nom, "%s_R_ForeArmIK_jnt"%self.nom, "%s_L_WristIK_jnt"%self.nom, "%s_R_WristIK_jnt"%self.nom])
        if self.armRibbon:
            self.autoRibbon(["L", "R"], "Arm")
            auto.armRibbon(self.nom, ["L", "R"])
            cs = ["L_UpperArm", "R_UpperArm", "L_LowerArm", "R_LowerArm"]
            for c in cs:
                for i in range(1,6):
                    self.joints.extend(["%s_%s_Ribbn0%i_jnt"%(self.nom, c, i)])
        # doigts et clavicule
        if not self.handCtrl and not self.handUltimate and not self.handFK:
            self.handCtrl = True
        auto.fingersAndClavicle(self.nom, ["L", "R"], self.handCtrl, self.handUltimate, self.handFK, self.armFK)
        fingersName = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
        for finger in fingersName:
            for i in range(1, 5):
                self.joints.extend(["%s_L_%s0%i_jnt"%(self.nom, finger, i), "%s_R_%s0%i_jnt"%(self.nom, finger, i)])
        self.joints.extend(["%s_L_Clavicle_jnt"%self.nom, "%s_R_Clavicle_jnt"%self.nom])
        # arm suite
        if self.armIK and self.armFK:
            auto.switchArm(self.nom, ["L", "R"])
            self.joints.extend(["%s_L_Shoulder_jnt"%self.nom, "%s_R_Shoulder_jnt"%self.nom, "%s_L_Elbow_jnt"%self.nom, "%s_R_Elbow_jnt"%self.nom, "%s_L_ForeArm_jnt"%self.nom, "%s_R_ForeArm_jnt"%self.nom, "%s_L_Wrist_jnt"%self.nom, "%s_R_Wrist_jnt"%self.nom])
        else:
            cmds.delete(("%s_L_Shoulder_jnt"%self.nom), ("%s_R_Shoulder_jnt"%self.nom))
        # fingers suite
        auto.parentFingers(self.nom, ["L", "R"], self.armIK, self.armFK, self.handCtrl, self.handFK, self.handUltimate)
        # spine
        if self.spine == "IK":
            auto.spineIK(self.nom)
            self.joints.extend(["%s_C_Root_jnt"%self.nom, "%s_C_Spine01_jnt"%self.nom, "%s_C_Spine02_jnt"%self.nom, "%s_C_Spine03_jnt"%self.nom, "%s_C_Spine04_jnt"%self.nom, "%s_C_Spine05_jnt"%self.nom, "%s_C_Spine06_jnt"%self.nom, "%s_C_Spine07_jnt"%self.nom, "%s_C_Spine08_jnt"%self.nom])
        elif self.spine == "FK":
            auto.spineFK(self.nom)
            self.joints.extend(["%s_C_Root_jnt"%self.nom, "%s_C_Middle_jnt"%self.nom, "%s_C_Chest_jnt"%self.nom, "%s_C_MidChest_jnt"%self.nom])
        elif self.spine == "Ribbon":
            auto.spineRibbon(self.nom)
            self.joints.extend(["%s_C_Root_jnt"%self.nom, "%s_C_Spine_Ribbn01_jnt"%self.nom, "%s_C_Spine_Ribbn02_jnt"%self.nom, "%s_C_Spine_Ribbn03_jnt"%self.nom, "%s_C_Spine_Ribbn04_jnt"%self.nom, "%s_C_Spine_Ribbn05_jnt"%self.nom, "%s_C_Chest_jnt"%self.nom, "%s_C_MidChest_jnt"%self.nom])
        #head
        if self.head == "IK":
            auto.headIK(self.nom, self.spine)
            self.joints.extend(["%s_C_Neck_jnt"%self.nom, "%s_C_Head_jnt"%self.nom, "%s_C_HeadEnd_jnt"%self.nom, "%s_C_Jaw_jnt"%self.nom, "%s_C_JawEnd_jnt"%self.nom, "%s_R_Eye_jnt"%self.nom, "%s_L_Eye_jnt"%self.nom])
        elif self.head == "FK":
            auto.headFK(self.nom, self.spine)
            self.joints.extend(["%s_C_Neck_jnt"%self.nom, "%s_C_Head_jnt"%self.nom, "%s_C_HeadEnd_jnt"%self.nom, "%s_C_Jaw_jnt"%self.nom, "%s_C_JawEnd_jnt"%self.nom, "%s_R_Eye_jnt"%self.nom, "%s_L_Eye_jnt"%self.nom])
        #parentage
        # leg
        if self.legFK:
            cmds.parent(("%s_L_LegFK_jnt"%self.nom), ("%s_C_Pelvis_jnt"%self.nom))
            cmds.parent(("%s_R_LegFK_jnt"%self.nom), ("%s_C_Pelvis_jnt"%self.nom))
            cmds.parent(("%s_L_LegFK_grp"%self.nom), ("%s_C_Pelvis_ctrl"%self.nom))
            cmds.parent(("%s_R_LegFK_grp"%self.nom), ("%s_C_Pelvis_ctrl"%self.nom))
        if self.legIK:
            cmds.parent(("%s_L_LegIK_jnt"%self.nom), ("%s_C_Pelvis_jnt"%self.nom))
            cmds.parent(("%s_R_LegIK_jnt"%self.nom), ("%s_C_Pelvis_jnt"%self.nom))
        if self.legIK and self.legFK:
            cmds.parent(("%s_L_Leg_jnt"%self.nom), ("%s_C_Pelvis_jnt"%self.nom))
            cmds.parent(("%s_R_Leg_jnt"%self.nom), ("%s_C_Pelvis_jnt"%self.nom))
        # spine
        if self.spine == "IK":
            cmds.parent(("%s_L_Clavicle_jnt"%self.nom), ("%s_C_Spine07_jnt"%self.nom))
            cmds.parent(("%s_R_Clavicle_jnt"%self.nom), ("%s_C_Spine07_jnt"%self.nom))
            cmds.parent(("%s_L_Clavicle_grp"%self.nom), ("%s_C_SpineUpIK_ctrl"%self.nom))
            cmds.parent(("%s_R_Clavicle_grp"%self.nom), ("%s_C_SpineUpIK_ctrl"%self.nom))
            if self.head == "IK":
                cmds.parent(("%s_C_Head_ctrl"%self.nom),("%s_C_SpineUpIK_ctrl"%self.nom))
                cmds.pointConstraint(("%s_C_SpineUpIK_ctrl"%self.nom), ("%s_C_Neck_jnt"%self.nom), n=("%s_C_Neck_pointConstraint"%self.nom))
            if self.head == "FK":
                cmds.parent(("%s_C_Neck_ctrl"%self.nom), ("%s_C_SpineUpIK_ctrl"%self.nom))
                cmds.parentConstraint(("%s_C_Neck_ctrl"%self.nom), ("%s_C_Neck_jnt"%self.nom), mo=True, n=("%s_C_Neck_parentConstraint"%self.nom))
                lockAndHide([("%s_C_Neck_ctrl"%self.nom)], True, True, ["tx", "ty", "tz", "sx", "sy", "sz", "v"])
        if self.spine == "FK":
            cmds.parent(("%s_L_Clavicle_jnt"%self.nom), ("%s_C_MidChest_jnt"%self.nom))
            cmds.parent(("%s_R_Clavicle_jnt"%self.nom), ("%s_C_MidChest_jnt"%self.nom))
            cmds.parent(("%s_L_Clavicle_grp"%self.nom), ("%s_C_Chest_ctrl"%self.nom))
            cmds.parent(("%s_R_Clavicle_grp"%self.nom), ("%s_C_Chest_ctrl"%self.nom))
            if self.head == "IK":
                cmds.parent(("%s_C_Head_ctrl"%self.nom), ("%s_C_Chest_ctrl"%self.nom))
            if self.head == "FK":
                cmds.parent(("%s_C_Neck_ctrl"%self.nom), ("%s_C_Chest_ctrl"%self.nom))
                lockAndHide([("%s_C_Neck_ctrl"%self.nom)], True, True, ["tx", "ty", "tz", "sx", "sy", "sz", "v"])
        if self.spine == "Ribbon":
            cmds.parent(("%s_L_Clavicle_jnt"%self.nom), ("%s_C_MidChest_jnt"%self.nom))
            cmds.parent(("%s_R_Clavicle_jnt"%self.nom), ("%s_C_MidChest_jnt"%self.nom))
            cmds.parent(("%s_L_Clavicle_grp"%self.nom), ("%s_C_Chest_ctrl"%self.nom))
            cmds.parent(("%s_R_Clavicle_grp"%self.nom), ("%s_C_Chest_ctrl"%self.nom))
            if self.head == "IK":
                cmds.parent(("%s_C_Head_ctrl"%self.nom),("%s_C_Chest_ctrl"%self.nom))
            if self.head == "FK":
                cmds.parent(("%s_C_Neck_ctrl"%self.nom), ("%s_C_Chest_ctrl"%self.nom))
                lockAndHide([("%s_C_Neck_ctrl"%self.nom)], True, True, ["tx", "ty", "tz", "sx", "sy", "sz", "v"])
        # layers
        cmds.createDisplayLayer(self.joints, n=("%s_SKELETON_Layer"%self.nom), nr=True)
        if self.spine == "Ribbon":
            cmds.editDisplayLayerMembers("%s_SKELETON_Layer"%self.nom, "%s_C_Spine_Ribbn_GEO"%self.nom, "%s_C_Spine_Ribbn_fol_grp"%self.nom)
        if self.armRibbon:
            cmds.editDisplayLayerMembers("%s_SKELETON_Layer"%self.nom, "%s_L_LowerArm_Ribbn_GEO"%self.nom, "%s_L_LowerArm_Ribbn_fol_grp"%self.nom, "%s_R_LowerArm_Ribbn_GEO"%self.nom, "%s_R_LowerArm_Ribbn_fol_grp"%self.nom, "%s_L_UpperArm_Ribbn_GEO"%self.nom, "%s_L_UpperArm_Ribbn_fol_grp"%self.nom, "%s_R_UpperArm_Ribbn_GEO"%self.nom, "%s_R_UpperArm_Ribbn_fol_grp"%self.nom)
        if self.legRibbon:
            cmds.editDisplayLayerMembers("%s_SKELETON_Layer"%self.nom, "%s_L_LowerLeg_Ribbn_GEO"%self.nom, "%s_L_LowerLeg_Ribbn_fol_grp"%self.nom, "%s_R_LowerLeg_Ribbn_GEO"%self.nom, "%s_R_LowerLeg_Ribbn_fol_grp"%self.nom, "%s_L_UpperLeg_Ribbn_GEO"%self.nom, "%s_L_UpperLeg_Ribbn_fol_grp"%self.nom, "%s_R_UpperLeg_Ribbn_GEO"%self.nom, "%s_R_UpperLeg_Ribbn_fol_grp"%self.nom)
        # set selection
        auto.jointsSet(self.nom, self.legIK, self.legFK, self.legRibbon, self.armIK, self.armFK, self.armRibbon, self.head, self.spine)
        cmds.setAttr(("%s_SKELETON_Layer.displayType"%self.nom), 1)
        # ctrl
        # Ultimate
        cmds.curve(d=True, p=[(3, 0, 1), (1, 0, 1), (1, 0, 3), (2, 0, 3), (0, 0, 7), (-2, 0, 3), (-1, 0, 3), (-1, 0, 1), (-3, 0, 1), (-3, 0, 2), (-7, 0, 0), (-3, 0, -2), (-3, 0, -1), (-1, 0, -1), (-1, 0, -3), (-2, 0, -3), (0, 0, -7), (2, 0, -3), (1, 0, -3), (1, 0, -1), (3, 0, -1), (3, 0, -2), (7, 0, 0), (3, 0, 2), (3, 0, 1)], n=("%s_C_Ultimate_ctrl"%self.nom))
        cmds.scale((1.5 * scale[0]), (1.5 * scale[0]), (1.5 * scale[0]), ("%s_C_Ultimate_ctrl"%self.nom), r=True, os=True)
        cmds.makeIdentity("%s_C_Ultimate_ctrl"%self.nom, a=True, t=True, r=True, s=True, n=False)
        cmds.delete("%s_C_Ultimate_ctrl"%self.nom, ch=True)
        colorize("C", [("%s_C_Ultimate_ctrl"%self.nom)])
        # nom perso
        cmds.textCurves(ch=False, f="Arial|w400|h-11", t=("%s"%self.nom))
        cmds.rename("%s_C_Nom_grp"%self.nom)
        cmds.CenterPivot()
        cmds.rotate(-90, 0, 0)
        cmds.move(0, 0, (-12 * scale[0]), ("%s_C_Nom_grp"%self.nom), rpr=True)
        cmds.scale(scale[0], scale[0], scale[0], ("%s_C_Nom_grp"%self.nom))
        cmds.parent(("%s_C_Nom_grp"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
        lockAndHide([("%s_C_Nom_grp"%self.nom)], True, True, ["sx", "sy", "sz", "rx", "ry", "rz", "tx", "ty", "tz", "v"])
        lettres = cmds.listRelatives(ad=True, typ="transform")
        for lettre in lettres:
            lockAndHide([lettre], True, True, ["sx", "sy", "sz", "rx", "ry", "rz", "tx", "ty", "tz", "v"])
            colorize("C", [lettre])
        cmds.toggle("%s_C_Nom_grp"%self.nom, te=True)
        # parentage ctrl
        cmds.group(em=True, n=("%s_CTRL"%self.nom))
        cmds.group(em=True, n=("%s_XTRAS"%self.nom))
        # stretch
        if self.armIK and self.armRibbon:
            auto.stretchArm(self.nom, ["L", "R"])
        if self.legIK and self.legRibbon:
            auto.stretchLeg(self.nom, ["L", "R"])
        if self.spine == "Ribbon":
            auto.stretchSpine(self.nom)
        # arm
        if self.armIK:
            cmds.parent(("%s_L_ElbowIK_ctrl"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
            cmds.parent(("%s_R_ElbowIK_ctrl"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
            cmds.parent(("%s_L_ArmIK_grp"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
            cmds.parent(("%s_R_ArmIK_grp"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
        # leg
        if self.legIK:
            cmds.parent(("%s_L_KneeIK_ctrl"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
            cmds.parent(("%s_R_KneeIK_ctrl"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
            cmds.parent(("%s_L_Foot_ctrl"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
            cmds.parent(("%s_R_Foot_ctrl"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
        # spine
        if self.spine == "FK":
            cmds.parent(("%s_C_Root_ctrl"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
            cmds.parent(("%s_C_Ultimate_ctrl"%self.nom), ("%s_CTRL"%self.nom))
            if self.head != "FK":
                cmds.parent(("%s_C_Neck_ikhl"%self.nom), ("%s_XTRAS"%self.nom))
            cmds.group(("%s_C_Root_jnt"%self.nom), ("%s_C_Chest_jnt"%self.nom), ("%s_C_Middle_grp"%self.nom), n=("%s_SKELETON"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_SKELETON"%self.nom), n=("%s_Skeleton_Scale_contrainte"%self.nom))
            cmds.delete(("%s_Scale_ctrl"%self.nom))
        if self.spine == "IK":
            cmds.parent(("%s_C_COG_ctrl"%self.nom),("%s_C_Ultimate_ctrl"%self.nom))
            cmds.parent(("%s_C_Ultimate_ctrl"%self.nom), ("%s_C_SpineLowIK_grp"%self.nom),("%s_C_SpineMidIK_grp"%self.nom), ("%s_C_SpineUpIK_grp"%self.nom), ("%s_CTRL"%self.nom))
            cmds.parent(("%s_C_Spine_crv"%self.nom), ("%s_C_Spine_ikhl"%self.nom), ("%s_XTRAS"%self.nom))
            if self.head == "IK":
                cmds.parent(("%s_C_Neck_ikhl"%self.nom), ("%s_XTRAS"%self.nom))
            cmds.group(("%s_C_Pelvis_jnt"%self.nom), n=("%s_C_Pelvis_grp"%self.nom))
            cmds.group(("%s_C_Neck_jnt"%self.nom), n=("%s_C_Neck_grp"%self.nom))
            cmds.group(("%s_C_Spine_grp"%self.nom), ("%s_C_Pelvis_grp"%self.nom), ("%s_C_Neck_grp"%self.nom), n=("%s_SKELETON"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_C_Spine_Transform_grp"%self.nom), n=("%s_C_Spine_Transform_scale"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_C_Pelvis_grp"%self.nom), n=("%s_C_Pelvis_scale"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_C_Neck_grp"%self.nom), n=("%s_C_Neck_scale"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_C_SpineUpIK_ctrl"%self.nom), n=("%s_C_SpineUpIK_scale"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_C_SpineMidIK_ctrl"%self.nom), n=("%s_C_SpineMidIK_scale"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_C_SpineLowIK_ctrl"%self.nom), n=("%s_C_SpineLowIK_scale"%self.nom), sk="y")
            curveInfo = cmds.listConnections(("%s_C_Spine_crvShape"%self.nom), s=False)
            curveLength = cmds.getAttr("%s.arcLength"%curveInfo[0])
            cmds.shadingNode("multiplyDivide", n=("%s_C_Gscale_Spine_md"%self.nom), au=True)
            cmds.setAttr(("%s_C_Gscale_Spine_md.input1X"%self.nom), (curveLength))
            cmds.connectAttr(("%s_C_Ultimate_ctrl.scaleY"%self.nom), ("%s_C_Gscale_Spine_md.input2X"%self.nom))
            cmds.connectAttr(("%s_C_Gscale_Spine_md.outputX"%self.nom), ("%s_C_SpineStretch_cnd.secondTerm"%self.nom))
            cmds.connectAttr(("%s_C_Gscale_Spine_md.outputX"%self.nom), ("%s_C_SpineStretch_md.input2X"%self.nom))
            lockAndHide([("%s_C_SpineMidFK_ctrl"%self.nom), ("%s_C_SpineUpFK_ctrl"%self.nom), ("%s_C_SpineLowIK_ctrl"%self.nom), ("%s_C_SpineUpIK_ctrl"%self.nom)], True, True, ["sx", "sy", "sz", "v"])
            lockAndHide([("%s_C_SpineMidIK_ctrl"%self.nom)], True, True, ["rx", "ry", "rz", "sx", "sy", "sz", "v"])
            cmds.delete("%s_Scale_ctrl"%self.nom)
        if self.spine == "Ribbon":
            cmds.parent(("%s_C_Root_ctrl"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
            cmds.parent(("%s_C_Ultimate_ctrl"%self.nom), ("%s_CTRL"%self.nom))
            if self.head == "IK":
                cmds.parent(("%s_C_Neck_ikhl"%self.nom), ("%s_XTRAS"%self.nom))
            cmds.group(("%s_C_Root_jnt"%self.nom), ("%s_C_Chest_jnt"%self.nom), n=("%s_SKELETON"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_SKELETON"%self.nom), n=("%s_Skeleton_Scale_contrainte"%self.nom))
            cmds.delete(("%s_Scale_ctrl"%self.nom))
            cmds.parent(("%s_C_Spine_Ribbn_GRP"%self.nom), ("%s_XTRAS"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_C_SpineOff_grp"%self.nom), n=("%s_C_SpineOff_scale"%self.nom))
            for i in range(1,6):
                cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_C_Spine_Ribbn0%i_fol"%(self.nom, i)))
        if (self.armIK and self.armFK) or self.handCtrl:
            cmds.parent(("%s_L_Hand_ctrl"%self.nom), ("%s_CTRL"%self.nom))
            cmds.parent(("%s_R_Hand_ctrl"%self.nom), ("%s_CTRL"%self.nom))
            cmds.parent(("%s_L_Hand_ctrl"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
            cmds.parent(("%s_R_Hand_ctrl"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
        else:
            cmds.delete(("%s_L_Hand_ctrl"%self.nom), ("%s_R_Hand_ctrl"%self.nom))
        if self.armRibbon:
            cmds.parent(("%s_L_ElbowRibbn_grp"%self.nom), ("%s_R_ElbowRibbn_grp"%self.nom), ("%s_L_UpperArm_Ribbn_GRP"%self.nom), ("%s_R_UpperArm_Ribbn_GRP"%self.nom), ("%s_L_LowerArm_Ribbn_GRP"%self.nom), ("%s_R_LowerArm_Ribbn_GRP"%self.nom), ("%s_XTRAS"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_L_UpperArm_Ribbn_ctrl"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_L_ElbowRibbn_ctrl"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_L_LowerArm_Ribbn_ctrl"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_R_UpperArm_Ribbn_ctrl"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_R_ElbowRibbn_ctrl"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_R_LowerArm_Ribbn_ctrl"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_L_UpperArm_RibbnPos_hi_loc"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_L_UpperArm_RibbnPos_mid_loc"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_R_UpperArm_RibbnPos_hi_loc"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_R_UpperArm_RibbnPos_mid_loc"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_L_LowerArm_RibbnPos_low_loc"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_L_LowerArm_RibbnPos_mid_loc"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_R_LowerArm_RibbnPos_low_loc"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_R_LowerArm_RibbnPos_mid_loc"%self.nom))
            cs = ["L_UpperArm", "R_UpperArm", "L_LowerArm", "R_LowerArm"]
            for c in cs:
                for i in range(1,6):
                    cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_%s_Ribbn0%i_fol"%(self.nom, c, i)))
            lockAndHide(["%s_L_UpperArm_Ribbn_ctrl"%self.nom, "%s_R_UpperArm_Ribbn_ctrl"%self.nom, "%s_L_LowerArm_Ribbn_ctrl"%self.nom, "%s_R_LowerArm_Ribbn_ctrl"%self.nom, "%s_L_ElbowRibbn_ctrl"%self.nom, "%s_R_ElbowRibbn_ctrl"%self.nom], True, True, ["sx", "sy", "sz"])
            lockAndHide(["%s_L_UpperArm_Ribbn_ctrl"%self.nom, "%s_R_UpperArm_Ribbn_ctrl"%self.nom, "%s_L_LowerArm_Ribbn_ctrl"%self.nom, "%s_R_LowerArm_Ribbn_ctrl"%self.nom, "%s_L_ElbowRibbn_ctrl"%self.nom, "%s_R_ElbowRibbn_ctrl"%self.nom], False, True, ["v", "v", "v"])
            cmds.addAttr("%s_C_Ultimate_ctrl"%self.nom, k=True, h=False, ln="Ribbon", at="enum", en="-----:")
            cmds.addAttr("%s_C_Ultimate_ctrl"%self.nom, k=True, h=False, ln="Arm", at="bool")
            cmds.connectAttr("%s_C_Ultimate_ctrl.Arm"%self.nom,"%s_L_UpperArm_Ribbn_ctrl.visibility"%self.nom)
            cmds.connectAttr("%s_C_Ultimate_ctrl.Arm"%self.nom,"%s_R_UpperArm_Ribbn_ctrl.visibility"%self.nom)
            cmds.connectAttr("%s_C_Ultimate_ctrl.Arm"%self.nom,"%s_L_LowerArm_Ribbn_ctrl.visibility"%self.nom)
            cmds.connectAttr("%s_C_Ultimate_ctrl.Arm"%self.nom,"%s_R_LowerArm_Ribbn_ctrl.visibility"%self.nom)
            cmds.connectAttr("%s_C_Ultimate_ctrl.Arm"%self.nom,"%s_L_ElbowRibbn_ctrl.visibility"%self.nom)
            cmds.connectAttr("%s_C_Ultimate_ctrl.Arm"%self.nom,"%s_R_ElbowRibbn_ctrl.visibility"%self.nom)
        if self.legRibbon:
            cmds.parent(("%s_L_KneeRibbn_grp"%self.nom), ("%s_R_KneeRibbn_grp"%self.nom), ("%s_L_UpperLeg_Ribbn_GRP"%self.nom), ("%s_R_UpperLeg_Ribbn_GRP"%self.nom), ("%s_L_LowerLeg_Ribbn_GRP"%self.nom), ("%s_R_LowerLeg_Ribbn_GRP"%self.nom), ("%s_XTRAS"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_L_UpperLeg_Ribbn_ctrl"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_L_KneeRibbn_ctrl"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_L_LowerLeg_Ribbn_ctrl"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_R_UpperLeg_Ribbn_ctrl"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_R_KneeRibbn_ctrl"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_R_LowerLeg_Ribbn_ctrl"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_L_UpperLeg_RibbnPos_hi_loc"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_L_UpperLeg_RibbnPos_mid_loc"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_R_UpperLeg_RibbnPos_hi_loc"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_R_UpperLeg_RibbnPos_mid_loc"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_L_LowerLeg_RibbnPos_low_loc"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_L_LowerLeg_RibbnPos_mid_loc"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_R_LowerLeg_RibbnPos_low_loc"%self.nom))
            cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_R_LowerLeg_RibbnPos_mid_loc"%self.nom))
            cs = ["L_UpperLeg", "R_UpperLeg", "L_LowerLeg", "R_LowerLeg"]
            for c in cs:
                for i in range(1,6):
                    cmds.scaleConstraint(("%s_C_Ultimate_ctrl"%self.nom), ("%s_%s_Ribbn0%i_fol"%(self.nom, c, i)))
            lockAndHide(["%s_L_UpperLeg_Ribbn_ctrl"%self.nom, "%s_R_UpperLeg_Ribbn_ctrl"%self.nom, "%s_L_LowerLeg_Ribbn_ctrl"%self.nom, "%s_R_LowerLeg_Ribbn_ctrl"%self.nom, "%s_L_KneeRibbn_ctrl"%self.nom, "%s_R_KneeRibbn_ctrl"%self.nom], True, True, ["sx", "sy", "sz"])
            lockAndHide(["%s_L_UpperLeg_Ribbn_ctrl"%self.nom, "%s_R_UpperLeg_Ribbn_ctrl"%self.nom, "%s_L_LowerLeg_Ribbn_ctrl"%self.nom, "%s_R_LowerLeg_Ribbn_ctrl"%self.nom, "%s_L_KneeRibbn_ctrl"%self.nom, "%s_R_KneeRibbn_ctrl"%self.nom], False, True, ["v", "v", "v"])
            if not cmds.objExists("%s_C_Ultimate_ctrl.Ribbon"%self.nom):
                cmds.addAttr("%s_C_Ultimate_ctrl"%self.nom, k=True, h=False, ln="Ribbon", at="enum", en="-----:")
            cmds.addAttr("%s_C_Ultimate_ctrl"%self.nom, k=True, h=False, ln="Leg", at="bool")
            cmds.connectAttr("%s_C_Ultimate_ctrl.Leg"%self.nom,"%s_L_UpperLeg_Ribbn_ctrl.visibility"%self.nom)
            cmds.connectAttr("%s_C_Ultimate_ctrl.Leg"%self.nom,"%s_R_UpperLeg_Ribbn_ctrl.visibility"%self.nom)
            cmds.connectAttr("%s_C_Ultimate_ctrl.Leg"%self.nom,"%s_L_LowerLeg_Ribbn_ctrl.visibility"%self.nom)
            cmds.connectAttr("%s_C_Ultimate_ctrl.Leg"%self.nom,"%s_R_LowerLeg_Ribbn_ctrl.visibility"%self.nom)
            cmds.connectAttr("%s_C_Ultimate_ctrl.Leg"%self.nom,"%s_L_KneeRibbn_ctrl.visibility"%self.nom)
            cmds.connectAttr("%s_C_Ultimate_ctrl.Leg"%self.nom,"%s_R_KneeRibbn_ctrl.visibility"%self.nom)
        if self.legIK and self.legFK:
            cmds.parent(("%s_L_LegSwitch_ctrl"%self.nom), ("%s_CTRL"%self.nom))
            cmds.parent(("%s_R_LegSwitch_ctrl"%self.nom), ("%s_CTRL"%self.nom))
            cmds.parent(("%s_L_LegSwitch_ctrl"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
            cmds.parent(("%s_R_LegSwitch_ctrl"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
        if self.handUltimate:
            cmds.parent(("%s_L_Ultim_Hand_ctrl_grp"%self.nom), ("%s_CTRL"%self.nom))
            cmds.parent(("%s_R_Ultim_Hand_ctrl_grp"%self.nom), ("%s_CTRL"%self.nom))
            cmds.parent(("%s_L_Ultim_Hand_ctrl_grp"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
            cmds.parent(("%s_R_Ultim_Hand_ctrl_grp"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
        if self.handFK:
            cmds.parent(("%s_L_Thumb01_FK_pos_grp"%self.nom), ("%s_L_Index01_FK_pos_grp"%self.nom), ("%s_L_Middle01_FK_pos_grp"%self.nom), ("%s_L_Ring01_FK_pos_grp"%self.nom), ("%s_L_Pinky01_FK_pos_grp"%self.nom), ("%s_CTRL"%self.nom))
            cmds.parent(("%s_R_Thumb01_FK_pos_grp"%self.nom), ("%s_R_Index01_FK_pos_grp"%self.nom), ("%s_R_Middle01_FK_pos_grp"%self.nom), ("%s_R_Ring01_FK_pos_grp"%self.nom), ("%s_R_Pinky01_FK_pos_grp"%self.nom), ("%s_CTRL"%self.nom))
            cmds.parent(("%s_L_Thumb01_FK_pos_grp"%self.nom), ("%s_L_Index01_FK_pos_grp"%self.nom), ("%s_L_Middle01_FK_pos_grp"%self.nom), ("%s_L_Ring01_FK_pos_grp"%self.nom), ("%s_L_Pinky01_FK_pos_grp"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
            cmds.parent(("%s_R_Thumb01_FK_pos_grp"%self.nom), ("%s_R_Index01_FK_pos_grp"%self.nom), ("%s_R_Middle01_FK_pos_grp"%self.nom), ("%s_R_Ring01_FK_pos_grp"%self.nom), ("%s_R_Pinky01_FK_pos_grp"%self.nom), ("%s_C_Ultimate_ctrl"%self.nom))
        cmds.select("%s_C_Ultimate_ctrl"%self.nom)
        self.ctrls = ["%s_C_Ultimate_ctrl"%self.nom, "%s_L_ElbowIK_ctrl"%self.nom, "%s_R_ElbowIK_ctrl"%self.nom, "%s_L_ArmIK_ctrl"%self.nom, "%s_R_ArmIK_ctrl"%self.nom, "%s_L_ShoulderFK_ctrl"%persoSel.nom, "%s_R_ShoulderFK_ctrl"%persoSel.nom, "%s_L_ElbowFK_ctrl"%persoSel.nom, "%s_R_ElbowFK_ctrl"%persoSel.nom, "%s_L_WristFK_ctrl"%persoSel.nom, "%s_R_WristFK_ctrl"%persoSel.nom, "%s_L_KneeIK_ctrl"%self.nom, "%s_R_KneeIK_ctrl"%self.nom, "%s_L_Foot_ctrl"%self.nom, "%s_R_Foot_ctrl"%self.nom, "%s_C_COG_ctrl"%self.nom, "%s_C_SpineMidFK_ctrl"%self.nom, "%s_C_SpineUpFK_ctrl"%self.nom, "%s_C_Pelvis_ctrl"%self.nom, "%s_L_LegFK_ctrl"%self.nom, "%s_L_KneeFK_ctrl"%self.nom, "%s_L_AnkleFK_ctrl"%self.nom, "%s_L_BallFK_ctrl"%self.nom, "%s_R_LegFK_ctrl"%self.nom, "%s_R_KneeFK_ctrl"%self.nom, "%s_R_AnkleFK_ctrl"%self.nom, "%s_R_BallFK_ctrl"%self.nom, "%s_C_Neck_ctrl"%self.nom, "%s_C_Head_ctrl"%self.nom, "%s_C_Eyes_ctrl"%self.nom, "%s_L_Eye_ctrl"%self.nom, "%s_R_Eye_ctrl"%self.nom, "%s_C_Neck_ctrl_constraint"%self.nom, "%s_L_Hand_ctrl"%self.nom, "%s_R_Hand_ctrl"%self.nom, "%s_L_LegSwitch_ctrl"%self.nom, "%s_R_LegSwitch_ctrl"%self.nom, "%s_L_Ultim_Hand_ctrl"%self.nom, "%s_R_Ultim_Hand_ctrl"%self.nom, "%s_L_Thumb01_FK_ctrl"%self.nom, "%s_L_Thumb02_FK_ctrl"%self.nom, "%s_L_Thumb03_FK_ctrl"%self.nom, "%s_L_Index01_FK_ctrl"%self.nom, "%s_L_Index02_FK_ctrl"%self.nom, "%s_L_Index03_FK_ctrl"%self.nom, "%s_L_Middle01_FK_ctrl"%self.nom, "%s_L_Middle02_FK_ctrl"%self.nom, "%s_L_Middle03_FK_ctrl"%self.nom, "%s_L_Ring01_FK_ctrl"%self.nom, "%s_L_Ring02_FK_ctrl"%self.nom, "%s_L_Ring03_FK_ctrl"%self.nom, "%s_L_Pinky01_FK_ctrl"%self.nom, "%s_L_Pinky02_FK_ctrl"%self.nom, "%s_L_Pinky03_FK_ctrl"%self.nom, "%s_R_Thumb01_FK_ctrl"%self.nom, "%s_R_Thumb02_FK_ctrl"%self.nom, "%s_R_Thumb03_FK_ctrl"%self.nom, "%s_R_Index01_FK_ctrl"%self.nom, "%s_R_Index02_FK_ctrl"%self.nom, "%s_R_Index03_FK_ctrl"%self.nom, "%s_R_Middle01_FK_ctrl"%self.nom, "%s_R_Middle02_FK_ctrl"%self.nom, "%s_R_Middle03_FK_ctrl"%self.nom, "%s_R_Ring01_FK_ctrl"%self.nom, "%s_R_Ring02_FK_ctrl"%self.nom, "%s_R_Ring03_FK_ctrl"%self.nom, "%s_R_Pinky01_FK_ctrl"%self.nom, "%s_R_Pinky02_FK_ctrl"%self.nom, "%s_R_Pinky03_FK_ctrl"%self.nom, "%s_C_Chest_ctrl"%self.nom, "%s_C_SpineOff_ctrl"%self.nom, "%s_C_Spine_ctrl"%self.nom, "%s_C_Root_ctrl"%self.nom, "%s_L_UpperArm_Ribbn_ctrl"%self.nom, "%s_R_UpperArm_Ribbn_ctrl"%self.nom, "%s_L_LowerArm_Ribbn_ctrl"%self.nom, "%s_R_LowerArm_Ribbn_ctrl"%self.nom, "%s_L_ElbowRibbn_ctrl"%self.nom, "%s_R_ElbowRibbn_ctrl"%self.nom, "%s_L_UpperLeg_Ribbn_ctrl"%self.nom, "%s_R_UpperLeg_Ribbn_ctrl"%self.nom, "%s_L_LowerLeg_Ribbn_ctrl"%self.nom, "%s_R_LowerLeg_Ribbn_ctrl"%self.nom, "%s_L_KneeRibbn_ctrl"%self.nom, "%s_R_KneeRibbn_ctrl"%self.nom]
        print "Charactere %s created !"%self.nom
    # end def autoRig
    
    
    # def bindSkin
    def bindSkin(self):
        # variable
        sel = [""]
        sel = cmds.ls(sl=True, tr=True)
        if len(sel) != 0:
            cmds.group(n="%s_GEO"%self.nom)
            cotes = ["L", "R"]
            parts = ["UpperLeg", "LowerLeg"]
            if persoSel.legRibbon:
                for cote in cotes:
                    for part in parts:
                        for i in range(1, 6):
                            cmds.select("%s_%s_%s_Ribbn0%i_jnt"%(self.nom, cote, part, i), add=True)
                    if persoSel.legIK and persoSel.legFK:
                        for cote in cotes:
                            cmds.select("%s_%s_Ankle_jnt"%(self.nom, cote), "%s_%s_Ball_jnt"%(self.nom, cote), add=True)
                    elif persoSel.legFK:
                        for cote in cotes:
                            cmds.select("%s_%s_AnkleFK_jnt"%(self.nom, cote), "%s_%s_BallFK_jnt"%(self.nom, cote), add=True)
                    elif persoSel.legIK:
                        for cote in cotes:
                            cmds.select("%s_%s_AnkleIK_jnt"%(self.nom, cote), "%s_%s_BallIK_jnt"%(self.nom, cote), add=True)
            elif persoSel.legIK and persoSel.legFK:
                for cote in cotes:
                    cmds.select("%s_%s_Leg_jnt"%(self.nom, cote), "%s_%s_Knee_jnt"%(self.nom, cote), "%s_%s_Ankle_jnt"%(self.nom, cote), "%s_%s_Ball_jnt"%(self.nom, cote), add=True)
            elif persoSel.legFK:
                for cote in cotes:
                    cmds.select("%s_%s_LegFK_jnt"%(self.nom, cote), "%s_%s_KneeFK_jnt"%(self.nom, cote), "%s_%s_AnkleFK_jnt"%(self.nom, cote), "%s_%s_BallFK_jnt"%(self.nom, cote), add=True)
            else:
                for cote in cotes:
                    cmds.select("%s_%s_LegIK_jnt"%(self.nom, cote), "%s_%s_KneeIK_jnt"%(self.nom, cote), "%s_%s_AnkleIK_jnt"%(self.nom, cote), "%s_%s_BallIK_jnt"%(self.nom, cote), add=True)
            
            parts = ["UpperArm", "LowerArm"]
            if persoSel.armRibbon:
                for cote in cotes:
                    for part in parts:
                        for i in range(1, 6):
                            cmds.select("%s_%s_%s_Ribbn0%i_jnt"%(self.nom, cote, part, i), add=True)
                    if persoSel.armIK and persoSel.armFK:
                        for cote in cotes:
                            cmds.select("%s_%s_Wrist_jnt"%(self.nom, cote), add=True)
                    elif persoSel.armFK:
                        for cote in cotes:
                                cmds.select("%s_%s_WristFK_jnt"%(self.nom, cote), add=True)
                    elif persoSel.armIK:
                        for cote in cotes:
                                cmds.select("%s_%s_WristIK_jnt"%(self.nom, cote), add=True)
            elif persoSel.armIK and persoSel.legFK:
                for cote in cotes:
                    cmds.select("%s_%s_Clavicle_jnt"%(self.nom, cote), "%s_%s_Shoulder_jnt"%(self.nom, cote), "%s_%s_Elbow_jnt"%(self.nom, cote), "%s_%s_ForeArm_jnt"%(self.nom, cote), "%s_%s_Wrist_jnt"%(self.nom, cote), add=True)
            elif persoSel.armFK:
                for cote in cotes:
                    cmds.select("%s_%s_Clavicle_jnt"%(self.nom, cote), "%s_%s_ShoulderFK_jnt"%(self.nom, cote), "%s_%s_ElbowFK_jnt"%(self.nom, cote), "%s_%s_ForeArmFK_jnt"%(self.nom, cote), "%s_%s_WristFK_jnt"%(self.nom, cote), add=True)
            else:
                for cote in cotes:
                    cmds.select("%s_%s_Clavicle_jnt"%(self.nom, cote), "%s_%s_ShoulderIK_jnt"%(self.nom, cote), "%s_%s_ElbowIK_jnt"%(self.nom, cote), "%s_%s_ForeArmIK_jnt"%(self.nom, cote), "%s_%s_WristIK_jnt"%(self.nom, cote), add=True)
            
            print persoSel.spine
            if persoSel.spine == "Ribbon":
                for i in range(1,6):
                    cmds.select("%s_C_Spine_Ribbn0%i_jnt"%(self.nom, i), add=True)
                cmds.select("%s_C_Chest_jnt"%self.nom, "%s_C_MidChest_jnt"%self.nom, add=True)
            if persoSel.spine == "IK":
                for i in range(1,8):
                    cmds.select("%s_C_Spine0%i_jnt"%(self.nom, i), add=True)
            if persoSel.spine == "FK":
                cmds.select("%s_C_Chest_jnt"%self.nom, "%s_C_MidChest_jnt"%self.nom, "%s_C_Middle_jnt"%self.nom, add=True)
            
            cmds.select("%s_C_Root_jnt"%self.nom, "%s_C_Pelvis_jnt"%self.nom, "%s_C_Neck_jnt"%self.nom, "%s_C_Head_jnt"%self.nom, "%s_C_Jaw_jnt"%self.nom, "%s_L_Clavicle_jnt"%self.nom, "%s_R_Clavicle_jnt"%self.nom, add=True)
            for cote in cotes:
                for i in range(1, 4):
                    cmds.select("%s_%s_Thumb0%i_jnt"%(self.nom, cote, i), add=True)
                    cmds.select("%s_%s_Index0%i_jnt"%(self.nom, cote, i), add=True)
                    cmds.select("%s_%s_Middle0%i_jnt"%(self.nom, cote, i), add=True)
                    cmds.select("%s_%s_Ring0%i_jnt"%(self.nom, cote, i), add=True)
                    cmds.select("%s_%s_Pinky0%i_jnt"%(self.nom, cote, i), add=True)
            
            mel.eval("SmoothBindSkinOptions;")
        else:
            print "Please selected the GEO fisrt"
    # end def bindSkin

    # def supprPerso
    def supprPerso(self):
        # variables
        tempoJntsPerso = ["%s_C_Root_jnt"%self.nom, "%s_C_Middle_jnt"%self.nom, "%s_C_Chest_jnt"%self.nom, "%s_C_Chest_jnt"%self.nom, "%s_C_MidChest_jnt"%self.nom, "%s_C_Neck_jnt"%self.nom, "%s_C_Spine01_jnt"%self.nom, "%s_C_Spine02_jnt"%self.nom, "%s_C_Spine03_jnt"%self.nom, "%s_C_Spine04_jnt"%self.nom, "%s_C_Spine05_jnt"%self.nom, "%s_C_Spine06_jnt"%self.nom, "%s_C_Spine07_jnt"%self.nom, "%s_C_Spine08_jnt"%self.nom, "%s_C_Pelvis_jnt"%self.nom, "%s_L_Clavicle_jnt"%self.nom, "%s_L_Shoulder_jnt"%self.nom, "%s_L_Elbow_jnt"%self.nom, "%s_L_ForeArm_jnt"%self.nom, "%s_L_Wrist_jnt"%self.nom, "%s_R_Clavicle_jnt"%self.nom, "%s_R_Shoulder_jnt"%self.nom, "%s_R_Elbow_jnt"%self.nom, "%s_R_ForeArm_jnt"%self.nom, "%s_R_Wrist_jnt"%self.nom, "%s_L_Leg_jnt"%self.nom, "%s_L_Knee_jnt"%self.nom, "%s_L_Ankle_jnt"%self.nom, "%s_L_Ball_jnt"%self.nom, "%s_L_Toe_jnt"%self.nom, "%s_R_Leg_jnt"%self.nom, "%s_R_Knee_jnt"%self.nom, "%s_R_Ankle_jnt"%self.nom, "%s_R_Ball_jnt"%self.nom, "%s_R_Toe_jnt"%self.nom, "%s_L_Thumb01_jnt"%self.nom, "%s_L_Thumb02_jnt"%self.nom, "%s_L_Thumb03_jnt"%self.nom, "%s_L_Thumb04_jnt"%self.nom, "%s_L_Index01_jnt"%self.nom, "%s_L_Index02_jnt"%self.nom, "%s_L_Index03_jnt"%self.nom, "%s_L_Index04_jnt"%self.nom, "%s_L_Middle01_jnt"%self.nom, "%s_L_Middle02_jnt"%self.nom, "%s_L_Middle03_jnt"%self.nom, "%s_L_Middle04_jnt"%self.nom, "%s_L_Ring01_jnt"%self.nom, "%s_L_Ring02_jnt"%self.nom, "%s_L_Ring03_jnt"%self.nom, "%s_L_Ring04_jnt"%self.nom, "%s_L_Pinky01_jnt"%self.nom, "%s_L_Pinky02_jnt"%self.nom, "%s_L_Pinky03_jnt"%self.nom, "%s_L_Pinky04_jnt"%self.nom, "%s_R_Thumb01_jnt"%self.nom, "%s_R_Thumb02_jnt"%self.nom, "%s_R_Thumb03_jnt"%self.nom, "%s_R_Thumb04_jnt"%self.nom, "%s_R_Index01_jnt"%self.nom, "%s_R_Index02_jnt"%self.nom, "%s_R_Index03_jnt"%self.nom, "%s_R_Index04_jnt"%self.nom, "%s_R_Middle01_jnt"%self.nom, "%s_R_Middle02_jnt"%self.nom, "%s_R_Middle03_jnt"%self.nom, "%s_R_Middle04_jnt"%self.nom, "%s_R_Ring01_jnt"%self.nom, "%s_R_Ring02_jnt"%self.nom, "%s_R_Ring03_jnt"%self.nom, "%s_R_Ring04_jnt"%self.nom, "%s_R_Pinky01_jnt"%self.nom, "%s_R_Pinky02_jnt"%self.nom, "%s_R_Pinky03_jnt"%self.nom, "%s_R_Pinky04_jnt"%self.nom, "%s_C_Neck_jnt"%self.nom, "%s_C_Head_jnt"%self.nom, "%s_C_HeadEnd_jnt"%self.nom, "%s_C_Jaw_jnt"%self.nom, "%s_C_JawEnd_jnt"%self.nom, "%s_L_Eye_jnt"%self.nom, "%s_R_Eye_jnt"%self.nom]
        if cmds.objExists("%s_CTRL"%self.nom):
            cmds.delete("%s_CTRL"%self.nom)
        if cmds.objExists("%s_SKELETON"%self.nom):
            cmds.delete("%s_SKELETON"%self.nom)
        if cmds.objExists("%s_SKELETON_Layer"%self.nom):
            cmds.delete("%s_SKELETON_Layer"%self.nom)
        if cmds.objExists("%s_GEO"%self.nom):
            geo = cmds.listRelatives("%s_GEO"%self.nom, c=True)
            cmds.parent(geo, w=True)
            cmds.delete("%s_GEO"%self.nom)
        if cmds.objExists("%s_XTRAS"%self.nom):
            cmds.delete("%s_XTRAS"%self.nom)
        if cmds.objExists("%s_Scale_ctrl"%self.nom):
            cmds.delete("%s_Scale_ctrl"%self.nom)
        for tempoJnt in tempoJntsPerso:
            if cmds.objExists(tempoJnt):
                cmds.delete(tempoJnt)
        nodes = cmds.ls(dep=True)
        for node in nodes:
            if node.find("%s_"%self.nom) != -1 and cmds.objExists(node):
                cmds.delete(node)
        cmds.textScrollList("persoListe", e=True, ri=self.nom)
        print "Charactere %s deleted"%self.nom
        if cmds.textScrollList("persoListe", q=True, ai=True) == None:
            cmds.button("delPerso", e=True, en=False)
        win.persoSelected()
    # end def supprPerso
# end class personnage

# class fenetre
class fenetre:
    # var
    hiLRAon = False
    nomPerso = []
    objPerso = []
    
    # def hiLRA
    def hiLRA(self, on):
        self.hiLRAon = on
    # end def hiLRA
    
    # def addPersoVerif
    def addPersoVerif(self):
        newPerso = cmds.textField("addPersoName", q=True, tx=True)
        newPerso = newPerso.upper()
        if newPerso != "" and newPerso.isalnum() and not newPerso[0:1].isnumeric():
            persoListe = cmds.textScrollList("persoListe", q=True, ai=True)
            dejaListe = False
            if persoListe != None:
                for perso in persoListe:
                    if newPerso == perso:
                        dejaListe = True
            if dejaListe == False:
                self.addPerso(newPerso)
        cmds.textField("addPersoName", e=True, tx="")
    # end def addPerso

    # def addPerso
    def addPerso(self, nom):
        cmds.textScrollList("persoListe", e=True, a=nom)
        self.nomPerso.append(nom)
        newPerso = perso(nom)
        self.objPerso.append(newPerso)
        cmds.textScrollList("persoListe", e=True, si=nom)
        newPerso.spheres = []
        newPerso.tempoJnts = []
        newPerso.joints = []
        self.persoSelected()
    # end def addPerso

    # def persoSelected
    def persoSelected(self):
        global persoSel
        persoSelect = cmds.textScrollList("persoListe", q=True, si=True)
        for i in range(0, len(self.objPerso)):
            if not persoSelect == None:
                if self.nomPerso[i] == persoSelect[0]:
                    persoSel = self.objPerso[i]
                    print "Selected character : %s" %persoSel.nom
                    if cmds.objExists("%s_C_Ultimate_ctrl"%persoSel.nom):
                        cmds.select("%s_C_Ultimate_ctrl"%persoSel.nom)
                    majPerso(False)
            else:
                persoSel = ""
        self.majWin()
    # end def persoSelected

    # def majWin
    def majWin(self):
        if persoSel != "":
            # MaJ spine radio button
            if persoSel.spine == "FK":
                cmds.radioButton("FKSpine", e=True, sl=True)
            if persoSel.spine == "IK":
                cmds.radioButton("IKSpine", e=True, sl=True)
            if persoSel.spine == "Ribbon":
                cmds.radioButton("RibbonSpine", e=True, sl=True)
            # MaJ leg checkbox
            if persoSel.legFK:
                cmds.checkBox("FKLeg", e=True, v=True)
            else:
                cmds.checkBox("FKLeg", e=True, v=False)
            if persoSel.legIK:
                cmds.checkBox("IKLeg", e=True, v=True)
            else:
                cmds.checkBox("IKLeg", e=True, v=False)
            if persoSel.legRibbon:
                cmds.checkBox("RibbonLeg", e=True, v=True)
            else:
                cmds.checkBox("RibbonLeg", e=True, v=False)
            # MaJ arm checkbox
            if persoSel.armFK:
                cmds.checkBox("FKArm", e=True, v=True)
            else:
                cmds.checkBox("FKArm", e=True, v=False)
            if persoSel.armIK:
                cmds.checkBox("IKArm", e=True, v=True)
            else:
                cmds.checkBox("IKArm", e=True, v=False)
            if persoSel.armRibbon:
                cmds.checkBox("RibbonArm", e=True, v=True)
            else:
                cmds.checkBox("RibbonArm", e=True, v=False)
            # MaJ hand checkbox
            if persoSel.handCtrl:
                cmds.checkBox("CTRLHand", e=True, v=True)
            else:
                cmds.checkBox("CTRLHand", e=True, v=False)
            if persoSel.handFK:
                cmds.checkBox("FKHand", e=True, v=True)
            else:
                cmds.checkBox("FKHand", e=True, v=False)
            if persoSel.handUltimate:
                cmds.checkBox("ULTIMHand", e=True, v=True)
            else:
                cmds.checkBox("ULTIMHand", e=True, v=False)
            # MaJ head radio button
            if persoSel.head == "FK":
                cmds.radioButton("FKHead", e=True, sl=True)
            if persoSel.head == "IK":
                cmds.radioButton("IKHead", e=True, sl=True)
            # MaJ active buttons or not
            if persoSel.jp == False:
                cmds.radioButton("FKSpine", e=True, en=True)
                cmds.radioButton("IKSpine", e=True, en=True)
                cmds.radioButton("RibbonSpine", e=True, en=True)
                cmds.button("posJointsBtn", e=True, en=True)
                cmds.button("creaJointsBtn", e=True, en=False)
                cmds.button("autoRigBtn", e=True, en=False)
                cmds.button("delPerso", e=True, en=True)
                cmds.checkBox("FKArm", e=True, en=False)
                cmds.checkBox("IKArm", e=True, en=False)
                cmds.checkBox("RibbonArm", e=True, en=False)
                cmds.checkBox("FKLeg", e=True, en=False)
                cmds.checkBox("IKLeg", e=True, en=False)
                cmds.checkBox("RibbonLeg", e=True, en=False)
                cmds.checkBox("CTRLHand", e=True, en=False)
                cmds.checkBox("FKHand", e=True, en=False)
                cmds.button("autoRigBtn", e=True, en=False)
                cmds.button("bindSkinBtn", e=True, en=False)
            else:
                cmds.radioButton("FKSpine", e=True, en=False)
                cmds.radioButton("IKSpine", e=True, en=False)
                cmds.radioButton("RibbonSpine", e=True, en=False)
                cmds.button("posJointsBtn", e=True, en=False)
                cmds.button("creaJointsBtn", e=True, en=True)
                cmds.button("autoRigBtn", e=True, en=False)
                cmds.checkBox("FKArm", e=True, en=False)
                cmds.checkBox("IKArm", e=True, en=False)
                cmds.checkBox("RibbonArm", e=True, en=False)
                cmds.checkBox("FKLeg", e=True, en=False)
                cmds.checkBox("IKLeg", e=True, en=False)
                cmds.checkBox("RibbonLeg", e=True, en=False)
                cmds.checkBox("CTRLHand", e=True, en=False)
                cmds.checkBox("FKHand", e=True, en=False)
                cmds.checkBox("ULTIMHand", e=True, en=False)
                cmds.radioButton("FKHead", e=True, en=False)
                cmds.radioButton("IKHead", e=True, en=False)
                cmds.button("autoRigBtn", e=True, en=False)
                cmds.button("bindSkinBtn", e=True, en=False)
                cmds.button("delPerso", e=True, en=True)
            if persoSel.cj:
                cmds.radioButton("FKSpine", e=True, en=False)
                cmds.radioButton("IKSpine", e=True, en=False)
                cmds.radioButton("RibbonSpine", e=True, en=False)
                cmds.button("creaJointsBtn", e=True, en=False)
                cmds.checkBox("FKArm", e=True, en=True)
                cmds.checkBox("IKArm", e=True, en=True)
                cmds.checkBox("RibbonArm", e=True, en=True)
                cmds.checkBox("FKLeg", e=True, en=True)
                cmds.checkBox("IKLeg", e=True, en=True)
                cmds.checkBox("RibbonLeg", e=True, en=True)
                cmds.checkBox("CTRLHand", e=True, en=True)
                cmds.checkBox("FKHand", e=True, en=True)
                cmds.checkBox("ULTIMHand", e=True, en=True)
                cmds.radioButton("FKHead", e=True, en=True)
                cmds.radioButton("IKHead", e=True, en=True)
                cmds.button("autoRigBtn", e=True, en=True)
                cmds.button("bindSkinBtn", e=True, en=False)
                cmds.button("delPerso", e=True, en=True)
            if persoSel.ar:
                cmds.checkBox("FKArm", e=True, en=False)
                cmds.checkBox("IKArm", e=True, en=False)
                cmds.checkBox("RibbonArm", e=True, en=False)
                cmds.checkBox("FKLeg", e=True, en=False)
                cmds.checkBox("IKLeg", e=True, en=False)
                cmds.checkBox("RibbonLeg", e=True, en=False)
                cmds.checkBox("CTRLHand", e=True, en=False)
                cmds.checkBox("FKHand", e=True, en=False)
                cmds.checkBox("ULTIMHand", e=True, en=False)
                cmds.radioButton("FKHead", e=True, en=False)
                cmds.radioButton("IKHead", e=True, en=False)
                cmds.button("autoRigBtn", e=True, en=False)
                cmds.button("bindSkinBtn", e=True, en=True)
                cmds.button("delPerso", e=True, en=True)
        else:
            cmds.radioButton("FKSpine", e=True, en=True)
            cmds.radioButton("IKSpine", e=True, en=True)
            cmds.radioButton("RibbonSpine", e=True, en=True)
            cmds.button("posJointsBtn", e=True, en=True)
            cmds.button("creaJointsBtn", e=True, en=False)
            cmds.button("autoRigBtn", e=True, en=False)
            cmds.button("delPerso", e=True, en=False)
            cmds.checkBox("FKArm", e=True, en=False)
            cmds.checkBox("IKArm", e=True, en=False)
            cmds.checkBox("RibbonArm", e=True, en=False)
            cmds.checkBox("FKLeg", e=True, en=False)
            cmds.checkBox("IKLeg", e=True, en=False)
            cmds.checkBox("RibbonLeg", e=True, en=False)
            cmds.checkBox("CTRLHand", e=True, en=False)
            cmds.checkBox("FKHand", e=True, en=False)
            cmds.button("autoRigBtn", e=True, en=False)
            cmds.button("bindSkinBtn", e=True, en=False)
        if cmds.textScrollList("persoListe", q=True, ai=True) == None:
            cmds.button("delPerso", e=True, en=False)
            cmds.button("posJointsBtn", e=True, en=False)
            cmds.radioButton("FKSpine", e=True, en=False)
            cmds.radioButton("IKSpine", e=True, sl=True)
            cmds.radioButton("IKSpine", e=True, en=False)
            cmds.radioButton("RibbonSpine", e=True, en=False)
        else:
            cmds.button("delPerso", e=True, en=True)
    # end def majWin
# end class fenetre

# class selection
class selection:
    # def select
    def select(self, clickedBtn):
        global persoSel
        if persoSel != "":
            ctrls = [("%s_C_Head_ctrl"%persoSel.nom), ("%s_C_SpineUpFK_ctrl"%persoSel.nom), ("%s_C_SpineMidFK_ctrl"%persoSel.nom), ("%s_C_COG_ctrl"%persoSel.nom), ("%s_L_LegFK_ctrl"%persoSel.nom), ("%s_R_LegFK_ctrl"%persoSel.nom), ("%s_L_KneeFK_ctrl"%persoSel.nom), ("%s_R_KneeFK_ctrl"%persoSel.nom), ("%s_L_AnkleFK_ctrl"%persoSel.nom), ("%s_R_AnkleFK_ctrl"%persoSel.nom), ("%s_L_BallFK_ctrl"%persoSel.nom), ("%s_R_BallFK_ctrl"%persoSel.nom), ("%s_L_Foot_ctrl"%persoSel.nom), ("%s_R_Foot_ctrl"%persoSel.nom), ("%s_L_KneeIK_ctrl"%persoSel.nom), ("%s_R_KneeIK_ctrl"%persoSel.nom), ("%s_L_Clavicle_ctrl"%persoSel.nom), ("%s_R_Clavicle_ctrl"%persoSel.nom), ("%s_L_ElbowIK_ctrl"%persoSel.nom), ("%s_R_ElbowIK_ctrl"%persoSel.nom), ("%s_L_ArmIK_ctrl"%persoSel.nom), ("%s_R_ArmIK_ctrl"%persoSel.nom), ("%s_L_ShoulderFK_ctrl"%persoSel.nom), ("%s_R_ShoulderFK_ctrl"%persoSel.nom), ("%s_L_ElbowFK_ctrl"%persoSel.nom), ("%s_R_ElbowFK_ctrl"%persoSel.nom), ("%s_L_WristFK_ctrl"%persoSel.nom), ("%s_R_WristFK_ctrl"%persoSel.nom), ("%s_C_Pelvis_ctrl"%persoSel.nom), ("%s_C_Neck_ctrl"%persoSel.nom), ("%s_C_Chest_ctrl"%persoSel.nom), ("%s_C_Middle_ctrl"%persoSel.nom), ("%s_C_Root_ctrl"%persoSel.nom), ("%s_C_Spine_ctrl"%persoSel.nom)]
            btns = ["C_H", "C_C", "C_MS", "C_LS", "L_L", "R_L", "L_K", "R_K", "L_A", "R_A", "L_B", "R_B", "L_B", "R_B", "L_K", "R_K", "L_C", "R_C", "L_E", "R_E", "L_W", "R_W", "L_S", "R_S","L_E", "R_E", "L_W", "R_W", "C_P", "C_N", "C_C", "C_MS", "C_LS", "C_MS"]
            for i in range(0, len(btns)):
                if btns[i] == clickedBtn:
                    if cmds.objExists(ctrls[i]):
                        if cmds.getAttr("%s.visibility"%ctrls[i]):
                            cmds.select(ctrls[i], tgl=True)
    # end def select

    # def snapArmIK
    def snapArmIK(self, cote):
        global persoSel
        if persoSel != "":
            sel = []
            sel = cmds.ls(sl=True)
            if cmds.objExists("%s_%s_ShoulderIK_jnt"%(persoSel.nom, cote)) and  cmds.objExists("%s_%s_ShoulderFK_jnt"%(persoSel.nom, cote)):
                # variables
                shoulderIK = "%s_%s_ShoulderIK_jnt"%(persoSel.nom, cote)
                elbowIK = "%s_%s_ElbowIK_jnt"%(persoSel.nom, cote)
                wristIK = "%s_%s_WristIK_jnt"%(persoSel.nom, cote)
                pvCtrl = "%s_%s_ElbowIK_ctrl"%(persoSel.nom, cote)
                ikCtrl = "%s_%s_ArmIK_ctrl"%(persoSel.nom, cote)
                shoulderFK = "%s_%s_ShoulderFK_jnt"%(persoSel.nom, cote)
                elbowFK = "%s_%s_ElbowFK_jnt"%(persoSel.nom, cote)
                wristFK = "%s_%s_WristFK_jnt"%(persoSel.nom, cote)
                wristFKctrl = "%s_%s_WristFK_ctrl"%(persoSel.nom, cote)
                # positions
                sFKPos = cmds.xform(shoulderFK, q=True, ws=True, rp=True)
                eFKPos = cmds.xform(elbowFK, q=True, ws=True, rp=True)
                wFKPos = cmds.xform(wristFK, q=True, ws=True, rp=True)
                # vecteurs
                sFKVector = MVector(sFKPos[0], sFKPos[1], sFKPos[2])
                eFKVector = MVector(eFKPos[0], eFKPos[1], eFKPos[2])
                wFKVector = MVector(wFKPos[0], wFKPos[1], wFKPos[2])
                midPoint = (sFKVector + wFKVector) / 2
                pvDist = eFKVector - midPoint
                pvPos = pvDist * 2 + midPoint
                # locator
                cmds.spaceLocator(n="%s_%s_locatorSnapIK"%(persoSel.nom, cote))
                cmds.move(wFKPos[0], wFKPos[1], wFKPos[2], "%s_%s_locatorSnapIK"%(persoSel.nom, cote), a=True, ws=True)
                cmds.delete(cmds.pointConstraint(("%s_%s_locatorSnapIK"%(persoSel.nom, cote)), (ikCtrl)))
                cmds.delete("%s_%s_locatorSnapIK"%(persoSel.nom, cote))
                cmds.spaceLocator(n="%s_%s_locatorSnapPV"%(persoSel.nom, cote))
                cmds.move(pvPos.x, pvPos.y, pvPos.z, "%s_%s_locatorSnapPV"%(persoSel.nom, cote), a=True, ws=True)
                cmds.delete(cmds.pointConstraint(("%s_%s_locatorSnapPV"%(persoSel.nom, cote)), (pvCtrl)))
                cmds.delete("%s_%s_locatorSnapPV"%(persoSel.nom, cote))
                cmds.delete(cmds.orientConstraint(wristFKctrl, ikCtrl))
            if len(sel) > 0:
                cmds.select(sel)
    # end def snapArmIK

    # def snapArmFK
    def snapArmFK(self, cote):
        global persoSel
        if persoSel != "":
            sel = []
            sel = cmds.ls(sl=True)
            if cmds.objExists("%s_%s_ShoulderIK_jnt"%(persoSel.nom, cote)) and  cmds.objExists("%s_%s_ShoulderFK_jnt"%(persoSel.nom, cote)):
                # variables
                shoulderIK = "%s_%s_ShoulderIK_jnt"%(persoSel.nom, cote)
                elbowIK = "%s_%s_ElbowIK_jnt"%(persoSel.nom, cote)
                wristIK = "%s_%s_WristIK_jnt"%(persoSel.nom, cote)
                shoulderFKctrl = "%s_%s_ShoulderFK_ctrl"%(persoSel.nom, cote)
                elbowFKctrl = "%s_%s_ElbowFK_ctrl"%(persoSel.nom, cote)
                wristFKctrl = "%s_%s_WristFK_ctrl"%(persoSel.nom, cote)
                # contraintes
                cmds.delete(cmds.orientConstraint(shoulderIK, shoulderFKctrl))
                cmds.delete(cmds.orientConstraint(elbowIK, elbowFKctrl, sk=["x", "z"]))
                cmds.delete(cmds.orientConstraint(wristIK, wristFKctrl))
            if len(sel) > 0:
                cmds.select(sel)
    # end def snapArmFK

    # def switchArm
    def switchArm(self, cote):
        global persoSel
        if persoSel != "":
            if cmds.objExists("%s_%s_ShoulderIK_jnt"%(persoSel.nom, cote)) and  cmds.objExists("%s_%s_ShoulderFK_jnt"%(persoSel.nom, cote)):
                # varaible
                IKFK = "%s_%s_Hand_ctrl.IKFK_Switch"%(persoSel.nom, cote)
                valueIKFK = cmds.getAttr(IKFK)
                if valueIKFK < 5:
                    cmds.setAttr(IKFK, 10)
                else:
                    cmds.setAttr(IKFK, 0)
                cmds.select(cl=True)
    # end def switchArm

    # def snapLegIK
    def snapLegIK(self, cote):
        global persoSel
        if persoSel != "":
            sel = []
            sel = cmds.ls(sl=True)
            if cmds.objExists("%s_%s_LegIK_jnt"%(persoSel.nom, cote)) and  cmds.objExists("%s_%s_LegFK_jnt"%(persoSel.nom, cote)):
                # variables
                legIK = "%s_%s_LegIK_jnt"%(persoSel.nom, cote)
                kneeIK = "%s_%s_KneeIK_jnt"%(persoSel.nom, cote)
                ankleIK = "%s_%s_AnkleIK_jnt"%(persoSel.nom, cote)
                ballIK = "%s_%s_BallIK_jnt"%(persoSel.nom, cote)
                pvCtrl = "%s_%s_KneeIK_ctrl"%(persoSel.nom, cote)
                ikCtrl = "%s_%s_Foot_ctrl"%(persoSel.nom, cote)
                legFK = "%s_%s_LegFK_jnt"%(persoSel.nom, cote)
                kneeFK = "%s_%s_KneeFK_jnt"%(persoSel.nom, cote)
                ankleFK = "%s_%s_AnkleFK_jnt"%(persoSel.nom, cote)
                ballFK = "%s_%s_BallFK_jnt"%(persoSel.nom, cote)
                ankleFKctrl = "%s_%s_AnkleFK_ctrl"%(persoSel.nom, cote)
                # attr
                cmds.setAttr("%s.Foot_Step"%ikCtrl, 0)
                cmds.setAttr("%s.Toe_Pivot"%ikCtrl, 0)
                # positions
                lFKPos = cmds.xform(legFK, q=True, ws=True, rp=True)
                kFKPos = cmds.xform(kneeFK, q=True, ws=True, rp=True)
                aFKPos = cmds.xform(ankleFK, q=True, ws=True, rp=True)
                # vecteurs
                lFKVector = MVector(lFKPos[0], lFKPos[1], lFKPos[2])
                kFKVector = MVector(kFKPos[0], kFKPos[1], kFKPos[2])
                aFKVector = MVector(aFKPos[0], aFKPos[1], aFKPos[2])
                midPoint = (lFKVector + aFKVector) / 2
                pvDist = kFKVector - midPoint
                pvPos = pvDist * 2 + midPoint
                # locator
                cmds.spaceLocator(n="%s_%s_locatorSnapIK"%(persoSel.nom, cote))
                cmds.move(aFKPos[0], aFKPos[1], aFKPos[2], "%s_%s_locatorSnapIK"%(persoSel.nom, cote), a=True, ws=True)
                cmds.delete(cmds.pointConstraint(("%s_%s_locatorSnapIK"%(persoSel.nom, cote)), (ikCtrl)))
                cmds.delete("%s_%s_locatorSnapIK"%(persoSel.nom, cote))
                cmds.spaceLocator(n="%s_%s_locatorSnapPV"%(persoSel.nom, cote))
                cmds.move(pvPos.x, pvPos.y, pvPos.z, "%s_%s_locatorSnapPV"%(persoSel.nom, cote), a=True, ws=True)
                cmds.delete(cmds.pointConstraint(("%s_%s_locatorSnapPV"%(persoSel.nom, cote)), (pvCtrl)))
                cmds.delete("%s_%s_locatorSnapPV"%(persoSel.nom, cote))
                cmds.delete(cmds.parentConstraint(ankleFKctrl, ikCtrl))
                # rotation pied
                cmds.rotate(0, 0, 90, ikCtrl, r=True, os=True)
                ballIKPos = cmds.xform(ballIK, q=True, ws=True, rp=True)
                ballFKPos = cmds.xform(ballFK, q=True, ws=True, rp=True)
                ankleBallIK = MVector((ballIKPos[0] - aFKPos[0]), (ballIKPos[1] - aFKPos[1]), (ballIKPos[2] - aFKPos[2]))
                ankleBallFK = MVector((ballFKPos[0] - aFKPos[0]), (ballFKPos[1] - aFKPos[1]), (ballFKPos[2] - aFKPos[2]))
                angleIKFK = math.degrees(MVector.angle(ankleBallIK, ankleBallFK))
                if cote == "R":
                    angleIKFK = -angleIKFK
                cmds.rotate(angleIKFK, 0, 0, ikCtrl, r=True, os=True)
                # toe roll
                ballFKrotateY = cmds.getAttr("%s.rotateY"%ballFK)
                toeRoll = -ballFKrotateY * 10 / 45
                if toeRoll < -10:
                    toeRoll = -10
                if toeRoll > 10:
                    toeRoll = 10
                cmds.setAttr("%s.Toe_Roll"%ikCtrl, toeRoll)
            if len(sel) > 0:
                cmds.select(sel)
    # end def snapLegIK
    
    # def snapLegFK
    def snapLegFK(self, cote):
        global persoSel
        if persoSel != "":
            sel = []
            sel = cmds.ls(sl=True)
            if cmds.objExists("%s_%s_LegIK_jnt"%(persoSel.nom, cote)) and  cmds.objExists("%s_%s_LegFK_jnt"%(persoSel.nom, cote)):
                # variables
                legIK = "%s_%s_LegIK_jnt"%(persoSel.nom, cote)
                kneeIK = "%s_%s_KneeIK_jnt"%(persoSel.nom, cote)
                ankleIK = "%s_%s_AnkleIK_jnt"%(persoSel.nom, cote)
                ballIK = "%s_%s_BallIK_jnt"%(persoSel.nom, cote)
                legFKctrl = "%s_%s_LegFK_ctrl"%(persoSel.nom, cote)
                kneeFKctrl = "%s_%s_KneeFK_ctrl"%(persoSel.nom, cote)
                ankleFKctrl = "%s_%s_AnkleFK_ctrl"%(persoSel.nom, cote)
                ballFKctrl = "%s_%s_BallFK_ctrl"%(persoSel.nom, cote)
                # contraintes
                cmds.delete(cmds.orientConstraint(legIK, legFKctrl))
                cmds.delete(cmds.orientConstraint(kneeIK, kneeFKctrl, sk=["x", "z"]))
                cmds.delete(cmds.orientConstraint(ankleIK, ankleFKctrl))
                cmds.delete(cmds.orientConstraint(ballIK, ballFKctrl, sk=["x", "z"]))
            if len(sel) > 0:
                cmds.select(sel)
    # end def snapLegFK

    # def switchLeg
    def switchLeg(self, cote):
        global persoSel
        if persoSel != "":
            if cmds.objExists("%s_%s_LegIK_jnt"%(persoSel.nom, cote)) and  cmds.objExists("%s_%s_LegFK_jnt"%(persoSel.nom, cote)):
                # varaible
                IKFK = "%s_%s_LegSwitch_ctrl.IKFK_Switch"%(persoSel.nom, cote)
                valueIKFK = cmds.getAttr(IKFK)
                if valueIKFK < 5:
                    cmds.setAttr(IKFK, 10)
                else:
                    cmds.setAttr(IKFK, 0)
                cmds.select(cl=True)
    # end def switchLegf
    # def RaZ
    def RaZ(self, option):
        global persoSel
        if persoSel != "":
            ctrls = []
            if option == "A":
                ctrlsAndGrp = []
                ctrlsAndGrp = cmds.listRelatives("%s_CTRL"%persoSel.nom, ad=True, typ="transform")
                for ctrl in ctrlsAndGrp:
                    if ctrl.find("_ctrl") != -1 and not ctrl.find("C_Ultimate") != -1:
                        ctrls.append(ctrl)
                ctrlsAndGrp = cmds.listRelatives("%s_XTRAS"%persoSel.nom, ad=True, typ="transform")
                for ctrl in ctrlsAndGrp:
                    if ctrl.find("_ctrl") != -1 and not ctrl.find("C_Ultimate") != -1:
                        ctrls.append(ctrl)
            else:
                ctrlsAndOther = []
                ctrlsAndOther = cmds.ls(sl=True)
                for ctrl in ctrlsAndOther:
                    if ctrl.find("_ctrl") != -1 and not ctrl.find("C_Ultimate") != -1:
                        ctrls.append(ctrl)
            atts = ["translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ"]
            for ctrl in ctrls:
                for att in atts:
                    if cmds.getAttr("%s.%s"%(ctrl, att), se=True):
                        cmds.setAttr("%s.%s"%(ctrl, att), 0)
                autreAtts = cmds.listAttr(ctrl, ud=True)
                if isinstance(autreAtts, list):
                    for autreAtt in autreAtts:
                        cmds.setAttr("%s.%s"%(ctrl, autreAtt), (cmds.addAttr("%s.%s"%(ctrl, autreAtt), q=True, dv=True)))
# end class selection

win = fenetre()
auto = autoRig()
sel = selection()