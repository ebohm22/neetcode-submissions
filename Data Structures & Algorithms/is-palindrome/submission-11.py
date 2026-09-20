import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (s.translate(str.maketrans('', '', string.punctuation))).replace(" ","").lower()
        if len(s) < 2: return True

        if len(s)%2 == 0:
            count = len(s)/2  
        else: count= int(math.ceil(len(s)/2) +1)
        res = True
        for i in range(int(count)):
            if s[i] != s[len(s)-i-1]: 
                res = False
                break

        return res
