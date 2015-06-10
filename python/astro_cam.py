from picamera import PiCamera
from picamera.array import PiRGBArray
from astro_pi import AstroPi

ap = AstroPi()

while True:
    with PiCamera() as camera:
        camera.resolution = (64, 64)
        with PiRGBArray(camera, size=(8, 8)) as stream:
            camera.capture(stream, format='rgb', resize=(8, 8))
            image = stream.array

    pixels = [
        pixel
        for row in image
        for pixel in row
    ]

    ap.set_pixels(pixels)
