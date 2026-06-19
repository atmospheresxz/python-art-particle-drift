import sys
from PIL import Image, ImageDraw
import random
from pathlib import Path
import os

def create_canvas(width, height):

    bg = "#C3CDBB"
    im = Image.new("RGB", size=(width, height), color=bg)
    d = ImageDraw.Draw(im)

    return im, d

def create_particle(width, height):

    # Random start position but not at outer edges
    x = random.randint(500, width-500)
    y = random.randint(500, height-500)

    # Drift bias
    dx_bias = random.uniform(-0.5, 0.5)
    dy_bias = random.uniform(-0.5, 0.5)

    particle_colour, particle_alpha = "#10288C", 0.7

    # Create dictionary
    particle_dict = {"x":x,
                     "y":y,
                     "biasx":dx_bias,
                     "biasy":dy_bias,
                     "colour":particle_colour,
                     "opacity":particle_alpha
                     }
    
    return particle_dict

def move_particle(p):
    # store old_x and old_y before moving    
    old_x = p["x"]
    old_y = p["y"]

    wiggle_x = random.uniform(-1, 1) # change values to create different wiggle if needed
    wiggle_y = random.uniform(-1, 1)

    # update p["x"] and p["y"] using bias + random wiggle
    p["x"] = old_x + p["biasx"] + wiggle_x
    p["y"] = old_y + p["biasy"] + wiggle_y

    # return old_x, old_y so draw_particle can use them
    return old_x, old_y

def draw_particle(draw, p, old_x, old_y):
    # draw a short line from (old_x, old_y) to (p["x"], p["y"])
    draw.line([(old_x, old_y), (p["x"], p["y"])], fill=p["colour"], width=50, joint="curve")
    # use p["colour"] with low opacity
    

def run_simulation(particle_count=200):
    
    # create canvas and drawing context
    canvas = create_canvas(3000, 3000)
    image, drawing = canvas
    # create a list to store particle
    particle_list = []
    
    # loop particle_count times:
    # create a particle and append it to the list    
    for p in range(particle_count):
        particle_list.append(create_particle(3000, 3000))

    N = 1000

    # for a chosen number of steps:
        # for each particle:
            # old_x, old_y = move_particle(p)
            # draw_particle(draw, p, old_x, old_y)
    for i in range(N):
        for particle in particle_list:
            old_x, old_y = move_particle(particle)
            draw_particle(drawing, particle, old_x, old_y)

    # save the image
    output = Path("output/particle-drift.png")
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output)

run_simulation()




    
