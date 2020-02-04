import cv2
import numpy as np

img = np.empty((200, 200, 3), np.uint8)
img[..., 0] = 255
img[..., 1] = 0
img[..., 2] = 0
cv2.imshow("temp",img)
cv2.imwrite("./saves/2.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
