import math
from math import sqrt
import heapq


#!https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    result = [i,j]
                    return result

#!https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode()
        num1 = ""
        num2 = ""
        fake_l1=l1
        fake_l2=l2
        while(fake_l1!=None):
            num1 = num1+str(fake_l1.val)
            fake_l1=fake_l1.next
        while(fake_l2!=None):
            num2 = num2+str(fake_l2.val)
            fake_l2=fake_l2.next
            
        num1=int(num1[::-1])
        num2=int(num2[::-1])
        total_num = num1+num2
        carrier = l3
        reverse_total_num = str(total_num)[::-1]

        l3.val=reverse_total_num[0:1]
        
        
        for i in reverse_total_num[1:len(reverse_total_num)]:
            a = ListNode()
            a.val=i
            carrier.next = a
            carrier = a
        return l3
       
#!https://leetcode.com/problems/longest-substring-without-repeating-characters/        
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i=0
        array=[]
        while(len(s)>i):
            a=i
            string=""
            while(a<len(s)-1 and s[a] not in string):
                string+=s[a]
                if a+1==len(s)-1 and s[a+1] not in string:
                    string+=s[a+1]
                array.append(string)
                a+=1
            i+=1
            
        if len(s)<1:
            return 0
            
        if len(array)<1:
          
            return len(s[0])
        else:
            max_len=0
            for i in array:
                if len(i)>max_len:
                    max_len=len(i)
            return max_len
            for i in array:
                if len(i)==max_len:
                    break
        
#!https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        for i in nums2:
            nums1.append(i)
        nums1=sorted(nums1)
        
        if len(nums1)%2==1:
            return nums1[(len(nums1)/2+1)-1]
        else:
            num = (nums1[len(nums1)/2-1]+nums1[len(nums1)/2])/2.00
            return num       
        
#!https://leetcode.com/problems/longest-palindromic-substring/submissions/
class Solution(object):
    def longestPalindrome(self, s):
        result=""
        for i in range(0,len(s)+1):
           for j in range(i,len(s)+1):
                string = s[i:j] 
                if string!="" and string==string[::-1]:
                    if len(string)>len(result):
                        result=string
        return result
            
#!https://leetcode.com/problems/reverse-integer/submissions/
class Solution(object):
    def reverse(self, x):
        if str(x)[0]=="-":
            string = str(x)[1:len(str(x))][::-1]
            if int(string)*-1<-2147483648:
                return 0                
            else:
                return int(string)*-1
        else:
            if (int(str(x)[::-1]))>2147483647:
                return 0
            else:
                return (int(str(x)[::-1]))

