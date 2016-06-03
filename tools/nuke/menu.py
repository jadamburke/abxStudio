# create read node from write node
import readFromWrite
# add a hotkey but not the menu command


# activate threaded localise
import LocaliseThreaded
LocaliseThreaded.register()

## === QUBE SimpleCmd: BEGIN ===
import qubeSimpleCmd_menu
qubeSimpleCmd_menu.addMenuItems()
## === QUBE SimpleCmd: END ===

# create studio toolbar in menu
toolbar = nuke.menu('Nodes')
studioMenu = toolbar.addMenu('Studio', icon='studio.png')
studioMenu.addCommand( 'Read From Write', 'readFromWrite.readFromWrite()', 'alt+r' )
studioMenu.addCommand('Studio_Slate', 'nuke.createNode(\"Studio_Slate\")')
studioMenu.addCommand('RGBmatte', 'nuke.createNode(\"RGBmatte\")')
studioMenu.addCommand('ID_Matte_Maker', 'nuke.createNode(\"ID_Matte_Maker\")')
studioMenu.addCommand('L_Alpha_Clean', 'nuke.createNode(\"L_AlphaClean_v03\")')
studioMenu.addCommand('Despill_Power', 'nuke.createNode(\"Despill_Power\")')
studioMenu.addCommand('Aberration_jb', 'nuke.createNode(\"Aberration_jb\")')
studioMenu.addCommand('BumpNormals', 'nuke.createNode(\"BumpNormals\")')
studioMenu.addCommand('Reload All Read Nodes', 'reloadAllNodes()')
studioMenu.addCommand('Postage Stamp Generator', 'postageStampGenerator()', 'ctrl+alt+p')

# create world position toolkit menu
wptkMenu = toolbar.addMenu('World Position Tool Kit', icon='wptk.png')
wptkMenu.addCommand('Mask3DCubical_ik', 'nuke.createNode("Mask3DCubical_ik")') 
wptkMenu.addCommand('Mask3DGradient_ik', 'nuke.createNode("Mask3DGradient_ik")') 
wptkMenu.addCommand('Mask3DSpherical_ik', 'nuke.createNode("Mask3DSpherical_ik")') 
wptkMenu.addCommand('TransformWorld_ik', 'nuke.createNode("TransformWorld_ik")') 
wptkMenu.addCommand('WorldPos_Texture_Projection_ik', 'nuke.createNode("WorldPos_Texture_Projection_ik")') 
wptkMenu.addCommand('WorldPos_Texture_Generator_ik', 'nuke.createNode("WorldPos_Texture_Generator_ik")') 
wptkMenu.addCommand('WorldPos_Lambert_Shader_ik', 'nuke.createNode("WorldPos_Lambert_Shader_ik")') 

# 3DEqualizer Plugin Nodes
nuke.menu("Nodes").addCommand("3DE4/LD_3DE4_Anamorphic_Standard_Degree_4", "nuke.createNode('LD_3DE4_Anamorphic_Standard_Degree_4')")
nuke.menu("Nodes").addCommand("3DE4/LD_3DE4_Anamorphic_Degree_6", "nuke.createNode('LD_3DE4_Anamorphic_Degree_6')")
nuke.menu("Nodes").addCommand("3DE4/LD_3DE4_Radial_Standard_Degree_4", "nuke.createNode('LD_3DE4_Radial_Standard_Degree_4')")
nuke.menu("Nodes").addCommand("3DE4/LD_3DE4_Radial_Fisheye_Degree_8", "nuke.createNode('LD_3DE4_Radial_Fisheye_Degree_8')")
nuke.menu("Nodes").addCommand("3DE4/LD_3DE_Classic_LD_Model", "nuke.createNode('LD_3DE_Classic_LD_Model')")


# custom defaults
nuke.knobDefault("Tracker.label", "Ref frame [value reference_frame]")
nuke.knobDefault("Shuffle.label", "[value in] to [value out]")

# better vesrion of update to latest version
# nuke.menu( 'Nuke' ).addCommand( 'Edit/Node/Filename/Version to Latest (Reads only)' , versionToLatest.versionToLatest)



# Method to reload ALL possible reload-able nodes        
def reloadAllNodes():
  for n in nuke.allNodes():
    try:
      n.knob('reload').execute()
      print n.name() + ' reloaded'
    except(AttributeError):
      'No knob named Reload'



def postageStampGenerator():
    nodeSelection = []
    for n in nuke.selectedNodes():
        node = n
        nodeName = node.knob('name').value()
        nodeXPosition = node['xpos'].value()
        nodeYPosition = node['ypos'].value()
        nodeColor = node.knob('tile_color').getValue()
        node.knob('selected').setValue(False)
        PS = nuke.createNode('PostageStamp', inpanel = False)
        PS.setInput(0,node)
        checkName = nodeName+'_PostageStamp'
        nodeNameCheck = 1
        nameIncrements = 0
        nameNumberFound = False
        while nameNumberFound is False:
            for i in nuke.allNodes():
                if i.knob('name').value() == checkName+str(nodeNameCheck):
                    print i.knob('name').value()
                    nodeNameCheck = nodeNameCheck + 1
            nameIncrements = nameIncrements + 1
            if nodeNameCheck == nameIncrements:
                nameNumberFound = True
        PS.knob('name').setValue(checkName+str(nodeNameCheck))
        if node.Class() == 'Read':
            PS.knob('label').setValue('[file tail [value '+nodeName+'.file]]\n[value '+nodeName+'.label]')
        else:
            PS.knob('label').setValue('[value '+nodeName+'.label]')
        PS['xpos'].setValue(nodeXPosition+75)
        PS['ypos'].setValue(nodeYPosition+75)
        PS.knob('hide_input').setValue(True)
        PS.knob('selected').setValue(False)
        nodeSelection.append(n)
    for y in nodeSelection:
        y.knob('selected').setValue(True)
        print nodeSelection
    
    if len(nuke.selectedNodes()) == 0:
        nuke.message('No nodes selected')


