class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            for x in range(len(t)):
                if s[i] != t[x]:
                    return False
        return True