
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
        
    
#?------------------