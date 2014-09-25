{
function myScript(thisObj) {
          function myScript_buildUI(thisObj) {
                    var myPanel = (thisObj instanceof Panel) ? thisObj : new Window("palette", "My Panel Name", [0, 0, 300, 300]);
 
                    res="group{orientation:'column', alignment:['fill', 'fill'], alignChildren:['fill', 'fill'],\
                              myStaticText: StaticText{text:'StaticText Text'},\
                              myEditText: EditText{text:'EditText text'},\
                              myButton: Button{text:'Button Name'},\
                              myCheckbox: Checkbox{text:'Checkbox Name'},\
                              myRadioButton: RadioButton{text:'RadioButton Name'},\
                              myDropDownList: DropDownList{properties:{items:['Item 1 Name', 'Item 2 Name', 'Item 3 Name', 'Item 4 Name']}},\
                              myListBox: ListBox{properties:{items:['Item 1 Name', 'Item 2 Name', 'Item 3 Name', 'Item 4 Name']}},\
                              myGroup: Group{orientation:'row', alignment:['fill', 'fill'], alignChildren:['fill', 'fill'],\
                                        myGroupItem1: Button{text:'Hi'},\
                                        myGroupItem2: Button{text:'Hello'},\
                                        myGroupItem3: Button{text:'Goodbye'},\
                              },\
                              myPanel: Panel{text:'Panel Name', orientation:'column', alignChildren:['right', 'fill'],\
                                        myPanelItem1: Button{text:'One'},\
                                        myPanelItem2: Button{text:'Two'},\
                                        myPanelItem3: Button{text:'Three'},\
                              },\
                              myTabbedPanel: Panel{type:'tabbedpanel', text:'Tabbed Panel Name', orientation:'column', alignChildren:['right', 'fill'],\
                                  myTab1: Panel{type:'tab', text:'Tab 1', orientation:'column', alignChildren:['right', 'center'],\
                                      aButton1: Button{text:'Button1'},\
                                  },\
                                  myTab2: Panel{type:'tab', text:'Tab 2', orientation:'column', alignChildren:['left', 'center'],\
                                      aButton2: Button{text:'Button2'},\
                                  },\
                                                                      },\
                              myProgressBar: Progressbar{text:'Progressbar Name', minvalue:0, maxvalue:100, value:50},\
                    }"
 
                    //Add resource string to panel
                    myPanel.grp = myPanel.add(res);
 
                    // DropDownList default selection
                    myPanel.grp.myDropDownList.selection = 2;//Item index starts at 0
 
 
                    //Setup panel sizing and make panel resizable
                    myPanel.layout.layout(true);
                    myPanel.grp.minimumSize = myPanel.grp.size;
                    myPanel.layout.resize();
                    myPanel.onResizing = myPanel.onResize = function () {this.layout.resize();}
 
                    return myPanel;
          }
 
 
          var myScriptPal = myScript_buildUI(thisObj);
 
 
          if ((myScriptPal != null) && (myScriptPal instanceof Window)) {
                    myScriptPal.center();
                    myScriptPal.show();
                    }
          }
 
 
          myScript(this);
}