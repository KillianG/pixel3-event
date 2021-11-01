import requests
import urllib
from PIL import Image
import os
PATH = os.environ.get('PATH_IMAGES', './tests')


def push_image_to_ipfs(file_path):
    NODE = "http://localhost:5005"
    MFS_PATH = "/current-image"  # mfs path you're trying to write to

    response = requests.post(NODE + "/api/v0/files/write?arg=%s&create=true" % urllib.parse.quote(MFS_PATH),
                             files={file_path: open(file_path, 'rb')})
    print(response)


def string_to_tuple(color):
    n = 2
    color = [int(color[i:i+n], 16) for i in range(0, len(color), n)]
    return color[0], color[1], color[2]


def get_pos_from_id(id):
    y = id // 1000
    x = id % 1000
    return x, y


def generate_image(color, nft_id, export_to=None):
    path = PATH + '/default.png'
    if not os.path.isfile(path):
        img = Image.new('RGB', [1000, 1000], 0)
        img.save(path)

    color = string_to_tuple(color)
    x, y = get_pos_from_id(nft_id)
    print(x, y)
    print(color)
    with Image.open(path) as im:
        image = im.load()
        image[x, y] = color
        im.save(path)
        if export_to:
            im.save(PATH + '/' + export_to)

    push_image_to_ipfs(path)


if __name__ == "__main__":
    generate_image('ff00ff', 0)