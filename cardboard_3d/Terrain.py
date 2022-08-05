from direct.showbase.ShowBase import ShowBase, GeoMipTerrain, WindowProperties
from panda3d.bullet import ZUp, BulletHeightfieldShape, BulletRigidBodyNode
from panda3d.core import PNMImage, Filename, Vec3
from panda3d.ode import *
from pandac.PandaModules import BitMask32, CardMaker, Vec4, Quat
class Terrain:
    def __init__(self,window,world,height,coords,heightmapfile="cardboard_3d/images/unkown.png",texture="cardboard_3d/images/missing.png",size=100):
        self.window = window.window
        self.world = world
        #self.coords = position
        self.height = height
        self.heightmap = heightmapfile
        self.texture_file = texture
        self.coords = coords
        self.img = PNMImage(Filename(self.heightmap))
        self.offset = self.img.getXSize() / 2.0 - 0.5
        self.terrain = GeoMipTerrain('terrain')
        self.terrain.setHeightfield(self.heightmap)
        self.terrain.setBlockSize(30)
        self.terrainNP = self.terrain.getRoot()
        self.terrainNP.setScale(Vec3(0.8,0.8,height - 5))
        self.terrainNP.setPos(self.coords[0] -self.offset - 5.2, self.coords[1] -self.offset - 5.2, -height / 2 +2.5)
        self.entity_texture = self.window.loader.loadTexture(self.texture_file)
        self.terrainNP.setTexture(self.entity_texture)
        self.terrainNP.reparentTo(self.window.render)

        self.window.taskMgr.add(self.updateTask, "update")

    def updateTask(self,task):
        self.terrain.update()
        return task.cont

    def Create_body(self):

        self.shape = BulletHeightfieldShape(self.img, self.height, ZUp)

        self.node = BulletRigidBodyNode("Terrain")

#        if body_type != "static":
#            self.node.setMass(mass)


        self.node.addShape(self.shape)
        self.np = self.window.render.attachNewNode(self.node)
        self.np.setPos(self.coords)#[0] + self.offset - 5.2, self.coords[1] + self.offset - 5.2, -self.height / 2 + 5)
        self.world.world.attachRigidBody(self.node)
        #self.new_entity.setScale(inputs[0],inputs[1],inputs[2])

        self.terrainNP.copyTo(self.np)

