"""
    This program is here in case you have stopped generation of a GIF 
    prematurely and are left with just images, but you still want to 
    generate a GIF from what you have.
"""
# imports needed libraries
import imageio
import os

# creates images array and depth counter
imageFiles = []
depth = 0

# adds filenames to the images array
while True:
    try:
        imageFiles.append(f"imgs/plot{depth}.png")
        depth += 1
    except:
        break

# gets the images
images = map(imageio.imread, imageFiles)

# saves the gif
imageio.mimsave("plot.gif", images, duration=0.1)

# deletes all the images
for filename in imageFiles:
    os.remove(filename)