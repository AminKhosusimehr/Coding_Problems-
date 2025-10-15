class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        index = len(s) + 1  
        for i in s[-1:0:-1] :
            index-=1
            if i == ' ' :
                return len(s) - index
            