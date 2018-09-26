import maya.cmds as cmds
import maya.mel as mel

# timeSliderCopyKey;
# timeSliderPasteKey false;
# timeSliderClearKey;

def cpy():
    mel.eval("timeSliderCopyKey;")

def pst():
    mel.eval("timeSliderPasteKey false;")

def dlt():
    mel.eval("timeSliderClearKey;")

cmds.window(title='KeyframeBox', w=200)
cmds.columnLayout(adj=True)
cmds.separator( h=3 )
cmds.text("KeyframeBox")
cmds.separator( h=3 )
cmds.button( label = 'Copy', w=100, h=40, command='cpy()')

cmds.button( label = 'Paste', w=100, h=40, command='pst()')

cmds.button( label = 'Delete', w=100, h=40, command='dlt()')

cmds.showWindow()
