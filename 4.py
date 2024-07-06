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
    
#!https://leetcode.com/problems/merge-nodes-in-between-zeros/
class Solution(object):
    def mergeNodes(self, head):
        temp=head
        arr=[]
        x=0
        while temp!=None:
            x+=temp.val
            if temp.val==0: 
                arr.append(x)
                x=0
            temp=temp.next
        arr=arr[1:]
        arr=arr[::-1]
        head=ListNode(arr.pop())
        tmp=head
        while len(arr)>0:
            temp=ListNode(arr.pop())
            tmp.next=temp
            tmp=tmp.next
        return head

#!https://leetcode.com/problems/pass-the-pillow/
class Solution(object):
    def passThePillow(self, n, time):
        if time<n:
            return 1+time
        x = time//(n-1)
        y = time%(n-1)
        if x%2==1:
            return n-y
        else:
            return y+1
