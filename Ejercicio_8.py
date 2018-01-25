import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_orange = np.array([1, 100, 100])
    upper_orange = np.array([21, 255, 255])

    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15, 15), np.float32) / 225
    smoothed = cv2.filter2D(res, -1, kernel)

    #mejorar granularidad
    blur = cv2.GaussianBlur(res, (15, 15), 0)
    median = cv2.medianBlur(res, 15)
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)


    cv2.imshow('Original', frame)
    #cv2.imshow('Averaging', smoothed)
   # cv2.imshow('Gaussian Blurring', blur)
   # cv2.imshow('Median Blur', median)
    cv2.imshow('bilateral Blur', bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()