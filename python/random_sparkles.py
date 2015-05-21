from astro_pi import AstroPi
from random import randint
from time import sleep

ap = AstroPi()

while True:
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    pixel = (r, g, b)
    ap.set_pixel(x, y, pixel)
    sleep(0.01)
