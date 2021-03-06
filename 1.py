import cv2
import numpy as np
import matplotlib.pyplot as plt
#                               0
img = cv2.imread('dulces.jpg',cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1

##cv2.imshow('image', img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()


plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([100,59],[80,100], 'c', linewidth=5)
plt.show()

cv2.imwrite('dulcesgray.png', img)
