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

#!https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
class Solution(object):
    def getConcatenation(self, nums):
        arr=[]
        for i in range(2):
            for j in nums:
                arr.append(j)
        return arr
        
#!https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
class Solution(object):
    def minBitFlips(self, start, goal):
        return bin(start ^ goal).count('1')
        
#!https://leetcode.com/problems/maximum-repeating-substring/
class Solution(object):
    def maxRepeating(self, sequence, word):
        count=0
        while True:
            if word*(count+1) not in sequence:
                return count
            count+=1

#!https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
class Solution(object):
    def minimumCost(self, cost):
        res=0
        x=0
        cost = sorted(cost)
        while len(cost)>0:
            if x==2:
                x=0
                cost.pop()
            else:
                res+=cost.pop()
                x+=1
        return res
    
#!https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)
        mx = cnt = sum(nums[:k])
        n = len(nums)
        for i in range(k, n + k):
            cnt += nums[i % n]
            cnt -= nums[(i - k + n) % n]
            mx = max(mx, cnt)
        return k - mx

#!https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/
class Solution:
    def minimumPushes(self, input_text: str) -> int:
        # Count letter occurrences
        letter_counts = [0] * 26
        for char in input_text:
            letter_counts[ord(char) - ord('a')] += 1
        
        # Sort counts in descending order
        sorted_counts = sorted(letter_counts, reverse=True)
        
        total_key_presses = 0
        for index, count in enumerate(sorted_counts):
            if count == 0:
                break
            total_key_presses += (index // 8 + 1) * count
        
        return total_key_presses
        
#!https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(x-y) for x, y in zip(sorted(seats), sorted(students)))

#!https://leetcode.com/problems/ugly-number-ii/ 
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly=[1]
        two=three=five=0
        
        while len(ugly)<n:
            while ugly[two]*2<=ugly[-1]: two+=1
            
            while ugly[three]*3<=ugly[-1]:three+=1
                
            while ugly[five]*5<=ugly[-1]:five+=1
                
            ugly.append(min(ugly[two]*2,ugly[three]*3,ugly[five]*5))
            
        return ugly[-1]  
    
#!https://leetcode.com/problems/longest-nice-substring/
class Solution(object):
    def longestNiceSubstring(self, s):
        arr=[]
        def isNiceSubstring(x):
            string=""
            for i in x:
                if i.lower() in x and i.upper() in x:
                    string+=i
            return string==x
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if isNiceSubstring(s[i:j]) and len(s[i:j])>0:
                    arr.append(s[i:j])
        arr.sort(key=len, reverse=True)
        if len(arr)>0:
            return arr[0]
        return ""

#!https://leetcode.com/problems/smallest-index-with-equal-value/   
class Solution(object):
    def smallestEqual(self, nums):
        for i in range(len(nums)):
            if nums[i]==i%10:
                return i
        return -1

#!https://leetcode.com/problems/check-distances-between-same-letters/
class Solution(object):
    def checkDistances(self, s, distance):
        arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        res = []
        for i in range(len(arr)):
            res.append(0)
        for i in range(len(arr)):
            if arr[i] in s:
                x = abs(s.index(arr[i])-s.rindex(arr[i]))-1
                if distance[i]!=x:
                    return False
        return True
    
#!https://leetcode.com/problems/maximum-number-of-pairs-in-array/
class Solution(object):
    def numberOfPairs(self, nums):
        def areAnyPairsLeft():
            for i in nums:
                if nums.count(i)>1:
                    return True
            return False
        x=0
        while areAnyPairsLeft():
            for i in nums:
                if nums.count(i)>1:
                    nums.remove(i)
                    nums.remove(i)
                    x+=1
                    break
        return [x,len(nums)]

#!https://leetcode.com/problems/minimum-number-game/  
class Solution(object):
    def numberGame(self, nums):
        temp_arr=[]
        bob=0
        alice=0
        while len(nums)>0:
            bob=min(nums)
            nums.remove(bob)
            if len(nums)>0:
                alice=min(nums)
                nums.remove(alice)
            temp_arr.append(alice)
            temp_arr.append(bob)
        return temp_arr

#!https://leetcode.com/problems/walking-robot-simulation/     
class Solution:
    def robotSim(self,commands,obstacles):
        x,y,d=0,0,0
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        max_distance=0
        obstacles=set(map(tuple,obstacles))
        
        for cmd in commands:
            if cmd==-1:
                d=(d+1)%4
            elif cmd==-2:
                d=(d-1)%4
            else:
                for _ in range(cmd):
                    nx,ny=x+direction[d][0],y+direction[d][1]
                    if (nx,ny) in obstacles:
                        break
                    x,y=nx,ny
                    max_distance=max(max_distance,x*x+y*y)
        
        return max_distance        
  

#!https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
class Solution(object):
    def modifiedList(self, nums, head):
        temp = head
        while temp!=None and temp.next!=None:
            while temp.next and temp.next.val in nums:
                temp.next=temp.next.next
            temp=temp.next
        for i in range(2):
            if head.val in nums:
                head=head.next
        return head

#!https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/    
class Solution(object):
    def areNumbersAscending(self, s):
        arr=s.split(" ")
        num_arr=[]
        for i in arr:
            try:
                num_arr.append(int(i))
            except:
                continue
        for i in range(len(num_arr)-1):
            if num_arr[i]>=num_arr[i+1]:
                return False
        return True

#!https://leetcode.com/problems/split-linked-list-in-parts/      
class Solution(object):
    def splitListToParts(self, head, k):
        n = 0
        curr = head
        while curr:
            n += 1 
            curr = curr.next
        
        base = n // k  
        extra = n % k 
        
        res = []
        curr = head
        for i in range(k):
            part_head = curr  
            part_size = base + (1 if extra > 0 else 0) 
            extra -= 1
            
            for _ in range(part_size - 1):
                if curr:
                    curr = curr.next
            
            if curr:
                next_part = curr.next 
                curr.next = None 
                curr = next_part 
            
            res.append(part_head)
        
        return res


#!https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
from fractions import gcd
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        temp = head
        while temp.next:
            node = ListNode(val=gcd(temp.val, temp.next.val),next=temp.next)
            temp.next=node
            temp=temp.next.next
        return head
        
        


        