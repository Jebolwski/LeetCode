import collections

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
        arr = []

        def helper(node, string):
            if not node.left and not node.right:
                string += str(node.val)
                arr.append(string)
                return
            string += str(node.val)
            if node.left:
                helper(node.left, string)
            if node.right:
                helper(node.right, string)
        helper(root, "")
        return sum([int(i, 2) for i in arr])

#!https://leetcode.com/problems/occurrences-after-bigram/


class Solution(object):
    def findOcurrences(self, text, first, second):
        arr = text.split(" ")
        res = []
        for i in range(len(arr)-2):
            if arr[i] == first and arr[i+1] == second:
                res.append(arr[i+2])
        return res


#!https://leetcode.com/problems/combinations/
class Solution(object):
    def combine(self, n, k):
        array = [i for i in range(1, n+1)]
        return combinations(array, k)

#!https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/


class Solution(object):
    def sortByBits(self, arr):
        arr = sorted(arr)
        res = []
        for i in arr:
            res.append([i, bin(i)[2:].count('1')])
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
        flag = False
        arr = []
        dp = collections.Counter(s)
        for i in dp.keys():
            if dp[i] >= 2:
                arr.append(i)
        res = []
        for i in arr:
            res.append(s.rindex(i)-s.index(i)-1)

        if len(res) > 0:
            return max(res)
        return -1

#!https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ""
        for i in word1:
            s1 += i
        s2 = ""
        for i in word2:
            s2 += i
        return s1 == s2

#!https://leetcode.com/problems/count-the-number-of-consistent-strings/


def compare(list1, list2):
    for j in list1:
        if j not in list2:
            return False
    return True
    count = 0
    allowed_list = sorted(list(allowed))
    for i in words:
        list_i = sorted(list(i))
        arr = []
        for i in list_i:
            if i not in arr:
                arr.append(i)
        if compare(arr, allowed_list):
            count += 1
    return count

#!https://leetcode.com/problems/defuse-the-bomb/


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        temp = [i for i in code]
        if k == 0:
            return [0]*len(code)
        if k > 0:
            for i in range(len(code)):
                total = 0
                for j in range(1, k+1):
                    total += temp[(i+j) % len(code)]
                code[i] = total
        else:
            for i in range(len(code)):
                total = 0
                for j in range(1, abs(k)+1):
                    total += temp[(i-j) % len(code)]
                code[i] = total
        return code

#!https://leetcode.com/problems/truncate-sentence/


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = s.split(" ")
        return " ".join(arr[:k])

#!https://leetcode.com/problems/find-center-of-star-graph/


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]

#!https://leetcode.com/problems/destination-city/


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        arr = []
        for i in paths:
            for j in i:
                arr.append(j)
        ones = []
        for i in arr:
            if arr.count(i) == 1:
                ones.append(i)
        for i in ones:
            for j in paths:
                if j[1] == i:
                    return i

#!https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        arr = []
        for i in range(len(nums)):
            if nums[i] == 1:
                arr.append(i)

        for i in range(len(arr)-1):
            if arr[i]+k >= arr[i+1]:
                return False
        return True

#!https://leetcode.com/problems/search-a-2d-matrix/


class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in matrix:
            for j in i:
                if target == j:
                    return True
        return False

#!https://leetcode.com/problems/richest-customer-wealth/


class Solution(object):
    def maximumWealth(self, accounts):
        for i in range(len(accounts)):
            accounts[i] = sum(accounts[i])
        return max(accounts)

#!https://leetcode.com/problems/goal-parser-interpretation/


class Solution(object):
    def interpret(self, command):
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")
        return (command)

#!https://leetcode.com/problems/create-target-array-in-the-given-order/


class Solution(object):
    def createTargetArray(self, nums, index):
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target

#!https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/


class Solution(object):
    def maxDepth(self, s):
        stack = []
        x = 0
        for i in s:
            if i == "(":
                stack.append(i)
            elif i == ")":
                stack.pop()
            if len(stack) > x:
                x = len(stack)
        return x

#!https://leetcode.com/problems/count-of-matches-in-tournament/


class Solution(object):
    def numberOfMatches(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        elif n == 4:
            return 3
        elif n == 8:
            return 7
        elif n == 16:
            return 15
        elif n == 32:
            return 31
        elif n == 64:
            return 63
        elif n == 128:
            return 127
        teams = n
        match = 0
        while teams > 0:
            if teams == 1:
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
        for i in range(0, len(s), k):
            if len(s[i:i+k]) == k:
                arr.append(s[i:i+k])
            else:
                string = s[i:i+k]+fill*(k - len(s[i:i+k]))
                arr.append(string)
        return arr

#!https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/


class Solution(object):
    def maxProduct(self, nums):
        maxi = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i]-1)*(nums[j]-1) > maxi:
                    maxi = (nums[i]-1)*(nums[j]-1)
        return maxi

#!https://leetcode.com/problems/running-sum-of-1d-array/


class Solution(object):
    def runningSum(self, nums):
        res = []
        for i in range(len(nums)):
            res.append(sum(nums[:i+1]))
        return res

#!https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/


class Solution(object):
    def maximumTime(self, time):
        arr = []
        for i in range(len(time)):
            arr.append(time[i])
        if arr[0] == "?" and arr[1] == "?":
            arr[0] = "2"
            arr[1] = "3"
        for i in range(len(arr)):
            if arr[i] == "?":
                if i == 0:
                    if arr[1] < "4":
                        arr[i] = "2"
                    else:
                        arr[i] = "1"
                if i == 1:
                    if arr[0] == "0" or arr[0] == "1":
                        arr[i] = "9"
                    else:
                        arr[i] = "3"
                if i == 3:
                    arr[i] = "5"
                if i == 4:
                    arr[i] = "9"
        return "".join(arr)

#!https://leetcode.com/problems/find-the-highest-altitude/


class Solution(object):
    def largestAltitude(self, gain):
        arr = []
        for i in range(len(gain)):
            arr.append(sum(gain[:i+1]))
        print(arr)
        if max(arr) < 0:
            return 0
        return max(arr)

#!https://leetcode.com/problems/decode-xored-array/


class Solution(object):
    def decode(self, encoded, first):
        arr = [first]
        for i in range(len(encoded)):
            arr.append(arr[-1] ^ encoded[i])
        return (arr)

#!https://leetcode.com/problems/maximum-units-on-a-truck/


class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total = 0
        res = 0
        for i in range(len(boxTypes)):
            if total == truckSize:
                break
            elif (truckSize - total) > boxTypes[i][0]:
                total += boxTypes[i][0]
                res += boxTypes[i][0]*boxTypes[i][1]
            else:
                res += (truckSize - total) * boxTypes[i][1]
                total += truckSize - total
        return res

#!https://leetcode.com/problems/count-items-matching-a-rule/


class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        count = 0
        if ruleKey == "type":
            for i in items:
                if i[0] == ruleValue:
                    count += 1
        elif ruleKey == "color":
            for i in items:
                if i[1] == ruleValue:
                    count += 1
        elif ruleKey == "name":
            for i in items:
                if i[2] == ruleValue:
                    count += 1
        return count

