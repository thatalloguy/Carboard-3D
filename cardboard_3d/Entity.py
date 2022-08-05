from panda3d.bullet import *
from panda3d.ode import OdeWorld, OdeBody, OdeMass, OdePlaneGeom
from panda3d.core import Quat, Vec4, Vec3, PNMImage, Filename, Shader


class Entity():
    def __init__(self,window,world,coord,model,size=(1,1,1),rotation=(0,0,0),body_type="dynamic",texture=None,shaders="myshader.frag",shadersenabled=False):
        super().__init__()
        self.world = world
        self.texture = texture
        self.window = window.window
        self.window_class = window
        self.coords = coord
        self.model = model
        self.deltaTimeAccumulator = 0.0
        self.size = size
        self.shaders = shaders
        self.shadersenabled = shadersenabled
        self.rotation = rotation
        self.body_type = body_type
        self.fps = 90
        self.stepSize = 1.0 / self.fps
        if self.model == "PRESET CUBE":
            self.model = "cardboard_3d/models/cube/cube.obj"

        elif self.model == "PRESET SPHERE":
            self.model = "cardboard_3d/models/sphere/sphere.obj"

        self.body_created = False
        self.render()
        #self.window_class.addTasks(self.Simulation, 'update')#self.window.taskMgr.doMethodLater(1.0, self.Simulation, "update")

    def render(self):
        self.new_entity = self.window.loader.loadModel(self.model)
        self.new_entity.setHpr(self.rotation[0],self.rotation[1],self.rotation[2])
        #self.new_entity.reparentTo(self.window.render)
        #self.new_entity.setPos(self.coords)
        self.new_entity.setScale(self.size)
        if self.texture == None:
            pass
        else:
            try:
                self.entity_texture = self.window.loader.loadTexture(self.texture)
            except:
                self.entity_texture = self.window.loader.loadTexture("cardboard_3d/images/missing.png")

            self.new_entity.setTexture(self.entity_texture)
    def force_draw(self):
        self.new_entity = self.window.loader.loadModel(self.model)
        self.new_entity.reparentTo(self.window.render)
        self.new_entity.setPos(self.coords)
        self.new_entity.setScale(self.size)
        if self.texture == None:
            pass
        else:
            try:
                self.entity_texture = self.window.loader.loadTexture(self.texture)
            except:
                self.entity_texture = self.window.loader.loadTexture("cardboard_3d/images/missing.png")

            self.new_entity.setTexture(self.entity_texture)

        if self.shadersenabled:
            pass

    def getPos(self):
        return self.node.getShapePos()

    def Create_body(self,shape,inputs,id="MyBox",mass=1,body_type="static"):
        self.shape = shape
        self.inputs = inputs

        if self.shape == "sphere":
            self.shape = BulletSphereShape(inputs[0])

        elif self.shape == "plane":
            self.shape = BulletPlaneShape(Vec3(0, 0, 1), 1)#inputs[0],inputs[1],inputs[2]),inputs[3])

        elif self.shape == "box":
            self.shape = BulletBoxShape(Vec3(inputs[0],inputs[1],inputs[2]))

        elif self.shape == "cylinder":
            self.shape = BulletCylinderShape(inputs[0],inputs[1], ZUp)

        elif self.shape == "capsule":
            self.shape = BulletCapsuleShape(inputs[0],inputs[1],ZUp)

        elif self.shape == "cone":
            self.shape = BulletConeShape(inputs[0],inputs[1], ZUp)

        elif self.shape == "heightmap":
            self.img = PNMImage(Filename(inputs[0]))
            self.shape = BulletHeightfieldShape(self.img, inputs[1], ZUp)

        self.node = BulletRigidBodyNode(id)

        if body_type != "static":
            self.node.setMass(mass)


        self.node.addShape(self.shape)
        self.np = self.window.render.attachNewNode(self.node)
        self.np.setPos(self.new_entity.getPos())
        self.world.world.attachRigidBody(self.node)
        #self.new_entity.setScale(inputs[0],inputs[1],inputs[2])
        self.new_entity.copyTo(self.np)



#    def Simulation(self):
#        if self.body_created:
#            self.dt = self.window_class.get_DeltaTime()
#            self.world.doPhysics(self.dt)