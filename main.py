from fract_funct import Fractal
import image_creation as ic
import settings
import numpy as np


mandelbrot = Fractal()

# p = mandelbrot.julia(complex(-0.76-0.19j))
p = mandelbrot.mandelbrot()

image_mandelbrot = ic.ImageCreator(p)
image_mandelbrot.saveBW('MandelbrotBW')
image_mandelbrot.saveColor('MandelbrotColor')

# gif_mandelbrot = ic.GifCreator(p)
# gif_mandelbrot.saveGif('Mandelbrot')

