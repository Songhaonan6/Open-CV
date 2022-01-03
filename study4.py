import cv2

img1 = cv2.imread('image2.jpg')
img2 = cv2.imread('text.jpg')
print(img1,img2)
res = cv2.addWeighted(img1 , 0.6 , img2 , 0.4 , 0)

cv2.imshow('test',res)
cv2.waitKey(0)