#!https://leetcode.com/problems/second-largest-digit-in-a-string/


class Solution(object):
    def secondHighest(self, s):
        arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        res = []
        for i in s:
            if i in arr and int(i) not in res:
                res.append(int(i))
        res.sort()
        if len(res) <= 1:
            return -1
        return res[-2]

#!https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/


class Solution(object):
    def removeDigit(self, number, digit):
        arr = []
        for i in range(len(number)):
            if number[i] == digit:
                arr.append(int(number[:i]+number[i+1:]))
        return str(max(arr))

#!https://leetcode.com/problems/sorting-the-sentence/


class Solution(object):
    def sortSentence(self, s):
        words = s.split(" ")
        arr = [0]*len(words)
        for i in words:
            arr[int(i[-1])-1] = i[:len(i)-1]
        return " ".join(arr)

#!https://leetcode.com/problems/minimum-distance-to-the-target-element/


class Solution(object):
    def getMinDistance(self, nums, target, start):
        mini = 99999999
        for i in range(len(nums)):
            if nums[i] == target and abs(i-start) < mini:
                mini = abs(i-start)
        return mini

#!https://leetcode.com/problems/shuffle-string/


class Solution(object):
    def restoreString(self, s, indices):
        arr = [0]*len(s)
        for i in range(len(indices)):
            arr[indices[i]] = s[i]
        return "".join(arr)

#!https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/


class Solution(object):
    def averageValue(self, nums):
        count = 0
        total = 0
        for i in nums:
            if i % 3 == 0 and i % 2 == 0:
                total += i
                count += 1
        if count == 0:
            return 0
        return total / count

#!https://leetcode.com/problems/binary-prefix-divisible-by-5/


class Solution(object):
    def prefixesDivBy5(self, nums):
        arr = []
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        for i in range(len(nums)):
            arr.append(int("".join(nums[:i+1]), 2) % 5 == 0)
        return arr

#!https://leetcode.com/problems/determine-if-string-halves-are-alike/


class Solution(object):
    def halvesAreAlike(self, s):
        s = lower(s)
        first = s[:len(s)/2]
        second = s[len(s)/2:]
        vowels = ['a', 'e', 'i', 'o', 'u']
        first_1 = 0
        second_1 = 0
        for i in first:
            if i in vowels:
                first_1 += 1
        for i in second:
            if i in vowels:
                second_1 += 1
        return second_1 == first_1

#!https://leetcode.com/problems/check-if-the-sentence-is-pangram/


class Solution(object):
    def checkIfPangram(self, sentence):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in sentence:
            if i in alphabet:
                alphabet.remove(i)
        return len(alphabet) == 0

#!https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/


class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr = sorted(arr)
        k = abs(arr[0]-arr[1])
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1]) != k:
                return False
        return True

#!https://leetcode.com/problems/sum-of-all-odd-length-subarrays/


class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        total = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)+1):
                if len(arr[i:j]) % 2 == 1:
                    total += sum(arr[i:j])
        return total

#!https://leetcode.com/problems/maximum-number-of-balls-in-a-box/


class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        arr = [0]*50
        for i in range(lowLimit, highLimit+1):
            arr[sum([int(i) for i in list(str(i))])] += 1
        return max(arr)

#!https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/


class Solution(object):
    def minOperations(self, nums):
        total = 0
        for i in range(len(nums)-1):
            if nums[i+1] <= nums[i]:
                total += (nums[i]+1)-(nums[i+1])
                nums[i+1] = nums[i]+1
        return total

#!https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/


class Solution(object):
    def countGoodSubstrings(self, s):
        arr = []
        counter = 0
        for i in range(len(s)-2):
            if len(list(s[i:i+3])) == len(collections.Counter(s[i:i+3]).keys()):
                counter += 1
        return counter

#!https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/


class Solution(object):
    def countPairs(self, nums, k):
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i*j) % k == 0:
                    count += 1
        return count

#!https://leetcode.com/problems/count-prefixes-of-a-given-string/


class Solution(object):
    def countPrefixes(self, words, s):
        count = 0
        for i in words:
            if i in s and s.index(i) == 0:
                count += 1
        return count

#!https://leetcode.com/problems/counting-words-with-a-given-prefix/


class Solution(object):
    def prefixCount(self, words, pref):
        count = 0
        for i in words:
            if pref in i and i.index(pref) == 0:
                count += 1
        return count

#!https://leetcode.com/problems/count-integers-with-even-digit-sum/


class Solution(object):
    def countEven(self, num):
        def sumOfDigits(num):
            dizi = [int(i) for i in str(num)]
            return sum(dizi) % 2 == 0
        count = 0
        for i in range(1, num+1):
            if sumOfDigits(i):
                count += 1
        return count

#!https://leetcode.com/problems/separate-the-digits-in-an-array/


class Solution(object):
    def separateDigits(self, nums):
        arr = []
        for i in nums:
            dizi = [int(i) for i in str(i)]
            arr += dizi
        return arr

#!https://leetcode.com/problems/alternating-digit-sum/


class Solution(object):
    def alternateDigitSum(self, n):
        dizi = [int(i) for i in str(n)]
        flag = False
        total = 0
        for i in dizi:
            if flag:
                total += -1*i
                flag = False
            else:
                total += i
                flag = True
        return total

#!https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/


class Solution(object):
    def finalPrices(self, prices):
        def findJ(i):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    return j
            return -1
        arr = []
        for i in range(len(prices)):
            j = findJ(i)
            if j == -1:
                arr.append(prices[i])
            else:
                arr.append(prices[i]-prices[j])
        return arr

#!https://leetcode.com/problems/calculate-money-in-leetcode-bank/


class Solution(object):
    def totalMoney(self, n):
        x = 1
        week = 1
        arr = []
        for i in range(n):
            if i % 7 == 0:
                x = week
                week += 1
            arr.append(x)
            x += 1
            print(week, x)
        return sum(arr)

#!https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/


class Solution(object):
    def makeEqual(self, words):
        total = ""
        for i in words:
            total += i
        counter = collections.Counter(total)
        for i in counter:
            if counter[i] % len(words) != 0:
                return False
        return True

#!https://leetcode.com/problems/count-square-sum-triples/


class Solution(object):
    def countTriples(self, n):
        count = 0
        for i in range(n+1):
            for j in range(i+1, n+1):
                for k in range(j+1, n+1):
                    if (j**2)+(i**2) == k**2:
                        count += 1
        return count*2

#!https://leetcode.com/problems/reverse-prefix-of-word/


class Solution(object):
    def reversePrefix(self, word, ch):
        for i in range(len(word)):
            if word[i] == ch:
                return word[:i+1][::-1]+word[i+1:]
        return word

#!https://leetcode.com/problems/convert-1d-array-into-2d-array/


