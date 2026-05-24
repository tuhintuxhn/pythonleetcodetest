class Solution:
    def isPerfectSquare(self, num: int) -> bool: 
        if num >= 0:
            sqrt = int(num ** 0.5)
            return sqrt * sqrt == num
        return False    