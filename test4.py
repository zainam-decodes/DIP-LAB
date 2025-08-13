import cv2
img=cv2.imread("C:/Users/Student/Pictures/dip/lenaimagecolor.jfif")
cv2.imshow("Lena Image",img)

k=cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
       status=cv2.imwrite("C:/Users/Student/Pictures/dip/new.png",img)
       print("File writing status",status)
       cv2.destroyAllWindows()
