import cv2
import numpy as np

# img = input("Enter the image name: ")
img = cv2.imread('source/yzu1.jpg')
img = cv2.resize(img, (800, 600))

dot1 = [] 
dot2 = [] 

#固定視窗大小為800x600
#使用滑桿等比例調整圖片大小

#
def show_xy(event, x, y, flag, param):
    global dot1, dot2, img
    
    # 滑鼠拖曳發生時
    if flag == 1: 
        if event == 1:
            dot1 = [x, y]
        if event == 0:
            img2 = img.copy() 
            dot2 = [x, y] 
                        
            cv2.rectangle(img2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), (0,0,255), 2)
            cv2.imshow('Assignment1', img2)
    if event == 4:
        interest_zone = img[dot1[1]:dot2[1], dot1[0]:dot2[0]]
        interest_zone = cv2.resize(interest_zone, (600, 600))
        cv2.imshow('Assignment1', interest_zone)

cv2.imshow('Assignment1', img)
cv2.setMouseCallback('Assignment1', show_xy) # 設定滑鼠事件

cv2.waitKey(0)
cv2.destroyAllWindows()