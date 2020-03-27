#try with webcam

import numpy as np
import cv2 as cv

cap = cv.VideoCapture("input/race.mp4")

#print the widht and height of the video
print(cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT))


# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
fps = 20
size = int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
out = cv.VideoWriter()
success = out.open('output/output.mp4', fourcc, fps, size, True)

while cap.isOpened():
	# Capture frame-by-frame
	ret, frame = cap.read()

	# if frame is read correctly ret is True
	if not ret:
		print("Can't receive frame (stream end?). Exiting ...")
		break
	# Our operations on the frame come here
	
	frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	frame = cv.flip(frame, 0)
	
	out.write(frame)

	# Display the resulting frame
	cv.imshow('frame', frame)
	if cv.waitKey(25) & 0xFF == ord('q'):
		break	

# When everything done, release the capture
cap.release()
out.release()

cv.destroyAllWindows()