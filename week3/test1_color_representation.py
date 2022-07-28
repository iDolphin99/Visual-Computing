import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("home.jpg")

# a student asked if this color representation issue is related to endianness
# http://www.tcpschool.com/c/c_refer_endian
cv.imshow("opencv api", img)    # opencv displays color images with BGR representation by default 

plt.imshow(img) # plt displays color images with RGB representation by defulat

plt.subplot(1,2,1) 
plt.imshow(img)
plt.title("bgr image")

img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.subplot(1,2,2) 
plt.imshow(img_rgb)
plt.title("rgb image")

plt.show()