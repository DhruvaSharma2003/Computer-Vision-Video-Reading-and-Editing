import cv2

source="C:/Users/sharm/Downloads/video.mp4"
cap=cv2.VideoCapture(source)
if not cap.isOpened():
    print("Error opening video file")
    
ret, frame=cap.read()
import matplotlib.pyplot as plt
plt.imshow(frame[...,::-1])
plt.show()

win_name='Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_FULLSCREEN)
while cv2.waitKey(1)!=27:
    has_frame, frame=cap.read()
    if not has_frame:
        break
    cv2.imshow(win_name,frame)
cap.release()
cv2.destroyWindow(win_name)
