//After Effects Toolbar by Mike Zugschwert

{   
   
    var makeToolbar = new Object();	// Store globals in an object
    var scriptList = new Array(                                                                             // add a new script [Script File, script icon, script helptip]
                                            ["folderTreeGenerator.jsx", "folderTree.png", "Generate A Folder Tree!"]
                                            );

//~     An example of many scripts in the scriptList array. Note that there are commas after every line but the last in the list.
//~
//~     var scriptList = new Array( 
//~                                             ["folderTreeGenerator.jsx", "folderTree.png", "Generate A Folder Tree!"],
//~                                             ["notation comp.jsx", "not.png", "Notation Comp"],
//~                                             ["cameraInstancer.jsx","camInst.png","Instance Camera"]
//~                                             );                                            
                                            
    var iconLocation = "\\\\pp-fs-nyc\\pipeline\\nyc\\tools\\aftereffects\\icons\\";                                            
    var scriptLocation = "\\\\pp-fs-nyc\\pipeline\\nyc\\tools\\aftereffects\\scripts\\";
   
//////////////////  Begin Create UI Function
    function createUI(thisObj)
        {
            var mydlg = (thisObj instanceof Panel) ? thisObj : new Window("palette", "Make Toolbar", undefined, {resizeable:true});
            mydlg.orientation = "column";
                
            btnSize = 32;
            leftMargin = 5;
            
            for (var i=0; i<scriptList.length; i++)
                {
                    scriptBtn = mydlg.add("iconbutton", "x:"+leftMargin+",y:"+",width:"+btnSize+" ,height:"+btnSize, iconLocation+scriptList[i][1], {style: 'toolbutton'});
                    scriptBtn.ID = i;
                    scriptBtn.helpTip = scriptList[i][2];            
                    scriptBtn.onClick = function(){launchScript(this.ID);}
                }
            
            mydlg.onResizing = mydlg.onResize = function () {
                this.layout.resize();
                if (this.size[0] < this.size[1]){mydlg.orientation = "column";}else{mydlg.orientation = "row";}
                }            
            
            return mydlg;
            
        }
//////////////////  End Create UI Function

    function launchScript(ID)
        {
            scriptFile = new File(scriptLocation+scriptList[ID][0]);
            if (scriptFile.exists){
                $.evalFile(scriptFile);
            }else{
                alert("Could not find the script to launch.");}
        };


    var dlg = createUI(this);
        if (dlg instanceof Window) dlg.show();
    
    
}

