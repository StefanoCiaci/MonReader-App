import os
import random
import numpy as np
from keras.preprocessing.image import load_img, img_to_array


def load_random_images(img_directory: str,
                       n_images: int = 1,
                       color_mode: str = "rgb",
                       target_size: tuple | None = None
                       ) -> None:
    try:
        img_list = os.listdir(path=img_directory)
        if not img_list:
            raise ValueError("The directory is empty or does not exist.")
        random_imgs = random.sample(img_list,
                                    n_images)
        loaded_imgs = []
        for img_name in random_imgs:
            img_path = os.path.join(img_directory,
                                    img_name)
            img = load_img(path=img_path,
                           color_mode=color_mode,
                           target_size=target_size)
            loaded_imgs.append(img)
        return loaded_imgs
    except Exception as e:
        print(f"Error: {e}")


def preprocess_images(imgs: list
                      ) -> list:
    processed_imgs = []
    for img in imgs:
        processed_img = np.expand_dims(img_to_array(img=img),
                                       axis=0)
        processed_imgs.append(processed_img)
    return processed_imgs


def count_items(path: str
                ) -> int:
    if not os.path.isdir(path):
        raise ValueError(f"The path {path} is not a valid directory.")

    items_list = os.listdir(path)
    return len(items_list)
