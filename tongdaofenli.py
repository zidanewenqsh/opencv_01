import cv2
import numpy as np
'''色彩空间转换
通道分离
'''
path = r"./images/04.jpg"
img = cv2.imread(path)
# img[:,:,0]=0
# img[:,:,1]=0
img[:,:,2]=0

cv2.imshow("04.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()