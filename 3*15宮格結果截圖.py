#玩家遊玩中截圖, 驗證計算
import cv2

# 影片檔案路徑
video_path = "/Users/user/Desktop/leetcode/2024AWS競賽/尊博Jumbo/龍門_遊戲說明_音量語系押注大小切換_自動玩.mp4"

# 讀取影片
cap = cv2.VideoCapture(video_path)

# 檢查影片是否成功打開
if not cap.isOpened():
    print("Error: Cannot open video file")
else:
    # 讀取影片中的第一幀
    ret, img = cap.read()

    if ret: #True=確定可讀取下一幀
        # 設置截圖範圍
        crop_areas = [
            (1210,1470,190,470), #11
            (1210,1470,505,785),  #12
            (1210,1470,820,1100), #13
            (1210,1470,1135,1415),#14
            (1210,1470,1450,1730),#15
            (1480,1740,190,470), #21
            (1480,1740,505,785), #22
            (1480,1740,820,1100), #23
            (1480,1740,1135,1415),#24,
            (1480,1740,1450,1730),#25,
            (1750,2010,190,470), #31
            (1750,2010,505,785), #32
            (1750,2010,820,1100), #33
            (1750,2010,1135,1415), #34
            (1750,2010,1450,1730) #35
        ]

        # 顯示原圖
        cv2.imshow('img', img)

        # 存截圖
        for i, (y1, y2, x1, x2) in enumerate(crop_areas, start=1):
            cropped_img = img[y1:y2, x1:x2]
            output_path = f'/Users/user/Desktop/leetcode/2024AWS競賽/尊博Jumbo/截圖測試/位置{i}.png'
            cv2.imwrite(output_path, cropped_img)  # 存圖片
            print(f'Screenshot saved to {output_path}')
        
        cv2.waitKey(10)
    else:
        print("Error: Cannot read frame from video")

# 釋放影片資源
#cap.release()
#cv2.destroyAllWindows()
