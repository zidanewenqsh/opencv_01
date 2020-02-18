import cv2

path = r"./images/4.jpg"
img = cv2.imread(path)
# img = cv2.imread(path,0) # 以灰度方式读入

print("img.shape", img.shape, type(img.shape),type(img)) #(2720, 1813, 3) <class 'tuple'> <class 'numpy.ndarray'>
height, width = img.shape[:2]
print("height,width", height, width)

# 下面的 None 本应该是输出图像的尺寸，但是因为后边我们设置了缩放因子
# 因此这里为 None
res = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_CUBIC)
print("res.shape", res.shape)

#OR
# 这里呢，我们直接设置输出图像的尺寸，所以不用设置缩放因子
# res = cv2.resize(img, (int(0.3*width),int(0.3*height)),interpolation=cv2.INTER_CUBIC) # 注意宽度高度的顺序

cv2.imshow("4.jpg", res)
# cv2.imshow("4.jpg", img) # 原图太大
cv2.imwrite("./images/04.jpg",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
