import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_brg = cv.imread("ponyo1.jpg")
img_rgb = cv.cvtColor(img_brg, cv.COLOR_BGR2RGB)

img_blur = cv.blur(img_rgb,(5,5)) # OpenCV에서 제공하는 blur fuction 
img_gaussianblur = cv.GaussianBlur(img_rgb,(5,5),0) # 두번째 항은 mask의 크기, 세번째 항은 sigma값
 
# https://numpy.org/doc/stable/reference/generated/numpy.array.html
kernel = np.array(np.mat('0,-1,0;-1,5,-1;0,-1,0'))  # kernel을 만들어서 
img_sharp = cv.filter2D(img_rgb, -1, kernel)  # filter2D에 적용함

plt.subplot(2,2,1), plt.imshow(img_rgb)
plt.title("input rgb image")
plt.subplot(2,2,2), plt.imshow(img_blur)
plt.title("blur image")
plt.subplot(2,2,3), plt.imshow(img_gaussianblur)
plt.title("gaussian blur image")
plt.subplot(2,2,4), plt.imshow(img_sharp)
plt.title("sharpen image")
plt.show()