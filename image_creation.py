import numpy as np
from PIL import Image, ImageDraw
from skimage import measure

import settings


class GifCreator():

    def __init__(self, pixels):

        self.images = []

        for i in range(settings.MAX_ITER):

            contours = measure.find_contours(pixels, i)

            im = Image.new('RGB', (settings.WIDTH, settings.HEIGHT), '#1A2023')
            draw = ImageDraw.Draw(im)
            for contour in contours:
                draw.line(list(zip(contour[:, 1], contour[:, 0])), fill='#CAD2C5', width=0)

            self.images.append(im)

    def saveGif(self, name):

        self.images.extend(self.images[::-1])
        self.images[0].save(f'Gifs/{name}.gif',
                            save_all=True, append_images=self.images[1:],
                            optimize=False, duration=40, loop=0)


class ImageCreator():

    def __init__(self, p):

        self.im_array = np.zeros((settings.HEIGHT, settings.WIDTH, 3), dtype=np.uint8)
        self.update_image(p)

    def update_image(self, p):
        self.p = p

    def saveColor(self, name):
        self.im_array[:, :, 0] = 255*self.p/settings.MAX_ITER
        self.im_array[:, :, 1] = 255
        mask = self.p < settings.MAX_ITER
        self.im_array[mask, 2] = 255

        im = Image.fromarray(self.im_array, 'HSV')
        im.convert('RGB').save(f'Images/{name}.png', 'PNG')
        im.show()

    def saveBW(self, name):
        self.im_array[:, :, 0] = 0
        self.im_array[:, :, 1] = 0
        self.im_array[:, :, 2] = 255*self.p/settings.MAX_ITER
        mask = self.p == settings.MAX_ITER
        self.im_array[mask, 2] = 10

        im = Image.fromarray(self.im_array, 'HSV')
        im.convert('RGB').save(f'Images/{name}.png', 'PNG')
        im.show()

