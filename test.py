import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
from random import randint

noise = PerlinNoise(octaves=5, seed=randint(1,1000000000))
xpix, ypix = 100, 100
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

print(str(pic))

plt.imshow(pic, cmap='terrain')
plt.savefig("TEST.png",bbox_inches="tight",pad_inches=-1)
