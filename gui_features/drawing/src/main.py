import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 1 px
							#BGR
cv.line(img,(0,0),(511,511),(255,255,255),1)

cv.rectangle(img,(384,0),(510,128),(0,255,0),2)

pts = np.array([[10,100],[110,100],[10,300],[110,300]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))


font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,450), font, 4,(255,255,255),1, cv.LINE_AA)

cv.imshow("img", img)
cv.waitKey(0)