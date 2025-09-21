from collections import Counter
from math import gcd
from functools import reduce
from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return reduce(gcd, Counter(deck).values()) >= 2
