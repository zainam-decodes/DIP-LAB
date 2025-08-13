import cv2
img=cv2.imread("C:/Users/Student/Pictures/dip/lenaimagecolor.jfif")
cv2.imshow("Lena Image",img)
status=cv2.imwrite("C:/Users/Student/Pictures/dip/newimage.png",img)
print("File writing status",status)
cv2.waitKey(0)
cv2.destroyAllWindows()
