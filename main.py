from cardboard_3d import *
import os
from random import randint
#Terrain Generation
#import test
#test.run()


# Actaul Game
keymap = {
    "a": False,
    "d": False
}
gen = True
offset = 200
def ticker():
    global gen, offset
    dt = window.get_DeltaTime()
    #print("TICK")
    keymap  = window.getKeyMap()



    if keymap["a"]:
        new_bob = Entity(window, world, (randint(-100, 100), randint(-100, 100), 40), "PRESET CUBE", texture="cardboard_3d/images/missing.png")
        new_bob.Create_body("box", (0.5, 0.5, 0.5), id="Box", body_type="dynamic")

    if keymap["d"]:
        pass




window = Board((1280,720),"Cardboard 3D")
sky = Skybox(window,texture="assets/sky.png",size=1000)
world = World(window,(0,0,-9.81))
#terrain = Terrain(window,world,50,(0,0,0),heightmapfile="TEST.png",texture="TEST.png")
#terrain.Create_body()
window.setKeyMap(keymap)
window.addTasks(ticker)

# WATERRR
#water = Entity(window,world,(0,0,5),"PRESET CUBE",texture="water.jpg",size=(100,100,0.2))
#water.force_draw()
# Physics
camera = window.window.camera


floor = Entity(window,world,(0,0,-10),"my_models/island/island.obj",size=(40,40,40),texture="my_models/island/island_texture.png",rotation=(0,90,0))
floor.Create_body("plane",(0,0,1,1),id="Ground",body_type="static")
# Create the Body


# Input
window.bind("a",["a",True])
window.bind("a-up",["a",False])
window.bind("d",["d",True])
window.bind("d-up",["d",False])

# Run
window.run()