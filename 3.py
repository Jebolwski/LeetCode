
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
