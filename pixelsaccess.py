import cv2 as cv
img=cv.imread("C:/DIPLAB/lenaimagecolor.jfif")
rows , cols = img.shape[0:2]
print("NUMBER OF ROWS :",rows)
print("NUMBER OF COLS :",cols)

for i in range(rows):
    for j in range(cols):
        img[i,j]=sum(img[i,j])/3
cv.imshow(" Grayscale Image",img)
cv.waitKey(0)
cv.destroyAllWindows()