class Solution(object):
    def construct2DArray(self, original, m, n):
        if (m*n) != len(original):
            return []
        if m == 1:
            return [original]
        arr = []
        for i in range(0, len(original), n):
            arr.append(original[i:i+n])
        return arr

#!https://leetcode.com/problems/final-value-of-variable-after-performing-operations/


class Solution(object):
    def finalValueAfterOperations(self, operations):
        count = 0
        for i in operations:
            if "+" in i:
                count += 1
            else:
                count -= 1
        return count


#!https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
class Solution(object):
    def numOfStrings(self, patterns, word):
        count = 0
        for i in patterns:
            if i in word:
                count += 1
        return count

#!https://leetcode.com/problems/find-the-middle-index-in-array/


class Solution(object):
    def findMiddleIndex(self, nums):
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1

#!https://leetcode.com/problems/find-greatest-common-divisor-of-array/


class Solution(object):
    def findGCD(self, nums):
        from fractions import gcd
        nums = sorted(nums)
        if nums[len(nums)-1] == nums[0]:
            return nums[0]
        if nums[len(nums)-1] % nums[0] == 0:
            return nums[0]
        else:
            return gcd(nums[0], nums[len(nums)-1])

#!https://leetcode.com/problems/calculate-amount-paid-in-taxes/


class Solution(object):
    def calculateTax(self, brackets, income):
        if income == 0:
            return 0.00
        total = 0
        if len(brackets) == 1:
            return brackets[0][1]*income*0.01
        for i in range(len(brackets)):
            if income == 0:
                return total
            if i == 0:
                if brackets[i][0] > income:
                    return income*brackets[i][1]*0.01
                total += brackets[i][0]*brackets[i][1]*0.01
                income -= brackets[i][0]
            else:
                if (brackets[i][0]-brackets[i-1][0]) <= income:
                    total += (brackets[i][0]-brackets[i-1]
                              [0])*brackets[i][1]*0.01
                    income -= brackets[i][0]-brackets[i-1][0]
                elif (brackets[i][0]-brackets[i-1][0]) > income:
                    total += income*brackets[i][1]*0.01
                    income = 0
        return total

#!https://leetcode.com/problems/maximum-ascending-subarray-sum/


class Solution(object):
    def maxAscendingSum(self, nums):
        def ifAscending(arr):
            for i in range(len(arr)-1):
                if arr[i+1] <= arr[i]:
                    return False
            return True
        maxi = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if ifAscending(nums[i:j]) and sum(nums[i:j]) > maxi:
                    maxi = sum(nums[i:j])
        return maxi

#!https://leetcode.com/problems/build-array-from-permutation/


class Solution(object):
    def buildArray(self, nums):
        arr = []
        for i in range(len(nums)):
            arr.append(nums[nums[i]])
        return arr

#!https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/


class Solution(object):
    def minSubsequence(self, nums):
        if len(nums) == 1:
            return nums
        if len(nums) == 2 and nums[0] == nums[1]:
            return nums
        nums = sorted(nums)[::-1]
        for i in range(len(nums)):
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]


#!https://leetcode.com/problems/lucky-numbers-in-a-matrix/
class Solution(object):
    def luckyNumbers(self, matrix):
        col = []
        for i in range(len(matrix[0])):
            inner = []
            for j in range(len(matrix)):
                inner.append(matrix[j][i])
            col.append(inner)
        arr1 = []
        arr2 = []
        for i in col:
            arr1.append(max(i))
        for i in matrix:
            arr2.append(min(i))
        res = []
        for i in arr1:
            for j in arr2:
                if i == j:
                    res.append(i)
        return res

#!https://leetcode.com/problems/string-matching-in-an-array/


class Solution(object):
    def stringMatching(self, words):
        arr = []
        for i in range(len(words)):
            for j in words[:i]+words[i+1:]:
                if words[i] in j and words[i] not in arr:
                    arr.append(words[i])
        return arr

#!https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/


class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and queryTime <= endTime[i]:
                count += 1
        return count

#!https://leetcode.com/problems/xor-operation-in-an-array/


class Solution(object):
    def xorOperation(self, n, start):
        arr = []
        for i in range(n):
            arr.append(start+i*2)
        print(arr)
        total = 0
        for i in arr:
            total ^= i
        return total

#!https://leetcode.com/problems/combination-sum-iv/


class Solution(object):
    def combinationSum4(self, nums, target):
        dp = {0: 1}
        for i in range(1, target+1):
            dp[i] = 0
            for n in nums:
                dp[i] += dp.get(i-n, 0)
        return dp[target]

#!https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/


class Solution(object):
    def canBeEqual(self, target, arr):
        if sorted(target) == sorted(arr):
            return True
        return False

#!https://leetcode.com/problems/number-of-good-pairs/


class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count

#!https://leetcode.com/problems/path-crossing/


class Solution(object):
    def isPathCrossing(self, path):
        arr = [[0, 0]]
        res = []
        x = 0
        y = 0
        for i in path:
            if i == "N":
                y += 1
                arr.append([x, y])
            elif i == "E":
                x += 1
                arr.append([x, y])
            elif i == "W":
                x -= 1
                arr.append([x, y])
            else:
                y -= 1
                arr.append([x, y])
        for i in arr:
            if i not in res:
                res.append(i)
        if len(res) != len(arr):
            return True
        return False


#!https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
class Solution(object):
    def nearestValidPoint(self, x, y, points):
        arr = []
        distances = []
        for i in points:
            if i[0] == x or i[1] == y:
                arr.append([i, points.index(i)])
        if len(arr) == 0:
            return -1
        for i in arr:
            distances.append([abs(x-i[0][0])+abs(y-i[0][1]), i[1]])
        distances = sorted(distances, key=lambda x: x[0])
        if len(distances) == 1:
            return distances[0][1]
        return distances[0][1]

#!https://leetcode.com/problems/maximum-product-difference-between-two-pairs/


class Solution(object):
    def maxProductDifference(self, nums):
        top = max(nums)
        nums.remove(max(nums))
        top *= max(nums)
        bot = min(nums)
        nums.remove(min(nums))
        bot *= min(nums)
        return top-bot

#!https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/


class Solution(object):
    def checkZeroOnes(self, s):
        i = 0
        arr = []
        while i < len(s)-1:
            if i < len(s)-1 and s[i] == '0':
                j = i
                while j < len(s) and s[j] == '0':
                    j += 1
                arr.append(s[i:j])
                i = j
            if i < len(s)-1 and s[i] == '1':
                j = i
                while j < len(s) and s[j] == '1':
                    j += 1
                arr.append(s[i:j])
                i = j
        arr0 = []
        arr1 = []
        for x in arr:
            if '1' in x:
                arr1.append(x)
            if '0' in x:
                arr0.append(x)
        total = ""
        for i in arr:
            total += i
        if len(total)-len(s) == -1:
            if s[-1] == '1':
                arr1.append('1')
            if s[-1] == '0':
                arr0.append('0')
        if '0' not in s and len(s) > 1:
            return True
        if '1' not in s and len(s) > 1:
            return False
        if s == "0":
            return False
        if s == "1":
            return True
        return len(max(arr1))-len(max(arr0)) > 0