#!https://leetcode.com/problems/roman-to-integer/submissions/
class Solution(object):
    def romanToInt(self, s):
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        result=0
        for i in range(0,len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                result-=roman[s[i]]
            else:
                result+=roman[s[i]]
        result+=roman[s[len(s)-1]]
        
        return result
        

#!https://leetcode.com/problems/longest-common-prefix/
class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix=strs[0]
        
        for i in strs:
            while i[0:len(prefix)]!=prefix:
                prefix=prefix[0:len(prefix)-1]
                
        return prefix
        
#!https://leetcode.com/problems/3sum/
class Solution(object):
    def threeSum(self, nums):
        array=[]
        array1=[]
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0 and i!=j and j!=k and sorted([nums[i],nums[j],nums[k]]) not in array:
                        array.append(sorted([nums[i],nums[j],nums[k]]))  
        return (sorted(array))

#!https://leetcode.com/problems/merge-two-sorted-lists/submissions/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1==None and list2==None:
            node = ListNode()
            node.val=""
            return node
        
        array=[]
        a = list1
        b = list2
        while a!=None:
            array.append(a.val)
            a=a.next
        while b!=None:
            array.append(b.val)
            b=b.next
        array = list(reversed(sorted(array)))
        newlist=ListNode()
        resultlist = newlist
        while len(array)>0:
            resultlist.val=array.pop()
            if len(array)!=0:
                listnode = ListNode()
                resultlist.next = listnode
                resultlist=resultlist.next
        return(newlist)

#!https://leetcode.com/problems/plus-one/submissions/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        array=[]
        strin=""
        for i in digits:
            strin+=str(i)
        strin=str(int(strin)+1)
        for i in strin:
            array.append(i)
        return array

#!https://leetcode.com/problems/divide-two-integers/submissions/
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        result = int(dividend/divisor)
        if result>pow(2,31)-1:
            return pow(2,31)-1 
        elif result<pow(-2,31):
            return pow(-2,31)
        else:
            return result

#!https://leetcode.com/problems/sqrtx/submissions/
class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(sqrt(x))

#!https://leetcode.com/problems/valid-perfect-square/submissions/
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if sqrt(num)!=math.floor(sqrt(num)):
            return False
        return True

#!https://leetcode.com/problems/sum-of-square-numbers/submissions/
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if sqrt(c)==math.floor(sqrt(c)):
            return True
        karekok = int(sqrt(c))
        l,r=0,int(math.sqrt(c))
        
        while l<=r:
            a2=l*l
            b2=r*r
            if a2+b2==c:
                return True
            elif a2+b2<c:
                l+=1
            else:
                r-=1

#!https://leetcode.com/problems/permutations/submissions/
class Solution(object):
    def __init__(self):
        self.res=[]
    def permute(self, nums):
        self.backtrack(nums,[])
        return self.res
    def backtrack(self,nums,path):
        if not nums:
            self.res.append(path)
        for x in range(len(nums)):
            self.backtrack(nums[:x]+nums[x+1:],path+[nums[x]])
            
#!https://leetcode.com/problems/powx-n/submissions/        
class Solution(object):
    def myPow(self, x, n):
        if 0.5>x and x>-0.5 and n>10:
            return 0.0
        if x==1:
            return 1
        if x==-1 and n%2==0:
            return 1
        if x==-1 and n%2==1:
            return -1
        if n>0:
            result=1
            while(n>0):
                n-=1
                result*=x
        else:
            result=x**n
        
        return result   

#!https://leetcode.com/problems/super-pow/submissions/
class Solution(object):
    def superPow(self, a, b):
        b_full=""
        for i in b:
            b_full+=str(i)
        b=int(b_full)
        return pow(a,b,1337)    

#!https://leetcode.com/problems/number-of-1-bits/submissions/
class Solution(object):
    def hammingWeight(self, n):
        number = (bin(n)[2:])
        result = 0
        for i in number:
            if i=="1":
                result+=1
        return result  

#!https://leetcode.com/problems/reverse-linked-list/submissions/
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        
        if not head:
            node = ListNode()
            node.val=""
            return node
        array = []
        while head!=None:
            array.append(head.val)
            head=head.next
        node = ListNode()
        resultlist = node
        while len(array)>0:
            resultlist.val=array.pop()
            if len(array)!=0:
                listnode = ListNode()
                resultlist.next = listnode
                resultlist=resultlist.next
        return node    

#!https://leetcode.com/problems/reverse-string/submissions/
class Solution(object):
    def reverseString(self, s):
        a = s.reverse()
        return a

#!https://leetcode.com/problems/subsets/submissions/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        subset = []
        
        def backtrack(i):
            if i>=len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i+1)
            
            subset.pop()
            backtrack(i+1)
            
        backtrack(0)
        return result

#!https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.right),self.maxDepth(root.left))                       

