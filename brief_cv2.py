import cv2
from dataclasses import dataclass
from typing import Any, Dict
import functools
import hashlib
from numpy import ndarray

@dataclass
class Bag:
    eval_func: Any
    context: Any = None
    
    def __call__(self, *args, **kwargs):
        return self.eval_func(self.context, *args, **kwargs)
    
@dataclass
class HashableNDArrayContainer:
    ndarray: ndarray
    
    def __hash__(self) -> int:
        hash = hashlib.blake2b(self.ndarray.tobytes(), digest_size=20)
        for dim in self.ndarray.shape:
            hash.update(dim.to_bytes(4, byteorder='big'))
        return int.from_bytes(hash.digest())

    
namespace_morph = lambda: [
    *{
        "m_" + name.removeprefix("MORPH_").lower(): Bag(lambda ctx, img, *a, **k: cv2.morphologyEx(img, ctx['type'], *a, **k), {'type': cv2.__dict__[name]}) for name in cv2.__dict__ if name.startswith("MORPH_")
    }.items(),
    *{
        "m_erode": lambda *args, **kwargs: cv2.erode(*args, **kwargs),
        "m_dilate": lambda *args, **kwargs: cv2.dilate(*args, **kwargs),
    }.items()
]
namespace_color = lambda: [
    *{
        "c_" + name.removeprefix("COLOR_").lower().replace('2', "_to_"): Bag(lambda ctx, img, *a, **k: cv2.cvtColor(img, ctx['type'], *a, **k), {'type': cv2.__dict__[name]}) for name in cv2.__dict__ if name.startswith("COLOR_")
    }.items(),
    *{
        "c_red": (0, 0, 255),
        "c_green": (0, 255, 0),
        "c_blue": (255, 0, 0)
    }.items()
]
namespace_threshold = lambda: [
    *{
        "t_" + name.removeprefix("THRESH_").lower(): Bag(lambda ctx, img, *a, **k: cv2.threshold(img, *a, **k, type=ctx['type'])[1], {'type': cv2.__dict__[name]}) for name in cv2.__dict__ if name.startswith("THRESH_")
    }.items()
]
namespace_contours = lambda: [
    *{
        "fc": lambda *args, **kwargs: cv2.findContours(*args, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE, **kwargs)[0],
        "fc_nonapprox": lambda *args, **kwargs: cv2.findContours(*args, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE, **kwargs)[0],
        "br_xy": lambda *args, **kwargs: (lambda r: ((r[0], r[1]), (r[0] + r[2], r[1] + r[3])))(cv2.boundingRect(*args, **kwargs))
    }.items(),
]
namespace_cache = lambda: [
    *{
        "contourArea": lambda arr: functools.lru_cache()(cv2.contourArea)(HashableNDArrayContainer(arr)).ndarray
    }.items()
]

def create_namespace(attributes_dict: Dict):
    return [
        *attributes_dict.items()
    ]

class Namespaces:
    color = namespace_color
    morph = namespace_morph
    threshold = namespace_threshold
    contours = namespace_contours
    all = [namespace_color, namespace_morph, namespace_threshold, namespace_contours]

def flatten(l):
    return [item for sublist in l for item in sublist]

def using(*namespaces):
    for i in flatten([
            i() for i in namespaces
        ]):
        setattr(cv2, i[0], i[1])
        