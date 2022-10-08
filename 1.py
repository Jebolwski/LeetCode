
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
        