#!https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/
class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(0,len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1    

#!https://leetcode.com/problems/repeated-substring-pattern/submissions/
class Solution(object):
    def repeatedSubstringPattern(self, s):
        for i in range(1,len(s)):
            if len(s)%i==0:
                if str(s[:i])*(len(s)/i)==s:
                    return True
        return False
        
#!https://leetcode.com/problems/repeated-string-match/submissions/
class Solution(object):
    def repeatedStringMatch(self, a, b):
        count=1
        fake_a=a
        if a==b or b in a:
            return 1
        while True:
            
            count+=1
            fake_a=a*count
            if b in fake_a:
                return count
            if count>10000 or len(fake_a)>len(b)*8:
                return -1
        return -1

#!https://leetcode.com/problems/trapping-rain-water/
class Solution(object):
    def trap(self, height):
        total=0
        if len(height)<=2:
            return 0
        for i in range(0,len(height)):
            if height[:i]:
                left_max=max(height[:i])
            else:
                left_max=0
            if height[i:len(height)]:
                right_max=max(height[i:len(height)])
            else:
                right_max=0
            if (min(left_max,right_max)-height[i])>0:
                total+=min(left_max,right_max)-height[i]
        return total


#!https://leetcode.com/problems/rotate-image/submissions/
class Solution(object):
    def rotate(self, matrix):
        #transpoze
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                print(i,j)
                temp = matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
                
        #horizontal shift
        for i in range(len(matrix)):
            for j in range(len(matrix)/2):
                temp = matrix[i][len(matrix[i])-j-1]
                matrix[i][len(matrix[i])-j-1]=matrix[i][j]
                matrix[i][j]=temp 


#!https://leetcode.com/problems/majority-element/submissions/
class Solution(object):
    def majorityElement(self, nums):
        array=[]
        for i in nums:
            if i not in array:
                array.append(i)
        max_count=0        
        for i in array:
            if nums.count(i)>max_count:
                max_count=nums.count(i)
        for i in array:
            if nums.count(i)==max_count:
                return i

#!https://leetcode.com/problems/jump-game/submissions/        
class Solution(object):
    def canJump(self, nums):
        goal=len(nums) - 1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        if goal==0:
            return True
        return False

#!https://leetcode.com/problems/single-number/submissions/     
class Solution(object):
    def singleNumber(self, nums):
        res=0
        for i in nums:
            res= i^res
        return res

#!https://leetcode.com/problems/unique-paths/submissions/
class Solution(object):
    def uniquePaths(self, m, n):
        small=min(n-1,m-1)
        big=max(n-1,m-1)
        smaller_fact = 1
        top=1
        for i in range(1,small+1):
            smaller_fact*=i
        for i in range(big+1,big+small+1):
            top*=i
        return top/smaller_fact

#!https://leetcode.com/problems/fizz-buzz/submissions/   
class Solution(object):
    def fizzBuzz(self, n):
        array=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                array.append("FizzBuzz")
            elif i%3==0:
                array.append("Fizz")
            elif i%5==0:
                array.append("Buzz")
            else:
                array.append(str(i))
        return array
        
#!https://leetcode.com/problems/valid-anagram/submissions/
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        s_array=[]
        t_array=[]
        for i in s:
            s_array.append(i)
        for i in t:
            t_array.append(i)
        for i in s_array:
            if i in t_array:
                t_array.remove(i)
        if len(t_array)==0:
            return True
        return False
        
#!https://leetcode.com/problems/sort-colors/submissions/
class Solution(object):
    def sortColors(self, nums):
        temp_index=0
        for i in range(len(nums)):
            min_ind=i
            for j in range(i,len(nums)):
                if nums[min_ind]>nums[j]:
                    min_ind=j
            nums[min_ind],nums[i]=nums[i],nums[min_ind]

#!https://leetcode.com/problems/move-zeroes/submissions/
class Solution(object):
    def moveZeroes(self, nums):
        zero_length =(nums.count(0))
        while 0 in nums:
            nums.remove(0)
        for i in range(zero_length):
            nums.append(0)
            
        return nums
        
#!https://leetcode.com/problems/apply-operations-to-an-array/submissions/
class Solution(object):
    def applyOperations(self, nums):
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        zero_length =(nums.count(0))
        while 0 in nums:
            nums.remove(0)
        for i in range(zero_length):
            nums.append(0)
            
        return nums

#!https://leetcode.com/problems/sliding-window-median/submissions/
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        result_array=[]
        for i in range(len(nums)-k+1):
            array = list(sorted(nums[i:i+k]))
            if len(array)%2 == 0:
                result = ((array[(len(array))/2])+(array[len(array)/2-1]))/2.0
                result_array.append(result)
            else:
                result = array[int(math.floor(len(array)/2))]
                result_array.append(result)
        return result_array

#!https://leetcode.com/problems/intersection-of-two-arrays-ii/submissions/
class Solution(object):
    def intersect(self, nums1, nums2):
        array=[]
        for i in nums1:
            if i in nums2 and i not in array:
                arr1=nums1.count(i)
                arr2=nums2.count(i)
                for j in range(min(arr1,arr2)):
                    array.append(i)
        return array
        
#!https://leetcode.com/problems/intersection-of-two-arrays/submissions/
class Solution(object):
    def intersection(self, nums1, nums2):
        array=[]
        for i in nums1:
            if i in nums2 and i not in array:
                array.append(i)
        return array

#!https://leetcode.com/problems/find-the-difference-of-two-arrays/submissions/
class Solution(object):
    def findDifference(self, nums1, nums2):
        array=[]
        array1=[]
        array2=[]
        for i in nums1:
            if i not in nums2 and i not in array1:
                array1.append(i)
        for i in nums2:
            if i not in nums1 and i not in array2:
                array2.append(i)
        array.append(array1)
        array.append(array2)
        return array

#!https://leetcode.com/problems/count-common-words-with-one-occurrence/submissions/
class Solution(object):
    def countWords(self, words1, words2):
        count=0
        for i in words1:
            if words1.count(i)==1 and words2.count(i)==1:
                count+=1
        return count

#!https://leetcode.com/problems/uncommon-words-from-two-sentences/submissions/
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        array=[]
        s1=s1.split(" ")
        s2=s2.split(" ")
        for i in s1:
            print(i,s1.count(i),s2.count(i))
            if s1.count(i)==1 and i not in s2:
                array.append(i)
                
        for i in s2:
            print(i,s1.count(i),s2.count(i))
            if s2.count(i)==1 and i not in s1:
                array.append(i)
                
        return array
                
#!https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/submissions/
class Solution(object):
    def findMaxK(self, nums):
        array=[]
        for i in nums:
            if i*-1 in nums:
                print(i)
                array.append(abs(i))
        if array:
            return max(array)        
        return -1
        
#!https://leetcode.com/problems/contains-duplicate/submissions/   
class Solution(object):
    def containsDuplicate(self, nums):
        array = set()
        for i in nums:
            if i in array:
                return True
            if i not in array:
                array.add(i)
        return False

#!https://leetcode.com/problems/happy-number/submissions/  
class Solution(object):
    def isHappy(self, n):
        n=str(n)
        total=0
        count=0
        while total!=1 and count<15:
            total=0
            count+=1
            for i in n:
                i=int(i)
                total+=i*i
            if total==1:
                return True
            else:
                n=str(total)

#!https://leetcode.com/problems/palindrome-linked-list/submissions/
class Solution(object):
    def isPalindrome(self, head):
        length = 0
        t=head
        while t!=None:
            t=t.next
            length+=1
        if length==1:
            return True
        
        if length%2==0:
            half_length=length/2
            temp=head
            array_first_half=[]
            array_second_half=[]
            for i in range(half_length):
                array_first_half.append(temp.val)
                if len(array_first_half)==half_length:
                    break
                temp=temp.next
            for i in range(half_length):
                temp=temp.next
                array_second_half.append(temp.val)
            if array_first_half==array_second_half[::-1]:
                return True
            return False
        else:
            half_ceil=int(math.ceil(length/2))
            temp=head
            array_first_half=[]
            array_second_half=[]
            for i in range(half_ceil):
                array_first_half.append(temp.val)
                temp=temp.next
            for i in range(half_ceil):
                temp=temp.next
                array_second_half.append(temp.val)
            print(array_first_half,array_second_half)
            if array_first_half==array_second_half[::-1]:
                return True
            return False
        
#!https://leetcode.com/problems/palindrome-number/submissions/
class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        if len(x)%2==0:
            if (x[:len(x)/2]==(x[len(x)/2:])[::-1]):
                return True
            return False
        else:
            if x[:int(math.ceil(len(x)/2))+1]==(x[int(math.floor(len(x)/2)):])[::-1]:
                return True
            return False
        
#!https://leetcode.com/problems/power-of-three/submissions/
class Solution(object):
    def isPowerOfThree(self, n):
        i=0
        while n>=math.pow(3,i):
            if math.pow(3,i)==n:
                return True
            i+=1 
        return False
            
#!https://leetcode.com/problems/power-of-four/submissions/
class Solution(object):
    def isPowerOfFour(self, n):
        i=0
        while n>=math.pow(4,i):
            if math.pow(4,i)==n:
                return True
            i+=1 
        return False

#!https://leetcode.com/problems/power-of-two/submissions/         
class Solution(object):
    def isPowerOfTwo(self, n):
        i=0
        while n>=math.pow(2,i):
            if math.pow(2,i)==n:
                return True
            i+=1 
        return False

#!https://leetcode.com/problems/pascals-triangle/submissions/
class Solution(object):
    def generate(self, numRows):
        array=[[1],[1,1]]
        if numRows==0:
            return None
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        array1=[]
        i=1
        while len(array)!=numRows:
            array1=[]
            
            for j in range(len(array[i])-1):
                array1.append(array[i][j]+array[i][j+1])
            array1.insert(0,1)
            array1.append(1)
            array.append(array1)
            i+=1
        return array
        
#!https://leetcode.com/problems/odd-even-linked-list/submissions/   
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head==None:
            return None
        array=[]
        temp_head=head
        while temp_head!=None:
            array.append(temp_head.val)
            temp_head=temp_head.next
        result=ListNode()
        temp=result
        for i in range(0,len(array),2):
            temp.val=array[i]
            nexttemp=ListNode()
            temp.next=nexttemp
            temp=temp.next
        
        for i in range(1,len(array),2):
            temp.val=array[i]
            nexttemp=ListNode()
            temp.next=nexttemp
            temp=temp.next
        temp=result
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None
        return result
        
#!https://leetcode.com/problems/rotate-array/submissions/
class Solution(object):
    def rotate(self, nums, k):
        array=[]
        for i in range(len(nums)):
            array.append(i)
        for i in range(len(nums)):
            array[(i+k)%len(nums)]=nums[i]
        print(array)
        for i in range(len(array)):
            nums[i]=array[i]

#!https://leetcode.com/problems/spiral-matrix/submissions/        
class Solution(object):
    def spiralOrder(self, matrix):
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res=[]
        while top<bottom and right>left:
            
            #get top
            for i in range(left, right):
                res.append(matrix[top][i])
            top+=1
            
            #get right
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right-=1
            if not (left<right and top<bottom):
                break
            #get bottom
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom-=1
            
            #get left
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left+=1
            
        return res


#!https://leetcode.com/problems/search-a-2d-matrix-ii/submissions/
class Solution(object):
    def searchMatrix(self, matrix, target):
        array=[]
        for i in range(len(matrix)):
            for j in matrix[i]:
                if j==target:
                    return True
        return False
        
#!https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/
class Solution(object):
    def maxProfit(self, prices):
        i=0
        profit=0
        while i<len(prices)-1:
            if prices[i+1]-prices[i]>0:
                profit+=prices[i+1]-prices[i]
            i+=1
        return profit

#!https://leetcode.com/problems/excel-sheet-column-number/submissions/
class Solution(object):
    def titleToNumber(self, s):
        result=0
        for c in s:
            d=ord(c)-ord("A")+1
            result=result*26+d
        return result
        
#!https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        for i in range(k-1):
            nums.pop()
        return nums.pop()

#!https://leetcode.com/problems/third-maximum-number/submissions/
class Solution(object):
    def thirdMax(self, nums):
        nums.sort()
        print(nums)
        array=[]
        for i in nums:
            if i not in array:
                array.append(i)
        nums=array
        print(nums)
        
        if len(nums)<3:
            return nums.pop()
        for i in range(2):
            nums.pop()
        return nums.pop()
        
#!https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/submissions/
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        for i in range(k):
            nums[nums.index(min(nums))]*=-1
        return sum(nums)
        
#!https://leetcode.com/problems/k-closest-points-to-origin/submissions/
class Solution(object):
    def kClosest(self, points, k):
        array=[]
        array1=[]
        for i in points:
            array.append([abs(i[0])*abs(i[0])+abs(i[1])*abs(i[1]),i])
        heapq.heapify(array)
        
        for i in range(k):
            array1.append(heapq.heappop(array)[1])
        return array1

#!https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/submissions/
class Solution(object):
    def kthLargestNumber(self, nums, k):
        for i in range(len(nums)):
            nums[i]=int(nums[i])
        nums.sort()
        for i in range(k-1):
            nums.pop()
        return str(nums.pop())

#!https://leetcode.com/problems/reverse-words-in-a-string-iii/submissions/
class Solution(object):
    def reverseWords(self, s):
        array=s.split(" ")
        for i in range(len(array)/2):
            array[i],array[len(array)-i-1]=array[len(array)-i-1],array[i]    
        print(array)   
        string=""
        for i in array:
            string=string+i+" "
        string = string[:len(string)-1]
        return string[::-1]

#!https://leetcode.com/problems/count-asterisks/submissions/
class Solution(object):
    def countAsterisks(self, s):
        s=s.split("|")
        print(s)
        count=0
        for i in range(0,len(s),2):
            for j in range(len(s[i])):
                if s[i][j]=="*":
                    count+=1
        return count

#!https://leetcode.com/problems/longest-palindromic-substring/submissions/
class Solution(object):
    def longestPalindrome(self, s):
        
        result=""
        resultLen=0
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>resultLen:
                    resultLen=r-l+1
                    result=s[l:r+1]
                r+=1
                l-=1

            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>resultLen:
                    resultLen=r-l+1
                    result=s[l:r+1]
                r+=1
                l-=1
        print(result,resultLen)
        return result

#!https://leetcode.com/problems/search-insert-position/submissions/863224959/        
class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            print(nums.index(target))
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)

