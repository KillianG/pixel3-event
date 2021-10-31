from generate_image import generate_image
from datetime import datetime


def save_pixel_in_versioned_image(color, nft_id):
    versioned_path = datetime.now().isoformat() + '.png'
    print(versioned_path)
    generate_image(color, nft_id, versioned_path)


if __name__ == "__main__":
    save_pixel_in_versioned_image('00ffff', 1)
