import cv2

#img = cv2.imread('text.jpg',cv2.IMREAD_ANYCOLOR)  #读取彩色图
#img = cv2.imread('text.jpg',cv2.IMREAD_GRAYSCALE)  #读取灰度图
img = cv2.imread('text.jpg',cv2.IMREAD_UNCHANGED)  #读取包含透明通道的彩色图

cv2.imshow('text',img)
cv2.waitKey(0)