#!https://leetcode.com/problems/valid-parentheses/submissions/863765870/
class Solution(object):
    def isValid(self, s):
        if len(s)%2==1:
            return False
        if s[0]==")" or s[0]=="}" or s[0]=="]":
            return False
        if s.count("(")!=s.count(")") or s.count("[")!=s.count("]") or s.count("{")!=s.count("}"):
            return False
        stack=[]
        for c in s:
            if c=="(" or c=="{" or c=="[":
                stack.append(c)
            if stack and c==")" and stack[len(stack)-1]=="(":
                stack.pop()
            if stack and c=="]" and stack[len(stack)-1]=="[":
                stack.pop()
            if stack and c=="}" and stack[len(stack)-1]=="{":
                stack.pop()
        if len(stack)==0:
            return True
        return False

#!https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/864326897/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next

#!https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    string=""
    def Helper(self,root):
        if not root:
            return string
        self.string+=str(root.val)+" "
        self.Helper(root.right)
        self.Helper(root.left)
    def kthSmallest(self, root, k):
        self.Helper(root)
        array = self.string.split(" ")
        array.pop()
        for i in range(len(array)):
            array[i]=int(array[i])
        array = sorted(array)
        
        print(array)
        return (array[k-1])

#!https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/864651552/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        stack=[]
        result=[]
        if not root:
            return result
        
        temp = root

        while temp!=None or len(stack)!=0:
            while temp!=None:
                stack.append(temp)
                temp=temp.left
            
            temp=stack.pop()
            result.append(temp.val)
            temp=temp.right
        
        return result

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root) 
        return res


