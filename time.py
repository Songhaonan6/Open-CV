import cv2
import math
import time
import numpy as np

#静态表盘，动态的表针

margin = 5   #上下左右距离
radius = 220 #圆弧半径
thickness_crecle = 5 #表盘外轮廓的宽度
len_sec = 15 #秒盘的刻度线长度
thickness_sec = 2 #秒盘的宽度
len_15sec = 25 #秒盘较长的刻度线长度
thickness_15sec = 5 #秒盘较长的宽度
center = (center_x,center_y) = (225,225) #表的中间位置

img =np.zeros((450,450,3),np.uint8)    #创建一个图片
img[::] = [255,255,255]   #填充为白色

cv2.circle(img,center,radius,(0,0,0),thickness=thickness_crecle)

for i in range(60):    #画出六十个小的线

    x1 = center_x + (radius - thickness_crecle) * math.cos(i*6*np.pi/180)    #计算出秒针盘的起点
    y1 = center_y + (radius - thickness_crecle) * math.sin(i*6*np.pi/180)

    if i%5==0:     #应该画的比较长一些
        x2 = center_x + (radius-len_15sec) * math.cos(i*6*np.pi/180)   #计算出秒盘的终点
        y2 = center_y + (radius-len_15sec) * math.sin(i*6*np.pi/180)
        cv2.line(img, (int(x1),int(y1)),(int(x2),int(y2)),(0,0,0),thickness=thickness_15sec)
    else:        
        x2 = center_x + (radius-len_sec) * math.cos(i*6*np.pi/180)   #计算出秒盘的终点
        y2 = center_y + (radius-len_sec) * math.sin(i*6*np.pi/180)
        cv2.line(img, (int(x1),int(y1)),(int(x2),int(y2)),(0,0,0),thickness=thickness_sec)
        pass
    pass

while(True):

    temp = np.copy(img)

    now_time = time.localtime(time.time())    #获取当前的时间
    hour , minute , second = now_time.tm_hour , now_time.tm_min , now_time.tm_sec   #去除其中的小时，分钟，秒

    #画出秒针
    sec_angle = second*6+270 
    sec_x = center_x+(radius-margin)*math.cos(sec_angle*np.pi/180.0)
    sec_y = center_y+(radius-margin)*math.sin(sec_angle*np.pi/180.0)
    cv2.line(temp, center, (int(sec_x), int(sec_y)), (0 , 0 , 0), 2)

    # 画分刻线
    min_angle = minute*6+270 
    min_x = center_x+(radius-35)*math.cos(min_angle*np.pi/180.0)
    min_y = center_y+(radius-35)*math.sin(min_angle*np.pi/180.0)
    cv2.line(temp, center, (int(min_x), int(min_y)), (0 , 0 , 0), 8)

    # 画时刻线
    hour_angle = hour*30+270 
    hour_x = center_x+(radius-65)*math.cos(hour_angle*np.pi/180.0)
    hour_y = center_y+(radius-65)*math.sin(hour_angle*np.pi/180.0)
    cv2.line(temp, center, (int(hour_x), int(hour_y)), (0 , 0 , 0), 15)

    cv2.imshow('clock',temp)
    k = cv2.waitKey(50)
    if k == ord('q'):
        break
    elif k == ord('s'):
        cv2.imwrite('image3.jpg',temp)
        pass
    pass
