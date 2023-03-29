# imports packages
import math
import random
import matplotlib.pyplot as plt
import pandas as pd
import imageio.v2 as imageio
import os

# constants and settings - CHANGE THESE AS YOU WISH
ZOOMSPEED = 0.045                               # change this to change zoom speed if there is a bug or anything
FRAMEDURATION = 0.1                             # number of seconds a frame lasts
POINTCOUNT = 300_000                          # number of points
POINTMULTIPLIER = math.sqrt(POINTCOUNT / 12)    # x-y multiplier for points
XPOINTS = int(POINTMULTIPLIER * 4)              # number of points on x-axis on grid (generally higher when you want a borders - more clear)
YPOINTS = int(POINTMULTIPLIER * 3)              # number of points on y-axis on grid
BORDERS = [-2, 0.5, -1.1, 1.1]                  # [x1, x2, y1, y2]
ZOOM = True                                     # zoom into random point?
BORDERONLY = False                              # have only borders?
CENTERSTRICTNESS = 0.999995                      # change how strict the center's border is (higher = more time but more accurate, max = 1)
DEPTH = 500                                      # how many frames will be there?

# intializes images
images = []

# gets depth
depth = DEPTH

# gets bounds
x1, x2, y1, y2 = BORDERS

# option for only showing the border; if you need a border then perform calculations to limit it
border = BORDERONLY

# zoom or not
zoom = ZOOM

# gets a random number within the bounds
def randomInBounds(min, max):
    return (random.random()) * (max - min) + min

# runs mandelbrot set algorithm
def test(a, b, depth, lowerBound):
    
    # initializes starter values
    xValue = 0
    yValue = 0

    for _ in range(depth):

        # computes the square
        xTemp = xValue
        xValue = (xValue)**2-(yValue)**2
        yValue = 2*(xTemp)*(yValue)
        
        # adds the randomly generated constant point
        xValue = xValue + a
        yValue = yValue + b
    
    # can set bounds for border
    value = math.sqrt(xValue**2 + yValue**2)
    if value < 2 and value > lowerBound: # edit this to change the border width manually
        return True

# gets the point to zoom into
def getCenter(x1, x2, y1, y2, d):

    # prints status message
    print("Getting center...")

    while True:
        # gets random point
        e, f = randomInBounds(x1, x2), randomInBounds(y1, y2)       ### IF YOU WANT YOUR OWN CENTER, WRITE "e, f = x, y" WHERE X AND Y ARE THE COORDINATES

        # gets a lower bound for the test
        lb = 1 + CENTERSTRICTNESS ** d     ### Make sure its truly on the border

        # returns the point if good
        try:
            if test(e, f, d, lb):
                return e, f
        except:
            continue

# gets the central point if we need to zomo 
if zoom:
    cx, cy = getCenter(x1, x2, y1, y2, depth)

# goes through all the depths
for d in range(1, depth+1):

    # declares empty arrays that will store the points
    xVals, yVals = [], []

    # sets the lowerbound
    lowerBound = (1.8 if d < 20 else (1.6 if d < 50 else (1.4 if d < 100 else (1.2 if d < 200 else 1)))) if border else 0

    # performs thing until thing 
    for a in range(XPOINTS+1):
        for b in range(YPOINTS+1):

            e, f = ((x2-x1)/XPOINTS) * a + x1, ((y2-y1)/YPOINTS) * b + y1

            # saves point if test passed
            try:
                if test(e, f, d, lowerBound):
                    xVals.append(e)
                    yVals.append(f)
            except OverflowError:
                continue

    # plots the graph
    df = pd.DataFrame({'x': xVals, 'y': yVals})
    df.plot.scatter(x = 'x', y = 'y', s = 0.4)
    plt.xlim([x1, x2])
    plt.ylim([y1, y2])
    plt.grid(False)
    plt.axis('off')
    plt.savefig(f"imgs/plot{d}.png")
    plt.close()

    # prints progress
    print(f"Plot with depth {d} done.")

    # gets the new bounds (if needed)
    if zoom:
        x1 = x1 - (x1 - cx) * ZOOMSPEED
        x2 = x2 - (x2 - cx) * ZOOMSPEED
        y1 = y1 - (y1 - cy) * ZOOMSPEED
        y2 = y2 - (y2 - cy) * ZOOMSPEED


# gets images
for d in range(1, depth+1):
    images.append(imageio.imread(f"imgs/plot{d}.png"))

# creates gif
imageio.mimsave("plot.gif", images, duration=FRAMEDURATION)

# removes files
for d in range(1, depth+1):
    os.remove(f"imgs/plot{d}.png")

# prints center
if zoom:
    print(f"Your center was ({cx}, {cy})")