import cv2

# read image
img = cv2.imread('flori.png')

# to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# init FAST detector
fast = cv2.FastFeatureDetector_create()

# detect keypoints
kp = fast.detect(gray, None)

# draw keypoints on original image
img2 = cv2.drawKeypoints(img, kp, None)

# print detector parameters
print("Threshold:", fast.getThreshold())
print("nonmaxSuppression:", fast.getNonmaxSuppression())
print("neighborhood:", fast.getType())
print("Total Keypoints:", len(kp))

# show result
cv2.imshow("Keypoints", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()