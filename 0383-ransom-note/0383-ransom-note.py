class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        letter_count = [0] * 26
        for char in magazine:
            letter_count[ord(char) - ord('a')] += 1
        for char in ransomNote:
            index = ord(char) - ord('a')
            letter_count[index] -= 1
            if letter_count[index] < 0:
                return False
            
        return True

        