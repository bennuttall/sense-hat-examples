from astro_pi import AstroPi
from random import randint
from pi3d import Keyboard
from time import sleep

ESC = 27
STEP = 10

def random_colour():
    r = randint(0, 25) * STEP
    g = randint(0, 25) * STEP
    b = randint(0, 25) * STEP
    return (r, g, b)

def set_centre_square(colour):
    centre_pixels = [(3, 3), (3, 4), (4, 3), (4, 4)]
    for x, y in centre_pixels:
        ap.set_pixel(x, y, colour)

ap = AstroPi()

keyb = Keyboard()

target_colour = random_colour()
initial_colour = random_colour()

ap.clear(target_colour)
set_centre_square(initial_colour)

colour = initial_colour

while colour != target_colour:
    r, g, b = colour
    keypress = keyb.read()

    if keypress == ESC:
        keyb.close()
        break
    if keypress == ord('r'):
        if r < (255 - STEP):
            r += STEP
    elif keypress == ord('t'):
        if r >= STEP:
            r -= STEP
    elif keypress == ord('g'):
        if g < (255 - STEP):
            g += STEP
    elif keypress == ord('h'):
        if g >= STEP:
            g -= STEP
    elif keypress == ord('b'):
        if b < (255 - STEP):
            b += STEP
    elif keypress == ord('n'):
        if b >= STEP:
            b -= STEP

    colour = (r, g, b)
    set_centre_square(colour)

print()

if colour == target_colour:
    print("Well done")
else:
    diff = tuple(c - t for c, t in zip(colour, target_colour))
    print("Aiming for (%4.0f, %4.0f, %4.0f)" % target_colour)
    print("You got    (%4.0f, %4.0f, %4.0f)" % colour)
    print("Difference (%4.0f, %4.0f, %4.0f)" % diff)
    print("Out by %i" % sum(diff))
