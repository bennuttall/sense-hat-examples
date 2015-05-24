from astro_pi import AstroPi
from random import randint
from pi3d import Keyboard
from time import sleep

def random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def set_centre_square(colour):
    centre_pixels = [(3, 3), (3, 4), (4, 3), (4, 4)]
    for x, y in centre_pixels:
        ap.set_pixel(x, y, colour)

ap = AstroPi()

keyb = Keyboard()

ESC = 27

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
        if r < 255:
            r += 1
    elif keypress == ord('t'):
        if r > 0:
            r -= 1
    elif keypress == ord('g'):
        if g < 255:
            g += 1
    elif keypress == ord('h'):
        if g > 0:
            g -= 1
    elif keypress == ord('b'):
        if b < 255:
            b += 1
    elif keypress == ord('n'):
        if b > 0:
            b -= 1

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
