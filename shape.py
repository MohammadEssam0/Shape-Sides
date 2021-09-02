import cv2 as cv
import numpy as np
import sys

img = cv.imread(sys.argv[1])
greyImage = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_ ,thresholdImage  = cv.threshold(greyImage, 240 , 255, cv.CHAIN_APPROX_NONE)
contours , _ = cv.findContours(thresholdImage, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01* cv.arcLength(contour, True), True)
    cv.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0] - 8
    y = approx.ravel()[1]
    cv.putText( img, "it Has " + str(len(approx)) +' side', (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255) )
    print("it Has " + str(len(approx)) +' side')
cv.imshow('shapes', img)
Key = cv.waitKey(0)
cv.destroyAllWindows()
