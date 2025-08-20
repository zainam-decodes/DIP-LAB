import cv2
imgbgr = cv2.imread("C:/DIPLAB/lenaimagecolor.jfif")
img_rgb=cv2.cvtColor(imgbgr,cv2.COLOR_BGR2LUV)
cv2.imshow("BGR IMAGE",imgbgr)
cv2.waitKey(0)
cv2.imshow("RGB IMAGE",img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()


