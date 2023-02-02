## Problem1 
# Pow(x,n) (https://leetcode.com/problems/powx-n/)
# TC : O(log n)
# SC : O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n<0:
            return 1/self.myPow(x, -n)
        elif n%2==0:
            # print(self.myPow(x*x, n//2),"1")
            return self.myPow(x*x, n//2)
        else:
            # print(self.myPow(x*x, n//2)*x,"2")
            return self.myPow(x*x, n//2) * x