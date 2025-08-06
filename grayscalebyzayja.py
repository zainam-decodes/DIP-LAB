import cv2
img=cv2.imread("C:/Users/Student/Pictures/lenatest.jpeg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Lena Image",img)
cv2.waitKey(0)

cv2.destroyAllWindows()
