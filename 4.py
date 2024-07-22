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

#!https://leetcode.com/problems/water-bottles/
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total=numBottles
        while numBottles>=numExchange:
            mod=numBottles%numExchange
            numBottles/=numExchange
            total+=numBottles
            numBottles+=mod
        return total

#!https://leetcode.com/problems/root-equals-sum-of-children/
class Solution(object):
    def checkTree(self, root):
        return root.left.val+root.right.val==root.val

#!https://leetcode.com/problems/average-waiting-time/
class Solution(object):
    def averageWaitingTime(self, customers):
        time=customers[0][0]
        x=0
        for i in customers:
            if time<i[0]:
                time=i[0]
            time+=i[1]
            x+=(time-i[0])
        return x*1.00/len(customers)
    
#!https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses
class Solution(object):
    def __init__(self):
        self.i = 0

    def reverseParentheses(self, s):
        def helper(s):
            sb = []

            while self.i < len(s):
                if s[self.i] == ')':
                    self.i += 1
                    return ''.join(sb)[::-1]
                elif s[self.i] == '(':
                    self.i += 1
                    st = helper(s)
                    sb.append(st)
                else:
                    sb.append(s[self.i])
                    self.i += 1

            return ''.join(sb)

        return helper(s)

#!https://leetcode.com/problems/check-if-array-is-good/      
class Solution(object):
    def isGood(self, nums):
        arr=[]
        en_b=max(nums)
        for i in range(1,en_b+1):
            arr.append(i)
        arr.append(en_b)
        return sorted(nums)==arr

#!https://leetcode.com/problems/neither-minimum-nor-maximum/
class Solution(object):
    def findNonMinOrMax(self, nums):
        en_b=max(nums)
        en_k=min(nums)
        x=0
        for i in nums:
            if i<en_b and i>en_k:
                return i
        return -1 
    
#!https://leetcode.com/problems/find-the-peaks/
class Solution(object):
    def findPeaks(self, mountain):
        arr=[]
        for i in range(1,len(mountain)-1):
            if mountain[i]>mountain[i+1] and mountain[i]>mountain[i-1]:
                arr.append(i)
        return arr
    
#!https://leetcode.com/problems/sum-of-squares-of-special-elements/
class Solution(object):
    def sumOfSquares(self, nums):
        n=len(nums)
        x=0
        for i in range(1,len(nums)+1):
            if n%i==0:
                x+=nums[i-1]**2
        return (x)     
        
#!https://leetcode.com/problems/maximum-strong-pair-xor-i/
class Solution(object):
    def maximumStrongPairXor(self, nums):
        x=0
        arr=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if abs(nums[i]-nums[j]) <= min(nums[i],nums[j]):
                    arr.append([nums[i],nums[j]])
        res=[0,0]
        last_biggest=0
        for i in arr:
            a,b=i
            if a^b > last_biggest:
                last_biggest=a^b
                res=i
        return last_biggest

#!https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> list:
        self.res = 0  
        
        def dfs(node) -> list:
            if not node: return []
            if not node.left and not node.right: return [1]

            left_list = dfs(node.left)
            right_list = dfs(node.right)
            self.res += sum(l+r <= distance for l in left_list for r in right_list)
            return [1+item for item in left_list+right_list]
        
        dfs(root)
        return self.res 

#!https://leetcode.com/problems/two-out-of-three/  
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        arr=[]
        for i in nums1:
            if i in nums2 and i not in arr:
                arr.append(i)
        for i in nums2:
            if i in nums3 and i not in arr:
                arr.append(i)
        for i in nums1:
            if i in nums3 and i not in arr:
                arr.append(i)
        return arr
        
#!https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==0:
            return 'a'+('b'*(n-1))
        else:
            return 'a'*n

#!https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/
class Solution(object):
    def countPrefixSuffixPairs(self, words):
        x=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if len(words[i])>len(words[j]):
                    continue
                else:
                    bas=words[j][:len(words[i])]
                    son=words[j][(len(words[j])-len(words[i])):]
                    if bas==words[i] and son==words[i]:
                        x+=1
        return x

        
