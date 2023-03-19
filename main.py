# imports packages
import math
import random
import matplotlib.pyplot as plt
import pandas as pd
import imageio
import os

# mandelbrot set maker 

# intializes images
images = []

# gets depth
depth = int(input("Depth: "))

# gets bounds
x1, x2, y1, y2 = list(map(float, input("Enter bounds here in the format \"x1 x2 y1 y2\": ").split(" ")))

# gets count of points
goal = int(input("Point Count: "))

# option for only showing the border; if you need a border then perform calculations to limit it
border = input("Only show a border? [y/n]: ") == "y"

# zoom or not
zoom = input("Would you like the graph to slowly zoom to a random point? (y/n): ") == "y"

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
    while True:
        # gets random point
        e, f = randomInBounds(x1, x2), randomInBounds(y1, y2)       ### IF YOU WANT YOUR OWN CENTER, WRITE "e, f = x, y" WHERE X AND Y ARE THE COORDINATES

        # gets a lower bound for the test
        lb = 1.8 if d < 20 else (1.6 if d < 50 else (1.4 if d < 100 else (1.2 if d < 200 else 1)))

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

    # declares starting count
    count = 0

    # sets the lowerbound
    lowerBound = (1.8 if d < 20 else (1.6 if d < 50 else (1.4 if d < 100 else (1.2 if d < 200 else 1)))) if border else 0

    # performs thing until thing 
    while count < goal:
        # sets bounds for points
        e, f = randomInBounds(x1, x2), randomInBounds(y1, y2)

        # saves point if test passed
        try:
            if test(e, f, d, lowerBound):
                xVals.append(e)
                yVals.append(f)
                count += 1
                if not count % (goal // 10): # shows progress
                    print(str(count) + " points generated...")
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
        x1 = x1 - (x1 - cx) * 0.05
        x2 = x2 - (x2 - cx) * 0.05
        y1 = y1 - (y1 - cy) * 0.05
        y2 = y2 - (y2 - cy) * 0.05


# gets images
for d in range(1, depth+1):
    images.append(imageio.imread(f"imgs/plot{d}.png"))

# creates gif
imageio.mimsave("plot.gif", images, duration=0.1)

# removes files
for d in range(1, depth+1):
    os.remove(f"imgs/plot{d}.png")

# prints center
print(f"Your center was ({cx}, {cy})")