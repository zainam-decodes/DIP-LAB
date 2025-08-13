import cv2
img=cv2.imread("C:/Users/Student/Pictures/dip/lenaimagecolor.jfif")
cv2.imshow("Lena Image",img)
cv2.imwrite("C:/Users/Student/Pictures/dip/newimage.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()