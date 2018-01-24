import numpy as np
import cv2

gray = cv2.imread('herramientas.jpg', cv2.IMREAD_GRAYSCALE)

"""
THRESH_TRUNC
THRESH_TOZERO
THRESH_TOZERO_INV
"""
t, dst = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
t, dst2 = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY_INV)
t, dstCalulate = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)


cv2.imshow('gray', gray)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.imshow('dstCalulate', dstCalulate)


cv2.waitKey(0)
cv2.destroyAllWindows()