from PIL import Image
import os


class GeneratedImage(object):
    def __init__(self, path):
        self.path = path
        if not os.path.isfile(self.path):
            img = Image.new('RGB', [1000, 1000], 255)
            img.save(self.path)

    def edit_pixel(self, nft_id, color):
        n = 2
        y = nft_id // 1000
        x = nft_id % 1000
        color = [int(color[i:i+n], 16) for i in range(0, len(color), n)]
        print(x, y)
        print(color)
        with Image.open(self.path) as im:
            self.image = im.load()
            self.image[x, y] = (color[0], color[1], color[2])
            im.save(self.path)