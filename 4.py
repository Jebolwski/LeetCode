#!https://leetcode.com/problems/find-the-maximum-achievable-number/
class Solution(object):
    def theMaximumAchievableX(self, num, t):
        return num+t*2

#!https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
class Solution(object):
    def minimumOperations(self, nums):
        x=0
        for i in nums:
            if i==1:
                x+=1
            elif (i+1)%3==0 or (i-1)%3==0:
                x+=1
        return x

#!https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/   
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        x=0
        y=0
        for i in nums:
            x+=i
            for j in str(i):
                y+=int(j)
        return abs(x-y)