#-*-coding:utf-8-*-

import cv2

cap = cv2.VideoCapture(r"D:\PycharmProjects\opencv_01\videos\iccas.mp4")

fps =int(cap.get(cv2.CAP_PROP_FPS))

size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print(fps, size, cap.get(cv2.CAP_PROP_FPS))

# videoWriter = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc('M', 'P', '4', '2'), fps, size)
videoWriter = cv2.VideoWriter('video1.avi', cv2.VideoWriter_fourcc(*"XVID"), fps, size)

ret, frame = cap.read()

while(ret):

    # 展示一帧

    # cv2.imshow("capture", frame)

    videoWriter.write(frame)

    # cv2.waitKey(fps)

    ret,frame = cap.read()

cap.release()

cv2.destroyAllWindows()