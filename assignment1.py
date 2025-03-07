import cv2
import numpy as np

# 定義旋轉函數
def transFormImage(angle, scale):
    M = cv2.getRotationMatrix2D(center, angle, scale)
    transformed_image = cv2.warpAffine(img, M, (width, height))
    cv2.imshow('Assignment1', transformed_image)

# 定義滑桿回調函數
def trackerbarAngle(val):
    angle = val - 180  # 使角度範圍從-180到180
    scale = cv2.getTrackbarPos('Scale', 'Assignment1') / 100.0
    transFormImage(angle, scale)

def trackerbarScale(val):
    scale = val/100.0 # 將縮放範圍設置成0.1~2.0
    # angle = cv2.getTrackbarPos('Angle', 'Assignment1') - 180
    transFormImage(angle, scale)    

# 定義滑鼠事件
def cropImage(event, x, y, flag, param):
    global dot1, dot2, img
    
    # 滑鼠拖曳發生時
    if flag == 1:
        trackerBarInit()
        if event == 1:
            dot1 = [x, y]
        if event == 0:
            img2 = img.copy() 
            dot2 = [x, y] 
                        
            cv2.rectangle(img2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), (0,0,255), 2)
            cv2.imshow('Assignment1', img2)
    if event == 4:
        cropped_image = img[dot1[1]:dot2[1], dot1[0]:dot2[0]]
        cropped_height, cropped_width, cropped_center = getData(cropped_image)

        # 創建一個黑色背景的圖像，大小與原始視窗相同
        background = np.zeros((height, width, 3), dtype=np.uint8)

        # 計算將裁切後的圖像置中的位置
        start_x = (width - cropped_width) // 2
        start_y = (height - cropped_height) // 2

        # 將裁切後的圖像放置在背景上
        background[start_y:start_y+cropped_height, start_x:start_x+cropped_width] = cropped_image

        img = background
        cv2.imshow('Assignment1', img)

def resizeImage(image_path, min_size=600, max_size=1000):
    global width, height, center, img, origin_img

    source_img = cv2.imread(image_path)
    height, width, center = getData(source_img)

    scale_percent = 100
    if max(width, height) > max_size:
        scale_percent = max_size / max(width, height) * 100
    elif min(width, height) < min_size:
        scale_percent = min_size / min(width, height) * 100

    width = int(width * scale_percent / 100)
    height = int(height * scale_percent / 100)

    img = cv2.resize(source_img, (width, height), interpolation=cv2.INTER_LINEAR)
    height, width, center = getData(img)
    cv2.imshow('Assignment1', img)
    origin_img = img.copy() # 保存resize後的圖像

def trackerBarInit():
    cv2.setTrackbarPos('Scale', 'Assignment1', 100)
    cv2.setTrackbarPos('Angle', 'Assignment1', 180)

def getData(image_name): #增加參數
    (height, width) = image_name.shape[:2]
    center = (width // 2, height // 2)

    return height, width, center

# image_path = input("Enter the image name: ")
image_path = 'source/yzu1.jpg'
resizeImage(image_path)

dot1 = [] 
dot2 = [] 

cv2.namedWindow('Assignment1')

cv2.setMouseCallback('Assignment1', cropImage) # 設定滑鼠事件

cv2.createTrackbar('Scale', 'Assignment1', 10, 200, trackerbarScale) #設定滑桿(縮放比例)
cv2.setTrackbarPos('Scale', 'Assignment1', 100)
cv2.createTrackbar('Angle', 'Assignment1', 180, 360, trackerbarAngle) #設定滑桿(旋轉角度)

while True:
    key = cv2.waitKey(0)
    # 按下ESC鍵退出
    if key == 27: 
        img = origin_img.copy()
        trackerBarInit()
        cv2.imshow('Assignment1', img)
    elif key == 113:
        break

    if cv2.getWindowProperty('Assignment1', cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()