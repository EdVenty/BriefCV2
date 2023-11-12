import cv2
import numpy as np
from brief_cv2 import using, create_namespace

namespace_custom_colors = lambda: create_namespace({
    "pink": (255, 110, 110)[::-1], # convert from RGB to BGR
    "cyan": (10, 255, 255)[::-1]
})

using(namespace_custom_colors)

img = np.ones((100, 100, 3), np.uint8) * 255
cv2.circle(img, (50, 50), 20, cv2.pink, -1)
cv2.circle(img, (50, 50), 10, cv2.cyan, -1)

cv2.imshow("img", img)
cv2.waitKey(0)