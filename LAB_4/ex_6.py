import numpy as np
import cv2
from matplotlib import pyplot as plt
import numpy as np
import cv2
from matplotlib import pyplot as plt

# read image
img = cv2.imread('flori.png')

# to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# find good corners for tracking (max 25, quality 0.01, min distance 10)
corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)

# convert to int coordinates
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

# display with matplotlib
plt.imshow(img)
plt.show()