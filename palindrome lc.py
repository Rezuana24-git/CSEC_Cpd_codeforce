class Solution:
    def isPalindrome(self, x: int) -> bool:
        m=str(x)
        reverse=m[::-1]
        if reverse==m:
            return True
        else:
            return False
