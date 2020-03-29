# python3 src/main.py -p opencv
# python3 src/main.py -p matplotlib

import numpy as np
import cv2 as cv
import argparse

args = argparse.ArgumentParser()
args.add_argument(
	"-p", "--plot",
	required=True,
	help="select opencv or matplotlib to plot the img",
	default="opencv"
)

ap = vars(args.parse_args())

# Color image loaded by OpenCV is in BGR mode. But Matplotlib displays in RGB mode. 
# So color images will not be displayed correctly in Matplotlib if image is read with OpenCV


# Load a color image in grayscale
# 1 or not = default
# 0 = grayscale
# -1 = alpha channel
img = cv.imread('input/example.jpeg', 0)

####
# plot with opencv
####

if ap["plot"] == "opencv":
	cv.namedWindow('image', cv.WINDOW_NORMAL) #enable the window resize, the default flag is cv.WINDOW_AUTOSIZE
	cv.imshow('image',img)

	key = cv.waitKey(0) & 0xFF #64bit machine (0xFF = 255 integer)

	if key == ord("s"):
		cv.imwrite("output/gray.png", img)
		cv.destroyAllWindows()

	elif key == 27: #wait for esc to close and exit
		cv.destroyAllWindows()

	#its unnecessary, but is to try the keyboards events

elif ap["plot"] == "matplotlib":
	import matplotlib.pyplot as plt
	plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
	plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
	plt.show()

