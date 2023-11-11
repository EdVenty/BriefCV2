# Brief OpenCV/CV2
```python
cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]

|
V

cv2.fc(img)
```
## Shortify your code & develop faster

Long CV2 commands can really tire you out. Write less code to get more result.

```python
img = cv2.imread("r.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
r, bin = cv2.thresh(gray, 200, 255, cv2.THRESH_BINARY_INV)
bin = cv2.morpholoxyEx(bin, np.ones([5, 5]), cv2.MORPH_CLOSE)

cnts, _ = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
min_area = cv2.contourArea(min(cnts, cv2.contourArea))
cnts = [c for c in cnts if cv2.contourArea(c) / min_area < 1.2]

for c in cnts:
    r = cv2.boundingRect(c)
    cv2.rectangle(img, (r[0], r[1]), (r[2], r[3]) (255, 0, 0), 2)
```

Can be written as

```python
img = cv2.imread("r.png")
gray = cv2.c_bgr_to_gray(img)
bin = cv2.t_binary_inv(gray, 200, 255)
bin = cv2.m_close(bin, np.ones([5, 5]))

cnts = cv2.fc(bin)
min_area = min_key(cnts, cv2.contourArea)
cnts = [c for c in cnts if cv2.contourArea(c) / min_area < 1.2]
[cv2.rectangle(img, *cv2.br_xy(c), cv2.c_blue, 2) for c in cnts]
```

But don't forget to include `BriefCV2` library and `BriefBuiltins` module:

```python
from brief_cv2 import Namespaces as n, using
from brief_builtins import min_key

using(*n.all)
```

## Use only required alises

```python
from brief_cv2 import Namespaces as n, using

# to use color functions and attributes
using(n.color)
# to use thresholds and morphology operations
using(n.thresh, n.morph)
# to use all
using(*n.all)
```

See through using examples:

```python
using(n.color)

cv2.c_bgr_to_gray(img) # cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

```python
using(n.thresh)

cv2.t_binary_inv(gray, 200, 255) # cv2.thresh(gray, 200, 255, cv2.THRESH_BINARY_INV)
```

```python
using(n.contour)

cv2.fc_nonapprox(bin) # cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
``` 

## And auxiliary `builtins` function

```python
from brief_builtins import min_key

...
min_area = min_key(cnts, cv2.contourArea)
...

# does the same 

...
min_area = cv2.contourArea(min(cnts, cv2.contourArea))
...
```
