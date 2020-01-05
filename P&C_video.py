import cv2
import numpy as nm
cap = cv2.VideoCapture(0) 
while cap.isOpened():
    ret, img = cap.read()

    cv2.imshow("my video",img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('p'):
        cv2.waitKey(-1) #wait until any key is pressed
cap.release()
cv2.destroyAllWindows()