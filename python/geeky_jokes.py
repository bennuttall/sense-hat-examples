from astro_pi import AstroPi
from pyjokes import get_joke

ap = AstroPi()

joke = get_joke()

ap.show_message(joke)
