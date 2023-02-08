import image_creation as ic
from fract_funct import Fractal

mandelbrot = Fractal()

p_man = mandelbrot.mandelbrot()

image_mandelbrot = ic.ImageCreator(p_man)
image_mandelbrot.saveBW('MandelbrotBW')
image_mandelbrot.saveColor('MandelbrotColor')

mandelbrot.updateC(0, 0, 1.5)
p_jul = mandelbrot.julia(complex(-0.76-0.19j))

image_mandelbrot.update_image(p_jul)
image_mandelbrot.saveBW('JuliaBW')
image_mandelbrot.saveColor('JuliaColor')

gif_mandelbrot = ic.GifCreator(p_man)
gif_mandelbrot.saveGif('Mandelbrot')

gif_julia = ic.GifCreator(p_jul)
gif_julia.saveGif('Julia')
