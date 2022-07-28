import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img_bgr = cv.imread("ponyo1.jpg")
img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img_bgr,cv.COLOR_RGB2GRAY)

hist_r = cv.calcHist([img_rgb], [0], None, [255], [0, 255]) 
hist_g = cv.calcHist([img_rgb], [1], None, [255], [0, 255]) 
hist_b = cv.calcHist([img_rgb], [2], None, [255], [0, 255]) 

hist_gray = cv.calcHist([img_gray], [0], None, [255], [0, 255])   

plt.subplot(1,4,1)
plt.imshow(img_rgb)
plt.title("input rgb image")

plt.subplot(1,4,2)
plt.plot(hist_r, color = "r")
plt.plot(hist_g, color = "g")
plt.plot(hist_b, color = "b")
plt.xlim([0,256])

plt.subplot(1,4,3)
plt.imshow(img_gray, cmap='gray')
plt.title("input gray image")

plt.subplot(1,4,4)
plt.plot(hist_gray)
plt.xlim([0,256])

plt.show() 