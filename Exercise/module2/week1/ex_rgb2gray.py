import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2
img = mpimg.imread ("dog.jpeg")    

def lightness(img):

    channel_r = img[:,:,0]
    channel_g = img[:,:,1]
    channel_b = img[:,:,2]

    gray_value = (np.maximum(channel_r, np.maximum(channel_g, channel_b)) + np.minimum(channel_r, + np.minimum(channel_g, channel_b))) /2
    return gray_value

def avaerage(img):

    channel_r = img[:,:,0]
    channel_g = img[:,:,1]
    channel_b = img[:,:,2]

    gray_value = channel_r /3 + channel_g/3 + channel_b/3
    return gray_value

def luminority(img):

    channel_r = img[:,:,0]
    channel_g = img[:,:,1]
    channel_b = img[:,:,2]

    gray_value = channel_r * 0.21 + channel_g *  0.72 + channel_b* 0.07
    return gray_value


if __name__ == "__main__":

    gray_lightness_img   = lightness(img)
    cv2.imwrite("gray_lightness_img.png", gray_lightness_img)

    gray_avaerage_img    = avaerage(img)
    cv2.imwrite("gray_avaerage_img.png", gray_avaerage_img)

    gray_limunitory_img  = luminority(img)
    cv2.imwrite("gray_limunitory_img.png", gray_limunitory_img)

