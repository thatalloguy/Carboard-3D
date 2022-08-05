from panda3d.core import TextureStage, TexGenAttrib

class Skybox:
    def __init__(self,window,texture='cardboard_3d/images/default_skybox.png',size=100):
        self.window = window.window
        self.texture =texture
        cubeMap = self.window.loader.loadTexture(self.texture)
        self.spaceSkyBox = self.window.loader.loadModel('cardboard_3d/models/cube/cube.obj')
        self.spaceSkyBox.setTexture(cubeMap)
        self.spaceSkyBox.setScale(size)
        #self.spaceSkyBox.setBin('background', 0)
        #self.spaceSkyBox.setDepthWrite(0)

        self.spaceSkyBox.setTwoSided(True)
        #self.spaceSkyBox.setTexGen(TextureStage.getDefault(), TexGenAttrib.MWorldCubeMap)
        #self.spaceSkyBox.setTexture(cubeMap, 1)
        self.spaceSkyBox.reparentTo(self.window.camera)
        self.spaceSkyBox.reparentTo(self.window.render)