#!https://leetcode.com/problems/replace-all-digits-with-characters/


class Solution(object):
    def replaceDigits(self, s):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        string = ""
        for i in range(len(s)):
            if s[i] not in alphabet:
                string += alphabet[alphabet.index(s[i-1])+int(s[i])]
            else:
                string += s[i]
        return (string)

#!https://leetcode.com/problems/design-an-ordered-stream/


class OrderedStream(object):

    def __init__(self, n):
        self.arr = [[]]*n
        self.index = 0

    def insert(self, idKey, value):
        self.arr[idKey-1] = value
        liste = []
        while self.index < len(self.arr) and self.arr[self.index] != []:
            liste.append(self.arr[self.index])
            self.index += 1
        return liste

#!https://leetcode.com/problems/count-good-triplets/


class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        count += 1
        return count

#!https://leetcode.com/problems/find-the-duplicate-number/


class Solution(object):
    def findDuplicate(self, nums):
        collection = collections.Counter(nums)
        for i in collection:
            if collection[i] > 1:
                return i

#!https://leetcode.com/problems/monotonic-array/
class Solution(object):
    def isMonotonic(self, nums):
        flag1=True
        flag2=True
        for i in range(len(nums)-1):
            if not nums[i]<=nums[i+1]:
                flag1=False
        for i in range(len(nums)-1):
            if not nums[i]>=nums[i+1]:
                flag2=False
        return flag1 or flag2

#!https://leetcode.com/problems/count-complete-tree-nodes/
class Solution(object):
    def countNodes(self, root):
        arr=[]
        if root!=None:
            arr.append(-1)

        def helper(node):
            if not node:
                return
            if node.left:
                arr.append(node.left.val)
                helper(node.left)
            if node.right:
                arr.append(node.right.val)
                helper(node.right)
        helper(root)
        return len(arr)   

#!https://leetcode.com/problems/reverse-bits/
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s=bin(n)
        s=s[2:]
        s=s[::-1] + ("0"*(32-len(s)))
        return int(s,2)

#!https://leetcode.com/problems/sort-vowels-in-a-string/ 
class Solution(object):
    def sortVowels(self, s):
        vowels = ['a','e','i','o','u']
        madagasko = []
        vowe = []
        arr = []
        string = ""
        for i in s:
            if lower(i) in vowels:
                vowe.append(i)
                arr.append(0)
            else: 
                madagasko.append(i)
                arr.append(1)
        madagasko = madagasko[::-1]
        vowe = sorted(vowe)
        vowe = vowe[::-1]
        for i in arr:
            if i==1:
                string+=madagasko.pop()
            else:
                string+=vowe.pop()
        return string

#!https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
class Solution(object):
    def countPalindromicSubsequence(self, s):
        arr=[]
        for i in s:
            if i not in arr:
                arr.append(i)
        total=0
        for i in arr:
            lst=s.rindex(i)
            fst=s.index(i)
            tmp=[]
            for i in s[fst+1:lst]:
                if i not in tmp:
                    tmp.append(i)
            total+=len(tmp)
        return (total)

#!https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging
class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr=sorted(arr)
        arr[0]=1
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]>1:
                arr[i+1]=arr[i]+1
        return arr[-1]
            
#!https://leetcode.com/problems/find-unique-binary-string/ 
class Solution(object):
    def findDifferentBinaryString(self, nums):
        arr=[]
        for num in nums:
            res=""
            res1=""
            res2=""
            res3=""
            for i in num:
                if i=='0':
                    res+='1'
                else:
                    res+='0'
            for i in num:
                res1+='1'
            for i in num:
                res2+='0'
            for i in range(len(num)):
                if i%2==0:
                    res3+='0'
                else:
                    res3+='1'
            
            arr+=[res1,res2,res,res3]
        for i in arr:
            if i not in nums:
                return i

        
#!https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/
class Solution(object):
    def garbageCollection(self, garbage, travel):
        n = len(garbage)
        ans = 0

        for i in range(n - 1):
            ans += 3 * travel[i]

        for s in garbage:
            ans += len(s)

        for i in range(n - 1, 0, -1):
            if "G" not in garbage[i]:
                ans -= travel[i - 1]
            else:
                break

        for i in range(n - 1, 0, -1):
            if "P" not in garbage[i]:
                ans -= travel[i - 1]
            else:
                break

        for i in range(n - 1, 0, -1):
            if "M" not in garbage[i]:
                ans -= travel[i - 1]
            else:
                break

        return ans
    
#!https://leetcode.com/problems/minimum-time-visiting-all-points/
class Solution(object):
    def toTime(self, from_point, to_point):
            x_diff = abs(from_point[0] - to_point[0])
            y_diff = abs(from_point[1] - to_point[1])
            return max(x_diff, y_diff)
    def minTimeToVisitAllPoints(self, points):
        time = 0
        for i in range(1, len(points)):
            print(self.toTime(points[i - 1], points[i]))
            time += self.toTime(points[i - 1], points[i])
        return time

#!https://leetcode.com/problems/largest-odd-number-in-string/
class Solution(object):
    def largestOddNumber(self, num):
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2==1:
                return num[:i+1]
        return ""
    

#!https://leetcode.com/problems/valid-anagram/
class Solution(object):
    def isAnagram(self, s, t):
        se=collections.Counter(s)
        te=collections.Counter(t)
        xe=True
        re=True
        for i in se:
            if i not in te or se[i]!=te[i]:
                xe=False
        for i in te:
            if i not in se or se[i]!=te[i]:
                re=False
        return xe and re
    
#!https://leetcode.com/problems/destination-city/
class Solution(object):
    def destCity(self, paths):
        inn=[]
        outt=[]
        for come,out in paths:
            if come not in inn:
                inn.append(come)
            if out not in outt:
                outt.append(out)
        for i in outt:
            if i not in inn:
                return i
            
#!https://leetcode.com/problems/cheapest-flights-within-k-stops/
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices=[float("inf")]*n
        prices[src]=0
        for i in range(k+1):
            tempPrices=[i for i in prices]
            for s, d, price in flights:
                if prices[s]==float("inf"):
                    continue
                elif prices[s]+price<tempPrices[d]:
                    tempPrices[d] = prices[s]+price
            prices=tempPrices
        return -1 if prices[dst]==float("inf") else prices[dst]

