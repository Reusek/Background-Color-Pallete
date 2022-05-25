""" Image module """
from pathlib import Path
import numpy as np
from PIL import Image

def load_image(path: Path) -> np.ndarray:
    """ Load image file to numpy ndarray. """
    img = Image.open(path)
    img.load()
    return np.asarray(img, dtype=np.int32)
