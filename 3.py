
#!https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
class Solution(object):
    def subtractProductAndSum(self, n):
        products = 1
        for i in str(n):
            products *= int(i)
        total = 0
        for i in str(n):
            total += int(i)
        return (products - total)

#!https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/


class Solution(object):
    def getDecimalValue(self, head):
        arr = []

        def helper(node):
            if not node:
                return
            arr.append(node.val)
            if node.next:
                helper(node.next)
        helper(head)
        total = ""
        for i in arr:
            total += str(i)
        return int(total, 2)

#!https://leetcode.com/problems/sum-multiples/


class Solution(object):
    def sumOfMultiples(self, n):
        total = 0
        for i in range(1, n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total += i
        return total

#!https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/


class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        sentence = sentence.split(" ")
        index = -1
        for i in sentence:
            if searchWord in i:
                if i.index(searchWord) == 0:
                    index = sentence.index(i)
                    break
        if index == -1:
            return -1
        return index+1

#!https://leetcode.com/problems/maximum-69-number/


class Solution(object):
    def maximum69Number(self, num):
        x = 0
        arr = list(str(num))
        for i in range(len(arr)):
            if arr[i] == "6":
                arr[i] = "9"
                break
        return int("".join(arr))

#!https://leetcode.com/problems/find-the-pivot-integer/


class Solution(object):
    def pivotInteger(self, n):
        if n == 1:
            return 1

        def check(num1, num2):
            x1, x2 = 0, 0
            for i in range(num1+1):
                x1 += i
            for i in range(num1, num2+1):
                x2 += i
            if x1 == x2:
                return True
            return False

        for i in range(n):
            if check(i, n):
                return i
        return -1

#!https://leetcode.com/problems/find-lucky-integer-in-an-array/


class Solution(object):
    def findLucky(self, arr):
        listo = collections.Counter(arr).keys()
        listo = sorted(listo)
        listo = listo[::-1]
        for i in listo:
            if arr.count(i) == i:
                return i
        return -1

#!https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/


class Solution(object):
    def getNoZeroIntegers(self, n):
        if n == 2:
            return [1, 1]
        else:
            for i in range(n):
                if "0" not in str(i) and "0" not in str(n-i):
                    return [i, n-i]


#!https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
class Solution(object):
    def numberOfSteps(self, num):
        count = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            count += 1
        return count

#!https://leetcode.com/problems/count-operations-to-obtain-zero/


class Solution(object):
    def countOperations(self, num1, num2):
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 == num2:
                return count+1
            elif max(num1, num2) == num2:
                num2 = num2-num1
            elif max(num1, num2) == num1:
                num1 = num1-num2
            count += 1
        return 0

#!https://leetcode.com/problems/reformat-date/


class Solution(object):
    def reformatDate(self, date):
        arr = date.split(" ")
        dayy = arr[0]
        dp = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
              "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        day = dayy[:len(dayy)-2]
        month = dp[arr[1]]
        year = arr[2]
        dp1 = {"1": "01", "2": "02", "3": "03", "4": "04",
               "5": "05", "6": "06", "7": "07", "8": "08", "9": "09"}
        if day == "1" or day == "2" or day == "3" or day == "4" or day == "5" or day == "6" or day == "7" or day == "8" or day == "9":
            day = dp1[day]
        string = year
        string += "-"
        string += month
        string += "-"
        string += day
        return (string)

#!https://leetcode.com/problems/distance-between-bus-stops/


class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        if start > destination:
            start, destination = destination, start
        way1 = sum(distance[start:destination])
        if start == 0:
            way2 = sum(distance[destination:])
        else:
            way2 = sum(distance[:start])+sum(distance[destination:])
        return min(way1, way2)

#!https://leetcode.com/problems/unique-morse-code-words/
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        alphabet = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--",
                    "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
        arr = []
        for word in words:
            string = ""
            for i in word:
                string += alphabet[i]
            arr.append(string)
        arr1 = []
        for i in arr:
            if i not in arr1:
                arr1.append(i)
        return len(arr1)

#!https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
class Solution(object):
    def sumRootToLeaf(self, root):
        arr=[]
        def helper(node,string):
            if not node.left and not node.right:
                string+=str(node.val)
                arr.append(string)
                return
            string+=str(node.val)
            if node.left:
                helper(node.left,string)
            if node.right:
                helper(node.right,string)
        helper(root,"")
        return sum([int(i,2) for i in arr])
    
#!https://leetcode.com/problems/occurrences-after-bigram/
class Solution(object):
    def findOcurrences(self, text, first, second):
        arr = text.split(" ")
        res = []
        for i in range(len(arr)-2):
            if arr[i]==first and arr[i+1]==second:
                res.append(arr[i+2])
        return res


#!https://leetcode.com/problems/combinations/
class Solution(object):
    def combine(self, n, k):
        array = [i for i in range(1,n+1)]
        return combinations(array,k)
        
#!https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
class Solution(object):
    def sortByBits(self, arr):
        arr = sorted(arr)
        res = []
        for i in arr:
            res.append([i,bin(i)[2:].count('1')])
        res = sorted(res, key=lambda x: x[1])
        outp = []
        for i in res:
            outp.append(i[0])
        return outp

#!https://leetcode.com/problems/sort-array-by-increasing-frequency
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)[::-1]
        return (sorted(nums, key=lambda x: nums.count(x)))
    
