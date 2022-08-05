from direct.showbase.DirectObject import DirectObject
from panda3d.core import Vec3
from panda3d.bullet import BulletWorld, BulletDebugNode


class World:
    def __init__(self,window,gravity,debugtoggle=True):
        self.window = window
        self.world = BulletWorld()
        self.world.setGravity(Vec3(gravity[0],gravity[1],gravity[2]))
        self.debugNode = BulletDebugNode('Debug')
        self.debugNode.showWireframe(True)
        self.debugNode.showConstraints(True)
        self.debugNode.showBoundingBoxes(False)
        self.debugNode.showNormals(False)
        self.debugNP = self.window.window.render.attachNewNode(self.debugNode)

        self.world.setDebugNode(self.debugNP.node())
        if debugtoggle:
            o = DirectObject()
            o.accept('f1', self.toggleDebug)
        self.window.addTasks(self.update)
    def getWorld(self):
        return self.world

    def update(self):
        self.dt = self.window.get_DeltaTime()
        self.world.doPhysics(self.dt)

    def toggleDebug(self):
        if self.debugNP.isHidden():
            self.debugNP.show()
        else:
            self.debugNP.hide()