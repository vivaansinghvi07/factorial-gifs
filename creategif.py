"""
    This program is here in case you have stopped generation of a GIF 
    prematurely and are left with just images, but you still want to 
    generate a GIF from what you have.
"""
# imports needed libraries
import imageio
import os

# creates images array and depth counter
images = []
depth = 1

# adds filenames to the images array
while True:
    try:
        images.append(imageio.imread(f"imgs/plot{depth}.png"))
        depth += 1
    except:
        break

# saves the gif
imageio.mimsave("plot.gif", images, duration=0.1)

# deletes all the images
for depth in range(1, len(images)+1):
    os.remove(f"imgs/plot{depth}.png")