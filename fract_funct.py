import numpy as np

import settings


class Fractal():

    def __init__(self):

        self.c = np.zeros((settings.HEIGHT, settings.WIDTH), dtype=complex)
        self.z0 = np.zeros_like(self.c)
        self.updateC(-0.5, 0, 1.5)

    def updateC(self, c_re, c_im, radius):

        re_st = c_re-radius
        re_end = c_re+radius
        im_st = c_im-radius
        im_end = c_im+radius

        real_axis = np.linspace(re_st, re_end, num=settings.WIDTH)
        imaginary_axis = np.linspace(im_end, im_st, num=settings.HEIGHT)
        self.c.real, self.c.imag = np.meshgrid(real_axis, imaginary_axis)

    def mandelbrot(self):
        pixels = np.zeros(np.shape(self.c))
        z = self.z0
        elements_todo = np.ones(np.shape(self.c), dtype=bool)
        for iteration in range(settings.MAX_ITER):
            z[elements_todo] = \
                z[elements_todo]**2 + self.c[elements_todo]
            mask = np.logical_and((z.real**2 + z.imag**2) > 4, elements_todo)
            pixels[mask] = iteration
            elements_todo = np.logical_and(elements_todo, np.logical_not(mask))

        pixels[elements_todo] = settings.MAX_ITER

        return pixels

    def julia(self, shift):

        self.z0 = self.c
        self.c = np.zeros_like(self.z0) + shift

        pixels = self.mandelbrot()

        return pixels
