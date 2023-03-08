import math
import random
import matplotlib as mpl
import pandas as pd

# mandelbrot set maker 

# gets depth
depth = int(input("Depth: "))

# gets bounds
x1, x2, y1, y2 = list(map(float, input("Enter bounds here in the format \"x1 x2 y1 y2\": ").split(" ")))

# gets count of points
goal = int(input("Point Count: "))

# declares empty arrays that will store the points
xVals, yVals = [], []

# declares starting count
count = 0

# option for only showing the border
border = input("Only show a border? [y/n]: ") == "y"


# gets a random number within the bounds
def randomInBounds(min, max):
    return (random.random()) * (max - min) + min

# runs mandelbrot set algorithm
def test(a, b, depth):
    
    xValue = 0
    yValue = 0

    for _ in range(depth):
        xTemp = xValue
        xValue = (xValue)**2-(yValue)**2
        yValue = 2*(xTemp)*(yValue)
        
        xValue = xValue + a
        yValue = yValue + b
    
    # can set bounds for border
    value = math.sqrt(xValue**2 + yValue**2)
    if value < 2 and value > 0: # edit this to change the border width
        return True

while count < goal:
    # sets bounds for points
    e, f = randomInBounds(x1, x2), randomInBounds(y1, y2)

    # saves point if test passed
    try:
        if test(e, f, depth):
            xVals.append(e)
            yVals.append(f)
            count += 1
            if not count % (goal // 100): # shows progress
                print(str(count) + " points generated...")
    except OverflowError:
        continue

# plots the graph
df = pd.DataFrame({'x': xVals, 'y': yVals})
df.plot.scatter(x = 'x', y = 'y', s = 0.4)
mpl.pyplot.show()