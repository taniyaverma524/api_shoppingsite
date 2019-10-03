import os
import time
import random
from PIL import Image


def make_dir(dirname):
    """
    Creates new directory if not exists
    :param dirname: String
    :return: String
    """
    try:
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        return dirname
    except Exception as e:

        raise e


def image_upload_handler(image_object, root_dir, filename=None, resize=False, dimension=(), extension='JPEG',
                         quality=100):
    return_value = False
    if image_object:
        file_name = filename if filename is not None else str(random.randint(10000, 10000000)) + '_' + str(
            int(time.time())) + '_' + image_object.name
        try:
            im = Image.open(image_object)
            if resize:
                if len(dimension) == 2:
                    im.thumbnail(dimension, Image.ANTIALIAS)
                else:
                    raise ValueError('Dimension is required, when resize is True.')
            im.save(root_dir + file_name, extension, quality=quality)
            return_value = file_name
        except Exception as e:
            raise e
    return return_value


