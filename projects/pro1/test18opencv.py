#  Computer Vision(opencv:Open Source Computer Vision 라이브러리 사용)

import cv2
print(cv2.__version__)

img1 = cv2.imread('test18ani.jpeg')
print(type(img1))

cv2.imshow('image test', img1)
cv2.waitKey()
cv2.destroyAllWindows()
print('end')

cv2.imwrite('test18ani2.jpg', img1)
cv2.imwrite('test18ani3.jpg', img1, [cv2.IMWRITE_JPEG_QUALITY, 20])

img2 = cv2.resize(img1, (300, 100), interpolation=cv2.INTER_AREA)
cv2.imwrite('test18ani4.jpg', img2)  