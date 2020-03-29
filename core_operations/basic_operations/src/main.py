import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#Accessing and Modifying pixel values

img = cv.imread("input/messi5.jpg")

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyWindow("img")

print("\nAccessing and Modifying pixel values")

pixel = img[100, 100]
print(pixel)

#BGR - BLUE, GREEN AND RED
# accessing only blue pixel
blue = img[100, 100, 0] #0 - blue
green = img[100, 100, 1] #1 - green
red = img[100, 100, 2] #2 - red

print(blue)
print(green)
print(red)

#modifying value
img[100, 100] = [255, 255, 255]

print(img[100, 100])

#the method above is good for a set of pixels, for individuals pixels, is good to use the method below

modified_img = np.copy(img)

#modifying a set of pixels
modified_img[0:100, 0:100] = [255, 255, 255]

cv.imshow("modified_img", modified_img)
cv.waitKey(0)
cv.destroyWindow("modified_img")

#acessing value
print(img.item(10,10,2))

#modifying value
img.itemset((10, 10, 2), 100)

print(img.item(10,10,2))


#Accessing Image Properties
print("\nAccessing Image Properties")

print(img.shape)

#if the shape length is 2, the image its on grayscale, that's, row and column.

print(img.size, "= that's, n_rows * n_columns * n_channels")

#img.dtype is very important while debugging because a large number of errors in OpenCV-Python code are caused by invalid datatype.
print( img.dtype )

print("\nImage ROI")

print("ROI = Region on interested")

ball = img[280:340, 330:390]

cv.imshow("ball", ball)
cv.waitKey()
cv.destroyWindow("ball")

img[273:333, 100:160] = ball

cv.imshow("img", img)
cv.waitKey()
cv.destroyWindow("img")

print("\nSplitting and Merging Image Channels")

b,g,r = cv.split(img)

#or 

b = img[:,:,0] #its better

#merging
img = cv.merge((b,g,r))

#setting red pixels to 0
img[:,:,2] = 0

cv.imshow("img", img)
cv.waitKey()
cv.destroyWindow("img")

print("\nMaking Borders for Images (Padding)")

BLUE = [255,0,0]
img1 = cv.imread('input/opencv-logo.png')
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.show()
