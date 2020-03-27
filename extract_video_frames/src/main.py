import cv2
from args import args
import matplotlib.pyplot as plt


if __name__ == "__main__":

    parser = vars(args())

    video = parser["video"]
    name_video = video.split("/")[-1][:-4]
    
    path_output = parser["output"]


    # Opens the Video file
    capture = cv2.VideoCapture(video)
    i = 0
    while(capture.isOpened()):
        ret, frame = capture.read()
        if ret == False:
            break
        cv2.imwrite(path_output + "/" + name_video + str(i) + '.jpg', frame)
        i+=1
    
    capture.release()
    cv2.destroyAllWindows()