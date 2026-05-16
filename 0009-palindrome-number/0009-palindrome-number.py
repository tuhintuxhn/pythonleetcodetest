class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        sum = 0
        while (x>0):
            rem = x % 10
            sum = (sum*10) + rem
            x = x // 10
        if sum == temp:
            return True 
        else:
            return False            