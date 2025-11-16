# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        result = False
        left = 1
        right = num // 2
        result = False
        while (left <= right):
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
        return False
