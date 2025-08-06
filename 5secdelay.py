import cv2
img1=cv2.imread("C:/Users/Student/Pictures/lenatest.jpeg")
img2=cv2.imread("C:/Users/Student/Pictures/lenatest.jpeg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Lena Image",img1)
cv2.imshow("Lena gary scale  Image",img2)
cv2.waitKey(5000)

cv2.destroyAllWindows()
