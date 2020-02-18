import cv2
import numpy as np
'''色彩空间转换
色彩空间 RGB/RGBA/GRAY/HSV/YUV
通道分离
理解HSV
'''
path = r"./images/04.jpg"
src = cv2.imread(path)

#
# dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) # 将颜色转为灰度
dst = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# dst = cv2.cvtColor(src, cv2.COLOR_BGR2YUV) #
cv2.imshow("src show", src)
cv2.imshow("dst show", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()