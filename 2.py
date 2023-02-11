import collections
#!https://leetcode.com/problems/find-the-difference/
class Solution(object):
    def findTheDifference(self, s, t):
        if s=="":
            return t
        arr1=list(s)
        arr2=list(t)
        d1={}
        d2={}
        for i in arr1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for i in arr2:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        for i in d1:
            if i in d2 and d2[i]==d1[i]:
                del d2[i]
            elif i in d2:
                d2[i]=d2[i]-d1[i]
        string=""
        for i in d2:
            string+=i*d2[i]
        return string

#!https://leetcode.com/problems/pascals-triangle-ii/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        arr=[]
        for i in range(rowIndex+1):
            arr.append([1])
        arr[1].append(1)

        for i in range(2,rowIndex+1):
            for j in range(1,len(arr[i-1])):
                arr[i].append(arr[i-1][j-1]+arr[i-1][j])
            arr[i].append(1)
        return arr[rowIndex]

#!https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={}
        for i in words:
            d[i]=[]
            for j in range(len(i)):
                arr=d[i]
                arr.append(order.index(i[j]))
                d[i]=arr
        res=d.values()
        tot=[]
        for i in res:
            tot.append(i)
        messi=sorted(tot)
        if messi==tot:
            return True
        return False

#!https://leetcode.com/problems/add-strings/
class Solution(object):
    def addStrings(self, num1, num2):
        return str(int(num1)+int(num2))

#!https://leetcode.com/problems/add-to-array-form-of-integer/  
class Solution(object):
    def addToArrayForm(self, num, k):
        ks=str(k)
        if len(ks)<len(num):
            while len(ks)!=len(num):
                ks="0"+ks
        numb=""
        for i in num:
            numb+=str(i)
        numb=int(numb)
        result=int(ks)+numb
        total=[]
        for i in str(result):
            total.append(int(i))
        return total
            
#!https://leetcode.com/problems/add-binary/
class Solution(object):
    def addBinary(self, a, b):
        def getDecimal(binary):
            total=0
            for i in range(len(binary)-1,-1,-1):
                if int(binary[i])==1:
                    total+=pow(2,len(binary)-1-i)
            return total
        
        def makeBinary(x):
            string=""
            for i in bin(x):
                string+=i
            return string[2:]
        a=getDecimal(a)
        b=getDecimal(b)
        return makeBinary(a+b)
        
#!https://leetcode.com/problems/valid-palindrome/
class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        arr=['1','2','3','4','5','6','7','8','9','0','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        string=""
        for i in s:
            if i in arr:
                string+=i
        print(string)
        if string==string[::-1]:
            return True
        return False

#!https://leetcode.com/problems/guess-number-higher-or-lower/
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        l,r=1,n
        while True:
            m=(l+r)//2
            res=guess(m)
            if res==1:
                l=m+1
            elif res==-1:
                r=m-1
            else:
                return m

#!https://leetcode.com/problems/shuffle-the-array/submissions/892524765/        
class Solution(object):
    def shuffle(self, nums, n):
        arr1=nums[:n][::-1]
        arr2=nums[n:][::-1]
        res=[]
        for i in range(n):
            res.append(arr1.pop())
            res.append(arr2.pop())
        return res
    
#!https://leetcode.com/problems/excel-sheet-column-title/
class Solution(object):
    dicty={i:chr(65+i) for i in range(26)}
    def convertToTitle(self, columnNumber: int) -> str:
        i=0
        while True:
            if columnNumber-26**i<0:
                i-=1
                break
            columnNumber-=26**i
            i+=1
        res=""
        for j in range(i,-1,-1):
            res=res+self.dicty[columnNumber//(26**j)]
            columnNumber-=26**j*(columnNumber//(26**j))
        return res
        
#!https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr=[]
        coll=collections.Counter(s)
        for i in coll:
            arr.append([i,coll[i]])
        for i in arr:
            if i[1]==1:
                return s.index(i[0])
        return -1
    
#!https://leetcode.com/problems/self-dividing-numbers/
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr=[]
        for i in range(left,right+1):
            if '0' not in str(i):
                if len(str(i))==1:
                    arr.append(i)
                else:
                    for digit in str(i):
                        digit=int(digit)
                        if i%digit!=0:
                            break
                    if str(digit)==str(i)[len(str(i))-1] and i%digit==0:
                        arr.append(i)
        return arr

#!https://leetcode.com/problems/valid-palindrome-ii/   
class Solution(object):
    def validPalindrome(self, s):
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.validPalindromeUtil(s, i + 1, j) or self.validPalindromeUtil(s, i, j - 1)
        return True
    
    def validPalindromeUtil(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True

#!https://leetcode.com/problems/height-checker/
class Solution(object):
    def heightChecker(self, heights):
        expected=sorted(heights)
        count=0
        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                count+=1
        return count 

#!https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
class Solution(object):
    def countNegatives(self, grid):
        count=0
        for i in grid:
            for j in i:
                if j<0:
                    count+=1
        return count

#!https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/   
class Solution(object):
    def maximumCount(self, nums):
        n,p=0,0
        for i in nums:
            if i<0:
                n+=1
            elif i>0:
                p+=1
        return max(n,p)
#?------------------