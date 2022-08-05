
from panda3d.core import WindowProperties
from direct.showbase.ShowBase import ShowBase
from panda3d.bullet import BulletWorld
from panda3d.core import Vec3
class Board():
    def __init__(self,size,title,fullscreen=False):
        self.window = ShowBase()

        #self.window.disable_mouse()
        w, h = size[0], size[1]
        self.tasks = []
        props = WindowProperties()
        props.setSize(w, h)
        props.setTitle(title)
        props.setFullscreen(fullscreen)
        self.window.win.requestProperties(props)
        self.window.taskMgr.add(self.update, "update")
        self.world = BulletWorld()
        self.world.setGravity(Vec3(0, 0, -9.81))

    def update(self,task):
        self.dt = globalClock.getDt()
        self.world.doPhysics(self.dt, 10, 1.0/180.0)
        for Task in self.tasks:
            Task()


        return task.cont

    def setKeyMap(self,keymap):
        self.keymap = keymap

    def getKeyMap(self):
        return self.keymap

    def get_DeltaTime(self):
        return self.dt

    def updateKeyMap(self, controlName, controlState):
        self.keymap[controlName] = controlState
        print(controlName, "set to", controlState)

    def bind(self,key,keystatus):
        # IT would be something like window.bind("a", ["a",True])
        self.window.accept(key,self.updateKeyMap, keystatus)

    def addTasks(self,task):
        self.tasks.append(task)

    def run(self):
        self.window.run()