#!https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        def Helper(nums,left,right):
            if left>right:
                return None
            mid=(right+left) // 2
            node = TreeNode(nums[mid])
            node.left=Helper(nums,left,mid-1)
            node.right=Helper(nums,mid+1,right)
            return node
        return Helper(nums,0,len(nums)-1)

#!https://leetcode.com/problems/same-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (q and not p):
            return False
        
        if (p and p.left) and (q and not q.left):
            return False
        array_p=[]
        array_q=[]
        def Helper(array,node):
            if not node:
                return None
            Helper(array,node.left)
            if node.left and node.right:
                array.append([node.val,node.left.val,node.right.val])
            if node.left and not node.right:
                array.append([node.val,node.left.val])
            if not node.left and not node.right:
                array.append([node.val])
            Helper(array,node.right)
        Helper(array_p,p)
        Helper(array_q,q)
        if len(array_p)!=len(array_q):
            return False
        for i in range(len(array_p)):
            if array_p[i]!=array_q[i]:
                return False
        return True

#!https://leetcode.com/problems/symmetric-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        array1=[]
        array2=[]
        def Helper(array,node):
            if not node:
                return None
            Helper(array,node.left)
            if node.left and node.right:
                array.append([node.val,node.left.val,node.right.val])
            if node.left and not node.right:
                array.append([node.val,node.left.val,None])
            if not node.left and node.right:
                array.append([node.val,None,node.right.val])
            if not node.left and not node.right:
                array.append([node.val,None,None])
            Helper(array,node.right)
        Helper(array1,root.right)
        Helper(array2,root.left)
        print(array1)
        print(array2[::-1])
        for i in range(len(array2)):
            array2[i][1],array2[i][2]=array2[i][2],array2[i][1]
        print(array2[::-1])
        if array1==array2[::-1]:
            return True
        return False

