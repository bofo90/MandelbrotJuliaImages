import image_creation as ic
from fract_funct import Fractal
from obtain_pos import get_julia_pos, get_man_pos

pos_man = get_man_pos()
pos_julia = get_julia_pos()

mandelbrot = Fractal()

for i, pos in enumerate(pos_man):
    mandelbrot.updateC(*pos)
    p = mandelbrot.mandelbrot()

    image_mandelbrot = ic.ImageCreator(p)
    image_mandelbrot.saveBW(f'MandelbrotBW_{i}')
    image_mandelbrot.saveColor(f'MandelbrotColor_{i}')

# mandelbrot.updateC(0, 0, 1.5)
# p_jul = mandelbrot.julia(complex(-0.76-0.19j))

# image_mandelbrot.update_image(p_jul)
# image_mandelbrot.saveBW('JuliaBW')
# image_mandelbrot.saveColor('JuliaColor')

# gif_mandelbrot = ic.GifCreator(p_man)
# gif_mandelbrot.saveGif('Mandelbrot')

# gif_julia = ic.GifCreator(p_jul)
# gif_julia.saveGif('Julia')
