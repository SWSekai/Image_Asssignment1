import cv2

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
    angle = cv2.getTrackbarPos('Angle', 'Assignment1') -180
    transFormImage(angle, scale)    

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
        img = img[dot1[1]:dot2[1], dot1[0]:dot2[0]]
        img = cv2.resize(img, (600, 600))
        cv2.imshow('Assignment1', img)

def resizeImage(image_path, min_size=600, max_size=1000):
    origin_img = cv2.imread(image_path)
    (height, width) = origin_img.shape[:2]

    scale_percent = 100
    if max(width, height) > max_size:
        scale_percent = max_size / max(width, height) * 100
    elif min(width, height) < min_size:
        scale_percent = min_size / min(width, height) * 100

    width = int(width * scale_percent / 100)
    height = int(height * scale_percent / 100)

    return cv2.resize(origin_img, (width, height), interpolation=cv2.INTER_LINEAR)

def getUpdateData():
    (height, width) = img.shape[:2]
    center = (width // 2, height // 2)

    return center, height, width

# img = input("Enter the image name: ")
image_path = 'source/yzu1.jpg'
img = resizeImage(image_path)

dot1 = [] 
dot2 = [] 

(height, width) = img.shape[:2]
center = (width // 2, height // 2)

#固定視窗大小為800x600
cv2.namedWindow('Assignment1')
# cv2.resizeWindow('Assignment1', 800, 600) #待處理

cv2.setMouseCallback('Assignment1', show_xy) # 設定滑鼠事件

cv2.createTrackbar('Scale', 'Assignment1', 10, 200, trackerbarScale) #設定滑桿(縮放比例)
cv2.setTrackbarPos('Scale', 'Assignment1', 100)
cv2.createTrackbar('Angle', 'Assignment1', 180, 360, trackerbarAngle) #設定滑桿(旋轉角度)

cv2.waitKey(0)
cv2.destroyAllWindows()