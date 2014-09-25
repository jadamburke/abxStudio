

## === QUBE SimpleCmd: BEGIN ===
import qubeSimpleCmd_menu
qubeSimpleCmd_menu.addMenuItems()
## === QUBE SimpleCmd: END ===

# create toolbar in menu
toolbar = nuke.menu('Nodes')
passionMenu = toolbar.addMenu('Passion', icon='passion.png')
passionMenu.addCommand('Passion_Slate', 'nuke.createNode(\"Passion_Slate\")')
passionMenu.addCommand('RGBmatte', 'nuke.createNode(\"RGBmatte\")')
passionMenu.addCommand('ID_Matte_Maker', 'nuke.createNode(\"ID_Matte_Maker\")')
passionMenu.addCommand('L_Alpha_Clean', 'nuke.createNode(\"L_AlphaClean_v03\")')
passionMenu.addCommand('Despill_Power', 'nuke.createNode(\"Despill_Power\")')
passionMenu.addCommand('Aberration_jb', 'nuke.createNode(\"Aberration_jb\")')
passionMenu.addCommand('BumpNormals', 'nuke.createNode(\"BumpNormals\")')
passionMenu.addCommand('Reload All Read Nodes', 'reloadAllNodes()')
passionMenu.addCommand('Postage Stamp Generator', 'postageStampGenerator()', 'ctrl+alt+p')

# custom defaults
nuke.knobDefault("Tracker.label", "Ref frame [value reference_frame]")
nuke.knobDefault("Shuffle.label", "[value in] to [value out]")


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