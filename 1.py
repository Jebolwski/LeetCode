import math
from math import sqrt
#!https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    result = [i,j]
                    print(i,j)
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
        print(total_num)
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
                    print(i)
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
            print(nums1)
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
        print(dividend)
        
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
        