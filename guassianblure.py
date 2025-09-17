import cv2
import matplotlib.pyplot as plt

# Read the image
imgbgr = cv2.imread(r"C:\DIPLAB\SALTNPPRCAM.jpg")  # Use raw string to avoid escape issues
imgrgb = cv2.cvtColor(imgbgr, cv2.COLOR_BGR2RGB)

# Apply Gaussian Blur with different kernel sizes
gblur3 = cv2.GaussianBlur(imgrgb, (3, 3), 3)
gblur5 = cv2.GaussianBlur(imgrgb, (5, 5), 3)
gblur11 = cv2.GaussianBlur(imgrgb, (11, 11), 3)

# Plotting the results
plt.subplot(231), plt.imshow(imgbgr), plt.title("BGR Image"), plt.axis('off')
plt.subplot(232), plt.imshow(imgrgb), plt.title("RGB Image"), plt.axis('off')
plt.subplot(234), plt.imshow(gblur3), plt.title("Gaussian 3x3"), plt.axis('off')
plt.subplot(235), plt.imshow(gblur5), plt.title("Gaussian 5x5"), plt.axis('off')
plt.subplot(236), plt.imshow(gblur11), plt.title("Gaussian 11x11"), plt.axis('off')

plt.tight_layout()
plt.show()

