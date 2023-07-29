
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
