import cv2
img = cv2.imread("C:/Users/Student/Pictures/dip/cameraman.jfif")
(row,col,chan) = img.shape[0:3]
print("Number of rows :", row)
print("Number of columns :", col)
print("Number of channels :", chan)