#!https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        tmp=root.right
        root.right=root.left
        root.left=tmp
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root

#!https://leetcode.com/problems/binary-tree-paths/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        string=""
        array=[]
        
        def dfs(string,array,node):
            if not node:
                return None
            string = string + str(node.val) + "->"
            if node.left:
                dfs(string,array,node.left)
            
            if not node.left and not node.right:
                array.append(string[:len(string)-2])
                string=""

            if node.right:
                dfs(string,array,node.right)

        dfs(string,array,root)
        return array

#!https://leetcode.com/problems/increasing-order-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        array=[]
        if root and not root.left and not root.right:
            return root
        def Helper(node):
            if not node:
                return None
            Helper(node.left)
            array.append(node.val)
            Helper(node.right)
        Helper(root)
        tree = TreeNode()
        temp=tree
        for i in range(len(array)-1):
            temp.val=array[i]
            temp.right=TreeNode(array[i+1])
            temp.left=None
            temp=temp.right
        return tree


#!https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        array=[]
        for i in lists:
            temp=i
            while temp:
                array.append(temp.val)
                temp=temp.next
        array=sorted(array)
        array.reverse()
        liste = ListNode()
        temp=liste
        if len(array)==0:
            return None
        while len(array)>0:
            temp.val=array.pop()
            if len(array)>0:
                temp.next=ListNode()
                temp=temp.next
            else:
                break 
        print(liste)
        return liste 

