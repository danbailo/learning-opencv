import cv2

img = cv2.imread("../Computer-Vision-with-Python/DATA/00-puppy.jpg")

img = cv2.resize(img, (0,0), img, 0.5, 0.5)

cv2.imshow("window name", img)
cv2.waitKey(0)        
cv2.destroyAllWindows()