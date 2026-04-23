import numpy as np
import cv2

img = cv2.imread('flori.png',1)
cv2.imshow('flori.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()