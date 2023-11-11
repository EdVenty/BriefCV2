# The example of using BriefCV2 lib.
# In this example we detect not bumped robots.

import cv2
import numpy as np

from brief_cv2 import Namespaces as n, using
from brief_builtins import min_key

using(*n.all)

img = cv2.imread("r.png")
gray = cv2.c_bgr_to_gray(img)
bin = cv2.t_binary_inv(gray, 200, 255)
bin = cv2.m_close(bin, np.ones([5, 5]))

cnts = cv2.fc_nonapprox(bin)
min_area = min_key(cnts, cv2.contourArea)
cnts = [c for c in cnts if cv2.contourArea(c) / min_area < 1.2]
[cv2.rectangle(img, *cv2.br_xy(c), cv2.c_blue, 2) for c in cnts]

cv2.drawContours(img, cnts, -1, cv2.c_red, 2)
cv2.imshow("img", img)
cv2.waitKey()
