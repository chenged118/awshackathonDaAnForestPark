import cv2

def extract_frames(video_path, output_folder, frame_rate=1, start_x=0, start_y=0, width=100, height=100):
    # 打開影片檔案
    cap = cv2.VideoCapture(video_path)
    count = 0
    
    # 檢查影片是否成功打開
    if not cap.isOpened():
        print("Error: Unable to open video.")
        return
    
    # 建立輸出資料夾
    import os
    os.makedirs(output_folder, exist_ok=True)
    
    # 讀取影片每一幀並截取圖像
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: #初始化失敗的話ret=false
            break
        
        # 根據設定的幀率保存圖像
        if count % frame_rate == 0:
            # 對影片幀進行裁剪
            cropped_frame = frame[start_y:start_y+height, start_x:start_x+width]
            frame_path = os.path.join(output_folder, f"frame_{count}.jpg")
            cv2.imwrite(frame_path, cropped_frame) #存圖片
            print(f"Saved frame {count}")
        
        count += 1
    
    # 釋放影片檔案
    cap.release()

# 影片檔案路徑
video_path = "/Users/user/Desktop/leetcode/2024AWS競賽/尊博Jumbo/龍門_遊戲說明_音量語系押注大小切換_自動玩.mp4"
# 輸出圖像資料夾
output_folder = "frames"

# 截取幀的頻率，例如每秒截取一次可以設為 1
frame_rate = 1000

# 設定要截取的範圍 (左上角的 (start_x, start_y) 和寬高)
start_x = 1210
start_y = 1740
width = 190
height = 470

# 執行截取圖像的函式
extract_frames(video_path, output_folder, frame_rate, start_x, start_y, width, height)
