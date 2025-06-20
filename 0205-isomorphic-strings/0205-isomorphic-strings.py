class Solution(object):
    def isIsomorphic(self, s, t):
        return [s.index(char) for char in s] == [t.index(char) for char in t]

            
                


        