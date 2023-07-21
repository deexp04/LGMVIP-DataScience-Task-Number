# IMPORTING OPENCV

import cv2

# UPLOADING IMAGE

image = cv2.imread("jerry.png")

# GRAY SCALE IMAGE

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# INVERTED IMAGE

inverted_image = 255 - gray_image

# BLURRED IMAGE USING GAUSSIAN FUNCTION

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

# INVERTED BLURRED IMAGE

inverted_blurred = 255 - blurred

# IMAGE TO PENCIL SKETCH

pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("ORIGINAL IMAGE", image)
cv2.imshow("PENCIL SKETCH", pencil_sketch)
cv2.waitKey(0)
