"""# pip install opencv-contrin-python pillow mediapipe
import cv2 # library
import numpy as np

CAM_IDX = 0 # default camera
cam = cv2.VideoCapture(CAM_IDX)
while cam.isOpened():
    state, frame = cam.read()
    if not state:
        print('Camera is not available')
        break
    # teen panch yaha se shuru kro
    frame = cv2.flip(frame, 1) #mirror image
    # teen panch yaha pe khatm
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    outline = cv2.Canny(gray, 100, 110) # img, min, max
    img = np.hstack([gray, outline])
    # drawing
    img = cv2.put.Text(img, "GRAY IMAGE",(300,20),
                       cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),2)
    img = cv2.putText(img, "CANNY IMAGE", (1280-300, 40),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),2)
    #hstack = np.hstack([gray, outline])
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == 27: # ESC key
        break
cam.release()
cv2.destroyAllWindows()"""


# pip install opencv-contrin-python pillow mediapipe
import cv2 # library
import numpy as np

CAM_IDX = 0 # 0: default camera
cam = cv2.VideoCapture(CAM_IDX)
while cam.isOpened():
    state, frame = cam.read()
    if not state:
        print('Camera is not available')
        break
    # teen panch yaha se shuru kro
    frame = cv2.flip(frame, 1) # mirror image
    # teen panch yaha pe khatm
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) == 27: # ESC KEY
        break
cam.release()
cv2.destroyAllWindows()