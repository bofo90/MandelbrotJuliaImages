import image_creation as ic
from fract_funct import Fractal

mandelbrot = Fractal()

p = mandelbrot.mandelbrot()

image_mandelbrot = ic.ImageCreator(p)
image_mandelbrot.saveBW('MandelbrotBW')
image_mandelbrot.saveColor('MandelbrotColor')

mandelbrot.updateC(-1, 1, -1, 1)
p = mandelbrot.julia(complex(-0.76-0.19j))

image_mandelbrot.update_image(p)
image_mandelbrot.saveBW('JuliaBW')
image_mandelbrot.saveColor('JuliaColor')

# gif_mandelbrot = ic.GifCreator(p)
# gif_mandelbrot.saveGif('Mandelbrot')
