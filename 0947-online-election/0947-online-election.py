from bisect import bisect_right
from collections import defaultdict

class TopVotedCandidate:

    def __init__(self, persons, times):
        self.times = times
        self.leaders = []
        count = defaultdict(int)
        leader = -1
        for p in persons:
            count[p] += 1
            if count[p] >= count.get(leader, 0):
                leader = p
            self.leaders.append(leader)

    def q(self, t):
        i = bisect_right(self.times, t)
        return self.leaders[i-1]
