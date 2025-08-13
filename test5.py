import cv2
img=cv2.imread("C:/Users/Student/Pictures/dip/lenaimagecolor.jfif")
cv2.imshow("Lena Image",img)
img2=cv2.imread("C:/Users/Student/Pictures/dip/lenaimagecolor.jfif",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Lena Image Gray",img2)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('c'):
    status= cv2.imwrite("C:/Users/Student/Pictures/dip/dip3.png",img)
    print("Colour Image",status)
    cv2.destroyAllWindows()
elif k == ord('g'):
    status= cv2.imwrite("C:/Users/Student/Pictures/dip/dip3.png",img2)
    print("Gray Image",status)
    cv2.destroyAllWindows()