#!https://leetcode.com/problems/special-positions-in-a-binary-matrix/
class Solution(object):
    def numSpecial(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        srows = [0] * rows
        scols = [0] * cols 

        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==1:
                    srows[i] += 1
                    scols[j] += 1
        count=0

        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==1 and srows[i]==1 and scols[j]==1:
                    count+=1

        return count

#!https://leetcode.com/problems/buy-two-chocolates/
class Solution(object):
    def buyChoco(self, prices, money):
        ans = float('inf')

        for i in range(len(prices)):
            for j in range(len(prices)):
                if i != j:
                    total = prices[i] + prices[j]
                    ans = min(ans, total)

        fin = money - ans
        if(fin>=0):
            return fin
        else:
            return money

#!https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
class Solution(object):
    def minOperations(self, s):
        print (s[0])
        length = len(s)
        s_1=""
        s_2=""
        m=0
        for i in range(len(s)):
            if m==0:
                s_1+="1"
                m=1
            else:
                s_1+="0"
                m=0
        m=1
        for i in range(len(s)):
            if m==0:
                s_2+="1"
                m=1
            else:
                s_2+="0"
                m=0
        diff_1=0
        diff_2=0
        for i in range(len(s)):
            if s_1[i]!=s[i]:
                diff_1+=1
            if s_2[i]!=s[i]:
                diff_2+=1
        return min(diff_1,diff_2)
                
#!https://leetcode.com/problems/maximum-score-after-splitting-a-string/
class Solution(object):
    def maxScore(self, s):
        arr=[]
        for i in range(1,len(s)):
            arr.append(s[:i].count('0')+s[i:].count('1'))
        return max(arr)

#!https://leetcode.com/problems/largest-substring-between-two-equal-characters/
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        arr=[]
        for i in range(len(s)):
            if s.rindex(s[i])!=i:
                arr.append(s.rindex(s[i])-i-1)
        if len(arr)>0:
            return max(arr)
        return -1
        
#!https://leetcode.com/problems/assign-cookies/
class Solution(object):
    def findContentChildren(self, g, s):
        cookiesNums = len(s)
        if cookiesNums == 0:
            return 0
        g.sort()
        s.sort()

        maxNum = 0
        cookieIndex = cookiesNums - 1
        childIndex = len(g) - 1
        while cookieIndex >= 0 and childIndex >= 0:
            if s[cookieIndex] >= g[childIndex]:
                maxNum += 1
                cookieIndex -= 1
                childIndex -= 1
            else:
                childIndex -= 1
        
#!https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
class Solution(object):
    def minOperations(self, nums):
        dp = collections.Counter(nums)
        print(dp)
        count=0
        total=dp.keys()
        for i in total:
            x=dp[i]
            if x==1:
                return -1
            while x>4:
                x-=3
                count+=1
            if x%3==0:
                count+=x/3
            elif x%2==0:
                count+=x/2
        return count

#!https://leetcode.com/problems/longest-increasing-subsequence/    
class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        arr = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    arr[i] = max(arr[i], arr[j] + 1)
        return max(arr)
    


#!https://leetcode.com/problems/check-if-it-is-a-straight-line/
class Solution(object):
    def checkStraightLine(self, coordinates):
        x0,y0=coordinates[0]
        x1,y1=coordinates[1]
        for x,y in coordinates[2:]:
            if (y1-y0)*(x-x0)!=(y-y0)*(x1-x0):
                return False

        return True    

#!https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp, dp1, dp2 = 0, 0, 0
        for i in range(2, n + 1):
            oneStep = dp1 + cost[i - 1]
            twoStep = dp2 + cost[i - 2]
            dp = min(oneStep, twoStep)
            dp2 = dp1
            dp1 = dp
        return dp1

#!https://leetcode.com/problems/leaf-similar-trees/
class Solution(object):
    def leafSimilar(self, root1, root2):
        arr1=[]
        arr2=[]
        def helper(root,arr):
            if not root:
                return
            if root.left:
                helper(root.left,arr)
            if not root.left and not root.right:
                arr.append(root.val)
            if root.right:
                helper(root.right,arr)
        helper(root2,arr1)
        helper(root1,arr2)
        return arr1==arr2

#!https://leetcode.com/problems/jewels-and-stones/
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        arr_jewels=[]
        for i in jewels:
            if i not in arr_jewels:
                arr_jewels.append(i)
        count=0
        for i in stones:
            if i in arr_jewels:
                count+=1
        return count


#!https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
class Solution(object):
    def maxAncestorDiff(self, root):
        dp={}
        
        def find_node_by_number(num,node,arr):
            if len(arr)>0:
                return
            if not node:
                return
            if node.val==num:
                arr.append(node)
                return
            if node.left:
                find_node_by_number(num,node.left,arr)
            if node.right:
                find_node_by_number(num,node.right,arr)
        
        def helper(node):
            if not node:
                return
            if node.left:
                helper(node.left)
            dp[node.val]=0
            if node.right:
                helper(node.right)
        
        def helper_arr(arr,node):
            if not node:
                return
            if node.left:
                helper_arr(arr,node.left)
            arr.append(node.val)
            if node.right:
                helper_arr(arr,node.right)


        helper(root)
        diff=0
        for i in dp:
            node = []
            find_node_by_number(i,root,node)
            arr=[]
            helper_arr(arr,node[0])
            dp[i]=sorted(arr)
            if abs(i - dp[i][-1])>diff:
                diff=abs(i - dp[i][-1])
            if abs(i - dp[i][0])>diff:
                diff=abs(i - dp[i][0])
        return diff

#!https://leetcode.com/problems/longest-uncommon-subsequence-i/      
class Solution(object):
    def findLUSlength(self, a, b):
        maxi_gomez=-1
        if a==b:
            return -1
        if len(b)>len(a):
            return len(b)
        for i in range(len(b)):
            for j in range(len(a)):
                if b[:i]!=a[:j]:
                    if j-i+1>maxi_gomez:
                        maxi_gomez=j-i+1
        return maxi_gomez
    

#!https://leetcode.com/problems/subtree-of-another-tree/
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """ 
        if root is None and subRoot is None:
            return True
        if subRoot is None:
            return True
        if root is None and subRoot is not None:
            return False
        return self.isSame(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isSame(self,root,subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        return root.val == subRoot.val and self.isSame(root.left,subRoot.left) and self.isSame(root.right,subRoot.right)
    
#!https://leetcode.com/problems/set-mismatch/
class Solution(object):
    def findErrorNums(self, nums):
        dup, missing = -1, -1
        
        for i in range(1, len(nums) + 1):
            count = nums.count(i)
            if count == 2:
                dup = i
            elif count == 0:
                missing = i
        
        return [dup, missing]

#!https://leetcode.com/problems/valid-boomerang/
class Solution(object):
    def isBoomerang(self, x):
        return (x[0][0] - x[1][0]) * (x[0][1] - x[2][1]) != (x[0][0] - x[2][0]) * (x[0][1] - x[1][1])
    
#!https://leetcode.com/problems/intersection-of-two-linked-lists/
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        arrayA=[]
        arrayB=[]
        while headA:
            arrayA.append(headA)
            headA=headA.next
        while headB:
            arrayB.append(headB)
            headB=headB.next
        if arrayA[-1]!=arrayB[-1]:
            return
        elif len(arrayA)==len(arrayB)==1:
            return arrayA[0]
        else:
            B=len(arrayB)-1
            A=len(arrayA)-1
            while True:
                if A==0 and B==0:
                    return arrayA[0]
                elif arrayB[B]!=arrayA[A]:
                    return arrayB[B+1]
                B-=1
                A-=1
        
#!https://leetcode.com/problems/delete-columns-to-make-sorted/
class Solution(object):
    def minDeletionSize(self, strs):
        res=0
        for x in range(len(strs[0])):
            word=""
            for y in range(len(strs)):
                word+=(strs[y][x])
            flag=True
            for i in range(1,len(word)):
                if ord(word[i])<ord(word[i-1]):
                    flag=False
                    break
            if not flag:
                res+=1
        return res
    
#!https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        for i in range(len(tokens)):
            if tokens[i]=="+":
                stack.append(int(stack[-2])+int(stack[-1]))
                stack.pop(len(stack)-3)
                stack.pop(len(stack)-2)
            elif tokens[i]=="*":
                stack.append(int(stack[-2])*int(stack[-1]))
                stack.pop(len(stack)-3)
                stack.pop(len(stack)-2)
            elif tokens[i]=="/":
                if int(stack[-2])/float(stack[-1])<0:
                    x=ceil(int(stack[-2])/float(stack[-1]))
                else:
                    x=floor(int(stack[-2])/float(stack[-1]))
                stack.append(int(x))
                stack.pop(len(stack)-3)
                stack.pop(len(stack)-2)
            elif tokens[i]=="-":
                stack.append(int(stack[-2])-int(stack[-1]))
                stack.pop(len(stack)-3)
                stack.pop(len(stack)-2)
            else:
                stack.append(tokens[i])
        return int(stack[0])

#!https://leetcode.com/problems/average-of-levels-in-binary-tree/
class Solution(object):
    def averageOfLevels(self, root):
        arr=[[]]*2000
        def func(node,level):
            arr[level].append(node.val)
            if node.left:
                func(node.left,level+1)
            if node.right:
                func(node.right,level+1)
        func(root,0)
        res=[]
        for i in range(len(arr)):
            if len(arr[i])>0:
                res.append(sum(arr[i])/float(len(arr[i])))
        return (res)

#!https://leetcode.com/problems/find-smallest-letter-greater-than-target/
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        sorteda = sorted(letters)
        arr = [ord(i) for i in sorted(letters)]
        for i in range(len(arr)):
            if ord(target)<arr[i]:
                return sorteda[i]
        return letters[0]

class Solution(object):
    def licenseKeyFormatting(self, s, k):
        string=""
        for i in s:
            if i!="-":
                string+=upper(i)
        res=""
        x=len(string)%k
        if (len(string)%k!=0):
            res=string[0:x]+"-"
            for i in range(x,len(string),k):
                res+=string[i:i+k]+"-"
        else:
            for i in range(0,len(string),k):
                res+=string[i:i+k]+"-"
        return res[:-1]
        
#!https://leetcode.com/problems/longest-continuous-increasing-subsequence/
class Solution(object):
    def findLengthOfLCIS(self, nums):
        x=0
        arr=[]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                x+=1
            else:
                arr.append(x)
                x=0
            if i==len(nums)-1:
                arr.append(x)
        if len(arr)>0:
            return max(arr)+1
        return 1

#!https://leetcode.com/problems/sort-characters-by-frequency/
class Solution(object):
    def frequencySort(self, s):
        dp=collections.Counter(s)
        arr=[]
        string=""
        for i in dp:
            arr.append([i,dp[i]])
        arr = sorted(arr, key=lambda x: x[1], reverse=True)
        for i in arr:
            string+=i[0]*i[1]
        return (string)
        
#!https://leetcode.com/problems/palindromic-substrings/
class Solution(object):
    def countSubstrings(self, s):
        def isPalindrome(string):
            if string==string[::-1]:
                return True
            return False
        count=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                string = s[i:j]
                if isPalindrome(string):
                    count+=1
        return count


#!https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
class Solution(object):
    def findTarget(self, root, k):
        arr=[]
        def helper(node):
            if not node:
                return
            if node.left:
                helper(node.left)
            arr.append(node.val)
            if node.right:
                helper(node.right)
        helper(root)
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]==k:
                    return True
        return False
    
#!https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
class Solution(object):
    def firstPalindrome(self, words):
        for i in words:
            if i==i[::-1]:
                return i
        return ""

#!https://leetcode.com/problems/rearrange-array-elements-by-sign/
class Solution(object):
    def rearrangeArray(self, nums):
        negative=[]
        positive=[]
        for i in nums:
            if i>0:
                positive.append(i)
            else:
                negative.append(i)
        arr=[]
        negative=negative[::-1]
        positive=positive[::-1]
        for i in range(len(negative)+len(positive)):
            if i%2==1:
                arr.append(negative.pop())
            else:
                arr.append(positive.pop())
        return arr
        
#!https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        dp1 = collections.Counter(arr)
        sorted_dict = sorted(dp1.items(), key=lambda x:x[1],reverse=False)
        res=[]
        for i in sorted_dict:
            i=list(i)
            for j in range(i[1]):
                res.append(i[0])
        res=res[::-1]
        for i in range(k):
            res.pop()
        return len(collections.Counter(res).keys())


#!https://leetcode.com/problems/find-bottom-left-tree-value/
class Solution(object):
    def findBottomLeftValue(self, root):
        arr=[]
        def helper(node,level):
            if not node:
                return
            
            if node.left:
                helper(node.left,level+1)
            if not node.left and not node.right:
                arr.append([node.val,level])
            if node.right:
                helper(node.right,level+1)
        helper(root,0)
        arr=sorted(arr, key=lambda x: x[1], reverse=True)
        if len(arr)>0:
            return arr[0][0]
        if root.right:
            return root.right.val
        return root.val
    
#!https://leetcode.com/problems/maximum-odd-binary-number/
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count=0
        for i in s:
            if i=="1":
                count+=1
        return ("1"*(count-1))+("0"*(int(len(s))-count))+"1"
        
#!https://leetcode.com/problems/divisor-game
class Solution(object):
    def divisorGame(self, n):
        return n%2==0

#!https://leetcode.com/problems/decompress-run-length-encoded-list/ 
class Solution(object):
    def decompressRLElist(self, nums):
        arr=[]
        for i in range(0,len(nums),2):
            for j in range(nums[i]):
                arr.append(nums[i+1])
        return arr        
    
#!https://leetcode.com/problems/count-elements-with-maximum-frequency/
class Solution(object):
    def maxFrequencyElements(self, nums):
        max_count=0
        for i in nums:
            if nums.count(i)>max_count:
                max_count=nums.count(i)
        x=0  
        for i in nums:
            if nums.count(i)==max_count:
                x+=1
        return x       
    
#!https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
class Solution(object):
    def countStudents(self, students, sandwiches):
        x=0
        while x<=len(students) or len(sandwiches)>0:
            if len(sandwiches)==0:
                return 0
            if x>len(sandwiches):
                return len(sandwiches)
            if students[0]==sandwiches[0]:
                students=students[1:]
                sandwiches=sandwiches[1:]
                x=0
            else:
                students=students[1:]+[students[0]]
                x=x+1
        return len(sandwiches)

#!https://leetcode.com/problems/time-needed-to-buy-tickets/
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        a=max(tickets)
        x=0
        for i in range(a):
            arr=[]
            for i in tickets:
                if i>0:
                    arr.append(i-1)
                    if not (len(arr)>k and arr[k]==0):
                        x=x+1
                else:
                    arr.append(i)
            tickets = [i for i in arr]
            print(tickets,x)
            if tickets[k]==0:
                return x+1
        return x+1
        
#!https://leetcode.com/problems/remove-k-digits/
class Solution(object):
    def removeKdigits(self, num, k):
        stk = []
        ans = ""
        for c in num:
            while k > 0 and stk and stk[-1] > c:
                stk.pop()
                k -= 1
            stk.append(c)
        while k > 0:
            stk.pop()
            k -= 1
        for c in stk:
            if not ans and c == '0':
                continue
            ans += c
        return ans if ans else '0'

#!https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution(object):
    def trailingZeroes(self, n):
        x=1
        for i in range(1,n+1):
            x*=i
        res=0
        for i in str(x)[::-1]:
            if i=="0":
                res+=1
            else:
                break
        return res

#!https://leetcode.com/problems/1-bit-and-2-bit-characters/ 
class Solution(object):
    def findSecondMinimumValue(self, root):
        arr=[]
        def helper(node):
            if not node:
                return
            if node.left:
                helper(node.left)
            arr.append(node.val)
            if node.right:
                helper(node.right)
        helper(root)
        if len(collections.Counter(arr).keys())>1:
            return sorted(collections.Counter(arr).keys())[1]
        return -1
    
#!https://leetcode.com/problems/nim-game/solutions/4173613/return-n-4-0-one-line-answer-explanation-o-1/
class Solution(object):
    def canWinNim(self, n):
        return n%4!=0

#!https://leetcode.com/problems/perfect-number/    
class Solution(object):
    def checkPerfectNumber(self, n):
        if n==1:
            return False
        sq=int(sqrt(n))
        s=1
        for i in range(2,sq+1):
            if n%i==0:
                t=n//i
                s+=t+i
        return s==n

#!https://leetcode.com/problems/score-of-a-string/
class Solution(object):
    def scoreOfString(self, s):
        x=0
        for i in range(len(s)-1):
            x+=(abs(ord(s[i])-ord(s[i+1])))
        return x
    
#!https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
class Solution(object):
    def areOccurrencesEqual(self, s):
        return len(collections.Counter(collections.Counter(s).values()).values())==1

#!https://leetcode.com/problems/convert-the-temperature/
class Solution(object):
    def convertTemperature(self, celsius):
        return [celsius+273.15,celsius * 1.80 + 32.00]
        
#!https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
class Solution(object):
    def differenceOfSums(self, n, m):
        num1=0
        for i in range(1,n+1):
            if i%m!=0:
                num1+=i
        num2=0
        for i in range(1,n+1):
            if i%m==0:
                num2+=i
        return num1 - num2

#!https://leetcode.com/problems/count-the-digits-that-divide-a-number/
class Solution(object):
    def countDigits(self, num):
        count=0
        for i in str(num):
            if num%int(i)==0:
                count+=1
        return count
    
#!https://leetcode.com/problems/add-two-integers/
class Solution(object):
    def sum(self, num1, num2):
        return num1+num2
    
#!https://leetcode.com/problems/smallest-even-multiple/
class Solution(object):
    def smallestEvenMultiple(self, n):
        if n%2==0:
            return n
        return n*2
        
#!https://leetcode.com/problems/harshad-number/
class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        c=0
        for i in str(x):
            c+=int(i)
        if x%c==0:
            return c
        return -1
    
#!https://leetcode.com/problems/a-number-after-a-double-reversal/
class Solution(object):
    def isSameAfterReversals(self, num):
        def reverse(num):
            return int(str(num)[::-1])
        return reverse(reverse(num))==num
    
#!https://leetcode.com/problems/find-if-path-exists-in-graph/
class Solution(object):
    def validPath(self, n, edges, source, destination):
        adj_list = collections.defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        print(adj_list)
        seen=set()
        def dfs(node):
            if node==destination:
                return True
            seen.add(node)

            for v in adj_list[node]:
                if v not in seen and dfs(v):
                    return True
            return False
        return dfs(source)
        
#!https://leetcode.com/problems/number-of-common-factors/
class Solution(object):
    def commonFactors(self, a, b):
        x=0
        for i in range(1,min(a,b)+1):
            if a%i==0 and b%i==0:
                x+=1
        return x
    
#!https://leetcode.com/problems/calculate-delayed-arrival-time/
class Solution(object):
    def findDelayedArrivalTime(self, a, b):
        return (a+b)%24

#!https://leetcode.com/problems/count-symmetric-integers/
class Solution(object):
    def countSymmetricIntegers(self, low, high):
        res=0
        for i in range(low,high+1):
            length=len(str(i))
            x=0
            y=0
            if length%2==0:
                for j in str(i)[:length/2]:
                    x+=int(j)
                for j in str(i)[length/2:]:
                    y+=int(j)
                if x==y:
                    res+=1
        return res
    

#!https://leetcode.com/problems/three-divisors/
class Solution(object):
    def isThree(self, n):
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        return count==3
    
#!https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/
class Solution(object):
    def numberOfCuts(self, n):
        if n == 1: 
            return 0
        return n//2 if n%2==0 else n

#!https://leetcode.com/problems/check-if-the-number-is-fascinating/       
class Solution(object):
    def isFascinating(self, n):
        x=str(n)+str(n*2)+str(n*3)
        count=0
        for i in range(1,10):
            if str(i) in x and x.count(str(i))==1:
                count+=1
        return count==9
    
#!https://leetcode.com/problems/sort-the-people/
class Solution(object):
    def sortPeople(self, names, heights):
        arr=[]
        for i in range(len(names)):
            arr.append([names[i],heights[i]])
        arr = sorted(arr, key=lambda x: x[1], reverse=True)
        res=[]
        for i in arr:
            res.append(i[0])
        return res
        
#!https://leetcode.com/problems/find-words-containing-character/
class Solution(object):
    def findWordsContaining(self, words, x):
        arr=[]
        for i in range(len(words)):
            if x in words[i]:
                arr.append(i)
        return arr 
    
#!https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
class Solution(object):
    def minLength(self, s):
        while "AB" in s or "CD" in s:
            s=s.replace("AB","")
            s=s.replace("CD","")
        return len(s)

#!https://leetcode.com/problems/find-missing-and-repeated-values/  
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        x = (pow(len(grid[0]),2))
        arr=[]
        for i in grid:
            for j in i:
                arr.append(j)
        res=[]
        for i in range(1,x+1):
            if arr.count(i)==2:
                res.append(i)
        for i in range(1,x+1):
            if i not in arr:
                res.append(i)
        return (res)

#!https://leetcode.com/problems/number-of-senior-citizens/
class Solution(object):
    def countSeniors(self, details):
        x=0
        for i in details:
            if int(i[11:13])>60:
                x+=1
        return x

#!https://leetcode.com/problems/find-the-sum-of-encrypted-integers/       
class Solution(object):
    def sumOfEncryptedInt(self, nums):
        for i in range(len(nums)):
            nums[i] = int(max(str(nums[i]))*len(str(nums[i])))
        return (sum(nums))
    
#!https://leetcode.com/problems/delete-node-in-a-linked-list/
class Solution(object):
    def deleteNode(self, node):
        temp=node
        arr=[]
        while temp!=None:
            arr.append(temp.val)
            temp=temp.next
        arr=arr[1:]
        i=0
        temp=node
        while temp.next!=None:
            temp.val=arr[i]
            if temp.next.next==None:
                break
            temp=temp.next
            i+=1
        temp.next=None

#!https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
class Solution(object):
    def specialArray(self, nums):
        arr=[]
        for i in range(max(nums)+1):
            count=0
            for j in nums:
                if j>=i:
                    count+=1
            if count==i:
                arr.append(i)
        if len(arr)>0:
            return arr[-1]
        return -1

#!https://leetcode.com/problems/single-number-iii/  
class Solution(object):
    def singleNumber(self, nums):
        x=collections.Counter(nums).keys()
        arr=[]
        for i in x:
            if nums.count(i)==1:   
                arr.append(i)
            if len(arr)==2:
                break
        return arr

#!https://leetcode.com/problems/delete-characters-to-make-fancy-string/
class Solution(object):
    def makeFancyString(self, s):
        r = [s[0]]
        
        last_r_ind = 1
        last_r_value = s[0]
        
        for i in range(1, len(s)):
            if s[i] == last_r_value and last_r_ind < 2:
                r[-1] *= 2
                last_r_ind += 1

            if s[i] != last_r_value:
                r.append(s[i])
                last_r_ind = 1
                last_r_value = s[i]
                
        ans = ''.join(r)
        return ans

#!https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/  
class Solution(object):
    def largeGroupPositions(self, s):
        lst=[]
        c=""
        for i in range(len(s)):
            if c and c[-1]!=s[i]:
                if len(c)>=3:
                    lst.append([i-len(c),i-1])
                c=s[i]
            else:
                c+=s[i]
        if len(c)>=3:
            lst.append([len(s)-len(c),len(s)-1])
        return lst
    
#!https://leetcode.com/problems/find-common-characters/
class Solution(object):
    def commonChars(self, words):
        min_freq = Counter(words[0])
        for word in words:
            min_freq &= Counter(word)
        return list(min_freq.elements())

#!https://leetcode.com/problems/reshape-the-matrix/
class Solution(object):
    def matrixReshape(self, mat, r, c):
        x = len(mat)*len(mat[0])
        arr=[]
        for i in mat:
            for j in i:
                arr.append(j)
        if (r*c)!=x:
            return mat
        res=[]
        arr=arr[::-1]
        for i in range(r):
            temp=[]
            for i in range(c):
                temp.append(arr.pop())
            res.append(temp)
        return res

#!https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
class Solution(object):
    def removeAnagrams(self, words):
        def isAnagram(one,two):
            ones = collections.Counter(one)
            twos = collections.Counter(two)
            arr_one=[]
            arr_two=[]
            for i in ones:
                arr_one.append([i,ones[i]])
            for i in twos:
                arr_two.append([i,twos[i]])
            arr_one=sorted(arr_one) 
            arr_two=sorted(arr_two) 
            if arr_one==arr_two:
                return True
            return False
        indexes=[]
        for i in range(1,len(words)):
            if isAnagram(words[i],words[i-1]):
                indexes.append(i)
        count=0
        for i in indexes:
            words.pop(i-count)
            count+=1
        return words

#!https://leetcode.com/problems/make-the-string-great/
class Solution(object):
    def makeGood(self, s):
        if len(s)==1:
            return s
        elif len(s)==2 and lower(s[0])==lower(s[1]) and s[0]!=s[1]:
            return ""
        elif len(s)==2 and lower(s[0])!=lower(s[1]) and s[0]!=s[1]:
            return s
        res=s
        for j in range(80):
            for i in range(len(s)-1):
                if lower(s[i])==lower(s[i+1]) and s[i]!=s[i+1]:
                    res=s[:i]+s[i+2:]
            s=res
            if s=="":
                return s
        return s

#!https://leetcode.com/problems/subarray-sums-divisible-by-k/   
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        arr = [0] * k
        arr[0] = 1

        for num in nums:
            prefix = (prefix + num % k + k) % k
            res += arr[prefix]
            arr[prefix] += 1

        return res

#!https://leetcode.com/problems/increasing-decreasing-string/
class Solution(object):
    def sortString(self, s):
        freq = {}
        letters = sorted(set(s))
        res = ""
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] = 1
        while freq:
            for i in letters:
                if  i in freq:
                    if freq[i]>0:
                        res+=i
                        freq[i]-=1
                    else:
                        del freq[i]

            for i in letters[::-1]:
                if  i in freq:
                    if freq[i]>0:
                        res+=i
                        freq[i]-=1
                    else:
                        del freq[i]


        return res
        
#!https://leetcode.com/problems/count-number-of-nice-subarrays/      
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] %= 2
        
        prefix_count = [0] * (len(nums) + 1)
        prefix_count[0] = 1
        s = 0
        ans = 0
        
        for num in nums:
            s += num
            if s >= k:
                ans += prefix_count[s - k]
            prefix_count[s] += 1
        
        return ans

#!https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/ 
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        x=0
        for i in sentences:
            if len(i.split(" "))>x:
                x=len(i.split(" "))
        return x
        
#!https://leetcode.com/problems/kth-distinct-string-in-an-array/
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_dict = Counter(arr)
        count = 0

        for key, value in count_dict.items():
            if value == 1:
                count += 1            
            if count == k:
                return  key
        return ""

#!https://leetcode.com/problems/get-maximum-in-generated-array/
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr=[0,1]
        if n==0:
            return 0
        for i in range(n-1):
            arr.append(0)
        for i in range(2,n+1):
            if i%2==0:
                arr[i]=arr[int(i/2)]
            else:
                arr[i]=arr[int(i/2)]+arr[int(i/2)+1]
        return max(arr)

#!https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/
class Solution:
    def minTimeToType(self, word: str) -> int:
        arr=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        res=0
        start=min(arr.index(word[0]),26-arr.index(word[0]))
        res=start+1
        for i in range(1,len(word)):
            onceki=arr.index(word[i-1])
            simdiki=arr.index(word[i])
            fark1=abs(simdiki-onceki)
            if simdiki>onceki:
                fark2=(len(arr)-simdiki)+onceki
            else:
                fark2=(len(arr)-onceki)+simdiki
            x=min(fark1,fark2)
            res+=1+x
        return res