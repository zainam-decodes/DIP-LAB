import cv2
import matplotlib.pyplot as plt
imgbgr=cv2.imread("C:\DIPLAB\lenaimg.jpg")
imgrgb=cv2.cvtColor(imgbgr,cv2.COLOR_BGR2RGB)
ksize3=(3,3)
ksize5=(5,5)
ksize11=(11,11)
boxblur3=cv2.blur(imgrgb,ksize3)
boxblur5=cv2.blur(imgrgb,ksize5)
boxblur11=cv2.blur(imgrgb,ksize11)

plt.subplot(231),plt.imshow(imgbgr),plt.title("BGR Image"),plt.axis('off')
plt.subplot(232),plt.imshow(imgrgb),plt.title("RGB IMAGE"),plt.axis('off')
plt.subplot(234),plt.imshow(boxblur3),plt.title("BOXBLUR IMAGE 3x3 "),plt.axis('off')
plt.subplot(235),plt.imshow(boxblur5),plt.title("BOXBLUR IMAGE 5X5 "),plt.axis('off')
plt.subplot(236),plt.imshow(boxblur11),plt.title("BOXBLUR IMAGE 11X11 "),plt.axis('off')
plt.show()