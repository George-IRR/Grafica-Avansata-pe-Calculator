import cv2
import numpy as np

# image path
poza = 'flori.png'

# read color image
imagine = cv2.imread(poza)

# convert to grayscale (Harris requires gray image)
gray = cv2.cvtColor(imagine, cv2.COLOR_BGR2GRAY)

# convert to float32 (Harris requirement)
gray = np.float32(gray)

# Harris corner detection
dst = cv2.cornerHarris(gray, 2, 3, 0.05)

# dilate to make corners more visible
dst = cv2.dilate(dst, None)

# mark strong corners in red
imagine[dst > 0.01 * dst.max()] = [0, 0, 255]

# show result and wait for ESC
cv2.imshow('dst', imagine)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()