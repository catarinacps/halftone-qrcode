import numpy as np
import cv2

# Load color img as greyscale
img = cv2.imread('img/peace.jpg', 0)

cv2.imshow('teste', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
