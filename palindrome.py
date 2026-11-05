class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # Convert integer to string and check if it reads the same backwards
        s = str(x)
        return s == s[::-1]
