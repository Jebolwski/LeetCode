
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