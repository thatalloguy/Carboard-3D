import sys
import os
import platform
from panda3d.core import WindowProperties
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Filename
class Board(ShowBase):
    def __init__(self,size,title,fullscreen=False):
        ShowBase.__init__(self)
        w, h = size[0], size[1]

        props = WindowProperties()
        props.setSize(w, h)
        props.setTitle(title)
        props.setFullscreen(fullscreen)
        self.win.requestProperties(props)