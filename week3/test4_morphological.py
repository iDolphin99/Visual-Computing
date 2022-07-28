import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# most image processing uses grayscaled image
# so, cv.IMREAD_GRAYSCALE is very useful for this
img_gray = cv.imread("j.png", cv.IMREAD_GRAYSCALE) 
img_hole_gray = cv.imread("j_holes.png", cv.IMREAD_GRAYSCALE) 
img_outn_gray = cv.imread("j_outside_noise.png", cv.IMREAD_GRAYSCALE) 

# https://numpy.org/doc/stable/reference/generated/numpy.ones.html
kernel = np.ones((5,5),np.uint8) # morp위한 kernel, structure element를 uniform하게 가중치를 1로 두어 만들었음 
img_erosion = cv.erode(img_gray, kernel, iterations = 1) # openCV가 기본으로 제공하는 erosion dilation 
img_dilation = cv.dilate(img_gray, kernel, iterations = 1)
img_opening = cv.morphologyEx(img_gray, cv.MORPH_OPEN, kernel) # openCV는 morp~extension function을 통해서 일일히 조합하지 않고 
img_closing = cv.morphologyEx(img_gray, cv.MORPH_CLOSE, kernel) # 별도의 함수와 파라미터를 통해서 바로 구현을 할 수 있음 
img_gradient = cv.morphologyEx(img_gray, cv.MORPH_GRADIENT, kernel)

# open CV에서 제공하는 morp~extension을 쓰지 않고 fundemental한 erosion, dilation 필터의 조합으로 만든 것, 결과는 같다 
img_opening_m = cv.erode(img_outn_gray, kernel, iterations = 1) # 직접 구현한 opening 효과 
img_opening_m = cv.dilate(img_opening_m, kernel, iterations = 1) # 윗줄에서 image를 erosion하고 다시 dilation을 취함, 이때 파라미터에 copy본이 들어감 
 
img_closing_m = cv.dilate(img_hole_gray, kernel, iterations = 1) # 직접 구현한 closing 효과 
img_closing_m = cv.erode(img_closing_m, kernel, iterations = 1) # hole이 있는 영상에 dialation후 다시 erosion을 취함 

img_gradient_m = img_dilation - img_erosion

def plot_img(index, img, title): # 매번 title, plot, show를 일일히 만들 필요 없이 ploting 함수를 작성했음 
    plt.subplot(4,3,index), plt.imshow(img), plt.axis('off') # axis는 공통으로 그리지 않게
    plt.title(title)

plot_img(1, img_gray, "input image") # function을 호출하여 그리기 
plot_img(2, img_erosion, "erosion")
plot_img(3, img_dilation, "dilation")
plot_img(4, img_outn_gray, "input image")
plot_img(5, img_opening, "opening") 
plot_img(6, img_opening_m, "opening m")
plot_img(7, img_hole_gray, "input image")
plot_img(8, img_closing, "closing")
plot_img(9, img_closing_m, "closing m")
plot_img(10, img_gray, "input image")
plot_img(11, img_gradient, "gradient")
plot_img(12, img_gradient_m, "gradient m")

plt.show()

# grayscale image 같은 경우에는 matplotlib가 color 매핑을 하게 됨 
# color 매핑이 되어 0에 해당값은 보라색, 중간값은 푸른색, 밝은 값은 노란색으로 나오게 됨 
# 이것은 def 에서 plt.imshow(img, cmap='gray') 하면
# grayscale로 볼 수 있음 