#!https://leetcode.com/problems/largest-substring-between-two-equal-characters/
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        flag=False
        arr=[]
        dp=collections.Counter(s)
        for i in dp.keys():
            if dp[i]>=2:
                arr.append(i)
        res=[]
        for i in arr:
            res.append(s.rindex(i)-s.index(i)-1)

        if len(res)>0:
            return max(res)
        return -1

#!https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/  
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1=""
        for i in word1:
            s1+=i
        s2=""
        for i in word2:
            s2+=i
        return s1==s2
    
#!https://leetcode.com/problems/count-the-number-of-consistent-strings/
def compare(list1,list2):
        for j in list1:
            if j not in list2:
                return False
        return True 
        count=0
        allowed_list = sorted(list(allowed))
        for i in words:
            list_i = sorted(list(i))
            arr=[]
            for i in list_i:
                if i not in arr:
                    arr.append(i)
            if compare(arr,allowed_list):
                count+=1
        return count

#!https://leetcode.com/problems/defuse-the-bomb/
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        temp = [i for i in code]
        if k==0:
            return [0]*len(code)
        if k>0:
            for i in range(len(code)):
                total=0
                for j in range(1,k+1):
                    total+=temp[(i+j)%len(code)]
                code[i]=total
        else:
            for i in range(len(code)):
                total=0
                for j in range(1,abs(k)+1):
                    total+=temp[(i-j)%len(code)]
                code[i]=total
        return code
    
#!https://leetcode.com/problems/truncate-sentence/
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = s.split(" ")
        return " ".join(arr[:k])

#!https://leetcode.com/problems/find-center-of-star-graph/
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0]==edges[1][0] or edges[0][0]==edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]

#!https://leetcode.com/problems/destination-city/ 
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        arr=[]
        for i in paths:
            for j in i:
                arr.append(j)
        ones=[]
        for i in arr:
            if arr.count(i)==1:
                ones.append(i)
        for i in ones:
            for j in paths:
                if j[1]==i:
                    return i
                
#!https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        arr=[]
        for i in range(len(nums)):
            if nums[i]==1:
                arr.append(i)
        
        for i in range(len(arr)-1):
            if arr[i]+k>=arr[i+1]:
                return False
        return True
    
#!https://leetcode.com/problems/search-a-2d-matrix/
class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in matrix:
            for j in i:
                if target==j:
                    return True
        return False
    
#!https://leetcode.com/problems/richest-customer-wealth/
class Solution(object):
    def maximumWealth(self, accounts):
        for i in range(len(accounts)):
            accounts[i]=sum(accounts[i])
        return max(accounts)

#!https://leetcode.com/problems/goal-parser-interpretation/ 
class Solution(object):
    def interpret(self, command):
        command = command.replace("()","o")
        command = command.replace("(al)","al")
        return (command)

#!https://leetcode.com/problems/create-target-array-in-the-given-order/  
class Solution(object):
    def createTargetArray(self, nums, index):
        target=[]
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return target

#!https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/  
class Solution(object):
    def maxDepth(self, s):
        stack=[]
        x=0
        for i in s:
            if i=="(":
                stack.append(i)
            elif i==")":
                stack.pop()
            if len(stack)>x:
                x = len(stack)    
        return x

