import cv2

img = cv2.imread('D:\Soeasy\openCV\study1.jpg',cv2.IMREAD_UNCHANGED)  #读取包含透明通道的彩色图

cv2.imshow('text',img)
cv2.waitKey(0)