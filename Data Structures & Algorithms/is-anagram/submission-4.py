class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = [0] * 26
        t_freq = [0] * 26

        if len(s) != len(t):
            return False

        for ch in s:
            s_freq[ord(ch) - ord('a')] += 1

        for ch in t:
            t_freq[ord(ch) - ord('a')] += 1
            
        return s_freq == t_freq
        