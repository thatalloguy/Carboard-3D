from direct.showbase.InputStateGlobal import inputState
from panda3d.bullet import BulletCharacterControllerNode
from panda3d.bullet import BulletCapsuleShape
from panda3d.bullet import ZUp
from panda3d.core import BitMask32, Vec3


class Player:
    def __init__(self,window,world,model,radius,height,position=(0,0,0),size=(0,0,0),rotation=(0,0,0)):
        self.radius = radius
        self.height = height
        self.world = world
        self.shape = BulletCapsuleShape(self.radius, height - 2*self.radius, ZUp)
        self.crouching = False
        self.playerNode = BulletCharacterControllerNode(self.shape, 0.4, 'Player')
        self.playerNP = self.world.attachNewNode(self.playerNode)
        self.playerNP.setPos(-2, 0, 14)
        self.playerNP.setH(45)
        self.playerNP.setCollideMask(BitMask32.allOn())

        self.world.attachCharacter(self.playerNP.node())

    def processInput(self):
        speed = Vec3(0, 0, 0)
        omega = 0.0

        if inputState.isSet('forward'): speed.setY(3.0)
        if inputState.isSet('reverse'): speed.setY(-3.0)
        if inputState.isSet('left'):    speed.setX(-3.0)
        if inputState.isSet('right'):   speed.setX(3.0)
        if inputState.isSet('turnLeft'):  omega = 120.0
        if inputState.isSet('turnRight'): omega = -120.0

        self.player.setAngularMovement(omega)
        self.player.setLinearMovement(speed, True)

    def doJump(self):
        self.player.setMaxJumpHeight(5.0)
        self.player.setJumpSpeed(8.0)
        self.player.doJump()



    def doCrouch(self):
        self.crouching = not self.crouching
        sz = self.crouching and 0.6 or 1.0

        self.player.getShape().setLocalScale(Vec3(1, 1, sz))

        self.playerNP.setScale(Vec3(1, 1, sz) * 0.3048)
        self.playerNP.setPos(0, 0, -1 * sz)