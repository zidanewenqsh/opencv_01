# -*- coding:utf-8 -*-

import cv2

cap = cv2.VideoCapture(r"D:\PycharmProjects\opencv_01\videos\iccas.mp4")

while(1):

# 读取视频帧

    ret, frame = cap.read()

# 显示视频帧

    cv2.imshow("capture", frame)

#等候50ms,播放下一帧，或者按q键退出

    if cv2.waitKey(50) &0xFF ==ord('q'):

        break

#释放视频流

cap.release()

#关闭所有窗口

cv2.destroyAllWindows()