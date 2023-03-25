# Mandelbrot GIF Generator
A spin-off of my old project [here](https://github.com/vivaansinghvi07/factorial-points). I decided to try to make a several GIFS of the Mandelbrot Set forming it's true shape as approximations become closer and closer. 

## Setup
- Open a Python environment
- Open a new Python terminal
- Run the following commands to install needed libraries:
    ```
    $ pip install pandas
    $ pip install matplotlib
    $ pip install imageio
    ```

## Usage

As the program runs, it will place images in the `imgs` folder, and when complete, it will generate a GIF named `plot.gif` in the main directory. If you terminate the program prematurely, you can run `creategif.py` to generate a GIF using the images you have remaining (note: if you use this program, do not delete any images or it will not work properly). Run `main.py`, and follow the instructions below to create!

### Parameters

- `Depth`: Here, you control how deep (how many iterations) your computer will go. Therefore, this setting dictates how long you want your GIF to be. 
- `Bounds (x1 x2 y1 y2)`: This is the starting bounds for your graph. The numbers 1 and 2 represent the lower bound and upper bound respectively.
- `Border only (y/n)`: If you select this, the program will only generate the border of the set rather than the entire set.
- `Zoom (y/n)`: If you select this, the program will zoom into a random point that is on the border of the graph to create really cool zooms!
- The `Point Count` feature has been removed in new versions of his program. Therefore, zooms generated with it present will have this displayed, but crossed out.

## Output

Depending on your settings, the program will generate various GIFS. Here are examples with the settings:

### Filled

```
Depth: 50
Bounds: -2 0.5 -1.2 1.2
Only a border: n
Zoom: n
```
~~`Point Count: 200000`~~<br>



![Filled](examples/mandelbrot-filled.gif)

### Border

```
Depth: 20
Bounds: -2 0.5 -1 1
Only a border: y
Zoom: n
```

~~`Point Count: 10000`~~

![Border](examples/mandelbrot-border.gif)

### Zoom

```
Depth: 300          (note: this was stopped around 260 for time's sake)
Bounds: -2 0.5 -1 1
Only a border: n
Zoom: y
```

~~`Point Count: 400000`~~


![Zoom](examples/mandelbrot-zoom.gif)

Note: I do not have the center point that was generated because I added printing the center afterwards.

Personally, I like how you can see the graph become less and less smooth as you zoom in - something you don't often see in other demonstrations.

### Another Zoom

```
Depth: 400
Bounds: -2 0.5 -1.2 1.2
Only a border: n
Zoom: y
```

~~`Point Count: 350000`~~


![Zoom 2](examples/mandelbrot-zoom2.gif)

```
Center: (-0.9910690589907436, -0.2791206424126276)
```