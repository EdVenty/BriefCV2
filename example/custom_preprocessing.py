import cv2
import numpy as np
from brief_cv2 import using, create_namespace

namespace_custom_preprocessing = lambda: create_namespace({
    "gauss_s": lambda img: cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT),
    "gauss_m": lambda img: cv2.GaussianBlur(img, (7, 7), cv2.BORDER_DEFAULT),
    "gauss_l": lambda img: cv2.GaussianBlur(img, (21, 21), cv2.BORDER_DEFAULT),
})

using(namespace_custom_preprocessing)

img = cv2.imread("logo.png")
img = cv2.resize(img, (100, 100))

dst_s = cv2.gauss_s(img)
dst_m = cv2.gauss_m(img)
dst_l = cv2.gauss_l(img)

cv2.imshow("img", np.hstack((img, dst_s, dst_m, dst_l)))
cv2.waitKey(0)