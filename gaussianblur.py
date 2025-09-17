import cv2
import matplotlib.pyplot as plt
imgbgr=cv2.imread("C:\DIPLAB\SALTNPPRCAM.jpg")
imgrgb=cv2.cvtColor(imgbgr,cv2.COLOR_BGR2RGB)


mblur3=cv2.medianBlur(imgrgb,3)
mblur5=cv2.medianBlur(imgrgb,5)
mblur11=cv2.medianBlur(imgrgb,11)

plt.subplot(231),plt.imshow(imgbgr),plt.title("BGR Image"),plt.axis('off')
plt.subplot(232),plt.imshow(imgrgb),plt.title("RGB IMAGE"),plt.axis('off')
plt.subplot(234),plt.imshow(mblur3),plt.title("Median 3x3 "),plt.axis('off')
plt.subplot(235),plt.imshow(mblur5),plt.title("Median  5X5 "),plt.axis('off')
plt.subplot(236),plt.imshow(mblur11),plt.title("Median  11X11"),plt.axis('off')
plt.show()