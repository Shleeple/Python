import cv2 as cv
img = cv.imread('Pictures/cat.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)