#!https://leetcode.com/problems/count-of-matches-in-tournament/  
class Solution(object):
    def numberOfMatches(self, n):
        if n==1:
            return 0
        elif n==2:
            return 1
        elif n==4:
            return 3
        elif n==8:
            return 7
        elif n==16:
            return 15
        elif n==32:
            return 31
        elif n==64:
            return 63
        elif n==128:
            return 127
        teams = n
        match = 0
        while teams>0:
            if teams==1:
                return int(match + teams)
            if teams % 2 == 1:
                match += math.floor(teams / 2)
                teams = math.ceil(teams / 2)
            else:
                match += teams / 2
                teams = teams / 2
        return match
            

#!https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
class Solution(object):
    def divideString(self, s, k, fill):
        arr = []
        for i in range(0,len(s),k):
            if len(s[i:i+k])==k:
                arr.append(s[i:i+k])
            else:
                string = s[i:i+k]+fill*(k - len(s[i:i+k]))
                arr.append(string)
        return arr
            
#!https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
class Solution(object):
    def maxProduct(self, nums):
        maxi=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]-1)*(nums[j]-1)>maxi:
                    maxi=(nums[i]-1)*(nums[j]-1)
        return maxi

#!https://leetcode.com/problems/running-sum-of-1d-array/
class Solution(object):
    def runningSum(self, nums):
        res=[]
        for i in range(len(nums)):
            res.append(sum(nums[:i+1]))
        return res
    
#!https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/
class Solution(object):
    def maximumTime(self, time):
        arr=[]
        for i in range(len(time)):
            arr.append(time[i])
        if arr[0]=="?" and arr[1]=="?":
            arr[0]="2"
            arr[1]="3"
        for i in range(len(arr)):
            if arr[i]=="?":
                if i==0:
                    if arr[1]<"4":
                        arr[i]="2"
                    else:
                        arr[i]="1"
                if i==1:
                    if arr[0]=="0" or arr[0]=="1":
                        arr[i]="9"
                    else:
                        arr[i]="3"
                if i==3:
                    arr[i]="5"
                if i==4:
                    arr[i]="9"
        return "".join(arr)
    
#!https://leetcode.com/problems/find-the-highest-altitude/
class Solution(object):
    def largestAltitude(self, gain):
        arr=[]
        for i in range(len(gain)):
            arr.append(sum(gain[:i+1]))
        print(arr)
        if max(arr)<0:
            return 0
        return max(arr)
    
#!https://leetcode.com/problems/decode-xored-array/
class Solution(object):
    def decode(self, encoded, first):
        arr=[first]
        for i in range(len(encoded)):
            arr.append(arr[-1] ^ encoded[i]) 
        return (arr)
    
#!https://leetcode.com/problems/maximum-units-on-a-truck/
class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key = lambda x: x[1],reverse=True)
        total=0
        res=0
        for i in range(len(boxTypes)):
            if total==truckSize:
                break 
            elif (truckSize - total) > boxTypes[i][0]:
                total+=boxTypes[i][0]
                res+=boxTypes[i][0]*boxTypes[i][1]
            else:
                res += (truckSize - total) * boxTypes[i][1]
                total += truckSize - total
        return res

#!https://leetcode.com/problems/count-items-matching-a-rule/
class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        count = 0
        if ruleKey=="type":
            for i in items:
                if i[0]==ruleValue:
                    count+=1
        elif ruleKey=="color":
            for i in items:
                if i[1]==ruleValue:
                    count+=1
        elif ruleKey=="name":
            for i in items:
                if i[2]==ruleValue:
                    count+=1
        return count
    
#!https://leetcode.com/problems/second-largest-digit-in-a-string/
class Solution(object):
    def secondHighest(self, s):
        arr=["1","2","3","4","5","6","7","8","9","0"]
        res=[]
        for i in s:
            if i in arr and int(i) not in res:
                res.append(int(i))
        res.sort()
        if len(res)<=1:
            return -1
        return res[-2]

#!https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/  
class Solution(object):
    def removeDigit(self, number, digit):
        arr=[]
        for i in range(len(number)):
            if number[i]==digit:
                arr.append(int(number[:i]+number[i+1:]))
        return str(max(arr))