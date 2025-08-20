import cv2 as cv
img=cv.imread("C:/DIPLAB/lenaimagecolor.jfif")
imggray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Image",img)
cv.imshow(" Gray Image",imggray)
cv.waitKey(0)
cv.destroyAllWindows()
