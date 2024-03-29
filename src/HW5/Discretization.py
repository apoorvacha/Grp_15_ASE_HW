from Col import COL
from Query import *

from Data import *
import Update as upd

import math
from copy import deepcopy
from Range import *
  
def bins(cols, rowss):
    for _, col in enumerate(cols):
        ranges = {}
        index = 0 
        n_ranges = {}
        n_ranges_list = []
        for y, rows in rowss.items():
            for _, row in enumerate(rows):

                if (isinstance(col, COL)):
                   col = col.col
                   
                x = row[col.at]

                if x != '?':
                    k = int(bin(col, float(x) ))
                    if k in ranges:
                        ranges[k] = ranges[k] 
                    else:
                        ranges[k] = RANGE(col.at, col.txt, float(x))
                    upd.extend(ranges[k], float(x), y)

        ranges = {key: value for key, value in sorted(ranges.items(), key=lambda x: x[1].lo)}

        out = []

        for r in ranges:
            n_ranges[index] = ranges[r]
            index = index+1

        if(hasattr(col, "isSym") and col.isSym):
            out.append(n_ranges_list )
        
    return out

def bin(col, x):

    if x=="?" or hasattr(col, "isSym"):
        return x
    tmp = (col.hi - col.lo)/(16 - 1)
    
    if col.hi == col.lo:
        return 1 
    else:
        return  math.floor(x/tmp+0.5)*tmp

min = -float("inf")
max = float("inf")

def mergeAny(ranges0):

    def noGaps(t):
        for j in range(1, len(t)):
            t[j].lo = t[j-1].hi
        t[0].lo = min
        t[-1].hi = max
        return t

    ranges1, j , left, right , y= [], 0

    while j < len(ranges0):
        left, right = ranges0[j], ranges0[j+1]
        if right:
            y = merge2(left.y, right.y)
            if y:
               j = j+1
               left.hi, left.y = right.hi, y
        ranges1.append(left)
        j = j+1
    
    if len(ranges1) == len(ranges0):
        return noGaps(ranges0)
    else : 
       mergeAny(ranges1)

def merge2(col1, col2):

    new = merge(col1, col2)

    if div(new) <= (div(col1)*col1.n + div(col2)*col2.n)/new.n:
        return new

def merge(col1, col2):

    new = deepcopy(col1)
    if hasattr(col1, "isSym") and col1.isSym:
        for x, n in col2.has.items():
            upd.add(new, x, n)
    else:
        for n in col2.has:
            upd.add(new, n)

        new.lo = min(col1.lo, col2.lo)
        new.hi = max(col1.hi, col2.hi)

    return new