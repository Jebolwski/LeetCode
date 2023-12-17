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




        
