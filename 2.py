
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
        
        
        
            
        
    
#?------------------