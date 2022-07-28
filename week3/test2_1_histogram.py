import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("ponyo1.jpg")
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

plt.subplot(1,3,1) # 1행 3열 chart 공간의 첫 번째
plt.title("bgr image") # 1행 3열 첫 번째 공간의 제목 
plt.imshow(img) # 1행 3열 첫 번째 공간에 이미지를 넣겠다 

plt.subplot(1,3,2) # 1행 3열 chart의 두 번째
plt.title("rgb image")
plt.imshow(img_rgb)

plt.subplot(1,3,3) # 1행 3열 chart의 세 번째  
plt.title("gray image")
plt.imshow(img_gray, cmap='gray')

plt.show()