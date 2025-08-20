import cv2 as cv
img=cv.imread("C:\DIPLAB\AdditiveColorMixing.svg.png")
B,G,R = cv.split(img)
cv.imshow("COLOUR IMAGE",img)
cv.imshow("BLUE CHANNEL",B)
cv.imshow("GREEN CHANNEL",G)
cv.imshow("RED CHANNEL",R)
cv.waitKey(0)
cv.destroyAllWindows()
