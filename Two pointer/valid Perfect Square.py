class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left <= right:
            middle = (left + right)//2
            if middle ** 2 == num:
                return True
            elif middle **2 < num:
                left = middle + 1
            else:
                right = middle - 1


        
        return False