#!https://leetcode.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array=[]
        temp=head
        while temp:
            array.append(temp.val)
            temp=temp.next
            
        if len(array)==0:
            return None

        for i in range(0,len(array)-1,2):
            array[i],array[i+1]=array[i+1],array[i]

        array.reverse()
        liste = ListNode()
        temp = liste
        while len(array)>0:
            temp.val=array.pop()
            if len(array)>0:
                temp.next=ListNode()
                temp=temp.next
            else:
                break 
        head=liste
        return head

#!https://leetcode.com/problems/detect-capital/
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==1:
            return True
        if word.upper()==word:
            return True
        if word.lower()==word:
            return True
        if word[0].upper()==word[0] and word[1:].lower()==word[1:]:
            return True
        return False

#!https://leetcode.com/problems/capitalize-the-title/
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split(" ")
        string=""
        for word in title:
            wordd=""
            if len(word)<=2:
                pass
                wordd+=word.lower()
            else:
                wordd+=word[0].upper()
                wordd+=word[1:].lower()
            string+=wordd + " "
        
        return string[:len(string)-1]

#!https://leetcode.com/problems/to-lower-case/
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

#!https://leetcode.com/problems/simplify-path/submissions/870384909/
class Solution(object):
    def simplifyPath(self, path):
        if path=="/.":
            return "/"
        while "//" in path:
            path=path.replace("//","/")
        while "/./" in path:
            path=path.replace("/./","/")

        array = path.split("/")
        for i in array:
            if i=="":
                array.remove(i)

        if path=="/../":
            return "/"
        stack=[]
        for i in array:
            if i=="..":
                if len(stack)>0:
                    stack.pop()
            else:
                stack.append(i)
        
        string=""
        for i in stack:
            string+="/"+i
        
        
        if string[len(string)-2:]=="/.":
            string = string[:len(string)-2]
        if string=="":
            return "/"
        return string

#!https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/submissions/871223497/
from collections import Counter

class Solution(object):
    def minimumRounds(self, tasks):
        dicti = Counter(tasks)
        # for i in tasks:
        #     if i not in dicti:
        #         dicti[i]=tasks.count(i)
        count=0
        print(dicti)
        for i in dicti:
            if dicti[i]==1:
                return -1
            while dicti[i]!=0 and dicti[i]!=1:
                count+=1
                if dicti[i]%2==0 and dicti[i]%3==0:
                    dicti[i]-=3
                elif dicti[i]%2==0:
                    dicti[i]-=2
                else:
                    dicti[i]-=3
        print(dicti)
        return count

#!https://leetcode.com/problems/odd-string-difference/
class Solution(object):
    def oddString(self, words):
        letter_count = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        difference=[]
        array_b=[]
        for st in words:
            array=[]
            array_b.append(st)
            for i in range(len(st)-1):
                array.append(letter_count[st[i+1]] - letter_count[st[i]])
            difference.append(array)
        print(difference)
        index=0
        for i in range(len(difference)):
            if difference.count(difference[i])==1:
                index=i
                break
        return array_b[i]

#!https://leetcode.com/problems/counting-bits/
class Solution(object):
    def countBits(self, n):
        array=[]
        for i in range(n+1):
            binary=format(i,'b')
            count=0
            for i in binary:
                count+=int(i)
            array.append(count)
        return array

#!https://leetcode.com/problems/group-anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        dicti=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            dicti[tuple(count)].append(s)
        return dicti.values()

#!https://leetcode.com/problems/binary-tree-preorder-traversal/        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array=[]
        def helper(node):
            if not node:
                return None
            array.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root)
        return array

#!https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/874626446/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array=[]
        def helper(node):
            if not node:
                return None
            array.append(node.val)
            helper(node.right)
            helper(node.left)
        helper(root)
        return array[::-1]

#?----------