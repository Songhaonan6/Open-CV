import cv2

img = cv2.imread('text.jpg')


# px = img[100,100]
# print(px)

# img[100,100] = [0,0,0]
# px = img[100,100]
# print(px)

# cv2.imshow('123',img)
# cv2.waitKey(0)

# print(img.dtype)   #图像数据类型
# print(img.size)   #图像

# height,width,channels = img.shape

# print(height,width,channels)

#ROI region of interest  Region of interest

# img_part = img[100:350,240:420]

# cv2.imshow('part',img_part)
# cv2.waitKey(0)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('img',img)
cv2.imshow('img_gray',img_gray)
cv2.waitKey(0)