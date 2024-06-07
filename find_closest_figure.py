from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
import numpy as np
from PIL import Image
import cv2

def get_image():
    # Later, this will have a better intake functionality for the image, but for now, it just does this.
    return cv2.imread('user_image.png')

def main():
    image = get_image()
    h, w = image.shape[:2]
    print('Height = {}, Width = {}'.format(h, w))

if __name__ == '__main__':
    main()
else:
    print('Running from import')